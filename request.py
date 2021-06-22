from time import sleep
from selenium import webdriver
from info import user, password


class Bot():
    def __init__(self):
        self.login(user, password)

    def login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')

        accept = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/button[1]').click()
        sleep(1)
        username_input = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(1)
        # loginclick
        self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(5)

        # click on not now
       # clickkkk = self.driver.find_element_by_xpath(
        # '//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()

        a = self.driver.get(
            'https://www.instagram.com/accounts/access_tool/current_follow_requests')
        sleep(2)

        number_of_clicks = 0
        while number_of_clicks < 1:
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/article/main/button').click()
            sleep(2)
            number_of_clicks += 1

        list_of_usernames = []
        for names in self.driver.find_elements_by_class_name('-utLf'):
            list_of_usernames.append(names.text)

        for i in list_of_usernames:
            self.driver.get(f'https://www.instagram.com/{i}')
            sleep(1)
            # requested
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
            sleep(3)
            # unfollow
            self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div/div[3]/button[1]').click()


def main():
    myBot = Bot()


if __name__ == '__main__':
    main()

# first accept
# /html/body/div[3]/div/div/button[1]

# user name
# //*[@id="loginForm"]/div/div[1]/div/label/input

# password
# //*[@id="loginForm"]/div/div[2]/div/label/input

# loginbootom
# //*[@id="loginForm"]/div/div[3]


# //*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/button


# //*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/button
# //*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button
# /html/body/div[5]/div/div/div/div[3]/button[1]


