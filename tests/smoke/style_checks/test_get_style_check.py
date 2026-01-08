import os
from io import BufferedReader

from conftest import check_workflow_info, get_workflow_with_polling
from pytest_bdd import given, parsers, scenario, then, when

from markup_ai import MarkupAI, StyleCheckResponse, WorkflowResponse

FEATURE_PATH = os.path.join(os.path.dirname(__file__),
                            "../style_checks/get_style_check.feature")


# Scenarios
@scenario(FEATURE_PATH, "Get style check result by workflow_id without polling")
def test_get_style_check_result_by_workflow_id_without_polling():
    """Test scenario entrypoint"""
    pass


@scenario(FEATURE_PATH, "Get style check result by workflow_id with polling")
def test_get_style_check_result_by_workflow_id_with_polling():
    """Test scenario entrypoint"""
    pass


# Given Steps
@given("a style check has been created", target_fixture="workflow_response")
def create_style_check(client: MarkupAI,
                       sample_file: BufferedReader) -> WorkflowResponse:
    return client.style_checks.create_style_check(dialect="american_english",
                                                  file_upload=sample_file,
                                                  style_guide="ap")


# When Steps
@when(
    parsers.parse("I get a style check with an existing workflow_id without polling"),
    target_fixture="get_style_check_response",
)
def get_style_check_without_polling(client: MarkupAI,
                                    workflow_response: WorkflowResponse) -> StyleCheckResponse:
    return client.style_checks.get_style_check(
        workflow_id=workflow_response.workflow_id)


@when(
    parsers.parse("I get a style check with an existing workflow_id with polling"),
    target_fixture="get_style_check_response",
)
def get_style_check_with_polling(client: MarkupAI,
                                 workflow_response: WorkflowResponse) -> StyleCheckResponse:
    return get_workflow_with_polling(
        get_workflow_fn=client.style_checks.get_style_check,
        workflow_id=workflow_response.workflow_id
    )


# Then Steps
@then("the style check response should return a style check")
def check_style_check_response(get_style_check_response: StyleCheckResponse):
    assert isinstance(get_style_check_response, StyleCheckResponse)
    assert get_style_check_response.config is not None
    assert get_style_check_response.original is not None
    assert get_style_check_response.workflow is not None


@then("the workflow info should be valid")
def check_style_check_workflow_info(get_style_check_response: StyleCheckResponse):
    check_workflow_info(workflow_info=get_style_check_response.workflow)
