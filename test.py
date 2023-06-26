from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

url = "https://www.nepalstock.com/floor-sheet"

# Initialize webdriver
driver = webdriver.Chrome()
driver.get(url)

print(f"Title: {driver.title}")  # Print title of the page

while True:
    try:
        # Click the next page
        element = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Next page']")
        element.click()
    except:
        print("Error")
        break  # Break the loop if there is no next page button

    # Wait for the table to be present
    table_locator = (By.CSS_SELECTOR, "div.table-responsive")
    table = WebDriverWait(driver, 10).until(EC.presence_of_element_located(table_locator))

    # Extract data from the table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Print each row of data
    print("==============================================")
    for row in rows:
        try:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [cell.text for cell in cells]
            print(row_data)
        except StaleElementReferenceException:
            continue
    print("==============================================")

driver.quit()
