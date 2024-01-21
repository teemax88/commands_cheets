*** Settings ***
Documentation  Создание директорий и работа с файлами
Resource  OS.robot


*** Test Cases ***
Create Some Directories
    [Tags]  OperatingSystem
    OS.Create the Base Directory
    OS.Create Directory 1
    OS.Create Directory 2

Create Some Files
    [Tags]  OperatingSystem
    OS.Create the First File
    OS.Create the Second File
    OS.Create the Third File

Move a File
    [Tags]  OperatingSystem
    OS.Move File 3 from Directory 2 to Directory 1

Copy a File
    [Tags]  OperatingSystem
    OS.Copy File 1 from Directory 1 to Directory 2