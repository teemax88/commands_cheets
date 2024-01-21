*** Test Cases ***
Declare and set variables 2
    # Available in test only
    ${some_test_data} =  Set Variable  This is only available within this test
    Set Test Variable  ${more_test_data}  This is also only available within this test

    # Available inside suite
    Set Suite Variable  ${some_suite_data}  This is available within all tests in this suite

    # Was set in another module!
    Log  ${SOME_GLOBAL_DATA}

Another Test In Sutie
    # Was set in another test
    Log  ${some_suite_data}

This Is Failed Test
    # Will fail!
    Log  ${some_test_data}
