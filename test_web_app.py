import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless") # لو عايز تشغله في الخلفية
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_form_submission(driver):
    # فتح صفحة ويب تجريبية للاختبار (مثال: Form Authentication Page)
    driver.get("https://the-internet.herokuapp.com/login")
    
    # إدخال بيانات الدخول
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.TAG_NAME, "button")
    
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")
    login_button.click()
    
    time.sleep(2)
    
    # التحقق من نجاح تسجيل الدخول (Assertion)
    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message
    print("Test Passed: Login successful and message verified.")

def test_invalid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.TAG_NAME, "button")
    
    username_field.send_keys("wrong_user")
    password_field.send_keys("wrong_password")
    login_button.click()
    
    time.sleep(2)
    
    error_message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in error_message
    print("Test Passed: Invalid login error message verified.")
