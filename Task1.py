from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.by import By

TARGET_URL = "https://the-internet.herokuapp.com/"
WAIT_TIME = 3


def fetch_and_display_links(driver, url):
    driver.get(url)
    driver.implicitly_wait(WAIT_TIME)
    link_elements = driver.find_elements(by=By.TAG_NAME, value="a")
    valid_link_counter = 1

    for element in link_elements:
        link_text = element.text.strip()
        link_url = element.get_attribute("href")

        if link_text and link_url:
            print(f"{valid_link_counter}. {link_text} - {link_url}")
            valid_link_counter += 1


if __name__ == "__main__":
    with closing(webdriver.Chrome()) as driver:
        fetch_and_display_links(driver, TARGET_URL)

    print("Finish.")