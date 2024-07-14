import sys

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_object.BasePage import BasePage 


class Flight(BasePage):
    def __init__(self, driverd):
        super().__init__(driverd)

    def cheapest_dpt_flight(self):
        """
        the code will choose the cheapest departure flight
        """
        max_price = sys.maxsize
        min_price = None
        flight_details = self.find_elements(".journeys-wrapper>div:nth-child(1) ul>li")
        for flight in flight_details:
            self.driver.flight_price = None
            self.driver.is_display = True
            try:
                flight_price = flight.find_element(By.CSS_SELECTOR, ".price__integers")
                is_display = flight_price.is_displayed()
            except NoSuchElementException:
                self.driver.is_display = False
                print("the element not exist")
                continue
            if is_display:
                print("I can see number")
                price_num = int(self.get_text(flight_price))
                print("the price is ", price_num)
                if price_num < max_price:
                    max_price = price_num
                    min_price = flight_price
            else:
                print("I can not see number")
                continue

        print("The smallest number is: ", max_price)
        min_price.click()
        self.click_on_element(".flight-card-summary__select-btn")

    def cheapest_rtn_flight(self):
        """
        the code will choose the cheapest return flight
        """
        max_price = sys.maxsize
        min_price = None
        flight_details = self.find_elements(".journeys-wrapper>div:nth-child(2) ul>li")
        for flight in flight_details:
            self.driver.flight_price = None
            self.driver.is_display = True
            try:
                flight_price = flight.find_element(By.CSS_SELECTOR, ".price__integers")
                is_display = flight_price.is_displayed()
            except NoSuchElementException:
                self.driver.is_display = False
                print("the element not exist")
                continue
            if is_display:
                print("I can see number")
                price_num = int(self.get_text(flight_price))
                print("the price is ", price_num)
                if price_num < max_price:
                    max_price = price_num
                    min_price = flight_price
            else:
                print("I can not see number")
                continue

        print("The smallest number is: ", max_price)
        min_price.click()
        self.click_on_element(".flight-card-summary__select-btn")

    def extra_fare(self, extra_name):
        """
         add extra fare.
        :param extra_name:
        """
        extras = self.find_elements(".fare-header__description")
        try:
            for extra in extras:
                extra_title = extra.find_element(By.CSS_SELECTOR, ".fare-header__name.title-m-lg")
                if extra_name in self.get_text(extra_title).lower():
                    action = ActionChains(self.driver)
                    action.move_to_element(extra_title).click().perform()
                    break
        except (NoSuchElementException, ElementClickInterceptedException):
            pass

    def log_in_later(self):
        """
        you can log in later, and forward to choose gender.
        """
        self.click_on_element(".login-touchpoint__login-later.title-m-lg.title-m-sm")

    def gender(self, gender_title, first_name, last_name):
        """
        add your gender.
        :param gender_title:
        :param first_name:
        :param last_name:
        """
        self.click_on_element(".dropdown.body-l-lg.body-l-sm>.dropdown__toggle")
        genders = self.find_elements(".dropdown__menu-items .dropdown-item__link")
        for gender in genders:
            gender_name = gender.find_element(By.CSS_SELECTOR,
                                              ".dropdown__menu-items .dropdown-item__link .dropdown-item__content")
            if gender_title in self.get_text(gender_name).lower():
                gender_name.click()
            break
        self.fill_text('[name="form.passengers.ADT-0.name"]', first_name)
        self.fill_text('[name="form.passengers.ADT-0.surname"]', last_name)
        self.click_on_element("div > div > span > button")
