Feature: Tests profile settings management

  Scenario: User can go to settings and edit the personal information
    Given Open Reelly login page
    When Enter email address
    And Enter password
    Then Click login button
#    And Click on the settings option
    And Click on the Menu option
    Then Click on Edit profile option
    When Enter some test information in the input fields
    And Check the right information is present in the input fields
    Then Check “Close” and “Save Changes” buttons are available and clickable
