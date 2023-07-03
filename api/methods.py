from datetime import datetime as dt

import pandas
from sqlalchemy import text

from api.base import app
from bases import get_session_factory


@app.get("/dashboard/")
async def get_facility_consumption():
    session_factory = get_session_factory()
    now = int(dt.utcnow().timestamp()) - 3600 * 24 * 10

    with session_factory() as session:
        interval = f"date_trunc('hour', e.date_time)"

        statement = text(
            f"""
            SELECT {interval}  date_time, sum(total_active_energy) AS total_active_energy
            FROM events e
            JOIN panels p ON e.panel_id = p.id
            WHERE p.location_id = CAST(:location_id AS UUID)
                AND e.date_time > to_timestamp(:start_date_time)
                AND e.date_time <= to_timestamp(:end_date_time)
            GROUP BY 1
            ORDER BY date_time;
            """
        )

        events_df = pandas.read_sql(
            sql=statement,
            con=session.connection(),
            params={"location_id": "3746daae-99e9-4257-9aeb-de2e778c550f", "start_date_time": now - 3600 * 24 * 7, "end_date_time": now},
        )
    return events_df.to_dict()
