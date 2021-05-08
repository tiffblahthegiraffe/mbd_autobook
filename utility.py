from selenium import webdriver

class MyDrive():
    def __int__(self, path):
        self.driver = webdriver.Chrome(path)

    def get_site(self,url):
        self.driver.get(url)

    def click_button(self, search_term, class_name = False, id = False, xpath = False):
        if class_name:
            button = self.driver.find_element_by_class_name(search_term)
        elif id:
            button = self.driver.find_element_by_id(search_term)
        elif xpath:
            button = self.driver.find_element_by_xpath
        else:
            print('ERROR: please specify an element type (class_name, id, xpath)')
        button.click()

    def close_drive(self):
        self.driver.close()