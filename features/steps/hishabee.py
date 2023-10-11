import time
import pytest

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://hishabee.business/"

@given('I launch the Chrome Browser')
def open_chrome(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()


@when('I open the Hishabee Business Homepage')
def open_hishabee(context):
    context.driver.get(BASE_URL)

    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div/div/section[1]/div/div[1]/div/div[2]/div/h1")))
    element.is_displayed()

@then('I click Web Login button')
def login_button(context):
    wait = WebDriverWait(context.driver, 10)
    web_login = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                           "/html[1]/body[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[7]/a[1]")))
    web_login.click()

@then('Enter the phone number and click Continue button')
def input_number(context):
    wait = WebDriverWait(context.driver, 10)
    phone_number = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='01521xxxxxx']")))
    phone_number.send_keys("01715491942")

    contButtton = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
    contButtton.click()


@then('Enter the pin and click signin button')
def input_pin(context):
    wait = WebDriverWait(context.driver, 10)
    pin = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='00xxx']")))
    pin.send_keys("00000")

    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then('User must successfully login to the Shop select page')
def shop_page(context):
    wait = WebDriverWait(context.driver, 10)
    text = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div/div[3]/div/div/p"))).text
    assert text == "Select your shop"
    time.sleep(3)

@when('I press add shop button')
def abb_button(context):
    wait = WebDriverWait(context.driver, 10)
    button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='+ Add Shop']")))
    button.click()

@then('I fill up the Create shop form')
def fill_up(context):
    wait = WebDriverWait(context.driver, 25)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='mb-5 mt-3 text-center']")))
    time.sleep(3)

    logo = context.driver.find_element(By.XPATH, "//img[@src='/assets/images/hishabee/plus.png']")
    logo.click()
    time.sleep(3)

    keyword = Controller()
    keyword.type("C:\\Users\\nabil\\Desktop\\HishabeeAutomationTest\\file\\pet.jpg")
    keyword.press(Key.enter)
    keyword.release(Key.enter)
    time.sleep(3)

    shop_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Shop name']")))
    shop_name.send_keys("Pet House")
    time.sleep(1)

    shop = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[4]//div[1]//select[1]")))
    s = Select(shop)
    s.select_by_index(13)
    time.sleep(1)

    division = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[5]//div[1]//select[1]")))
    d = Select(division)
    d.select_by_index(3)
    time.sleep(1)

    district = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[6]//div[1]//select[1]")))
    d = Select(district)
    d.select_by_index(1)
    time.sleep(2)

    area = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[7]//div[1]//select[1]")))
    a = Select(area)
    a.select_by_index(9)
    time.sleep(1)

    address = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Address']")))
    address.send_keys("demra, dhaka")
    time.sleep(1)

    create_shop = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
    create_shop.click()

    permission = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Online order management']")))
    permission.click()
    time.sleep(4)

    submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
    submit.click()
    time.sleep(4)


@when('I enter the business page')
def business(context):
    wait = WebDriverWait(context.driver, 10)
    text = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div/div[3]/div/div/div[1]/div/div/h5"))).text
    assert text == "Today's Sale"
    time.sleep(3)


@then('I click in nav bar')
def navbar(context):
    wait = WebDriverWait(context.driver, 10)
    nav = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/nav/div[1]/i")))
    nav.click()

@then('Go to the Contacts page')
def contacts(context):
    wait = WebDriverWait(context.driver, 10)
    cont_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Contacts']")))
    cont_button.click()

@then('Close the nav bar')
def navclose(context):
    wait = WebDriverWait(context.driver, 10)
    close_nav = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div[1]/div")))
    close_nav.click()

    time.sleep(4)

@then('I click Add new customer')
def add_cust(context):
    wait = WebDriverWait(context.driver, 10)
    add_cust_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-md-5 col-lg-5 col-5 bg-primary p-2 mt-3']")))
    add_cust_button.click()

@then('I provide the name, phone number, address')
def add_cust(context):
    wait = WebDriverWait(context.driver, 10)
    name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
    phone = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Mobile Number']")))
    address = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Address']")))
    name.send_keys('Rafiul')
    phone.send_keys('01900000000')
    address.send_keys('Rampura')

@then('Click the save button')
def save(context):
    wait = WebDriverWait(context.driver, 10)
    save_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
    save_button.click()
    time.sleep(4)

@then('I click User bar')
def click_user(context):
    wait = WebDriverWait(context.driver, 10)
    user = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='productShoingTable']/div/table/tbody/tr/th")))
    user.click()
    time.sleep(1)

@then('I Click the edit button')
def edit_user(context):
    wait = WebDriverWait(context.driver, 10)
    user_edit = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='/assets/images/hishabee/edit-contact.png']")))
    user_edit.click()
    time.sleep(3)

@then('I edit the phone number and address')
def number_address(context):
    wait = WebDriverWait(context.driver, 10)
    number = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='মোবাইল নাম্বার']")))
    address = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='ঠিকানা']")))
    number.click()
    number.clear()
    number.send_keys('01900000011')
    address.click()
    address.clear()
    address.send_keys('Banasree')

@then('Click the save')
def update_button(context):
    wait = WebDriverWait(context.driver, 10)
    update = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
    update.click()

    time.sleep(4)

@when('I again click User bar')
def user_bar(context):
    wait = WebDriverWait(context.driver, 10)
    user = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='productShoingTable']/div/table/tbody/tr/th")))
    user.click()
    time.sleep(3)

@then('I again Click the edit button')
def edit_user_button(context):
    wait = WebDriverWait(context.driver, 10)
    user_edit = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='/assets/images/hishabee/edit-contact.png']")))
    user_edit.click()
    time.sleep(4)

@then('I click delete button')
def delete_user(context):
    wait = WebDriverWait(context.driver, 10)
    delete_user = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div/div[3]/div/div/div[3]/button")))

    delete_user.click()
    time.sleep(4)

@then('Confirm the delete user')
def confirm_delete(context):
    wait = WebDriverWait(context.driver, 10)
    confirm_delete = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Yes']")))
    confirm_delete.click()

    time.sleep(1)
    context.driver.close()

















