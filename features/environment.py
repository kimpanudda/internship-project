from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from app.application import Application

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    ### CHROME ####
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ### CHROME MOBILE EMULATION ###
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # ### FIREFOX ####
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)


    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # bs_user = 'kimp_kXaRcM'
    # bs_key = 'U5n6Y5H1iSavF1hurNsF'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion": "11",
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }

    bs_user = 'kimp_kXaRcM'
    bs_key = 'U5n6Y5H1iSavF1hurNsF'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "osVersion": "17",
        "deviceName": "iPhone 12 Pro",
        'browserName': 'Chrome',
        'sessionName': scenario_name
    }


    #
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.set_window_size(1920, 1080) # for only headless mode and browserstack
    # context.driver.set_window_size(400, 700)  # for only headless mode and browserstack

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

    ### HEADLESS MODE FIREFOX ####
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # browser_init(context)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
