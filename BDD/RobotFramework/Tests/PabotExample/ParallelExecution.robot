*** Settings ***
Library    SeleniumLibrary

Documentation    Это пример теста написанного с помощью Robot Framework
Test Setup    Open Browser    NONE    ${BROWSER}
Test Teardown    Close Browser

# Parallel launch
# pabot --processes 3 --outputdir Results Tests/OpenCart/*.robot - by suite
# pabot --testlevelsplit --processes 3 --outputdir Results Tests/OpenCart/*.robot - by test

*** Variables ***
# C переменными уже можно работать через опцию -v
${BROWSER}    chrome
${REQUEST}    hello


*** Test Cases ***
Check search item in title yandex
    Go To    https://yandex.ru
    Input And Submit Search    css=#text    ${REQUEST}
    Verify Page Title Contains    ${REQUEST}


Check search item in title google
    Go To    https://google.ru
    Input And Submit Search    name=q    ${REQUEST}
    Verify Page Title Contains    ${REQUEST}


Check search item in title duckduckgo
    Go To    https://duckduckgo.com
    Input And Submit Search    name=q    ${REQUEST}
    Verify Page Title Contains    ${REQUEST}


Check search item in title bing
    Go To    https://www.bing.com
    Input And Submit Search    name=q    ${REQUEST}
    Verify Page Title Contains    ${REQUEST}


Check search item in title go.mail
    Go To    https://go.mail.ru
    Input And Submit Search    name=q    ${REQUEST}
    Verify Page Title Contains    ${REQUEST}


*** Keywords ***
Verify Page Title Contains    [Arguments]    ${VALUE}
    ${TITLE}    Get Title
    Should Contain      ${TITLE}    ${VALUE}

Input And Submit Search    [Arguments]    ${SELECTOR}    ${VALUE}
    Input Text    ${SELECTOR}     ${REQUEST}
    Press Keys    ${SELECTOR}   ENTER
