import os
import time
from io import BufferedReader

from dotenv import find_dotenv, load_dotenv
from pytest_bdd import given, parsers, then

from constants import VALID_WORKFLOW_STATUSES
from markup_ai import (
    MarkupAI,
    RewriteResponse,
    StyleCheckResponse,
    SuggestionResponse,
    WorkflowInfo,
    WorkflowResponse,
)

load_dotenv(find_dotenv(".env"))


def get_workflow_with_polling(get_workflow_fn, workflow_id: str,
                              poll_interval: float = 1.0, timeout: float = 30.0):
    """
    Polls a get_workflow_fn (e.g., client.style_checks.get_style_check) until the workflow status is 'completed' or timeout is reached.
    - get_workflow_fn: function that takes workflow_id and returns a response object
    - workflow_id: the id to poll for
    - poll_interval: seconds between polls
    - timeout: max seconds to wait
    Returns the final response object.
    """
    start_time = time.time()
    while True:
        response: StyleCheckResponse | SuggestionResponse | RewriteResponse = get_workflow_fn(
            workflow_id=workflow_id)

        match response.workflow.status:
            case "completed":
                return response
            case "running":
                pass  # continue polling
            case "failed":
                raise RuntimeError(f"Workflow {workflow_id} failed.")
            case _:
                raise RuntimeError(
                    f"Unexpected status for workflow {workflow_id}: {response.workflow.status}")

        if time.time() - start_time > timeout:
            raise TimeoutError(
                f"Workflow {workflow_id} did not complete within {timeout} seconds.")

        time.sleep(poll_interval)


# Common Verification Functions


def check_workflow_info(workflow_info: WorkflowInfo):
    for field_name, value in workflow_info.model_dump().items():
        assert field_name is not None, f"Workflow field {field_name} is missing"


# Common Given Steps


@given("a valid MarkupAI client", target_fixture="client")
def client() -> MarkupAI:
    return MarkupAI(token=os.getenv("TOKEN"))


@given("a sample file to upload", target_fixture="sample_file")
def sample_file() -> BufferedReader:
    file_path = os.path.join(os.path.dirname(__file__) + "/resources/sample.txt")
    return open(file_path, "rb")


# Common Then Steps


@then("the response should contain a workflow_id")
def check_workflow_id(workflow_response: WorkflowResponse):
    assert workflow_response.workflow_id is not None


@then(
    parsers.parse('the workflow_id in the response begins with "{workflow_id_prefix}"'))
def check_workflow_id_prefix(workflow_response: WorkflowResponse, workflow_id_prefix):
    assert workflow_response.workflow_id.startswith(workflow_id_prefix)


@then('the response contains a valid workflow status')
def check_valid_workflow_status(workflow_response: WorkflowResponse):
    assert workflow_response.status in VALID_WORKFLOW_STATUSES
