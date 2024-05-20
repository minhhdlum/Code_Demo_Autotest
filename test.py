import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_button_cnn_xpath='//div[@class="user-account-nav__icons"]/button[3]'
login_email_field_xpath='//*[@id="login-email-input"]'
login_password_field_xpath='//*[@id="login-password-input"]'
account_login_xpath='//*[@id="desktop-header-account-nav"]/nav/div[1]/button[1]'
sign_in_button_xpath='//*[@id="user-account-login-form__button"]'
search_icon_xpath='//button[@id="headerSearchIcon"]'
search_bar_input_xpath='//*[@id="pageHeader"]/div/div/div[2]/div/div[1]/form/input'
search_query_xpath='//*[@id="search__query"]'
menu_header_icon_xpath='//*[@id="headerMenuIcon"]'
sub_nav_xpath='//*[@id="pageHeader"]/div/div/div[2]'
browser=webdriver.Chrome()
def wait_for_element_by_xpath(driver, xpath, timeout=50):
    """
    Hàm chờ đợi để tìm kiếm phần tử bằng XPath trong một khoảng thời gian nhất định
    Args:
        driver: WebDriver object
        xpath: XPath của phần tử cần tìm kiếm
        timeout: Thời gian tối đa chờ đợi (mặc định là 10 giây)
    Returns:
        Phần tử nếu được tìm thấy, None nếu không tìm thấy trong thời gian chờ đợi
    """
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element
    except:
        return None
browser.get('https://cnn.com')
login_button = wait_for_element_by_xpath(browser, login_button_cnn_xpath)
login_button.click()
time.sleep(3)
login_email_field = wait_for_element_by_xpath(browser, login_email_field_xpath)
login_email_field.send_keys('tueminhlengoc@gmail.com')
login_field_password = wait_for_element_by_xpath(browser, login_password_field_xpath)
login_field_password.send_keys('Minh@2002')
sign_in_button=wait_for_element_by_xpath(browser,sign_in_button_xpath)
sign_in_button.click()
time.sleep(5)
search_button = wait_for_element_by_xpath(browser, search_icon_xpath)
search_button.click()
# search_input_field = wait_for_element_by_xpath(browser, search_bar_input_xpath)
# search_input_field.send_keys('money')
# search_input_field.send_keys(Keys.ENTER)
# search_query = wait_for_element_by_xpath(browser, search_query_xpath)
# time.sleep(20)
# a=browser.find_element(By.PARTIAL_LINK_TEXT)
# header_menu = wait_for_element_by_xpath(browser, menu_header_icon_xpath)
# header_menu.click()
time.sleep(10)