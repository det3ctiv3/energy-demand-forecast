from prophet import Prophet
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

# Convert string data into DataFrame
# Load dataset from CSV
df = pd.read_csv("energy_demand.csv", parse_dates=["Date"])


# Aggregate hourly data to daily data
df["Total_Demand"] = df["UZB"] + df["KGZ"] + df["TJK"]
df_daily = df.resample("D", on="Date").sum().reset_index()

# Feature Engineering: Peak Demand Adjustment
df_daily["Peak_Demand"] = df.resample("D", on="Date")["Total_Demand"].max().values

df_prophet = df_daily.rename(columns={"Date": "ds", "Total_Demand": "y"})

# Initialize Prophet model with expert tuning
m = Prophet(
    changepoint_prior_scale=0.05,  # Controls trend flexibility
    seasonality_mode='multiplicative'  # Better for capturing growth
)

# Add Fourier terms for advanced seasonality modeling
m.add_seasonality(name='weekly', period=7, fourier_order=5)
m.add_seasonality(name='yearly', period=365.25, fourier_order=15)

# Add peak demand as an external regressor
m.add_regressor("Peak_Demand")

# Fit the model
m.fit(df_prophet)

# Create future dataframe extending to 2030
future = m.make_future_dataframe(periods=365 * 11, freq='D')  # 11 years ahead

# Add estimated peak demand into future dataframe
future["Peak_Demand"] = np.tile(df_daily["Peak_Demand"].mean(), len(future))

# Make forecast
forecast = m.predict(future)

# Display forecasted results
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
m.plot(forecast).savefig("forecast.png")
pl.show()
