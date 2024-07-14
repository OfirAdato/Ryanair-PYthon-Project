import time

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage


class MainPage(BasePage):
    def __init__(self, driverd):
        super().__init__(driverd)

    def cookies(self):
        """
        accept cookies.
        """
        try:
            self.click_on_element('[data-ref="cookie.accept-all"]')
        except NoSuchElementException:
            pass

    def departure_country(self, country_name, city_name):
        """
        choose your departure country.
        :param country_name:
        :param city_name:
        """
        self.click_on_element("#input-button__departure")
        countries = self.find_elements(".countries__country.body-l-lg.body-l-sm.ng-star-inserted")
        for country in countries:
            country_title = country.find_element(By.CSS_SELECTOR, ".countries__country-inner.ng-star-inserted")
            if country_name in self.get_text(country).lower():
                country_title.click()
                break

        cities = self.find_elements(".list__airports-scrollable-container.small-height>.ng-star-inserted")
        for city in cities:
            city_title = city.find_element(By.CSS_SELECTOR, ".body-l-lg.body-l-sm.airport-item")
            if city_name in self.get_text(city_title).lower():
                city_title.click()
                break

    def destination_country(self, country_name, city_name):
        """
        choose your destination country.
        :param country_name:
        :param city_name:
        """
        countries = self.find_elements(".countries__country.body-l-lg.body-l-sm.ng-star-inserted")
        for country in countries:
            country_title = country.find_element(By.CSS_SELECTOR, ".countries__country-inner.ng-star-inserted")
            if country_name in self.get_text(country).lower():
                country_title.click()
                break

        cities = self.find_elements(".list__airports-scrollable-container.large-height>.ng-star-inserted")
        for city in cities:
            city_title = city.find_element(By.CSS_SELECTOR, ".body-l-lg.body-l-sm.airport-item")
            try:
                if city_name in self.get_text(city_title).lower():
                    time.sleep(0.2)
                    city_title.click()
                    break
            except ElementClickInterceptedException:
                self.driver.implicitly_wait(10)
                pass

    def depart_date(self, month_name, day_number):
        """
        choose your departure date
        :param month_name:
        :param day_number:
        """
        months = self.find_elements(".m-toggle__scrollable-item.ng-star-inserted")
        for month in months:
            month_title = month.find_element(By.CSS_SELECTOR, ".m-toggle__month")
            if month_name in self.get_text(month_title).lower():
                month_title.click()
                break
        days = self.find_elements(".calendar-body__cell-wrap.ng-star-inserted")
        for day in days:
            try:
                day_num = day.find_element(By.CSS_SELECTOR, ".calendar-body__cell")
                try:
                    if day_number in self.get_text(day_num):
                        day_num.click()
                        break
                except (NoSuchElementException, ElementClickInterceptedException):
                    day_number = str(int(day_number) + 1)
                    pass
            except ElementClickInterceptedException:
                continue

    def return_date(self, month_name, day_number):
        """
        choose your return date.
        :param month_name:
        :param day_number:
        """
        months = self.find_elements(".m-toggle__scrollable-item.ng-star-inserted")
        for month in months:
            month_title = month.find_element(By.CSS_SELECTOR, ".m-toggle__month")
            if month_name in self.get_text(month_title).lower():
                month_title.click()
                break

        days = self.find_elements(".calendar-body__cell-wrap.ng-star-inserted")
        for day in days:
            try:
                day_num = day.find_element(By.CSS_SELECTOR, ".calendar-body__cell")
                is_enabled = day_num.is_enabled()
                if is_enabled:
                    try:
                        if day_number in self.get_text(day_num):
                            day_num.click()
                            break
                    except (NoSuchElementException, ElementClickInterceptedException):
                        day_number = str(int(day_number) + 1)
                        pass
            except ElementClickInterceptedException:
                continue

    def passenger(self):
        """
        choose your number of passenger.
        """
        self.click_on_element(".passengers__confirm-button.ry-button--anchor-blue.ry-button--anchor")

    def submit_trip(self):
        """
        accept all the data.
        """
        self.click_on_element(".flight-search-widget__start-search-cta.ng-tns-c983940023-3")
