*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Place value
    Go To  ${HOME_URL}
    Input Text  value  10
    Click Button  aseta
    Page Should Contain  nappia painettu 10 kertaa
