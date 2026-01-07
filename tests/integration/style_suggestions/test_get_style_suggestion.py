import os
from io import BufferedReader

from conftest import check_workflow_info, get_workflow_with_polling
from pytest_bdd import given, parsers, scenarios, then, when

from markup_ai import MarkupAI, SuggestionResponse, WorkflowResponse

FEATURE_PATH = os.path.join(os.path.dirname(__file__),
                            "../style_suggestions/get_style_suggestion.feature")
scenarios(FEATURE_PATH)


@given("a style suggestion has been created", target_fixture="workflow_response")
def create_style_suggestion(client: MarkupAI,
                            sample_file: BufferedReader) -> WorkflowResponse:
    return client.style_suggestions.create_style_suggestion(
        dialect="american_english", file_upload=sample_file, style_guide="ap"
    )


@when(
    parsers.parse(
        "I get a style suggestion with an existing workflow_id without polling"),
    target_fixture="get_style_suggestion_response",
)
def get_style_suggestion_without_polling(client: MarkupAI,
                                         workflow_response: WorkflowResponse) -> SuggestionResponse:
    return client.style_suggestions.get_style_suggestion(
        workflow_id=workflow_response.workflow_id)


@when(
    parsers.parse("I get a style suggestion with an existing workflow_id with polling"),
    target_fixture="get_style_suggestion_response",
)
def get_style_suggestion_with_polling(client: MarkupAI,
                                      workflow_response: WorkflowResponse) -> SuggestionResponse:
    return get_workflow_with_polling(
        get_workflow_fn=client.style_suggestions.get_style_suggestion,
        workflow_id=workflow_response.workflow_id
    )


@then("the style suggestion response should return a style suggestion")
def check_style_suggestion_response(get_style_suggestion_response: SuggestionResponse):
    assert isinstance(get_style_suggestion_response, SuggestionResponse)
    assert get_style_suggestion_response.config is not None
    assert get_style_suggestion_response.original is not None
    assert get_style_suggestion_response.workflow is not None


@then("the workflow info should be valid")
def check_style_suggestion_workflow_info(
        get_style_suggestion_response: SuggestionResponse):
    check_workflow_info(workflow_info=get_style_suggestion_response.workflow)
