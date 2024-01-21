Feature: Login into application with fixtures

  @fixture.browser.firefox
  Scenario: Valid login scenario fixture
    Given I open admin page
    When I input login "user" and password "bitnami"
    And I press submit button
    Then Admin page opens

  @fixture.browser.chrome
  Scenario Outline: Invalid login scenario fixture
    Given I open admin page
    When I input login "<login>" and password "<password>"
    And I press submit button
    Then Error message is displayed

    Examples:
      | login | password |
      | user  | wrong    |
      | wrong | bitnami  |
      | wrong | wrong    |
