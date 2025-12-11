"""
Data Analysis Worker Agent (Basic)
Reads telemetry data and detects simple anomalies.
"""

import pandas as pd

ENGINE_TEMP_THRESHOLD = 100     # Celsius
BATTERY_LOW_THRESHOLD = 12.2    # Volts
SPEED_MAX_THRESHOLD = 150       # km/h unusually high for typical city driving

class DataAnalysisAgent:
    def __init__(self, telemetry_path="data/telemetry_sample.csv"):
        self.telemetry_path = telemetry_path

    def load_data(self):
        try:
            print("Loading file from:", self.telemetry_path)
            df = pd.read_csv(self.telemetry_path)
            print("Loaded rows:", len(df))
            return df
        except Exception as e:
            print("ERROR LOADING CSV:", e)
            return None


    def analyze_latest(self):
        df = self.load_data()
        if df is None or df.empty:
            return {"error": "Telemetry data not found or empty"}

        # Get the newest row based on timestamp
        latest = df.sort_values("timestamp", ascending=False).head(1).iloc[0]

        vehicle = latest["vehicle_id"]
        temp = latest["engine_temp_c"]
        batt = latest["battery_v"]
        speed = latest["speed_kmh"]

        issues = []

        if temp > ENGINE_TEMP_THRESHOLD:
            issues.append("High engine temperature")

        if batt < BATTERY_LOW_THRESHOLD:
            issues.append("Low battery voltage")

        if speed > SPEED_MAX_THRESHOLD:
            issues.append("Abnormally high speed detected")

        return {
            "vehicle": str(vehicle),
            "timestamp": str(latest["timestamp"]),
            "speed_kmh": int(speed),
            "engine_temp_c": int(temp),
            "battery_v": float(batt),
            "issues": list(issues) if issues else ["No issues detected"]
        }
