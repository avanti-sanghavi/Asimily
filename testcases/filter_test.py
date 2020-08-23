import time
import unittest
import baseclass
from pages.main_page import MainPage
from utilities import BasePage


class FilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = baseclass.initialize_webdriver()
        BasePage(self.driver).open_url()

    def test_default_value_type(self):
        """
        Validate if the default value of "Type" filter is selected as "All"
        """
        MainPage(self.driver).wait_for_main_page()
        type_filter_value = MainPage(self.driver).check_selected_value_type()
        self.assertEqual(type_filter_value, 'All')

    def test_mobile_filter(self):
        """
        Validate upon selecting "Mobile" as a "Type", only mobile devices are shown in map
        """
        MainPage(self.driver).wait_for_main_page()
        MainPage(self.driver).select_mobile_filter()
        time.sleep(1)
        list_of_devices = MainPage(self.driver).check_device_map()
        self.assertFalse(any(elem in ['laptop', 'desktop'] for elem in list_of_devices))

    def test_manufacturer_filer(self):
        """
        Validate "manufacturer" dropdown values update as we select "Mobile" from "Type"
        """
        MainPage(self.driver).wait_for_main_page()
        MainPage(self.driver).select_mobile_filter()
        manufacturer_list = MainPage(self.driver).check_mobile_manufacturer_filter()
        self.assertEqual(manufacturer_list, ['all', 'Dell', 'HP', 'Nokia', 'Motorola', 'Google'])


if __name__ == "__main__":
    unittest.main()
