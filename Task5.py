from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


TARGET_URL = "https://the-internet.herokuapp.com/dropdown"
IMPLICIT_WAIT_TIME = 3
OPTION_TO_SELECT = "Option 2"


def execute_dropdown_selection(driver: webdriver.Chrome, url: str) -> None:
    print(f"Navigating to: {url}")
    driver.get(url)
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)

    print("Locating the dropdown HTML element")
    dropdown_element = driver.find_element(by=By.ID, value="dropdown")

    print("Initializing the Selenium Select wrapper")
    dropdown = Select(dropdown_element)

    print(f"Selecting '{OPTION_TO_SELECT}' by its visible text")
    dropdown.select_by_visible_text(OPTION_TO_SELECT)

    selected_option = dropdown.first_selected_option.text
    print(f"Verification -> Currently selected option is: {selected_option}")

    print("Action executed successfully")


if __name__ == "__main__":
    print("Initializing Chrome WebDriver")
    with closing(webdriver.Chrome()) as driver:
        execute_dropdown_selection(driver, TARGET_URL)

    print("WebDriver session closed")