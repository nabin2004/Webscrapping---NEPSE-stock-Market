from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

url = "https://www.nepalstock.com/floor-sheet"

# Initialize webdriver
driver = webdriver.Chrome()
driver.get(url)

print(f"Title: {driver.title}")  # Print title of the page

def click_next_page():
    # Click the next page button
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[aria-label='Next page']"))
        )
        element.click()
    except (NoSuchElementException, TimeoutException):
        return False
    return True


def extractor():
    # Wait for the table to be present
    table_locator = (By.CSS_SELECTOR, "div.table-responsive")
    table = WebDriverWait(driver, 10).until(EC.presence_of_element_located(table_locator))

    # Extract data from the table
    rows = table.find_elements(By.TAG_NAME, "tr")
    data = [['SN','Contract No.','Stock Symbol','Buyer','Seller','Quantity','Rate (Rs)','Amount (Rs)']]

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = []
        for cell in cells:
            row_data.append(cell.text)
        data.append(row_data)

    # Print each row of data
    print("==============================================")
    for i in data:
        print(i)
    print("==============================================")

extractor()
while True:
    click_next_page()
    extractor