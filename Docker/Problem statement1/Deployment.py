from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


frontend_url = "http://localhost:30000"
backend_url = "http://localhost:5000"


driver.get(frontend_url)
greeting_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "greeting-message"))
)
assert greeting_element.text == "Hello, from the backend!"

# Verify that the backend service can successfully communicate with the frontend service
driver.get(backend_url)
greeting_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "greeting-message"))
)
assert greeting_element.text == "Hello, from the frontend!"

# Import the necessary libraries
import pytest

def test_frontend_backend_integration():
    # Access the frontend URL
    driver.get(frontend_url)

    greeting_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "greeting-message"))
    )
    assert greeting_element.text == "Hello, from the backend!"

# Run the test using Pytest
pytest.main()

#NOTE : As QA Manual Tester i have know the Automation and no hands on Experience in Lottery Domain.
#As i understand the above the given Requirements is for the Deployment for Cloud services which i am not aware about it.
# Using the AI with correct prompt i have create the script

