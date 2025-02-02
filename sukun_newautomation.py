from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.by import By
import time
import os

desired_capabilities = {
  "platformName": "Android",
  "appium:platformVersion": "14.0",
  "appium:deviceName": "Galaxy A14 5G",
  "appium:app": "D:\\MobileApps\\Sukun.apk",
  "appium:GrantPermission": True,
  "appium:appWaitForLaunch\"": False,
  "appiuminteractiveDebugging": True,
  "appium:autoGrantPermission": True
}

# learning Gift commands

option = AppiumOptions().load_capabilities(desired_capabilities)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=option)
time.sleep(5)

selectserver = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/btnmore")
selectserver.click()
time.sleep(3)
adddeleteserver = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/addButton")
adddeleteserver.click()
time.sleep(8)
scan = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"Scan QR Code\"]/android.widget.ImageView")
scan.click()
time.sleep(2)
whileusingallow = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
whileusingallow.click()
time.sleep(5)
back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
back.click()
time.sleep(5)
selectserver = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/serverlisttext")
selectserver.click()
time.sleep(5)
adddeleteserver = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/addButton")
adddeleteserver.click()
time.sleep(5)
delete = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Server name")
delete.click()
time.sleep(5)
yes = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
yes.click()
time.sleep(5)
selectserver = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/serverlisttext")
selectserver.click()
time.sleep(5)
adddeleteserver = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/addButton")
adddeleteserver.click()
time.sleep(5)
entercodemanually = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"Enter Code Manually\"]/android.widget.ImageView")
entercodemanually.click()
time.sleep(5)
ServerName = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/servername")
ServerName.click()
ServerName.send_keys("EUM")
time.sleep(5)
ServerUrl = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/serverURL")
ServerUrl.click()
ServerUrl.send_keys("https://sahaj.liberty.online:27112/api/OOTP")
time.sleep(5)
Add = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/btnAddUpdate")
Add.click()
time.sleep(5)
Yes = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
Yes.click()
time.sleep(5)
delete = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Server name")
delete.click()
time.sleep(5)
yes = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
yes.click()
time.sleep(5)
selectserver = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/serverlisttext")
selectserver.click()
time.sleep(5)
adddeleteserver = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/addButton")
adddeleteserver.click()
time.sleep(5)
entercodemanually = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"Enter Code Manually\"]/android.widget.ImageView")
entercodemanually.click()
time.sleep(5)
pasteenterqrcode = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/serverToken")
pasteenterqrcode.click()
pasteenterqrcode.send_keys("RVVNO2h0dHBzOi8vc2FoYWoubGliZXJ0eS5vbmxpbmU6MjcxMTIvYXBpL09PVFA=")
time.sleep(5)
driver.back()
time.sleep(5)
add = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/btnAddToken")
add.click()
time.sleep(5)
yes = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
yes.click()
time.sleep(5)
back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
back.click()
time.sleep(5)
selectserver = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/serverlisttext")
selectserver.click()
time.sleep(5)
EUM = driver.find_element(by=AppiumBy.ID, value="android:id/text1")
EUM.click()
time.sleep(5)
enterloginid = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/username")
enterloginid.click()
enterloginid.send_keys("4111932853")
time.sleep(5)
enterpassword = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/password")
enterpassword.click()
enterpassword.send_keys("Secure@123")
time.sleep(5)
showpassword = driver.find_element(by=AppiumBy.ID, value="com.secure.beanbag:id/tvShowPassword")
showpassword.click()
time.sleep(5)
driver.back()
time.sleep(5)
Continue = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/btnsignin")
Continue.click()
time.sleep(10)
enterotp = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/otpText")
enterotp.click()
enterotp.send_keys("4166")
time.sleep(5)
Confirmotp = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/otpVerifyBtn")
Confirmotp.click()
time.sleep(5)
Generate = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/txtprogress_bar")
Generate.click()
time.sleep(5)
idbtnMenu = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/btnMenu")
idbtnMenu.click()
time.sleep(5)
checkstatus = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView")
checkstatus.click()
time.sleep(5)
ok = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
ok.click()
time.sleep(5)
idbtnMenu = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/btnMenu")
idbtnMenu.click()
time.sleep(5)
Remove = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView")
Remove.click()
time.sleep(5)
No = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
No.click()
time.sleep(5)
idbtnMenu = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/btnMenu")
idbtnMenu.click()
time.sleep(5)
Activate = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.TextView")
Activate.click()
time.sleep(5)
ok = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
ok.click()
time.sleep(5)
openmenu = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/navigation_dashboard")
openmenu.click()
time.sleep(5)
about = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView")
about.click()
time.sleep(5)
selectaserver = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/spinner_server_list")
selectaserver.click()
time.sleep(5)
EUM = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]")
EUM.click()
time.sleep(5)
FAQ = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/faq")
FAQ.click()
time.sleep(5)
driver.back()
time.sleep(5)
privacypolicy = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/privacypolicy")
privacypolicy.click()
time.sleep(5)
driver.back()
time.sleep(5)
back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
back.click()
time.sleep(5)
Adduser = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView")
Adduser.click()
time.sleep(5)
back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
back.click()
time.sleep(5)
serverdetail = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView")
serverdetail.click()
time.sleep(5)
back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
back.click()
time.sleep(5)
adduseraccount = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView")
adduseraccount.click()
time.sleep(5)
idbtnMenu = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/btnmore")
idbtnMenu.click()
time.sleep(5)
EUM = driver.find_element(by=AppiumBy.ID, value="android:id/text1")
EUM.click()
time.sleep(5)
button = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/serverlisttext")
button.click()
time.sleep(5)
Adddelete = driver.find_element(by=AppiumBy.ID, value="com.ootp:id/addButton")
Adddelete.click()
time.sleep(5)
delete = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Server name")
delete.click()
time.sleep(5)
yes = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
yes.click()
time.sleep(5)

print("sukun testing complete successfully, ThankYou")