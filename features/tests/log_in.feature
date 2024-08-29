Feature: Tests user can log in to the main page

  Scenario: Verify user can log in with valid credentials
    Given Open Reelly login page
    When Enter email address
    When Enter password
    Then Click login button

