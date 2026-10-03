# Bincom Django Submission

Implements the three questions visible in the supplied Bincom Experienced Software Developer questionnaire:
1. Individual polling-unit result page.
2. Summed result for a selected LGA, calculated from polling-unit results (not announced-LGA totals).
3. Form to create a new polling unit and save all party results.

The supplied questionnaire refers to a `bincom_test.sql` database. That SQL dump was not attached here, so a small Django schema and demo seed command are included. Replace the demo data with the actual supplied dump when available.

## Run
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Then visit http://127.0.0.1:8000/

## Deploy
`render.yaml` and `build.sh` deploy the app to Render as a web service (`gunicorn config.wsgi:application`). In production, set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False` and, if needed, `DJANGO_ALLOWED_HOSTS` / `DJANGO_CSRF_TRUSTED_ORIGINS`.
