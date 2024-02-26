# Overview

This is an extremely basic Django service using DRF to serve a simple product record (sku and description).
Its main purpose is just for experimenting with Django and DRF, with a special emphasis on using
gunicorn and having other systems call this service.

## Setup of Environment

* Initialize mamba environment `mamba create -n django-product-service -c conda-forge  python=3.12`
* `mamba activate django-product-service`
* `pip install poetry`
* `poetry install --no-root`
* `python manage.py migrate`
* `python manage.py createsuperuser`
* `python manage.py runserver`
  *  Alternatively can run with gunicorn `gunicorn --bind 0.0.0.0:8000 Product.wsgi -w 1`
* `python manage.py test`
* `mypy .`
* `black .`


## Relevant DB Queries

```sql
-- Generate some fake product records
INSERT INTO productcore_product (description, sku)
SELECT
    substr(concat(md5(random()::text), md5(random()::text)), 1, (random() * 64)::integer + 1) AS description,
    substr(concat(md5(random()::text), md5(random()::text)), 1, (random() * 64)::integer + 1) AS sku
FROM generate_series(1,10000) as n
;

-- Check on the table
SELECT COUNT(*) FROM productcore_product;
```