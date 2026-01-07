Feature: Get Style Check
  As a user
  I want to retrieve the results of a style check
  So that I can see the analysis

  Background:
    Given a valid MarkupAI client
    And a sample file to upload

  Scenario: Get style check result by workflow_id without polling
    Given a style check has been created
    When I get a style check with an existing workflow_id without polling
    Then the response should contain a workflow_id
    And the workflow_id in the response begins with "chk"
    And the response contains a valid workflow status

  Scenario: Get style check result by workflow_id with polling
    Given a style check has been created
    When I get a style check with an existing workflow_id with polling
    Then the style check response should return a style check
    And the workflow info should be valid


