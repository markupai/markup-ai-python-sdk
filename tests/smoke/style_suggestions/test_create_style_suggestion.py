import os
from io import BufferedReader
from markup_ai import MarkupAI
from pytest_bdd import parsers, scenario, when

FEATURE_PATH = os.path.join(os.path.dirname(__file__),
                            "../style_suggestions/create_style_suggestion.feature")


# Scenarios
@scenario(FEATURE_PATH, "Create a style suggestion with valid parameters")
def test_create_style_suggestion_with_valid_parameters():
    """Test scenario entrypoint"""
    pass


# When Steps
@when(parsers.parse(
    'I create a style suggestion with dialect "{dialect}" and style_guide "{style_guide}"'),
    target_fixture="workflow_response")
def create_style_suggestion(client: MarkupAI, sample_file: BufferedReader, dialect,
                            style_guide):
    response = client.style_suggestions.create_style_suggestion(
        dialect=dialect,
        style_guide=style_guide,
        file_upload=sample_file
    )
    return response
