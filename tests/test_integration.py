import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from app import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.app = app.test_client()

    def tearDown(self):
        self.driver.quit()

    def test_generate_button(self):
        # Navigate to the home page
        self.driver.get("http://localhost:5000")

        # Find the "Generate New Image" button and click it
        generate_button = self.driver.find_element(By.ID, "generateButton")
        generate_button.click()

        # Wait for the image to reload (adjust the sleep time if needed)
        self.driver.implicitly_wait(5)

        # Get the source URL of the color image
        color_image = self.driver.find_element(By.ID, "colorImage")
        src_before = color_image.get_attribute("src")

        # Click the "Generate New Image" button again
        generate_button.click()

        # Wait for the image to reload (adjust the sleep time if needed)
        self.driver.implicitly_wait(5)

        # Get the updated source URL of the color image
        src_after = color_image.get_attribute("src")

        # Assert that the source URL has changed, indicating a new image was loaded
        self.assertNotEqual(src_before, src_after)

    def test_performance(self):
        # Test that the application does not significantly impact browser performance
        from selenium.webdriver.support.ui import WebDriverWait

        self.driver.get("http://localhost:5000")

        # Measure the page load time
        load_time = self.driver.execute_script("return performance.timing.loadEventEnd - performance.timing.navigationStart")
        print(f"Page load time: {load_time} ms")

        # Assert that the load time is within an acceptable range
        self.assertLess(load_time, 5000)

        color_image = self.driver.find_element(By.ID, "colorImage")
        src_before = color_image.get_attribute("src")

        # Measure the time taken to generate a new image
        generate_button = self.driver.find_element(By.ID, "generateButton")
        generate_button.click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(By.ID, "colorImage").get_attribute("src") != src_before
        )

        # Assert that the image generation time is within an acceptable range
        generation_time = self.driver.execute_script("return performance.now()")
        print(f"Image generation time: {generation_time} ms")
        self.assertLess(generation_time, 2000)


if __name__ == "__main__":
    unittest.main()