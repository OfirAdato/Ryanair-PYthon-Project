from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage


class Seats(BasePage):
    def __init__(self, driverd):
        super().__init__(driverd)

    def choose_dpt_seat(self, row_number):
        """
        choose your row number to sit on the departure flight.
        :param row_number:
        """
        seat_rows = self.find_elements(".seatmap__seats")
        is_enabled = None
        seat_num = None
        for row in seat_rows:
            try:
                row_num = row.find_element(By.CSS_SELECTOR, ".seatmap__seat.seatmap__seat--aisle.b2.ng-star-inserted")
                is_display = row_num.is_displayed()
            except NoSuchElementException:
                print("the element not exist")
                continue
            if is_display:
                print("I can see number")
                if row_number in self.get_text(row_num):
                    try:
                        seat_num = row.find_element(By.CSS_SELECTOR,
                                                    ".seatmap__seat.seatmap__seat--standard.ng-star-inserted")
                        is_enabled = seat_num.is_enabled()
                    except NoSuchElementException:
                        pass
                    if is_enabled:
                        try:
                            seat_num.click()
                            self.click_on_element(".passenger-carousel__cta.passenger-carousel__cta--next")
                            break
                        except (NoSuchElementException, ElementClickInterceptedException):
                            pass
                    if not is_enabled:
                        row_number = str(int(row_number) + 1)

    def choose_rtn_seat(self, row_number):
        """
        choose your row number to sit on the return flight.
        :param row_number:
        """
        try:
            if self.find_element(".seats-offer__wrapper.ng-star-inserted").is_displayed():
                self.click_on_element("#main-content > div button:nth-child(3)")
        except (NoSuchElementException, ElementClickInterceptedException):
            seat_rows = self.find_elements(".seatmap__seats")
            is_enabled = None
            seat_num = None
            for row in seat_rows:
                try:
                    row_num = row.find_element(By.CSS_SELECTOR,
                                               ".seatmap__seat.seatmap__seat--aisle.b2.ng-star-inserted")
                    is_display = row_num.is_displayed()
                except NoSuchElementException:
                    print("the element not exist")
                    continue
                if row_number in self.get_text(row_num):
                    try:
                        seat_num = row.find_element(By.CSS_SELECTOR,
                                                    ".seatmap__seat.seatmap__seat--standard.ng-star-inserted")
                        is_enabled = seat_num.is_enabled()
                    except NoSuchElementException:
                        pass
                    if is_enabled:
                        try:
                            seat_num.click()
                            self.click_on_element(".passenger-carousel__cta.passenger-carousel__cta--next")
                            break
                        except (NoSuchElementException, ElementClickInterceptedException):
                            pass
                    if not is_enabled:
                        row_number = str(int(row_number) + 1)
                if is_display:
                    print("I can see number")
