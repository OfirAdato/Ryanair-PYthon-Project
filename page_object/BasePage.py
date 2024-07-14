import time

import pytest
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driverd):
        self.driver = driverd

    def find_element(self, el):
        return self.driver.find_element(By.CSS_SELECTOR, el)

    def find_elements(self, els):
        return self.driver.find_elements(By.CSS_SELECTOR, els)

    def open_web(self, url):
        self.driver.implicitly_wait(5)
        self.driver.get(url)

    def quit_web(self):
        self.driver.implicitly_wait(5)
        self.driver.quit()

    def close_tab(self):
        self.driver.implicitly_wait(5)
        self.driver.close()

    def click_on_element(self, el):
        self.driver.implicitly_wait(10)
        element = self.find_element(el)
        self.driver.execute_script("arguments[0].style.backgroundColor = 'green';", element)
        time.sleep(0.300)
        self.driver.execute_script("arguments[0].style.backgroundColor = '';", element)
        element.click()

    def close_tabs(self):
        curr = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if handle != curr:
                self.close_tab()

    def clear(self, el):
        self.driver.implicitly_wait(5)
        self.find_element(el).clear()

    def fill_text(self, el, text):
        try:
            element = self.find_element(el)
            self.driver.implicitly_wait(5)
            self.driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)
            self.clear(el)
            element.send_keys(text)
            time.sleep(0.300)
            self.driver.execute_script("arguments[0].style.backgroundColor = '';", el)
        except JavascriptException:
            pass

    def get_text(self, el):
        self.driver.implicitly_wait(5)
        self.driver.execute_script("arguments[0].style.backgroundColor = 'red';", el)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].style.backgroundColor = '';", el)
        return str(el.text)

    def back(self):
        self.driver.back()

    def scroll_down_page(self, speed=18):
        current_scroll_position, new_height = 0, 1
        while current_scroll_position <= new_height:
            current_scroll_position += speed
            self.driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = self.driver.execute_script("return document.body.scrollHeight")

    def scroll_up_page(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
