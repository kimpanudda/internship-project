from behave import when, then


@then('Click on the settings option')
def click_on_settings_option(context):
    context.app.settings_page.click_settings_option()


@then('Click on Edit profile option')
def click_on_edit_profile(context):
    context.app.settings_page.click_edit_profile_btn()


@when('Enter some test information in the input fields')
def enter_some_test_info(context):
    context.app.profile_page.enter_test_info()


@when('Check the right information is present in the input fields')
def check_test_info(context):
    context.app.profile_page.check_test_input()


@then('Check “Close” and “Save Changes” buttons are available and clickable')
def check_close_save_buttons(context):
    context.app.profile_page.check_close_save_changes_buttons()
