from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#s = Service(executable_path="chrome-linux64/chrome")
driver = webdriver.Chrome()
website = "http://10.0.0.13:8099/login"
driver.get(website)

title = ""
passwords = ["test123", "123456", "pass", "admin"]
usernames = ["test", "hallo123", "admin"]
i = 0

for username in usernames:
    input = driver.find_element(By.ID, "floatingInput")
    input.clear()
    input.send_keys(username)

    for passw in passwords:
        print("Testing this password...", passw)

        passwd = driver.find_element(By.ID, "floatingPassword")
        passwd.clear()
        input.send_keys(passw)

        button = driver.find_elements(By.CLASS_NAME, "btn btn-primary w-100 py-2")
        #assert(len(res) == 2)
        button.click()

        print(driver.title)
        if driver.title != "PyTask - Login":
            print(f"Password is {passw}")
            break