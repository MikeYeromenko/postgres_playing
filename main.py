from datetime import datetime as dt

import pandas
from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse
from sqlalchemy import text

from api.base import app
from bases import get_session_factory


@app.get("/")
async def root():
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
        """
    return HTMLResponse(content=content)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


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
