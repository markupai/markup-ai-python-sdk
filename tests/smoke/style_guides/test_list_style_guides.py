import os

from pytest_bdd import scenarios, then, when

from markup_ai import MarkupAI, StyleGuideResponse

FEATURE_PATH = os.path.join(os.path.dirname(__file__),
                            "../style_guides/list_style_guides.feature")
scenarios(FEATURE_PATH)


@when("I list all style guides", target_fixture="list_style_guides_response")
def list_style_guides(client: MarkupAI) -> list[StyleGuideResponse]:
    return client.style_guides.list_style_guides()


@then("the response should be a list of style guides")
def check_style_guides_list(list_style_guides_response: list[StyleGuideResponse]):
    assert len(list_style_guides_response) > 0
    for style_guide in list_style_guides_response:
        assert isinstance(style_guide, StyleGuideResponse)
        assert hasattr(style_guide, "id") and style_guide.id is not None
        assert hasattr(style_guide, "name") and style_guide.name is not None
        assert hasattr(style_guide, "created_at") and style_guide.created_at is not None
