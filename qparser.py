from selenium import webdriver

class ProghubParser(object):
    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang

    def parse(self):
        self.go_to_question_page()

    def go_to_question_page(self):
        self.driver.get('https://instasport.co/club/katefit/schedule/day/944/')
        test_elements = self.driver.find_element_by_xpath("//div[@class=' col-md-3 col-sm-3 col-xs-5 training']/a")
        go_link = test_elements.get_attribute('href')
        self.driver.get(go_link)
        """

        print(go_link)
        self.driver.get(go_link)
        break
        """

def main():
    driver = webdriver.Chrome('./chromedriver')
    parser = ProghubParser(driver, "python")
    parser.parse()

if __name__ == "__main__":
    main()

