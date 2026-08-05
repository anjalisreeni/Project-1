import random
from alert import send_email_alert


def apply_drift(sensor_data: dict) -> dict:
    """
    Apply small random variation to sensor readings to simulate
    a live sensor (instead of static CSV values).
    """
    sensor_data["temperature"] = round(sensor_data["temperature"] + random.uniform(-0.3, 0.3), 2)
    sensor_data["humidity"] = round(sensor_data["humidity"] + random.uniform(-2, 2), 2)
    sensor_data["vibration"] = round(sensor_data["vibration"] + random.uniform(-0.2, 0.2), 2)
    sensor_data["battery_level"] = max(0, sensor_data["battery_level"] - random.randint(0, 1))
    return sensor_data


def calculate_risk(sensor_data: dict) -> dict:
    """
    Compute risk_score and alert_status from current sensor readings.
    Mutates and returns sensor_data with both fields added.
    """
    risk_score = 0
    if sensor_data["temperature"] > 7:
        risk_score += 30
    if sensor_data["battery_level"] < 75:
        risk_score += 20
    if sensor_data["door_status"] == "Open":
        risk_score += 25
    if sensor_data["vibration"] > 4:
        risk_score += 25

    sensor_data["risk_score"] = risk_score

    if risk_score >= 70:
        sensor_data["alert_status"] = "Critical"
        
        # --- NEW ALERT CALLER ---
        container_id = sensor_data.get("container_id", "Unknown")
        alert_msg = f"Critical Alert: Container {container_id} has reached a risk score of {risk_score}."
        send_email_alert(subject=f"Critical Risk Threshold Breached - Container {container_id}", message=alert_msg)
        # ------------------------
        
    elif risk_score >= 40:
        sensor_data["alert_status"] = "Warning"
    else:
        sensor_data["alert_status"] = "Normal"

    return sensor_data


def process_reading(sensor_data: dict) -> dict:
    """
    Convenience wrapper: apply drift, then compute risk.
    """
    sensor_data = apply_drift(sensor_data)
    sensor_data = calculate_risk(sensor_data)
    return sensor_data