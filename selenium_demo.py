import selenium
import webdriver
import Keys

class Helper:

    self.driver = webdriver.Chrome()

    def open_youtube(self):

        driver.getUrl("https://www.youtube.com/")
        search_bar = driver.find_element(By.ID, "search")
        search_bar.send_keys("Golf")
        search_bar.send_keys(Keys.RETURN)

if __name__ == "__main__":
    Helper()
