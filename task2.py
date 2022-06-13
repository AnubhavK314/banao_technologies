"""
{
  "platformName": "android",
  "appium:appActivity": "com.atg.world.activity.SplashActivity",
  "appium:appWaitDuration": "5000",
  "appium:appExecTimeout": "50000",
  "appium:appPackage": "com.ATG.World",
  "appium:deviceName": "emulator-5554",
  "appium:driver": "http://localhost:4723/wd/hub"
}
"""

import time
from appium import webdriver

desire_cap = {
    "platformName": "android",
    "appium:appActivity": "com.atg.world.activity.SplashActivity",
    "appium:appWaitDuration": "5000",
    "appium:appExecTimeout": "50000",
    "appium:appPackage": "com.ATG.World",
    "appium:deviceName": "emulator-5554",
    "appium:driver": "http://127.0.0.1:4723/wd/hub"
}


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desire_cap)
time.sleep(2)

# allow ATG acess media
time.sleep(2)

# Get start main page
driver.find_element_by_id("com.ATG.World:id/getStartedTv").click()
time.sleep(2)

# email login click
driver.find_element_by_id("com.ATG.World:id/login_email").click()
time.sleep(2)

# login via email
driver.find_element_by_id("com.ATG.World:id/email_phone_login").send_keys("hello@atg.world")
driver.find_element_by_id("com.ATG.World:id/signinbutton").click()
time.sleep(2)
driver.find_element_by_id("com.ATG.World:id/password").send_keys("Pass@123")
driver.back()
time.sleep(3)
driver.find_element_by_id("com.ATG.World:id/passwordloginbutton").click()
driver.implicitly_wait(3)

# got it click
driver.find_element_by_id("com.ATG.World:id/btnGotit").click()
driver.implicitly_wait(5)

# click pencile btn to create post
driver.find_element_by_id("com.ATG.World:id/fab").click()
driver.implicitly_wait(5)

#post image click
driver.find_element_by_id("com.ATG.World:id/image_fab_clicked").click()
driver.implicitly_wait(5)

#selecting picture
driver.find_element_by_id("com.ATG.World:id/image_cell").click()
driver.implicitly_wait(5)

#clicking next
driver.find_element_by_id("com.ATG.World:id/toolbar_post_action").click()
driver.implicitly_wait(5)

#adding caption
driver.find_element_by_id("com.ATG.World:id/caption_edit_text").send_keys("First Post via Appium")
driver.implicitly_wait(2)

#posting
driver.find_element_by_id("com.ATG.World:id/toolbar_post_action").click()
driver.implicitly_wait(5)

#complete posting
driver.find_element_by_id("com.ATG.World:id/selection_done_btn").click()
time.sleep(3)

driver.back()
time.sleep(2)

driver.find_element_by_id("com.ATG.World:id/homeBottomSheetFragment").click()
driver.implicitly_wait(5)

driver.find_element_by_id("com.ATG.World:id/myPostsLabelTextView").click()

print("success")
time.sleep(10)

driver.quit()
