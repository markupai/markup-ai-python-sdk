import os
from io import BufferedReader

from pytest_bdd import parsers, scenarios, when

from markup_ai import MarkupAI, WorkflowResponse

FEATURE_PATH = os.path.join(os.path.dirname(__file__),
                            "../style_checks/create_style_check.feature")
scenarios(FEATURE_PATH)


@when(parsers.parse(
    'I create a style check with dialect "{dialect}" and style_guide "{style_guide}"'),
    target_fixture="workflow_response")
def create_style_check(client: MarkupAI, sample_file: BufferedReader, dialect,
                       style_guide) -> WorkflowResponse:
    return client.style_checks.create_style_check(
        dialect=dialect,
        style_guide=style_guide,
        file_upload=sample_file
    )
