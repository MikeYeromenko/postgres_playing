import uuid
from datetime import datetime as dt
from random import uniform


def get_date_time_ranges(days=61):
    # counter = days * 2 * 4 * 24  # 2 times in 15 minutes
    end = int(dt.now().timestamp() / 900) * 900 - 24 * 3600 * days
    start = end - 2 * 24 * 3600 * days
    result = []
    print(f"start: {dt.utcfromtimestamp(start)}; end: {dt.utcfromtimestamp(end)}")
    for interval in range(start, end + 1, 900):
        timestamp1 = uniform(interval, interval + 900)
        timestamp2 = uniform(interval, interval + 900)
        result.append((dt.utcfromtimestamp(timestamp1), dt.utcfromtimestamp(timestamp2)))
    return result

def get_event(date_time, panel_id, meter_id):
    return {
        "id": uuid.uuid4(),
        "date_time": date_time,
        "panel_id": panel_id,
        "meter_number": meter_id,
        "frequency": round(uniform(49, 51), 2),
        "voltage": round(uniform(200, 250), 2),
        "power_factor": round(uniform(0.5, 1), 2),

        "total_current": round(uniform(0, 5), 2),
        "total_active_power": round(uniform(0, 2), 2),
        "total_reactive_power": round(uniform(0, 2), 2),
        "total_active_energy": round(uniform(0, 10), 2),
        "total_reactive_energy": round(uniform(0, 10), 2),
        "total_apparent_power": round(uniform(0, 2), 2),
    }


def get_cm(date_time, panel_id, meter_id, event_id, channel):
    return {
        "id": uuid.uuid4(),
        "date_time": date_time,
        "panel_id": panel_id,
        "meter_number": meter_id,
        "event_id": event_id,
        "channel": channel,
        "current": round(uniform(0, 5), 2),
        "active_power": round(uniform(0, 2), 2),
        "reactive_power": round(uniform(0, 2), 2),
        "active_energy": round(uniform(0, 5), 2),
        "reactive_energy": round(uniform(0, 5), 2),
        "power_factor": round(uniform(0.5, 1), 2),
    }
