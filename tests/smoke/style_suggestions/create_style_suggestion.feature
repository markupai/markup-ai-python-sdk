Feature: Create Style Suggestion
  As a user
  I want to create a style suggestion
  So that I can get suggested corrections for style and brand issues

  Background:
    Given a valid MarkupAI client
    And a sample file to upload

  Scenario: Create a style suggestion with valid parameters
    When I create a style suggestion with dialect "american_english" and style_guide "ap"
    Then the response should contain a workflow_id
    And the workflow_id in the response begins with "sug"
    And the response contains a valid workflow status
