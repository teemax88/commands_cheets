Feature: Login into application

  Scenario: Valid login scenario
    Given I open "Chrome" browser
    And I open admin page
    When I input login "user" and password "bitnami"
    And I press submit button
    Then Admin page opens
    And I close browser

  Scenario Outline: Invalid login scenario
    Given I open "Firefox" browser
    And I open admin page
    When I input login "<login>" and password "<password>"
    And I press submit button
    Then Error message is displayed
    And I close browser

    Examples:
      | login | password |
      | user  | wrong    |
      | wrong | bitnami  |
      | wrong | wrong    |
