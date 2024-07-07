# Realtime Temperature Monitoring

## Project Description

This project implements a real-time temperature monitoring system using a combination of Flask, SQLite, and Plotly.js. The system allows users to manually enter temperature readings from different sensors and visualize these readings both in a tabular format and as a dynamic graph. The web interface provides a comprehensive view of recent sensor readings and trends over time.

## Features

- **Real-time Temperature Data Input**: Manually enter temperature readings for multiple sensors.
- **Data Storage**: Store sensor readings in an SQLite database.
- **Web Interface**: Display recent temperature readings in a table format.
- **Graph Representation**: Visualize temperature trends using Plotly.js.
- **RESTful API**: Update sensor readings via a POST request.

## Tech Stack

- **Backend**: Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript (Plotly.js)

## Project Structure

```bash
live_temp_reading/
│
├── templates/
│ └── index.html # HTML template for displaying data
├── client.py # Python script to simulate temperature readings
├── server.py # Flask server for handling requests and serving data
├── sensors.db # SQLite database (generated at runtime)
└── requirements.txt # Python dependencies
```

## Detailed Description

### Flask Server (`server.py`)

- Initializes the Flask app and configures the SQLite database.
- Defines a SQLAlchemy model (`SensorReading`) to represent temperature data.
- Provides routes:
  - `/updateReadings`: Accepts POST requests with JSON data to update sensor readings.
  - `/`: Renders the web page showing the table and graph of temperature readings.

### Client Script (`client.py`)

- Simulates manual temperature input from multiple sensors.
- Sends temperature data to the Flask server via POST requests.
- Runs in a loop with a delay to periodically send data.

### HTML Template (`index.html`)

- Displays recent sensor readings in a table.
- Uses Plotly.js to dynamically generate and update a graph showing temperature trends over time.

### Database (`sensors.db`)

- SQLite database created and managed by SQLAlchemy.
- Stores sensor readings with columns: `id`, `device_id`, `sensor_id`, `temperature`, and `timestamp`.

## Usage

### Setup

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Run the Server

```bash
python server.py
```
The server will start on [http://127.0.0.1:8080](http://127.0.0.1:8080).

### Simulate Sensor Readings

```bash
python client.py
```
Follow the prompts to enter temperature readings.

## View Data

Open a web browser and go to [http://127.0.0.1:8080](http://127.0.0.1:8080).

The web page will display the recent readings in a table and the temperature trends in a graph.

## Tech Stack Details

- **Flask**: A micro web framework for Python used to build the server and handle HTTP requests.
- **SQLite**: A lightweight, disk-based database used to store sensor readings.
- **SQLAlchemy**: An ORM used for database operations.
- **HTML/CSS**: Used to structure and style the web page.
- **JavaScript**: Handles dynamic data fetching and graph rendering.
- **Plotly.js**: A JavaScript library for creating interactive graphs.

## Graph Representation

- The graph shows temperature readings over time.
- X-axis represents the timestamp of each reading.
- Y-axis represents the temperature values.
- The graph is dynamically updated as new data is received.

## Error Handling

- Ensures proper data validation and error messages for invalid inputs.
- Rolls back transactions in case of database errors to maintain data integrity.

## Future Enhancements

- Automate data input from actual sensors.
- Add user authentication for data security.
- Enhance the UI with more interactive features and real-time updates.



