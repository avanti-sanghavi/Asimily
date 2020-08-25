import os
import configparser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions


def get_url():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    app_url = config['Application']['url']
    return app_url


def initialize_webdriver():
    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)
    # current_directory = os.getcwd()
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_experimental_option("detach", True)
    # print(current_directory + '\\Drivers\\chromedriver.exe')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # driver = webdriver.Chrome(options=options, executable_path=current_directory + '\\Drivers\\chromedriver.exe')
    # driver = webdriver.Chrome(options=options, executable_path=".\\chromedriver.exe")
    return driver
