Feature: Login into application with background

  Background: common
    Given I open browser
    And I open admin page

  Scenario: Valid login scenario background
    When I input login "user" and password "bitnami"
    And I press submit button
    Then Admin page opens
    And I close browser

  Scenario Outline: Invalid login scenario background
    When I input login "<login>" and password "<password>"
    And I press submit button
    Then Error message is displayed
    And I close browser

    Examples:
      | login | password |
      | user  | wrong    |
      | wrong | bitnami  |
      | wrong | wrong    |
