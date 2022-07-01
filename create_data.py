from datetime import datetime as dt
from datetime import timedelta as td

from apps.events.models import EventsBtree, CmBtree, Events, Cm, Events1, Cm1
from tests import data
from tests.factories import get_date_time_ranges, get_event, get_cm
from bases import get_session_factory


def create_main_data():
    session_factory = get_session_factory()
    with session_factory() as session:
        for loc in data.locations:
            session.add(loc)

        for pan in data.panels:
            session.add(pan)

        for mt in data.meter_types:
            session.add(mt)

        for meter in data.meters:
            session.add(meter)

        session.commit()

def create_events():
    session_factory = get_session_factory()
    time_btree = td(0)
    time_ = td(0)
    time_reserve = td(0)
    for meter in data.meters:
        print(f"Working with meter: {meter.id}")
        dt_ranges = get_date_time_ranges()
        for dt_range in dt_ranges:
            events = []
            cms = []
            kw1 = {"date_time": dt_range[0], "panel_id": meter.panel_id, "meter_id": meter.meter_id}
            kw2 = {"date_time": dt_range[1], "panel_id": meter.panel_id, "meter_id": meter.meter_id}
            e1 = get_event(**kw1)
            e2 = get_event(**kw2)
            events.extend((e1, e2))
            # print(meter.meter_type_id)
            for ch in range(1, data.get_number_channels(mt_id=meter.meter_type_id) + 1):
                cms.append(get_cm(event_id=e1["id"], channel=ch, **kw1))
                cms.append(get_cm(event_id=e2["id"], channel=ch, **kw2))

            events_btree = [EventsBtree(**ev) for ev in events]
            cms_btree = [CmBtree(**cm) for cm in cms]

            events_ = [Events(**ev) for ev in events]
            cms_ = [Cm(**cm) for cm in cms]

            events_reserve = [Events1(**ev) for ev in events]
            cms_reserve = [Cm1(**cm) for cm in cms]
            with session_factory() as session:
                start = dt.now()
                session.bulk_save_objects(events_btree + cms_btree)
                session.commit()
                time_btree += dt.now() - start

                start = dt.now()
                session.bulk_save_objects(events_ + cms_)
                session.commit()
                time_ += dt.now() - start

                start = dt.now()
                session.bulk_save_objects(events_reserve + cms_reserve)
                session.commit()
                time_reserve += dt.now() - start
        print(f"time_btree: {time_btree}, time_: {time_}, time_reserve: {time_reserve}")

    print(f"time_btree: {time_btree}, time_: {time_}, time_reserve: {time_reserve}")
