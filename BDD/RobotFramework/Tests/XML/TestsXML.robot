*** Settings ***
Documentation  Примеры работы с XML

Resource  XMLResource.robot

# Many ways to run:
# robot -d results/xml tests/TestsXML.robot
# robot -d results/xml -i XML tests
# robot -d results tests


*** Test Cases ***
Test Root Element Name
    Verify Root Element Name  breakfast_menu
    Verify Elements Count  food  6
