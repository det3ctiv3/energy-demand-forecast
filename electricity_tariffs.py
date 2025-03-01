import pandas as pd
import numpy as np

# Sample data for Germany's electricity tariffs
data = {
    'Year': list(range(2010, 2025)),
    'Household_Price_EUR_kWh': [0.250, 0.260, np.nan, 0.280, 0.290, np.nan, 0.310, 0.320, 0.330, np.nan, 0.350, 0.360, 0.370, 0.380, 0.3951],
    'Industrial_Price_EUR_kWh': [0.150, 0.155, np.nan, 0.165, 0.170, np.nan, 0.180, 0.185, 0.190, np.nan, 0.200, 0.205, 0.210, 0.215, np.nan]
}

# Create DataFrame
df = pd.DataFrame(data)

# Interpolate missing values
df['Household_Price_EUR_kWh'] = df['Household_Price_EUR_kWh'].interpolate()
df['Industrial_Price_EUR_kWh'] = df['Industrial_Price_EUR_kWh'].interpolate()

# Save to Excel file
df.to_excel("germany_electricity_tariffs.xlsx", index=False)

print("Excel file generated successfully!")
