from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.by import By

TARGET_URL = "https://the-internet.herokuapp.com/checkboxes"
IMPLICIT_WAIT_TIME = 3


def execute_checkbox_toggle(driver: webdriver.Chrome, url: str) -> None:
    print(f"Navigating to: {url}")
    driver.get(url)
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)

    print("Locating all checkbox elements on the page")
    checkboxes = driver.find_elements(by=By.CSS_SELECTOR, value='input[type="checkbox"]')

    if len(checkboxes) >= 2:
        checkbox_1 = checkboxes[0]
        checkbox_2 = checkboxes[1]

        print(f"Initial state -> Checkbox 1 is selected: {checkbox_1.is_selected()}")
        print(f"Initial state -> Checkbox 2 is selected: {checkbox_2.is_selected()}")

        print("Activating the first checkbox (if not already active)")
        if not checkbox_1.is_selected():
            checkbox_1.click()

        print("Deactivating the second checkbox (if currently active)")
        if checkbox_2.is_selected():
            checkbox_2.click()

        print(f"Final state -> Checkbox 1 is selected: {checkbox_1.is_selected()}")
        print(f"Final state -> Checkbox 2 is selected: {checkbox_2.is_selected()}")
        print("Checkbox manipulation executed successfully")
    else:
        print("Error: Could not locate the expected number of checkboxes on the page.")


if __name__ == "__main__":
    print("Initializing Chrome WebDriver")
    with closing(webdriver.Chrome()) as driver:
        execute_checkbox_toggle(driver, TARGET_URL)

    print("WebDriver session closed")