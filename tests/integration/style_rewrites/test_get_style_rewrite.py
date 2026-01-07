import os
from io import BufferedReader

from conftest import check_workflow_info, get_workflow_with_polling
from pytest_bdd import given, parsers, scenarios, then, when

from markup_ai import MarkupAI, RewriteResponse, WorkflowResponse

FEATURE_PATH = os.path.join(os.path.dirname(__file__),
                            "../style_rewrites/get_style_rewrite.feature")
scenarios(FEATURE_PATH)


@given("a style rewrite has been created", target_fixture="workflow_response")
def create_style_rewrite(client: MarkupAI,
                         sample_file: BufferedReader) -> WorkflowResponse:
    return client.style_rewrites.create_style_rewrite(
        dialect="american_english", file_upload=sample_file, style_guide="ap"
    )


@when(
    parsers.parse("I get a style rewrite with an existing workflow_id without polling"),
    target_fixture="get_style_rewrite_response",
)
def get_style_rewrite_without_polling(client: MarkupAI,
                                      workflow_response: WorkflowResponse) -> RewriteResponse:
    return client.style_rewrites.get_style_rewrite(
        workflow_id=workflow_response.workflow_id)


@when(
    parsers.parse("I get a style rewrite with an existing workflow_id with polling"),
    target_fixture="get_style_rewrite_response",
)
def get_style_rewrite_with_polling(client: MarkupAI,
                                   workflow_response: WorkflowResponse) -> RewriteResponse:
    return get_workflow_with_polling(
        get_workflow_fn=client.style_rewrites.get_style_rewrite,
        workflow_id=workflow_response.workflow_id
    )


@then("the style rewrite response should return a style rewrite")
def check_style_rewrite_response(get_style_rewrite_response: RewriteResponse):
    assert isinstance(get_style_rewrite_response, RewriteResponse)
    assert get_style_rewrite_response.config is not None
    assert get_style_rewrite_response.original is not None
    assert get_style_rewrite_response.workflow is not None
    assert get_style_rewrite_response.rewrite is not None


@then("the workflow info should be valid")
def check_style_rewrite_workflow_info(get_style_rewrite_response: RewriteResponse):
    check_workflow_info(workflow_info=get_style_rewrite_response.workflow)
