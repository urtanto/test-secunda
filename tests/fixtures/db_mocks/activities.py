from uuid import uuid4

from sqlalchemy_utils import Ltree

ACTIVITIES = (
    {'id': uuid4(), 'path': Ltree('cars.car.parts'), 'name': 'Запчасти'},
    {'id': uuid4(), 'path': Ltree('cars.car'), 'name': 'Легковые'},
    {'id': uuid4(), 'path': Ltree('cars.truck'), 'name': 'Грузовые'},
    {'id': uuid4(), 'path': Ltree('food.milk'), 'name': 'Молочная продукция'},
    {'id': uuid4(), 'path': Ltree('food.meat'), 'name': 'Мясная продукция'},
    {'id': uuid4(), 'path': Ltree('cars.car.accessories'), 'name': 'Аксессуары'},
    {'id': uuid4(), 'path': Ltree('cars'), 'name': 'Автомобили'},
    {'id': uuid4(), 'path': Ltree('food'), 'name': 'Еда'},
)
