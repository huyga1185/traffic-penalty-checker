import pytesseract
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image
from datetime import datetime
import time
import os


def fill_form_and_submit(browser_driver, bkx, loai):

    if not os.path.exists('results'):
        try:
            #neu khong tao folder backup
            os.makedirs('results')
        except PermissionError:
            print("Khong co quyen tao folder!")
            return

    service = Service(browser_driver)

    driver  = webdriver.Chrome(service=service)

    driver.get('https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html')

    #xpath cua textbox bien kiem soat
    bkx_txtbox_xpath = '//*[@id="formBSX"]/div[2]/div[1]/input'

    bkx_txtbox = driver.find_element(By.XPATH, bkx_txtbox_xpath)
    bkx_txtbox.send_keys(bkx)

    loai_xe_dropdown_xpath = '//*[@id="formBSX"]/div[2]/div[2]/select'
    loai_xe_dropdown = Select(driver.find_element(By.XPATH, loai_xe_dropdown_xpath))
    loai_xe_dropdown.select_by_index(loai)

    captcha_img_xpath = '//*[@id="imgCaptcha"]'
    captcha_img = driver.find_element(By.XPATH, captcha_img_xpath)
    location = captcha_img.location
    size = captcha_img.size

    driver.save_screenshot('full_page.png')
    img = Image.open('full_page.png')
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    captcha_image = img.crop((left, top, right, bottom))
    captcha_txt = pytesseract.image_to_string(captcha_image).strip()

    captcha_txtbox_xpath = '//*[@id="formBSX"]/div[2]/div[3]/div/input'
    captcha_txtbox = driver.find_element(By.XPATH, captcha_txtbox_xpath)
    captcha_txtbox.send_keys(captcha_txt)

    tra_cuu_btn_xpath = '//*[@id="formBSX"]/div[2]/input[1]'
    tra_cuu_btn = driver.find_element(By.XPATH, tra_cuu_btn_xpath)
    tra_cuu_btn.click()
    time.sleep(15)
    timestamp = datetime.now().strftime("%H%M%S_%Y%m%d")
    file_name = f"results/result{timestamp}.png"
    driver.save_screenshot(file_name)
    os.remove('full_page.png')