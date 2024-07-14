from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from page_object.BasePage import BasePage


class Extra(BasePage):
    def __init__(self, driverd):
        super().__init__(driverd)

    def insurance(self, insurance_1_0):
        """
        This code will add you a travel insurance.
        Press 1 to add insurance.
        Press 0 to forward without insurance.
        :param insurance_1_0:
        """
        try:
            if self.find_element(".ng-star-inserted .enhanced-takeover__modal").is_enabled():
                if int(insurance_1_0) == 1:
                    self.click_on_element(".enhanced-takeover__product-confirm-cta.ry-button--flat-yellow")
                elif int(insurance_1_0) == 0:
                    self.click_on_element(".enhanced-takeover__product-dismiss-cta.ry-button--anchor-blue")
        except NoSuchElementException:
            pass

    def continue_to_last_page(self):
        """
        This code will bring you to the page, the purchase page.

        """
        try:
            self.click_on_element(".ry-button--large")
        except StaleElementReferenceException:
            self.driver.implicitly_wait(5)
            self.click_on_element(".ry-button--large")
