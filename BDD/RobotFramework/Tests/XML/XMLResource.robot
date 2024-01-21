*** Settings ***
Library  XML


*** Variables ***
${XML_MENU_PATH} =  Data/XML/menu.xml
${EXPECTED_MENU_COUNT} =  1
${EXPECTED_FOOD_COUNT} =  5


*** Keywords ***
Verify Root Element Name
    [Arguments]  ${expected_name}
    ${root} =  Parse XML  ${XML_MENU_PATH}
    Should Be Equal  ${root.tag}  ${expected_name}

Verify Elements Count
    [Arguments]  ${target_element}  ${expected_amount}
    ${food_count} =  Get Element Count  ${XML_MENU_PATH}  ${target_element}
    Should Be Equal As Integers  ${food_count}  ${expected_amount}

Verify First Food Name
    # I would have thought I need to pass breakfast_menu/food[1]/name
    # but that is not the case. Only pass the name of the desired element
    ${first_food_name} =  Get Element  ${XML_MENU_PATH}  food[1]/name
    Should Be Equal As Strings  ${first_food_name.text}  Belgian Waffles

Verify First Food Price
    ${first_food_price} =  Get Element  ${XML_MENU_PATH}  food[1]/price
    Should Be Equal As Strings  ${first_food_price.text}  $5.95

Verify First Food Calories
    ${first_food_calories} =  Get Element  ${XML_MENU_PATH}  food[1]/calories
    Should Be Equal As Strings  ${first_food_calories.text}  650

Add New Food
    ${root} =  Parse XML  ${XML_MENU_PATH}
    Add Element  ${root}  <food></food>
    Add Element  ${root}  <name>Grilled Cheese Sandwich</name>  xpath=food[6]
    Add Element  ${root}  <price>$2.95</price>  xpath=food[6]
    Add Element  ${root}  <description>Yummy melted cheese on grilled sourdough slices</description>  xpath=food[6]
    Add Element  ${root}  <calories>300</calories>  xpath=food[6]
    Save XML     ${root}  ${XML_MENU_PATH}

Verify New Food Exists
    Element Should Exist  ${XML_MENU_PATH}  food[6]
