import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#Xpath
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
cnn_alert_login_failed='/html/body/div[1]/section[2]/section/section/section/div[2]/div[2]/div/form/div[3]/div/div[2]/p'
account_field_viblo_xpath='/html/body/div/div/div/div/div/div/div[3]/form/div[1]/div/div/input'
password_field_viblo_xpath='/html/body/div/div/div/div/div/div/div[3]/form/div[2]/div/div/input'
login_button_viblo_xpath='/html/body/div/div/div/div/div/div/div[3]/button'
ava_icon_viblo_xpath='/html/body/div/div/header/section/div[2]/div[2]/span[2]/img'
login_failed_alert_viblo_xpath='/html/body/div/div/div/div/div/div/div[3]/div[1]/div/span'
email_input_google_xpath='//*[@id="identifierId"]'
login_google_button_xpath='//*[@id="identifierNext"]/div/button'
google_login_alert_xpath='//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[2]/div[2]/div'
password_input_google_xpath='//*[@id="password"]/div[1]/div/div[1]/input'
register_viblo_checkbox_xpath='/html/body/div/div/div[2]/div/div/div/div/form/div[5]/div/label/span[2]/span'
name_alert_viblo_xpath='/html/body/div/div/div[2]/div/div/div/div/form/div[1]/div/div[2]'
register_viblo_button_xpath='/html/body/div/div/div[2]/div/div/div/div/div[1]/button'
register_practice_email_xpath='//*[@id="reg_email"]'
register_practice_password_xpath='//*[@id="reg_password"]'
register_practice_button_xpath='//*[@id="customer_login"]/div[2]/form/p[3]/input[3]'
account_name_after_regis_xpath='//*[@id="page-36"]/div/div[1]/div/p[1]/strong'
#ttn
search_result_ttn_xpath='//*[@id="txtHint"]/p'
search_input_field_ttn_xpath='//*[@id="fmsv"]'
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
def clear_cache(driver):
    driver.execute_cdp_cmd('Network.clearBrowserCache', {})
    driver.execute_cdp_cmd('Network.clearBrowserCookies', {})
def wait_for_element_by_xpath(driver, xpath, timeout=20):
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
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element
    except:
        return None
def test_login_cnn_failed( browser):
    browser.get('https://edition.cnn.com/')
    login_button = wait_for_element_by_xpath(browser, login_button_cnn_xpath)
    login_button.click()
    login_email_field = wait_for_element_by_xpath(browser, login_email_field_xpath)
    login_email_field.send_keys('tueminhlengoc@gmail.com')
    login_field_password = wait_for_element_by_xpath(browser, login_password_field_xpath)
    login_field_password.send_keys('1234@@@')
    sign_in_button = wait_for_element_by_xpath(browser, sign_in_button_xpath)
    sign_in_button.click()
    account_ava = wait_for_element_by_xpath(browser, account_login_xpath,10)
    assert account_ava is None

def test_login_cnn_success(browser):
    login_field_password = wait_for_element_by_xpath(browser, login_password_field_xpath)
    login_field_password.clear()
    login_field_password.send_keys('mật khẩu của  bạn')
    sign_in_button = wait_for_element_by_xpath(browser, sign_in_button_xpath)
    sign_in_button.click()
    account_ava = wait_for_element_by_xpath(browser, account_login_xpath,10)
    assert account_ava is not None

def test_search_cnn( browser):
    search_button = wait_for_element_by_xpath(browser, search_icon_xpath)
    search_button.click()
    search_input_field = wait_for_element_by_xpath(browser, search_bar_input_xpath)
    search_input_field.send_keys('money')
    search_input_field.send_keys(Keys.ENTER)
    search_query = wait_for_element_by_xpath(browser, search_query_xpath)
    assert search_query.text == 'money'
def test_login_viblo_failed(browser):
    browser.get('https://accounts.viblo.asia/')
    account_field=wait_for_element_by_xpath(browser,account_field_viblo_xpath)
    account_field.send_keys('minhhdlum')
    password_field_viblo=wait_for_element_by_xpath(browser,password_field_viblo_xpath)
    password_field_viblo.send_keys('1234@!#@!')
    login_viblo_button=wait_for_element_by_xpath(browser,login_button_viblo_xpath)
    login_viblo_button.click()
    login_failed_alert_viblo=wait_for_element_by_xpath(browser,login_failed_alert_viblo_xpath)
    assert login_failed_alert_viblo.text=="Wrong username/email or password"

