#!/usr/bin/env python3
\"\"\"Generate tiny synthetic telematics CSV for 10 vehicles.\"\"\"
import csv
import random
import time
from datetime import datetime, timedelta

VEHICLES = [f"VEH{100+i}" for i in range(10)]
start = datetime.utcnow() - timedelta(days=7)

with open('data/telemetry.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp','vehicle_id','speed_kmh','engine_temp_c','battery_v','odometer_km','fault_code'])
    for minute in range(7*24*60):  # 7 days, 1-minute granularity (this produces many rows; we will sample)
        ts = (start + timedelta(minutes=minute)).isoformat() + 'Z'
        v = random.choice(VEHICLES)
        speed = max(0, int(random.gauss(60, 15)))
        temp = max(60, int(random.gauss(90, 6)))
        batt = round(random.gauss(12.6, 0.15), 2)
        odo = random.randint(1000, 50000)
        # occasional fault codes
        fault = random.choice(['', '', '', 'P0010', 'P0300', 'P0420'])  # rare faults
        writer.writerow([ts, v, speed, temp, batt, odo, fault])
print("Synthetic telemetry written to data/telemetry.csv (may be large).")
