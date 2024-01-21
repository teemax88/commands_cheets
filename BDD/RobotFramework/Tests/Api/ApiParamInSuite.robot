*** Settings ***
Documentation  API Testing parametrization within suites

Library  RequestsLibrary
Library  ../../Libs/MyKeyWords.py

Test Template  Passing Id To Posts Handler


*** Variables ***
${JSONPLACEHOLDER}  https://jsonplaceholder.typicode.com


*** Test Cases ***
One Valid  1  1  200
Two Valid  2  1  200
Hundred Valid  100  100  200
Thousand Invalid  1000  EMPTY  404


*** Keywords ***
Passing Id To Posts Handler
    [Arguments]  ${user_id}  ${expected}  ${status}
    Create Session  json_place  url=${JSONPLACEHOLDER}  disable_warnings=1
    ${resp} =  GET On Session  json_place  /posts/${user_id}  expected_status=${status}
    ${size} =  Get Length  ${resp.json()}
    Dictionary ${resp.json()} should contain ${expected}
