import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt

file_path = "2019_UZB_KGZ_TJK_Electricity_Demand.csv"
df = pd.read_csv(file_path)

df.rename(columns={'Date': 'ds', 'UZB': 'y'}, inplace=True)
df['ds'] = pd.to_datetime(df['ds'])

df['y_mwh'] = df['y']

df_daily = df.resample('D', on='ds').sum().reset_index()

df = df_daily.copy()

df['temperature'] = 10 + 15 * np.sin(np.linspace(0, 6.28 * 3, len(df)))
df['gdp_growth'] = np.linspace(2, 5, len(df))
df['policy_effect'] = np.linspace(2, 6, len(df))

model = Prophet(
    daily_seasonality=False,
    weekly_seasonality=True,
    yearly_seasonality=True,
    growth='linear',
    changepoint_prior_scale=1.0,
    seasonality_prior_scale=5.0
)
model.add_seasonality(name='weekly', period=7, fourier_order=3)
model.add_regressor('temperature')
model.add_regressor('gdp_growth')
model.add_regressor('policy_effect')

model.fit(df)

future = model.make_future_dataframe(periods=365 * 16, freq='D')
future['temperature'] = 10 + 15 * np.sin(np.linspace(0, 6.28 * 16, len(future)))
future['gdp_growth'] = np.linspace(5, 10, len(future))
future['policy_effect'] = np.linspace(6, 12, len(future))

forecast = model.predict(future)

forecast['year'] = forecast['ds'].dt.year
forecast_yearly = forecast.groupby('year').agg({'yhat': 'sum'}).reset_index()
forecast_yearly['yhat_twh'] = forecast_yearly['yhat'] / 1_000_000

scaling_factor = 81.0 / forecast_yearly[forecast_yearly['year'] == 2023]['yhat_twh'].values[0]
forecast_yearly['steady_growth'] = forecast_yearly['yhat_twh'] * scaling_factor

current_2035_value = forecast_yearly[forecast_yearly['year'] == 2035]['steady_growth'].values[0]
adjustment_factor = 137.2 / current_2035_value
forecast_yearly['steady_growth'] = forecast_yearly['steady_growth'] * adjustment_factor

sectoral_expansion_2030_factor = 122.7 / forecast_yearly[forecast_yearly['year'] == 2030]['steady_growth'].values[0]
sectoral_expansion_2035_factor = 151.5 / forecast_yearly[forecast_yearly['year'] == 2035]['steady_growth'].values[0]
sectoral_expansion_factor = (sectoral_expansion_2030_factor + sectoral_expansion_2035_factor) / 2
forecast_yearly['sectoral_expansion'] = forecast_yearly['steady_growth'] * sectoral_expansion_factor

tariff_impact_2030_factor = 109.3 / forecast_yearly[forecast_yearly['year'] == 2030]['steady_growth'].values[0]
tariff_impact_2035_factor = 130.9 / forecast_yearly[forecast_yearly['year'] == 2035]['steady_growth'].values[0]
tariff_impact_factor = (tariff_impact_2030_factor + tariff_impact_2035_factor) / 2
forecast_yearly['tariff_impact'] = forecast_yearly['steady_growth'] * tariff_impact_factor

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(forecast_yearly['year'], forecast_yearly['steady_growth'], label='Steady Growth', color='blue')
ax.plot(forecast_yearly['year'], forecast_yearly['sectoral_expansion'], label='Sectoral Expansion', color='lightblue')
ax.plot(forecast_yearly['year'], forecast_yearly['tariff_impact'], label='Tariff Impact', color='orange')
ax.set_title('Uzbekistan Electricity Demand Forecast (2019-2035)')
ax.set_xlabel('Year')
ax.set_ylabel('Electricity Demand (TWh)')
ax.legend()
ax.grid(True)
plt.show()