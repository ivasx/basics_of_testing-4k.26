from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

TARGET_URL = "https://the-internet.herokuapp.com/drag_and_drop"
IMPLICIT_WAIT_TIME = 3


def execute_drag_and_drop(driver: webdriver.Chrome, url: str) -> None:
    print(f"Navigating to: {url}")
    driver.get(url)
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)

    print("Locating elements: 'column-a' and 'column-b'")
    source_element = driver.find_element(by=By.ID, value="column-a")
    target_element = driver.find_element(by=By.ID, value="column-b")

    print("Performing drag and drop action")
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()

    print("Action executed successfully")


if __name__ == "__main__":
    print("Initializing Chrome WebDriver")
    with closing(webdriver.Chrome()) as driver:
        execute_drag_and_drop(driver, TARGET_URL)

    print("WebDriver session closed")