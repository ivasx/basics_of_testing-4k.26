from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.by import By


TARGET_URL = "https://the-internet.herokuapp.com/inputs"
IMPLICIT_WAIT_TIME = 3
TEST_INPUT_VALUE = "1234"


def execute_data_input(driver: webdriver.Chrome, url: str) -> None:
    print(f"Navigating to: {url}")
    driver.get(url)
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)

    print("Locating the number input field")
    input_field = driver.find_element(by=By.CSS_SELECTOR, value='input[type="number"]')

    print("Clearing the input field to prevent appending to existing data")
    input_field.clear()

    print(f"Typing value '{TEST_INPUT_VALUE}' into the field")
    input_field.send_keys(TEST_INPUT_VALUE)

    entered_value = input_field.get_attribute("value")
    print(f"Verification -> Field currently contains: {entered_value}")

    print("Action executed successfully")


if __name__ == "__main__":
    print("Initializing Chrome WebDriver")
    with closing(webdriver.Chrome()) as driver:
        execute_data_input(driver, TARGET_URL)

    print("WebDriver session closed")