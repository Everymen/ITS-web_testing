import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from behave import *
import datetime
import time

@given(u'a web browser is at VALU3S home page')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    time.sleep(1)

@given(u'user is successfully logged in w/ permissions to create')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/login")
    time.sleep(1)
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").send_keys(Keys.ENTER)
    time.sleep(1)

@given(u'user selected "Add new...", "Evaluation Scenario" options')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++evaluation_scenario")
    time.sleep(1)

@given(u'user filled in all required fields')
def step_impl(context):
    for elem in context.driver.find_elements(By.XPATH, "//textarea[@class='textarea-widget required text-field'] | //input[@class='text-widget required textline-field']"):
        elem.send_keys(str(datetime.datetime.now()))
    # try:
    #     print("NENALEZENO")
    #     context.driver.switch_to.frame(1)
    #     element = context.driver.find_element(By.ID, "tinymce")
    #     context.driver.find_element(By.CSS_SELECTOR, "html").click()
    #     element = context.driver.find_element(By.ID, "tinymce")
    #     context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>TEXT</p>'}", element)
    #     context.driver.switch_to.default_content()
    #     print("PO SKRIPTU")
    # except:
    #     print("EXCEPTAN")



@when(u'user clicks "Save" button')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
    time.sleep(1)


@then(u'"Item created" information box pops up')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#global_statusmessage > .info")

@then(u'all fields filled in by user are saved (item created)')
def step_impl(context):
    pass

@then(u'item state is private')
def step_impl(context):
    if(context.driver.find_element(By.XPATH, "//span[@class='plone-toolbar-state-title']").text != "Private"):
        raise Exception(u'STEP: Then item state is private')

@given(u'user did not filled in all required fields')
def step_impl(context):
    for elem in context.driver.find_elements(By.XPATH, "//textarea[@class='textarea-widget required text-field'] | //input[@class='text-widget required textline-field']"):
        elem.clear()


@then(u'"There were some errors" error box pops up')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//dl[@class='portalMessage error']")


@then(u'all required fields not filled in are highlighted')
def step_impl(context):
    for elem in context.driver.find_elements(By.XPATH, "//textarea[@class='textarea-widget required text-field'] | //input[@class='text-widget required textline-field']"):
        if(elem.text == ""):
            return
    raise Exception(u'STEP: Then all required fields not filled in are highlighted')


@then(u'item is not created')
def step_impl(context):
    pass


@given(u'user is successfully logged in w/ permissions to edit')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/login")
    time.sleep(1)
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").send_keys(Keys.ENTER)
    time.sleep(1)


@given(u'user selected "Contents" option')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-folderContents span:nth-child(2)").click()
    time.sleep(1)


@given(u'user clicked on "Edit" button of desired item')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/organisations/edit")
    time.sleep(1)


@given(u'user edited desired fields w/ all required fields filled in')
def step_impl(context):
    for elem in context.driver.find_elements(By.XPATH, "//textarea[@class='textarea-widget required text-field'] | //input[@class='text-widget required textline-field']"):
        elem.send_keys(str(datetime.datetime.now()))


@then(u'"Changes saved" information box pops up')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#global_statusmessage > .info")


@then(u'all fields edited by user are saved')
def step_impl(context):
    pass


@given(u'user navigated to desired item')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/organisations/faculty-of-information-technology")
    time.sleep(1)


@given(u'user clicked on "Edit" option')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    time.sleep(1)



@given(u'user edited desired fields w/o all required fields filled in')
def step_impl(context):
    for elem in context.driver.find_elements(By.XPATH, "//textarea[@class='textarea-widget required text-field'] | //input[@class='text-widget required textline-field']"):
        elem.clear()


@then(u'all fields edited by user are not saved')
def step_impl(context):
    pass


@given(u'user is successfully logged in w/ permissions to delete')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/login")
    time.sleep(1)
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").send_keys(Keys.ENTER)
    time.sleep(1)


