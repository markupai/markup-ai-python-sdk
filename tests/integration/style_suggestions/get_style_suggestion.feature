Feature: Get Style Suggestion
  As a user
  I want to retrieve the results of a style suggestion
  So that I can see the suggested corrections

  Background:
    Given a valid MarkupAI client
    And a sample file to upload

  Scenario: Get style suggestion result by workflow_id without polling
    Given a style suggestion has been created
    When I get a style suggestion with an existing workflow_id without polling
    Then the response should contain a workflow_id
    And the workflow_id in the response begins with "sug"
    And the response contains a valid workflow status

  Scenario: Get style suggestion result by workflow_id with polling
    Given a style suggestion has been created
    When I get a style suggestion with an existing workflow_id with polling
    Then the style suggestion response should return a style suggestion
    And the workflow info should be valid

