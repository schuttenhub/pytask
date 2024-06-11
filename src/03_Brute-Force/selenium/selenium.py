from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#s = Service(executable_path="chrome-linux64/chrome")
driver = webdriver.Chrome()
website = "http://127.0.0.1:8099/login"
driver.get(website)

title = ""
passwords = ["test123", "123456", "pass", "admin"]
usernames = ["test", "hallo123", "admin"]
i = 0

for username in usernames:
    for passw in passwords:
        print("Testing this password...", passw)

        input = driver.find_element(By.ID, "floatingInput")
        input.clear()
        input.send_keys(username)

        passwd = driver.find_element(By.ID, "floatingPassword")
        passwd.clear()
        passwd.send_keys(passw)

        button = driver.find_elements(By.CSS_SELECTOR, ".btn.btn-primary.w-100.py-2")
        if len(button) > 0:
            button[0].click() 
        else:
            print("Button list is empty!")

        print(driver.title)
        if driver.title != "PyTask - Login":
            print(f"Password is {passw} for username {username}")
            break