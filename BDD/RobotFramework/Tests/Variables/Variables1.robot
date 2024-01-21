*** Test Cases ***
Declare and set variables 1
    # Available inside current test
    ${some_test_data} =  Set Variable  This is only available within this test
    Set Test Variable  ${more_test_data}  This is also only available within this test
    # Available inside
    Set Suite Variable  ${some_suite_data}  This is available within all tests in this suite
    # Available outside
    Set Global Variable  ${SOME_GLOBAL_DATA}  This available everywhere

Another Test In Sutie
    Log  ${some_suite_data}
