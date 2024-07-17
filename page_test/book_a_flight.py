import pytest

from page_object.BasePage import BasePage
from page_object.Bags import Bags
from page_object.Extra import Extra
from page_object.Flight import Flight
from page_object.MainPage import MainPage
from page_object.Seats import Seats


class TestRyanair(BaseTest):
    def test_book_a_flight(self, driverd):
        base_page = BasePage(driverd)
        main_page = MainPage(driverd)
        flight_page = Flight(driverd)
        seats_page = Seats(driverd)
        bags_page = Bags(driverd)
        extra_page = Extra(driverd)

        main_page.open_web("https://www.ryanair.com/gb/en")
        main_page.cookies()
        main_page.departure_country("albania", "tirana")
        main_page.destination_country("austria", "vienna")
        main_page.depart_date("sep", "9")
        main_page.return_date("sep", "14")
        main_page.passenger()
        main_page.submit_trip()
        flight_page.cheapest_dpt_flight()
        flight_page.cheapest_rtn_flight()
        flight_page.extra_fare("regular")
        flight_page.log_in_later()
        flight_page.gender("mr", "ofir", "adato")
        seats_page.choose_dpt_seat("16")
        base_page.driver.implicitly_wait(5)
        seats_page.choose_rtn_seat("16")
        bags_page.baggage(20)
        extra_page.insurance(0)
        extra_page.continue_to_last_page()
        extra_page.continue_to_last_page()
