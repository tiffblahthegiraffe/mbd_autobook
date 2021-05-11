import time
import datetime
from utility import MyDrive
from selenium.common.exceptions import NoSuchElementException

driver_path = '/Users/tiffanysung/Documents/chromedriver'
mbd_url = 'https://clients.mindbodyonline.com/classic/mainclass?studioid=841970'
DAILY_SCHEDULE_PREFERENCE = {'Mon': [5, ['7:15','6:15','8:15']],
                             'Tue': [5, ['7:15','6:15','8:15','7:00']],
                             'Wed': [5, ['7:15','6:15','8:15']],
                             'Thu': [5, ['7:15','6:15','8:15']],
                             'Fri': [3, ['7:15','6:15','8:15']],
                             'Sat': [3, ['8:00','9:15', '10:']],
                             'Sun': [2, ['9:30','10:30']]}
now = datetime.datetime.now()
DAY_TO_BOOK = now.strftime("%a")

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
    return driver


def check_schedule_and_book(schedule_table,DAY_TO_BOOK,DAILY_SCHEDULE_PREFERENCE):
    row_count = 0
    for row in schedule_table:
        if DAY_TO_BOOK in row.text:
            print('Booking for', row.text)
            start_row = row_count + 1
            end_row = row_count + 1 + DAILY_SCHEDULE_PREFERENCE[DAY_TO_BOOK][0]
            time = schedule_table[start_row:end_row]
            break
        row_count += 1

    preference_list = DAILY_SCHEDULE_PREFERENCE[DAY_TO_BOOK][1]

    for i in preference_list:
        print('try booking for', i)
        for t in time:
            print(t.text)
            if i in t.text:
                try:
                    sign_up = t.find_element_by_class_name('SignupButton')
                    print('There\'s still availibility for%s' % t.text[:10])
                    return sign_up

                except NoSuchElementException:
                    print('Can\'t signup for %s. Not booked!' % t.text[:10])

                break
def main():
    driver = MyDrive(driver_path)
    # Go on to mbd website
    driver.get_site(mbd_url)

    # Click sign-in button
    sign_in_button = driver.find_element('signInButton',class_name=True)
    driver.click_button(sign_in_button)

    #log in
    with open('mbd_credential.txt','r') as file:
        usr_email, usr_pw = file.readlines()
        log_in(driver, usr_email, usr_pw)
    print('Logged in to mindbody!')

    time.sleep(2) # an important step to wait for page load
    # Direct to CLASS Tab
    class_tab = driver.find_element('tabTD7', id=True)
    driver.click_button(class_tab)
    time.sleep(1)

    # Refresh page by clicking Today
    today_button = driver.find_element('today-button', id=True)
    driver.click_button(today_button)
    time.sleep(1)

    # Get class schedule table
    table_path = "//table/tbody/tr/td/table[@id ='classSchedule-mainTable']/tbody/tr"
    schedule_table = driver.find_element(table_path, xpath=True, multi=True)

    # Read table
    print('Start booking...')
    sign_up = check_schedule_and_book(schedule_table,DAY_TO_BOOK,DAILY_SCHEDULE_PREFERENCE)

    driver.close_drive()

if __name__ == "__main__":
    main()