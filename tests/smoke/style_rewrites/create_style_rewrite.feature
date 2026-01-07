Feature: Create Style Rewrite
  As a user
  I want to create a style rewrite
  So that I can get a rewritten document with improved style and brand consistency

  Background:
    Given a valid MarkupAI client
    And a sample file to upload

  Scenario: Create a style rewrite with valid parameters
    When I create a style rewrite with dialect "american_english" and style_guide "ap"
    Then the response should contain a workflow_id
    And the workflow_id in the response begins with "rw"
    And the response contains a valid workflow status
