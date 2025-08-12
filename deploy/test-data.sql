-- 1. Activity ------------------------------------------------------
INSERT INTO activity (id, path, name)
VALUES (gen_random_uuid(), 'cars.car.parts'::ltree, 'Запчасти'),
       (gen_random_uuid(), 'cars.car'::ltree, 'Легковые'),
       (gen_random_uuid(), 'cars.truck'::ltree, 'Грузовые'),
       (gen_random_uuid(), 'food.milk'::ltree, 'Молочная продукция'),
       (gen_random_uuid(), 'food.meat'::ltree, 'Мясная продукция'),
       (gen_random_uuid(), 'cars.car.accessories'::ltree, 'Аксессуары'),
       (gen_random_uuid(), 'cars'::ltree, 'Автомобили'),
       (gen_random_uuid(), 'food'::ltree, 'Еда');


-- 2. BUILDING ------------------------------------------------------
INSERT INTO building (id, address, latitude, longitude)
VALUES (gen_random_uuid(), 'г. Москва, Кремль, 1', 55.7560, 37.6175),
       (gen_random_uuid(), 'г. Москва, ул. Никольская, 5', 55.7605, 37.6150),
       (gen_random_uuid(), 'г. Москва, ул. Тверская, 20', 55.7700, 37.6200),
       (gen_random_uuid(), 'г. Москва, Садовая, 60', 55.7300, 37.6000),
       (gen_random_uuid(), 'г. Москва, Профсоюзная, 100', 55.8000, 37.7000),
       (gen_random_uuid(), 'г. Зеленоград, к. 1', 55.9400, 37.4000);

-- 3. ORGANIZATION --------------------------------------------------
WITH b AS (SELECT id, address
           FROM building)
INSERT
INTO organization (id, name, building_id)
VALUES (gen_random_uuid(), 'ООО "Рога и Копыта"', (SELECT id FROM b WHERE address LIKE '%Кремль%')),
       (gen_random_uuid(), 'ЗАО "Speedy Cars"', (SELECT id FROM b WHERE address LIKE '%Никольская%')),
       (gen_random_uuid(), 'ООО "Молочный путь"', (SELECT id FROM b WHERE address LIKE '%Тверская%')),
       (gen_random_uuid(), 'АО "Heavy Trucks"', (SELECT id FROM b WHERE address LIKE '%Садовая%')),
       (gen_random_uuid(), 'ИП "Spare Parts & Co"', (SELECT id FROM b WHERE address LIKE '%Профсоюзная%')),
       (gen_random_uuid(), 'ООО "Accessories Shop"', (SELECT id FROM b WHERE address LIKE '%Никольская%')),
       (gen_random_uuid(), 'ООО "Meat Lovers"', (SELECT id FROM b WHERE address LIKE '%Тверская%')),
       (gen_random_uuid(), 'ООО "FarAway Ltd"', (SELECT id FROM b WHERE address LIKE '%Зеленоград%'));

-- 4. ORGANIZATION_PHONE -------------------------------------------
INSERT INTO organization_phone (id, organization_id, number)
SELECT gen_random_uuid(), o.id, v.num
FROM (VALUES ('ООО "Рога и Копыта"', '8-495-111-11-11'),
             ('ООО "Рога и Копыта"', '8-800-555-00-01'),
             ('ЗАО "Speedy Cars"', '8-495-222-22-22'),
             ('ЗАО "Speedy Cars"', '8-800-555-00-02'),
             ('ООО "Молочный путь"', '8-495-333-33-33'),
             ('АО "Heavy Trucks"', '8-495-444-44-44'),
             ('ИП "Spare Parts & Co"', '8-495-555-55-55'),
             ('ООО "Accessories Shop"', '8-495-666-66-66'),
             ('ООО "Meat Lovers"', '8-495-777-77-77'),
             ('ООО "FarAway Ltd"', '8-495-888-88-88')) AS v(org_name, num)
         JOIN organization o ON o.name = v.org_name;

-- 5. ORGANIZATION_ACTIVITY ----------------------------------------
INSERT INTO organization_activity (organization_id, activity_id)
SELECT o.id,
       a.id
FROM organization o
         JOIN (VALUES ('ООО "Рога и Копыта"', 'food.meat'::ltree),
                      ('ЗАО "Speedy Cars"', 'cars.car'::ltree),
                      ('ООО "Молочный путь"', 'food.milk'::ltree),
                      ('АО "Heavy Trucks"', 'cars.truck'::ltree),
                      ('ИП "Spare Parts & Co"', 'cars.car.parts'::ltree),
                      ('ООО "Accessories Shop"', 'cars.car.accessories'::ltree),
                      ('ООО "Meat Lovers"', 'food.meat'::ltree),
                      ('ООО "Meat Lovers"', 'food.milk'::ltree),
                      ('ООО "FarAway Ltd"', 'food.meat'::ltree)) AS m(org_name, act_path)
              ON o.name = m.org_name
         JOIN activity a
              ON a.path = m.act_path;