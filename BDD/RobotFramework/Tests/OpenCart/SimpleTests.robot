*** Settings ***
Resource  ../../PageObjects/MainPage.robot


*** Test Cases ***
Test One
    Open Browser  http://localhost  chrome
    Search Product  MacBook
    Close Browser
