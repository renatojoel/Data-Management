
#pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Create Chrome browser options
options = Options()
# Run Chrome in headless mode (browser does not open on screen)
options.add_argument("--headless=new")  
# Start the Chrome WebDriver with the chosen options
driver = webdriver.Chrome(options=options)

# List of tweet URLs to scrape
urls = [
    "https://x.com/LeopoldHeinrich/status/2024878511375233380",
    "https://x.com/worldbankdata/status/2024122309175382390",
    "https://x.com/addis_fortune/status/2023759349458301046"
]

# This list will store the extracted tweets
new_tweets = []

# Loop through each tweet URL, navigate to the page, and extract the desired information
for url in urls:
    driver.get(url)
    time.sleep(5)

    texto = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]').text
    autor = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="User-Name"]').text
    data = driver.find_element(By.TAG_NAME, "time").get_attribute("datetime")
    tweet_id = url.split("/")[-1]

    new_tweets.append({
        "id": tweet_id,
        "author_id": autor,
        "text": texto,
        "created_at": data,
        "lang": "en"
    })

# Close the browser
driver.quit()

# Print all collected tweets
print(new_tweets)
