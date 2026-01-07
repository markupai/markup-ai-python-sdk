Feature: Get Style Rewrite
  As a user
  I want to retrieve the results of a style rewrite
  So that I can see the rewritten document and fixed style issues

  Background:
    Given a valid MarkupAI client
    And a sample file to upload

  Scenario: Get style rewrite result by workflow_id without polling
    Given a style rewrite has been created
    When I get a style rewrite with an existing workflow_id without polling
    Then the response should contain a workflow_id
    And the workflow_id in the response begins with "rw"
    And the response contains a valid workflow status

  Scenario: Get style rewrite result by workflow_id with polling
    Given a style rewrite has been created
    When I get a style rewrite with an existing workflow_id with polling
    Then the style rewrite response should return a style rewrite
    And the workflow info should be valid

