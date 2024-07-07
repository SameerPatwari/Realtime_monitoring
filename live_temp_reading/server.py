from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_sensors.db'  # keep you own database name here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# SQLAlchemy model for SensorReading
class SensorReading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer)
    sensor_id = db.Column(db.Integer)
    temperature = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/updateReadings', methods=['POST'])
def update_readings():
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        device_id = data['device_id']
        readings = data['readings']

        if not isinstance(readings, list):
            return jsonify({"error": "Invalid readings format"}), 400

        for reading in readings:
            sensor_id = reading['sensor_id']
            temperature = reading['temperature']

            if not (isinstance(sensor_id, int) and isinstance(temperature, (int, float))):
                return jsonify({"error": "Invalid sensor_id or temperature"}), 400

            new_reading = SensorReading(device_id=device_id, sensor_id=sensor_id, temperature=temperature)
            db.session.add(new_reading)

        db.session.commit()

        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    readings = SensorReading.query.all()
    return render_template('index.html', readings=readings)

@app.route('/graphData', methods=['GET'])
def graph_data():
    readings = SensorReading.query.order_by(SensorReading.timestamp).all()
    data = {
        "timestamps": [reading.timestamp.isoformat() for reading in readings],
        "temperatures": [reading.temperature for reading in readings]
    }
    return jsonify(data)

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(host='0.0.0.0', port=8080)
