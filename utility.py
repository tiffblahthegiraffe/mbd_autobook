from selenium import webdriver

class MyDrive:
    def __init__(self, path):
        self.path = path
        self.driver = webdriver.Chrome(self.path)

    def get_site(self,url):
        self.driver.get(url)

    def find_element(self, search_term, class_name = False, id = False, xpath = False, multi = False):
        if class_name:
            if multi:
                elem = self.driver.find_elements_by_class_name(search_term)
            else:
                elem = self.driver.find_element_by_class_name(search_term)
        elif id:
            if multi:
                elem = self.driver.find_elements_by_id(search_term)
            else:
                elem = self.driver.find_element_by_id(search_term)
        elif xpath:
            if multi:
                elem = self.driver.find_elements_by_xpath(search_term)
            else:
                elem = self.driver.find_element_by_xpath(search_term)
        else:
            print('ERROR: please specify an element type (class_name, id, xpath)')
        return elem

    def click_button(self, driver_elem):
        driver_elem.click()

    def fillin_sendkey(self, driver_elem, input_field):
        driver_elem.send_keys(input_field)

    def close_drive(self):
        self.driver.close()