@given(u'user selected desired items for deletion')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/folder_contents?_authenticator=b8c3d47b28e96d1f4c9b57a7dfd0ac8ade7451e4")
    time.sleep(1)
    context.driver.find_element(By.ID, "select4InputCheckbox").click()
    # element = context.driver.find_element(By.ID, "btn-rename")
    # actions = ActionChains(context.driver)
    # actions.move_to_element(element).perform()
    # element = context.driver.find_element(By.CSS_SELECTOR, "body")
    # actions = ActionChains(context.driver)
    # actions.move_to_element(element, 0, 0).perform()
    # element = context.driver.find_element(By.ID, "btn-delete")
    # actions = ActionChains(context.driver)
    # actions.move_to_element(element).perform()
    # element = context.driver.find_element(By.CSS_SELECTOR, "body")
    # actions = ActionChains(context.driver)
    # actions.move_to_element(element, 0, 0).perform()



@given(u'user clicks "Delete" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".glyphicon-trash").click()


@when(u'user clicks "Yes" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".applyBtn").click()


@then(u'"Successfully delete items" information box pops up')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fc-status-container > .alert")


@then(u'items are deleted')
def step_impl(context):
    pass


@given(u'user is successfully logged in w/ permissions to change state')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/login")
    time.sleep(1)
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").send_keys(Keys.ENTER)
    time.sleep(1)


@when(u'user selected desired item state from option menu')
def step_impl(context):
    try:
        context.driver.get("http://localhost:8080/VALU3S/tools")
        time.sleep(1)
        context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-logo > img").click()
        context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-workflow > .label-state-published").click()
        context.driver.find_element(By.ID, "workflow-transition-reject").click()
    except:
        pass


@then(u'"Item state changed" information box pops up')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#global_statusmessage > .info")


@then(u'item state changed to user\'s desired state')
def step_impl(context):
    pass


@given(u'user is successfully logged in w/o permissions to edit')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/login")
    time.sleep(1)
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsreviewer")
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsreviewer")
    context.driver.find_element(By.ID, "__ac_password").send_keys(Keys.ENTER)
    time.sleep(1)


@when(u'user clicks "Edit" button of desired item')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/organisations/edit")
    time.sleep(1)


@then(u'"Insufficient Privileges" page pops up')
def step_impl(context):
    time.sleep(1)
    if(context.driver.current_url != "http://localhost:8080/VALU3S/insufficient-privileges"):
        raise Exception(u'STEP: Then "Insufficient Privileges" page pops up')


@given(u'user is successfully logged in w/o permissions to delete')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/login")
    time.sleep(1)
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsreviewer")
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsreviewer")
    context.driver.find_element(By.ID, "__ac_password").send_keys(Keys.ENTER)
    time.sleep(1)


@then(u'"Permission denied" information box pops up')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fc-status-container > .alert")


@then(u'items are not deleted')
def step_impl(context):
    pass


@given(u'user is successfully logged in w/o permissions to change state')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/login")
    time.sleep(1)
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsreviewer")
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsreviewer")
    context.driver.find_element(By.ID, "__ac_password").send_keys(Keys.ENTER)
    time.sleep(1)


@then(u'item state is unchanged')
def step_impl(context):
    pass


@given(u'user selected "Add new...", "Method" options')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++method")
    time.sleep(1)


@given(u'user selected "Add new...", "Organization" options')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++organization")
    time.sleep(1)


@given(u'user selected "Add new...", "Requirement" options')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++requirement")
    time.sleep(1)


@given(u'user selected "Add new...", "Standard" options')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++standards")
    time.sleep(1)


@given(u'user selected "Add new...", "Test Case" options')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++test_case")
    time.sleep(1)


@given(u'user selected "Add new...", "Tool" options')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++tool")
    time.sleep(1)


@given(u'user selected "Add new...", "Use Case" options')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++use_case")
    time.sleep(1)
