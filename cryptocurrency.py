from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
import csv


# Website
website = "https://coinmarketcap.com/"

# Chrome options
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Start Chrome WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Open CoinMarketCap
    driver.get(website)

    # Find cryptocurrency table rows
    rows = driver.find_elements(
        By.XPATH,
        '//table[contains(@class,"cmc-table")]//tbody//tr'
    )

    # Save data to CSV
    with open(
        "crypto_data.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        datas = csv.writer(csvfile)

        datas.writerow([
            "Name",
            "Price",
            "24h_Change",
            "Market Cap",
            "Timestamp"
        ])

        # Extract top 10 cryptocurrencies
        for row in rows[:10]:
            cols = row.find_elements(By.TAG_NAME, "td")

            if len(cols) >= 7:
                name = cols[2].text
                price = cols[3].text
                change_24h = cols[4].text
                market_cap = cols[6].text

                timestamp = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                datas.writerow([
                    name,
                    price,
                    change_24h,
                    market_cap,
                    timestamp
                ])

    print("Cryptocurrency data successfully saved to crypto_data.csv")

finally:
    driver.quit()
