import json


def load_alert(file_path):
    """Load a security alert from a JSON file."""
    with open(file_path, "r") as file:
        alert = json.load(file)

    return alert


def main():
    alert = load_alert("alerts/brute_force.json")

    print("AI Security Alert Triage Assistant")
    print("-----------------------------------")
    print(f"Alert Type: {alert['alert_type']}")
    print(f"Username: {alert['username']}")
    print(f"Source IP: {alert['source_ip']}")
    print(f"Failed Attempts: {alert['failed_attempts']}")
    print(f"Time Window: {alert['time_window_minutes']} minutes")


if __name__ == "__main__":
    main()
