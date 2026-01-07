Feature: List Style Guides
  As a user
  I want to list all style guides
  So that I can see available style guides

  Background:
    Given a valid MarkupAI client

  Scenario: List all style guides
    When I list all style guides
    Then the response should be a list of style guides
