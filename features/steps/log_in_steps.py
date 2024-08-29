from behave import given, when, then


@given('Open Reelly login page')
def open_reelly_login_page(context):
    context.app.log_in_page.open_log_in_url()


@when('Enter email address')
def enter_email(context):
    context.app.log_in_page.enter_email('test@gmail.com')


@when('Enter password')
def enter_password(context):
    context.app.log_in_page.enter_password('testQA')


@then('Click login button')
def click_login_button(context):
    context.app.log_in_page.click_login_button()