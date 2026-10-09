from datetime import datetime, timedelta
import random
import pandas as pd

# Start date for a full year of weather records
start_date = datetime(2025, 12, 1)
total_days = 365

data = []
conditions_dry = ["Clear", "Partially cloudy", "Overcast"]
conditions_wet = [
    "Rain, Partially cloudy",
    "Rain, Overcast",
    "Light Rain",
    "Heavy Rain",
]

for day_idx in range(total_days):
  current_date = start_date + timedelta(days=day_idx)
  month = current_date.month

  # Seasonal temperature baseline (°C)
  if month in [12, 1, 2]:  # Winter
    base_temp = random.uniform(-6, 8.0)
    temp_range = random.uniform(3.0, 6.0)
  elif month in [3, 4, 5]:  # Spring
    base_temp = random.uniform(8.0, 16.0)
    temp_range = random.uniform(5.0, 9.0)
  elif month in [6, 7, 8]:  # Summer
    base_temp = random.uniform(17.0, 30.0)
    temp_range = random.uniform(7.0, 11.0)
  else:  # Autumn
    base_temp = random.uniform(9.0, 16.0)
    temp_range = random.uniform(4.0, 8.0)

  temp_min = round(base_temp - (temp_range / 2), 1)
  temp_max = round(base_temp + (temp_range / 2), 1)
  temp_avg = round((temp_min + temp_max) / 2, 1)

  # Rain probability & volume
  is_rainy = random.random() < 0.35
  if is_rainy:
    precip = round(random.uniform(0.5, 12.0), 1)
    precip_prob = random.randint(60, 100)
    condition = random.choice(conditions_wet)
    humidity = round(random.uniform(75.0, 95.0), 1)
  else:
    precip = 0.0
    precip_prob = random.randint(0, 20)
    condition = random.choice(conditions_dry)
    humidity = round(random.uniform(55.0, 80.0), 1)

  wind_speed = round(random.uniform(8.0, 30.0), 1)
  wind_gust = round(wind_speed + random.uniform(5.0, 18.0), 1)
  feels_like = round(temp_avg - (wind_speed * 0.1), 1)

  data.append({
      "name": "Eindhoven",
      "datetime": current_date.strftime("%Y-%m-%d"),
      "tempmax": temp_max,
      "tempmin": temp_min,
      "temp": temp_avg,
      "feelslike": feels_like,
      "humidity": humidity,
      "precip": precip,
      "precipprob": precip_prob,
      "windspeed": wind_speed,
      "windgust": wind_gust,
      "conditions": condition,
  })

# Create DataFrame
df = pd.DataFrame(data)

# Export directly to an Excel file with formatted column widths
output_filename = "weather_data.xls"
with pd.ExcelWriter(output_filename, engine="openpyxl") as writer:
  df.to_excel(writer, index=False, sheet_name="Daily_Weather")

  # Auto-fit column widths for a clean presentation
  worksheet = writer.sheets["Daily_Weather"]
  for col in worksheet.columns:
    max_len = max(len(str(cell.value or "")) for cell in col)
    col_letter = col[0].column_letter
    worksheet.column_dimensions[col_letter].width = max(max_len + 3, 12)

print(f"File created: '{output_filename}' containing {len(df)} rows.")