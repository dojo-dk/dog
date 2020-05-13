import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://phantombuster.com/login")

EMAIL = os.getenv("EMAIL")
PASS  = os.getenv("PASSWORD")

def handle_launch():
    time.sleep(1)

    try:
        launch = driver.find_element_by_xpath('//button[@analyticsId="agentLaunchBtn"]')
    except:
        time.sleep(0.5)

        print("[status] Dog taking another nap\n    ... zzzz")
        handle_launch()

    print("[status] Launching something")

    launch.click()


def handle_button(button):
    # href = button.get_attribute("href")
    # driver.execute_script(f'''window.open("{href}", "_blank")''')

    handle_launch()

def fetch_consoles():
    launch_buttons = driver.find_elements_by_link_text("Console")

    if len(launch_buttons) == 0:
        print("[status] Dog is sleeping ...")
        time.sleep(0.5)
        return fetch_consoles()

    for (i, button) in enumerate(launch_buttons):
        print(f"[status] Clicking button #{i}")

        ActionChains(driver) \
            .key_down(Keys.CONTROL) \
            .click(button) \
            .key_up(Keys.CONTROL) \
            .perform()

    for i in range(0, len(launch_buttons)):
        driver.switch_to.window(driver.window_handles[1 + i])
        time.sleep(1)

        handle_launch()

        # handle_launch()

def fetch_login(is_sleep=False):
    email_field = driver.find_element_by_xpath("//input[@placeholder='Enter your email']")
    pass_field  = driver.find_element_by_xpath("//input[@placeholder='Password']")

    if not email_field:
        time.sleep(0.5)
        if is_sleep:
            print("[status] Dog is sleeping ...")
        else:
            print("[status] zzZZzzzZZz ...")

        return fetch_login(True)

    email_field.send_keys(EMAIL)
    pass_field.send_keys(PASS)

    pass_field.send_keys(Keys.ENTER)

    fetch_consoles()

fetch_login()