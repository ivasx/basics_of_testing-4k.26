from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


TARGET_URL = "https://the-internet.herokuapp.com/infinite_scroll"
IMPLICIT_WAIT_TIME = 3
SCROLL_ITERATIONS = 5
SCROLL_OFFSET_Y = 1500


def execute_infinite_scroll(driver: webdriver.Chrome, url: str) -> None:
    print(f"Navigating to: {url}")
    driver.get(url)
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)

    actions = ActionChains(driver)

    print(f"Starting infinite scroll automation ({SCROLL_ITERATIONS} iterations)")

    for attempt in range(1, SCROLL_ITERATIONS + 1):
        elements_before = len(driver.find_elements(by=By.CLASS_NAME, value="jscroll-added"))
        print(f"Executing scroll {attempt}/{SCROLL_ITERATIONS}")
        actions.scroll_by_amount(delta_x=0, delta_y=SCROLL_OFFSET_Y).perform()
        WebDriverWait(driver, timeout=10).until(
            lambda d: len(d.find_elements(by=By.CLASS_NAME, value="jscroll-added")) > elements_before
        )
        elements_after = len(driver.find_elements(by=By.CLASS_NAME, value="jscroll-added"))
        print(f"Scroll {attempt} completed -> Total content blocks dynamically loaded: {elements_after}")

    print("Infinite scroll sequence executed successfully")


if __name__ == "__main__":
    print("Initializing Chrome WebDriver")
    with closing(webdriver.Chrome()) as driver:
        execute_infinite_scroll(driver, TARGET_URL)

    print("WebDriver session closed")