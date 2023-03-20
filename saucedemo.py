from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Saucedemo:
    
    #Kullanıcı adı ve şifresi boş iken,
    def test_username_ve_password_null(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
  
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
     

        username.send_keys("")
        password.send_keys("")


        login_button.click()
        error_message_container = driver.find_element(
            By.CLASS_NAME, "error-message-container")

        expected_message = "Epic sadface: Username is required"
        current_message = error_message_container.text
        status = expected_message == current_message

        print(f"Test Durumu: {'Geçerli' if status else 'Geçersiz'}")

        sleep(3)
#adı kısmı yazılı şifre boş iken,
    def test_password_null(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")


     username = driver.find_element(By.ID, "user-name")
     password = driver.find_element(By.ID, "password")
     login_button = driver.find_element(By.ID, "login-button")
 
     username.send_keys("kod")
     password.send_keys("")
     
     login_button.click()
     error_message_container = driver.find_element(
        By.CLASS_NAME, "error-message-container")

     expected_message = "Epic sadface: Password is required"
     current_message = error_message_container.text
     status = expected_message == current_message

     print(f"Test Durumu: {'Geçerli' if status else 'Geçersiz'}")

     sleep(3)
#kilitli kullanıcı
    def test_user_locked_error_text(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     

     username = driver.find_element(By.ID, "user-name")
     password = driver.find_element(By.ID, "password")
     login_button = driver.find_element(By.ID, "login-button")
     

     username.send_keys("locked_out_user")
     password.send_keys("secret_sauce")
     

     login_button.click()
     error_message_container = driver.find_element(
        By.CLASS_NAME, "error-message-container")

     expected_message = "Epic sadface: Sorry, this user has been locked out."
     current_message = error_message_container.text
     status = expected_message == current_message

     print(f"Test Durumu: {'Geçerli' if status else 'Geçersiz'}")

     sleep(3)
# çarpı butonuna basar
    def test_carpi_button_click(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
  
     username = driver.find_element(By.ID, "user-name")
     password = driver.find_element(By.ID, "password")
     login_button = driver.find_element(By.ID, "login-button")
    

     username.send_keys("")
     password.send_keys("")
    

     login_button.click()
     error_message_container = driver.find_element(
        By.CLASS_NAME, "error-message-container")
     error_button = driver.find_element(By.CLASS_NAME, "error-button")

     error_button.click()

     print("\nçarpı iconuna tıklama testi")

     sleep(3)
#site açııyor mu kontrol eder
    def test_standartuser_input_inventoryhtml(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
   
     username = driver.find_element(By.ID, "user-name")
     password = driver.find_element(By.ID, "password")
     login_button = driver.find_element(By.ID, "login-button")

     username.send_keys("standard_user")
     password.send_keys("secret_sauce")

     login_button.click()

     current_url = driver.current_url
     expected_url = "https://www.saucedemo.com/inventory.html"
     status = current_url == expected_url

     print(f"Test Durumu: {'Geçerli' if status else 'Geçersiz'}")

     sleep(3)
# 6 ürürn var mı onu listeler
    def test_6_item_list(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")

     username = driver.find_element(By.ID, "user-name")
     password = driver.find_element(By.ID, "password")
     login_button = driver.find_element(By.ID, "login-button")

     username.send_keys("standard_user")
     password.send_keys("secret_sauce")

     login_button.click()

     items = driver.find_elements(By.CLASS_NAME, "inventory_item")
     expected_item_count = 6
     status = len(items) == expected_item_count

     print(f"Test Durumu: {'Geçerli' if status else 'Geçersiz'}")

    sleep(3)
testClass = Saucedemo()

testClass.test_username_ve_password_null()
testClass.test_password_null()
testClass.test_user_locked_error_text()
testClass.test_carpi_button_click()
testClass.test_standartuser_input_inventoryhtml()
testClass.test_6_item_list()
