import time
import json
import requests

# Configurations
DELAY_IN_SECONDS = 10  # How frequently the temperature should be monitored.
DEVICE_ID = 1234
INVALID_TEMPERATURE = -1000
NUMBER_OF_SENSORS = 3
SENSOR_IDS = [1, 2, 3]

# Server URL (Local server IP address)
SERVER_URL = "http://127.0.0.1:8080/updateReadings"  # URL of the server

# Helper function to read temperature manually
def read_temperature_manually(sensor_id):
    try:
        temp = float(input(f"Enter temperature for sensor {sensor_id}: "))
        return round(temp, 2)
    except ValueError:
        print("Invalid temperature value entered.")
        return INVALID_TEMPERATURE

# Main loop
def main():
    while True:
        try:
            temperatures = []

            # Request temperature readings manually
            for sensor_id in SENSOR_IDS:
                temperature = read_temperature_manually(sensor_id)
                temperatures.append(temperature)

            # Create JSON object
            data = {
                "device_id": DEVICE_ID,
                "readings": []
            }

            # Add sensor readings to JSON object
            for i, temp in enumerate(temperatures):
                if temp != INVALID_TEMPERATURE:
                    data["readings"].append({
                        "sensor_id": SENSOR_IDS[i],
                        "temperature": temp
                    })
                else:
                    print("ERROR: SENSOR_UNHEALTHY. Please check sensor:", SENSOR_IDS[i])

            # Make a HTTP POST request
            response = requests.post(SERVER_URL, json=data)
            if response.status_code == 200:
                print("Data sent successfully to server.")
            else:
                print(f"Failed to send data to server. Status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        time.sleep(DELAY_IN_SECONDS)

if __name__ == "__main__":
    main()
