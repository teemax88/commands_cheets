*** Settings ***
Documentation  API Testing parametrization within tests

Library  RequestsLibrary
Library  ../../Libs/MyKeyWords.py


*** Variables ***
${JSONPLACEHOLDER}  https://jsonplaceholder.typicode.com


*** Test Cases ***
Test Posts Handler
    [Template]  Passing Id To Posts Handler
    1  1  200
    100  100  200
    1000  EMPTY  404
    0  EMPTY  404


Test Comments Handler
    [Template]  Test Comments Get Handle
    1  1  200
    2  2  200
    100  100  200
    0  EMPTY  200
    1000  EMPTY  200


*** Keywords ***
Passing Id To Posts Handler
    [Arguments]  ${user_id}  ${expected_id}  ${status}
    Create Session  json_place  url=${JSONPLACEHOLDER}  disable_warnings=1
    ${resp} =  GET On Session  json_place  /posts/${user_id}  expected_status=${status}
    ${resp_json} =  Set Variable  ${resp.json()}
    Dictionary ${resp_json} should contain ${expected_id}


Test Comments Get Handle
    [Arguments]  ${post_id}  ${expected_id}  ${status}
    Create Session  json_place  url=${JSONPLACEHOLDER}  disable_warnings=1
    ${resp} =  GET On Session  json_place  /posts/${post_id}/comments  expected_status=${status}
    ${resp_json} =  Set Variable  ${resp.json()}
    FOR  ${item}  IN  @{resp_json}
        Dictionary ${item} should contain ${post_id}
    END
