from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path="chrome-linux64/chrome")
driver = webdriver.Chrome(service=s)
website = "http://127.0.0.1:8099/login"
driver.get(website)

title = ""
passwords = ["test123", "123456", "pass"]
i = 0
for passw in passwords:
    print("Testing this password...", passw)
    res = driver.find_elements(By.CLASS_NAME, "form-control")
    #assert(len(res) == 2)
    res[0].clear()
    res[0].send_keys("Derk")    # --> Hier Login Field rein schreiben
    res[1].clear()
    res[1].send_keys(passw)

    button = driver.find_elements(By.CLASS_NAME, "btn btn-primary w-100 py-2")
    #assert(len(res) == 2)
    button[0].click()

    print(driver.title)
    if driver.title != "Login_page":
        print(f"Password is {passw}")
        break