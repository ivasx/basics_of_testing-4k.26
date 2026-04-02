from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

TARGET_URL = "https://the-internet.herokuapp.com/context_menu"
IMPLICIT_WAIT_TIME = 3


def execute_context_click(driver: webdriver.Chrome, url: str) -> None:
    print(f"Navigating to: {url}")
    driver.get(url)
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)

    print("Locating the hot-spot area")
    hot_spot = driver.find_element(by=By.ID, value="hot-spot")

    print("Performing right-click (context click) action")
    actions = ActionChains(driver)
    actions.context_click(hot_spot).perform()

    print("Handling JavaScript alert window")
    alert = driver.switch_to.alert
    print(f"Alert successfully caught with text: '{alert.text}'")
    alert.accept()

    print("Action executed successfully")


if __name__ == "__main__":
    print("Initializing Chrome WebDriver")
    with closing(webdriver.Chrome()) as driver:
        execute_context_click(driver, TARGET_URL)

    print("WebDriver session closed")