from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
IMPLICIT_WAIT_TIME = 5
EXPLICIT_WAIT_TIME = 10


def run_saucedemo_scenario(driver: webdriver.Chrome) -> None:
    print(f"Step 1: Navigating to {BASE_URL} and logging in...")
    driver.get(BASE_URL)
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)

    driver.find_element(by=By.ID, value="user-name").send_keys(USERNAME)
    driver.find_element(by=By.ID, value="password").send_keys(PASSWORD)
    driver.find_element(by=By.ID, value="login-button").click()

    print("Step 2: Inspecting all products...")
    inventory_items = driver.find_elements(by=By.CLASS_NAME, value="inventory_item_name")
    total_items = len(inventory_items)

    for index in range(total_items):
        current_items = driver.find_elements(by=By.CLASS_NAME, value="inventory_item_name")
        item_title = current_items[index].text
        print(f"  - Viewing product details: {item_title}")
        current_items[index].click()
        driver.back()

    print("Step 3: Adding two products to the shopping cart...")
    add_to_cart_buttons = driver.find_elements(by=By.CSS_SELECTOR, value=".btn_inventory")
    add_to_cart_buttons[0].click()
    add_to_cart_buttons[1].click()

    print("Step 4: Navigating to the cart and removing one item...")
    driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link").click()

    remove_buttons = driver.find_elements(by=By.CSS_SELECTOR, value=".cart_button")
    if remove_buttons:
        remove_buttons[0].click()

    print("Step 5: Proceeding to checkout and filling delivery details...")
    driver.find_element(by=By.ID, value="checkout").click()

    driver.find_element(by=By.ID, value="first-name").send_keys("Ivan")
    driver.find_element(by=By.ID, value="last-name").send_keys("Ambroziak")
    driver.find_element(by=By.ID, value="postal-code").send_keys("76000")
    driver.find_element(by=By.ID, value="continue").click()

    print("Step 6: Confirming the order completion...")
    finish_button = WebDriverWait(driver, EXPLICIT_WAIT_TIME).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )
    finish_button.click()

    print("Step 7: Returning to the main inventory page...")
    back_home_button = WebDriverWait(driver, EXPLICIT_WAIT_TIME).until(
        EC.element_to_be_clickable((By.ID, "back-to-products"))
    )
    back_home_button.click()

    print("Step 8: Opening sidebar menu and performing secure logout...")
    driver.find_element(by=By.ID, value="react-burger-menu-btn").click()

    logout_link = WebDriverWait(driver, EXPLICIT_WAIT_TIME).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()

    print("End-to-end automation scenario completed successfully.")


if __name__ == "__main__":
    print("Configuring Chrome Options to bypass security warnings...")
    chrome_options = Options()

    chrome_options.add_argument("--incognito")

    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    print("Initializing Chrome WebDriver in Incognito mode...")
    with closing(webdriver.Chrome(options=chrome_options)) as driver:
        run_saucedemo_scenario(driver)

    print("Browser session securely closed. Execution finished.")