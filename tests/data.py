import uuid

from apps.appliances.models import Panels, MeterTypes, Meters
from apps.locations.models import Locations

locations = [
    Locations(
        id="3746daae-99e9-4257-9aeb-de2e778c550f",
        created_at="2022-02-02 10:19:06.318251",
        name="Tariq home",
        area=200,
        tcl=27,
    ),
    Locations(
        id="c6f27362-edc0-480b-9db4-45dc55c304df",
        created_at="2022-05-12 16:36:44.499227",
        name="Eleganza",
        area=200,
        tcl=200,
    ),
    Locations(
        id="ecb1f50f-1fee-4404-a221-f59736f74d9a",
        created_at="2022-05-12 16:38:21.658323",
        name="ENOC - Jumeirah Village Circle",
        area=78,
        tcl=120,
    ),
    Locations(
        id="ecb4f87c-9a38-4c23-94c0-6682ea0f8a88",
        created_at="2022-05-12 16:38:21.658323",
        name="Al Warqa	",
        area=80,
        tcl=100,
    ),
]


panels = [
    Panels(
        id="0695e2c1-3a7c-40d4-93f5-d7018b53e0a3",
        location_id="ecb4f87c-9a38-4c23-94c0-6682ea0f8a88",
        node="san00015",
        name="Main Panel",
    ),
    Panels(
        id="2c5bec26-bfe6-4898-80f9-9437f2e23ee6",
        location_id="ecb1f50f-1fee-4404-a221-f59736f74d9a",
        node="san00015",
        name="Main Panel",
    ),
    Panels(
        id="cba9de13-9c2f-436e-aee5-3f3ff000d944",
        location_id="c6f27362-edc0-480b-9db4-45dc55c304df",
        node="san00011",
        name="Dining Room Panel",
    ),
    Panels(
        id="14b8531b-2c7c-4833-8e93-9297dffd60bf",
        location_id="c6f27362-edc0-480b-9db4-45dc55c304df",
        node="san00012",
        name="Kitchen Panel",
    ),
    Panels(
        id="b639cf31-c814-4bc1-ab87-aaa849d055fa",
        location_id="c6f27362-edc0-480b-9db4-45dc55c304df",
        node="san00012",
        name="Outdoor Panel",
    ),
    Panels(
        id="7e95d82b-f246-4a36-90fa-88809772054d",
        location_id="ecb1f50f-1fee-4404-a221-f59736f74d9a",
        node="san00013",
        name="Panel 2",
    ),
    Panels(
        id="1ec834d8-2146-4274-a5b6-5f8e0e66e5e2",
        location_id="3746daae-99e9-4257-9aeb-de2e778c550f",
        node="Node",
        name="Tariq home",
    ),
]


meter_types = [
    MeterTypes(id="a5bc898a-0708-4960-8904-d602e85fca5b", name=20, number_of_channels=30),
    MeterTypes(id="360fb5df-d633-45ed-9e62-82f0e91c02e9", name=202, number_of_channels=42),
    MeterTypes(id="391bdb42-0103-4660-b790-64f3297cbe54", name=211, number_of_channels=4),
]


meters = [
    Meters(id="694e9868-c023-45e8-a4d5-fe6004bbf2cf", panel_id="1ec834d8-2146-4274-a5b6-5f8e0e66e5e2", meter_type_id="a5bc898a-0708-4960-8904-d602e85fca5b", meter_id=1),
    Meters(id="ae1cf92a-d631-410f-90dc-0eef75394cf4", panel_id="0695e2c1-3a7c-40d4-93f5-d7018b53e0a3", meter_type_id="391bdb42-0103-4660-b790-64f3297cbe54", meter_id=3),
    Meters(id="a4ac8595-4d4b-4d64-8500-417b6c504041", panel_id="0695e2c1-3a7c-40d4-93f5-d7018b53e0a3", meter_type_id="391bdb42-0103-4660-b790-64f3297cbe54", meter_id=2),
    Meters(id="de6f30ff-3e19-4c0c-93bb-c52d52de0a12", panel_id="0695e2c1-3a7c-40d4-93f5-d7018b53e0a3", meter_type_id="a5bc898a-0708-4960-8904-d602e85fca5b", meter_id=1),
    Meters(id="6643e79a-6a98-48a8-b93c-f01cf6f4df37", panel_id="14b8531b-2c7c-4833-8e93-9297dffd60bf", meter_type_id="360fb5df-d633-45ed-9e62-82f0e91c02e9", meter_id=1),
    Meters(id="15677a87-bd67-4023-a487-888e6936aaa0", panel_id="2c5bec26-bfe6-4898-80f9-9437f2e23ee6", meter_type_id="391bdb42-0103-4660-b790-64f3297cbe54", meter_id=1),
    Meters(id="17e504a3-6659-4215-ab9c-888ba0e9673d", panel_id="7e95d82b-f246-4a36-90fa-88809772054d", meter_type_id="a5bc898a-0708-4960-8904-d602e85fca5b", meter_id=1),
    Meters(id="1b5038ae-67b6-40ba-905f-ca95fb86f6a5", panel_id="7e95d82b-f246-4a36-90fa-88809772054d", meter_type_id="a5bc898a-0708-4960-8904-d602e85fca5b", meter_id=2),
    Meters(id="b2313967-c353-4299-87c3-73f9f85e3dd9", panel_id="cba9de13-9c2f-436e-aee5-3f3ff000d944", meter_type_id="360fb5df-d633-45ed-9e62-82f0e91c02e9", meter_id=1),
]


def get_number_channels(mt_id):
    for mt in meter_types:
        if mt.id == mt_id:
            return mt.number_of_channels
