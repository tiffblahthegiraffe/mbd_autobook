from utility import MyDrive

driver_path = '/Users/tiffanysung/Documents/chromedriver'
mbd_url = 'https://clients.mindbodyonline.com/classic/mainclass?studioid=841970'

def log_in(driver, usr_email, usr_pw):
    usr_email_field = driver.find_element('su1UserName',id=True)
    driver.fillin_sendkey(usr_email_field,usr_email)
    usr_pw_field = driver.find_element('su1Password',id=True)
    driver.fillin_sendkey(usr_pw_field, usr_pw)
    log_in_button = driver.find_element('loginButton', class_name=True)
    driver.click_button(log_in_button)
    if driver.find_element('LoginError', id=True):
        print(driver.find_element('LoginError', id=True).text)
    else:
        print('Log in successful')


driver = MyDrive(driver_path)
# Go on to mbd website
driver.get_site(mbd_url)

# Click sign-in button
sign_in_button = driver.find_element('signInButton',class_name=True)
driver.click_button(sign_in_button)

#log in
with open('mbd_credential.txt','r') as file:
    urs_email, urs_pw = file.readlines()
    log_in(driver, urs_email, urs_pw)

# Direct to CLASS Tab
class_tab = driver.find_element('tabTD7', id=True)
driver.click_button(class_tab)

# Refresh page by clicking Today
today_button = driver.find_element('today-button', id=True)
driver.click_button(today_button)

# Get class schedule table
table_path = "//table/tbody/tr/td/table[@id ='classSchedule-mainTable']/tbody/tr"
schedule_table = driver.find_element(table_path, xpath=True)