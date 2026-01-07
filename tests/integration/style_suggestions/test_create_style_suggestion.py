import os
from io import BufferedReader
from markup_ai import MarkupAI
from pytest_bdd import parsers, scenarios, when

FEATURE_PATH = os.path.join(os.path.dirname(__file__), "../style_suggestions/create_style_suggestion.feature")
scenarios(FEATURE_PATH)

@when(parsers.parse('I create a style suggestion with dialect "{dialect}" and style_guide "{style_guide}"'), target_fixture="workflow_response")
def create_style_suggestion(client: MarkupAI, sample_file: BufferedReader, dialect, style_guide):
    response = client.style_suggestions.create_style_suggestion(
        dialect=dialect,
        style_guide=style_guide,
        file_upload=sample_file
    )
    return response
