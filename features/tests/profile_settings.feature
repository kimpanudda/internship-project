Feature: Tests profile settings management

  Scenario: User can go to settings and edit the personal information
    Given Open Reelly login page
    When Enter email address
    And Enter password
    Then Click login button
#    And Click on the settings option
