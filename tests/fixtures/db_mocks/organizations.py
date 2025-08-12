import datetime
from uuid import uuid4

from tests.fixtures.db_mocks.buildings import BUILDINGS

ORGANIZATIONS = (
    {'id': uuid4(), 'name': 'ООО "Рога и Копыта"', 'building_id': BUILDINGS[0]['id'],
     'created_at': datetime.datetime.now()},
    {'id': uuid4(), 'name': 'ЗАО "Speedy Cars"', 'building_id': BUILDINGS[1]['id'],
     'created_at': datetime.datetime.now()},
    {'id': uuid4(), 'name': 'ООО "Молочный путь"', 'building_id': BUILDINGS[2]['id'],
     'created_at': datetime.datetime.now()},
    {'id': uuid4(), 'name': 'АО "Heavy Trucks"', 'building_id': BUILDINGS[3]['id'],
     'created_at': datetime.datetime.now()},
    {'id': uuid4(), 'name': 'ИП "Spare Parts & Co"', 'building_id': BUILDINGS[4]['id'],
     'created_at': datetime.datetime.now()},
    {'id': uuid4(), 'name': 'ООО "Accessories Shop"', 'building_id': BUILDINGS[1]['id'],
     'created_at': datetime.datetime.now()},
    {'id': uuid4(), 'name': 'ООО "Meat Lovers"', 'building_id': BUILDINGS[2]['id'],
     'created_at': datetime.datetime.now()},
    {'id': uuid4(), 'name': 'ООО "FarAway Ltd"', 'building_id': BUILDINGS[5]['id'],
     'created_at': datetime.datetime.now()},
)
