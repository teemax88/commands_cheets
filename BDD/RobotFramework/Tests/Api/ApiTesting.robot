*** Settings ***
Documentation  API Testing small example
Library  RequestsLibrary


*** Variables ***
${JSONPLACEHOLDER}  https://jsonplaceholder.typicode.com


*** Test Cases ***
Test Posts Response
    [Documentation]  Check amount of returned posts equal 100
    Create Session  json_place  ${JSONPLACEHOLDER}
    ${resp} =  GET On Session  json_place  /posts
    Request Should Be Successful  ${resp}
    ${resp_size} =  Get Length  ${resp.json()}
    Should Be Equal As Integers  100  ${resp_size}