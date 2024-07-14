import time
from page_object.BasePage import BasePage


class Bags(BasePage):
    def __init__(self, driverd):
        super().__init__(driverd)

    def baggage(self, kg_begs):
        """
        add baggage or continue without baggage
        :param kg_begs:
        """
        if int(kg_begs) == 10:
            self.click_on_element(".content-plus-tag__button.ry-button--anchor-blue")
            self.click_on_element(".booking-content__section .ry-button--gradient-yellow")
        elif int(kg_begs) == 0:
            self.click_on_element(".booking-content__section .ry-button--gradient-yellow")
        elif int(kg_begs) == 20:
            self.click_on_element(".counter .counter__button-wrapper--enabled")
            time.sleep(1)
            self.click_on_element(".booking-content__section .ry-button--gradient-yellow")
