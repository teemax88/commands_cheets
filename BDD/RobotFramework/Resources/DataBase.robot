*** Settings ***
Library  DatabaseLibrary


*** Variables ***
${PRODUCT_DB}  oc_product
${PRODUCT_DESCRIPTION_DB}  oc_product_description


*** Keywords ***
Check Product In Database
    [Arguments]  ${value}
    Check If Exists In Database  select model from ${PRODUCT_DB} where model = '${value}'
    Check If Exists In Database  select name from ${PRODUCT_DESCRIPTION_DB} where name = '${value}'


Check Product Not In Database
    [Arguments]  ${product_name}
    Check If Not Exists In Database  select model from ${PRODUCT_DB} where model = '${product_name}'


Add Product To Catalog With Database
    [Arguments]  ${product_name}
    Execute Sql String  insert into ${PRODUCT_DB} (model, sku, upc, ean, jan, isbn, mpn, location, stock_status_id, manufacturer_id, tax_class_id, date_added, date_modified, quantity, date_available) VALUES ('${product_name}', 'sku', 'upc', 'ean', 'jan', 'isbn', 'mnp', 'test_location', 6, 6, 6, NOW(), NOW(), 1, '2009-02-03')
    ${product_id}  QUERY  select product_id from ${PRODUCT_DB} where model = '${product_name}'
    Execute Sql String  insert into ${PRODUCT_DESCRIPTION_DB} (product_id, name, language_id, description, tag, meta_title, meta_description, meta_keyword) VALUES ('${product_id}[0][0]', '${product_name}', 1, 'test_description', 'tag', 'meta_title', 'meta_description', 'meta_keyword')