def test_login_viblo_success(browser):
    password_field_viblo = wait_for_element_by_xpath(browser, password_field_viblo_xpath)
    password_field_viblo.clear()
    password_field_viblo.send_keys('passviblo')
    login_viblo_button = wait_for_element_by_xpath(browser, login_button_viblo_xpath)
    login_viblo_button.click()
    ava_icon_viblo = wait_for_element_by_xpath(browser, ava_icon_viblo_xpath)
    assert ava_icon_viblo.is_displayed(), "Chưa đăng nhập thành công"
def test_login_google_failed_blank(browser):
    browser.get('https://accounts.google.com/')
    login_google_button=wait_for_element_by_xpath(browser,login_google_button_xpath)
    login_google_button.click()
    google_alert=wait_for_element_by_xpath(browser,google_login_alert_xpath)
    assert google_alert.text=='Enter an email or phone number'
def test_login_google_failed_incorrect_email(browser):
    browser.get('https://accounts.google.com/')
    email_input_google=wait_for_element_by_xpath(browser,email_input_google_xpath)
    email_input_google.send_keys('mailtestkhongtontai')
    login_google_button = wait_for_element_by_xpath(browser, login_google_button_xpath)
    login_google_button.click()
    google_alert=wait_for_element_by_xpath(browser,google_login_alert_xpath)
    print(google_alert.text)
    assert google_alert.text=='Couldn’t find your Google Account'
def test_register_viblo_failed_blank_field(browser):
    clear_cache(browser)
    browser.get('https://accounts.viblo.asia/register')
    checkbox_viblo=wait_for_element_by_xpath(browser,register_viblo_checkbox_xpath)
    checkbox_viblo.click()
    register_viblo_button=wait_for_element_by_xpath(browser,register_viblo_button_xpath)
    register_viblo_button.click()
    name_alert_viblo=wait_for_element_by_xpath(browser,name_alert_viblo_xpath)
    assert name_alert_viblo.text=="Tên là bắt buộc"
def test_register_practice_automaition_testing(browser):
    browser.get('https://practice.automationtesting.in/my-account/')
    email_field=wait_for_element_by_xpath(browser,register_practice_email_xpath)
    email_field.send_keys('abbmt2@gmail.com')
    password_field=wait_for_element_by_xpath(browser,register_practice_password_xpath)
    password_field.click()
    browser.execute_script("arguments[0].value = 'Pdsa@1234#';", password_field)
    register_button=wait_for_element_by_xpath(browser,register_practice_button_xpath)
    register_button.click()
    time.sleep(5)
    account_name=wait_for_element_by_xpath(browser,account_name_after_regis_xpath)
    assert account_name=='abbmt2@gmai.com'
def test_register_practice_automaition_testing(browser):
    clear_cache(browser)
    browser.get('https://practice.automationtesting.in/my-account/')
    email_field=wait_for_element_by_xpath(browser,register_practice_email_xpath)
    email_field.send_keys('abbmt#!$2@gmail.com')
    password_field=wait_for_element_by_xpath(browser,register_practice_password_xpath)
    password_field.click()
    browser.execute_script("arguments[0].value = 'Pdsa@1234#';", password_field)
    register_button=wait_for_element_by_xpath(browser,register_practice_button_xpath)
    register_button.click()
    time.sleep(5)
    account_name=wait_for_element_by_xpath(browser,account_name_after_regis_xpath)
    assert account_name=='abbmt#!$2','Vẫn tạo được tài khoản nhưng đã loại bỏ ký tự đặc biệt'
def test_search_function_failed(browser):
    browser.get('https://www.ttn.edu.vn/?option=com_tnu&view=kqchinhquy')
    input_search_field=wait_for_element_by_xpath(browser,search_input_field_ttn_xpath)
    input_search_field.send_keys('20103029')
    input_search_field.send_keys(Keys.ENTER)
    search_result_ttn=wait_for_element_by_xpath(browser,search_result_ttn_xpath)
    print(search_result_ttn.text)
    assert search_result_ttn is not None
if __name__ == "__main__":
    pytest.main(args=["-v"])
