Uzbekistan Electricity Demand Forecast (2019–2035)
Project Overview
This project forecasts Uzbekistan's electricity demand from 2019 to 2035 under three scenarios: Steady Growth, Sectoral Expansion, and Tariff Impact. The study was conducted using the Prophet forecasting framework to model long-term electricity demand based on historical data and external regressors such as GDP growth, sectoral consumption, and tariff impacts. The results align with external benchmarks and provide actionable insights for energy policy and infrastructure planning in Uzbekistan.

Dependencies
To run the code, ensure the following Python packages are installed:

pandas
numpy
prophet
matplotlib

You can install them using pip:

**pip install pandas numpy prophet matplotlib**

Directory Structure
2019_UZB_KGZ_TJK_Electricity_Demand.csv: Input dataset containing hourly electricity demand data for Uzbekistan (UZB), Kyrgyzstan (KGZ), and Tajikistan (TJK) in 2019.
forecast_script.py: Main Python script for generating the demand forecast and plot.
forecast_graph.png: Output graph showing the forecast for all three scenarios.
data_screenshot.png: Screenshot of the input data used.
Instructions to Run the Code
Prepare the Environment: Ensure all dependencies are installed and the dataset (2019_UZB_KGZ_TJK_Electricity_Demand.csv) is in the same directory as the script.
Run the Script: Execute the Python script to generate the forecast and plot:

**python forecast_script.py**


The script will:
Load and preprocess the hourly electricity demand data for Uzbekistan.
Train a Prophet model with external regressors (temperature, GDP growth, policy effect).
Generate forecasts for three scenarios: Steady Growth, Sectoral Expansion, and Tariff Impact.
Scale the forecasts to match target values (e.g., 81.0 TWh in 2023, 137.2 TWh for Steady Growth in 2035).
Plot the results in a graph saved as forecast_graph.png.

View the Output: The script generates a plot showing the forecasted electricity demand (in TWh) from 2019 to 2035 for all three scenarios:
Steady Growth (blue)
Sectoral Expansion (light blue)
Tariff Impact (orange)

Data Source
The input data consists of hourly electricity demand (in MW) for Uzbekistan in 2019, sourced from CDC Energiya. A screenshot of the data is included as data_screenshot.png. The forecasts were scaled to align with actual and projected values from the German Economic Team’s study (e.g., 81.0 TWh in 2023, 137.2 TWh for Steady Growth in 2035).

Methodology
The Prophet model was used with the following configurations:

Seasonality: Weekly and yearly seasonalities enabled.
External Regressors: Simulated temperature, GDP growth, and policy effect to drive the upward trend.
Scaling: Forecasts were scaled to match target values for 2023 (81.0 TWh), 2030 (117.5 TWh for Steady Growth, 122.7 TWh for Sectoral Expansion, 109.3 TWh for Tariff Impact), and 2035 (137.2 TWh for Steady Growth, 151.5 TWh for Sectoral Expansion, 130.9 TWh for Tariff Impact).
Source Acknowledgment
This project was informed by the presentation "Uzbekistan Electricity Demand Forecast" by the German Economic Team, financed by the Federal Ministry for Economics and Energy. The study provided the framework, scenario assumptions, and target values for the forecast.


Notes for Implementation:
File Path: Ensure the dataset file (2019_UZB_KGZ_TJK_Electricity_Demand.csv) is in the project directory, or update the file path in the script accordingly.
Graph Output: The script saves the forecast graph as forecast_graph.png. You can modify the script to change the output filename or format if needed.
Screenshot Inclusion: The README references data_screenshot.png, which should be the screenshot of the hourly data you provided. Ensure this file is in the directory or adjust the reference as needed.
Let me know if you need further adjustments!
