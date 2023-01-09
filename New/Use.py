from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import selenium
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import SessionNotCreatedException
from selenium.common.exceptions import WebDriverException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2Options()'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Galaxy A20DD8D'
desired_caps['app'] = ('C:/Users/user/Downloads/mobileApp.apk')
desired_caps['appPackage'] = 'co.threewin.wowzi.app'
desired_caps['appActivity'] = 'com.wazi.MainActivity'

driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_id = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                             "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                             ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android"
                                             ".view.ViewGroup/android.view.ViewGroup["
                                             "3]/android.view.ViewGroup/android.widget.HorizontalScrollView/android"
                                             ".view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android"
                                             ".view.ViewGroup[1]/android.widget.TextView")
ele_id.click()


