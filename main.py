from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

url = "https://www.nepalstock.com/floor-sheet"

# box floorsheet

driver = webdriver.Chrome()
driver.get(url)

print(f"Title: {driver.title}") #title of page

def floorsheet():
    #Prints Floorsheet
    tag = driver.find_element(By.TAG_NAME, 'h1')
    tag_title = tag.text
    print(f" NAME: {tag_title}")


# Wait for the table to be present
table_locator = (By.CSS_SELECTOR, "div.table-responsive")
table = WebDriverWait(driver, 10).until(EC.presence_of_element_located(table_locator))
table_locator = (By.CSS_SELECTOR, "div.table-responsive")
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

#write into file
with open('nepse.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
    

driver.quit()

