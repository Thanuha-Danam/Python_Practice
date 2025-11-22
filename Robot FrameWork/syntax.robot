*** Settings ***
Library  String

*** Test Cases ***
Create A Random String
    Log To Console  We are creating a random string.
    Generate Random String  10
    Log To Console  Creation of random string completed.
