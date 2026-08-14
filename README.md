# Cryptocurrency Price Tracker

## Project Description

The Cryptocurrency Price Tracker is a Python-based web automation project that extracts real-time cryptocurrency market data from CoinMarketCap.

The system uses Selenium WebDriver to access dynamically rendered web pages and collects information such as cryptocurrency name, price, 24-hour price change, and market capitalization. The collected data is organized and exported into a CSV file for further analysis.

## Objective

To develop an automated cryptocurrency price tracker that collects live cryptocurrency data, processes it using Python and Selenium, and exports the results into a structured CSV file.

## Key Features

- Real-time cryptocurrency data extraction
- Extracts data for the top 10 cryptocurrencies
- Collects cryptocurrency name, price, 24-hour change, and market capitalization
- Handles JavaScript-rendered web pages using Selenium
- Supports automated browser execution
- Adds timestamps for historical tracking
- Exports collected data to CSV format

## Technology Stack

- Python 3.x
- Selenium
- Pandas
- WebDriver Manager
- CSV
- Datetime

## Project Workflow

1. Initialize Selenium WebDriver
2. Open the CoinMarketCap website
3. Extract cryptocurrency market data
4. Organize the extracted data
5. Add timestamp information
6. Export the results to a CSV file

## Output

The project generates a CSV file containing cryptocurrency market information and timestamps. The output can be used for data analysis and historical trend tracking.

## Benefits

- Automates repetitive cryptocurrency data collection
- Reduces manual data entry
- Provides structured and analyzable data
- Saves time when monitoring cryptocurrency prices

## Limitations

- Requires an internet connection
- Changes to the CoinMarketCap website layout may require updates to the selectors
- The current project focuses on CoinMarketCap as the data source
- The project exports data to CSV rather than providing a graphical dashboard

## Future Enhancements

- Develop a graphical cryptocurrency dashboard
- Add cryptocurrency price trend analysis
- Implement market forecasting
- Add portfolio tracking
- Add custom price alerts

## Conclusion

The Cryptocurrency Price Tracker demonstrates how Python and Selenium can be used to automate real-time cryptocurrency data collection. The project provides structured data that can serve as a foundation for dashboards, trend analysis, alerts, and predictive analytics.
