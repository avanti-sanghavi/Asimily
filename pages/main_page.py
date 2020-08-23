from selenium.webdriver.support.ui import Select
from locators.locators import FilterLocators
from utilities import *


class MainPage(BasePage):

    def wait_for_main_page(self, *locator):
        self.wait_for_element(FilterLocators.type_filter)

    def find_type_filter(self):
        return self.driver.find_element(*FilterLocators.type_filter)

    def check_selected_value_type(self):
        select = Select(self.find_type_filter())
        return select.first_selected_option.text

    def select_mobile_filter(self):
        select = Select(self.find_type_filter())
        select.select_by_visible_text('Mobile')

    def check_device_map(self):
        final_devices = []
        device_map = self.driver.find_element(*FilterLocators.device_map)
        devices_list = device_map.find_elements_by_tag_name('image')
        for devices in devices_list:
            device_type_text = (devices.get_attribute('href').split('/')[2]).split('.')[0]
            final_devices.append(device_type_text)
        return final_devices

    def check_mobile_manufacturer_filter(self):
        option_list=[]
        manufacturer_filter = self.driver.find_element(*FilterLocators.manufacturer)
        options = [x for x in manufacturer_filter.find_elements_by_tag_name("option")]

        for element in options:
            option_list.append(element.get_attribute("value"))
        return option_list
