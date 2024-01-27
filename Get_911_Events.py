from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'your_url_here' with the URL of the website containing the JavaScript table
url = 'https://911events.ongov.net/CADInet/app/_rlvid.jsp?_rap=pc_Cad911Toweb.doLink1Action&_rvip=/events.jsp'

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get(url)

# Wait for the JavaScript table to load (adjust the timeout as needed)
wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.ID, 'form1')))  # Replace 'table_id_here' with the actual ID of the table


# Extract data from the table
table_data = []
rows = table.find_elements(By.TAG_NAME, 'tr')  # Use By.TAG_NAME to find elements by tag name
for row in rows:
    row_data = []
    cells = row.find_elements(By.TAG_NAME, 'td')  # Use By.TAG_NAME to find elements by tag name
    for cell in cells:
        row_data.append(cell.text)
    if row_data:  # Check if row_data is not empty (to avoid empty rows)
        table_data.append(row_data)

# Close the WebDriver
driver.quit()

# Print the table data
for row in table_data:
    print(row)