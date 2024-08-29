from behave import when, then


@then('Click on the settings option')
def click_on_settings_option(context):
    context.app.settings_page.click_settings_option()


@then('Click on Edit profile option')
def click_on_edit_profile(context):
    context.app.settings_page.click_edit_profile_btn()