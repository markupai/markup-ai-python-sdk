Feature: Create Style Check
  As a user
  I want to create a style check
  So that I can analyze my document for style and brand issues

  Background:
    Given a valid MarkupAI client
    And a sample file to upload

  Scenario: Create a style check with valid parameters
    When I create a style check with dialect "american_english" and style_guide "ap"
    Then the response should contain a workflow_id
    And the workflow_id in the response begins with "chk"
    And the response contains a valid workflow status

