# Taana Baana

Online store for Taana Baana, a handloom clothing label from Jaipur working with weaving families across India.

Built with Flask and Jinja templates. The range is in `catalog.py`; the bag lives in the signed session cookie.

```bash
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
python app.py        # http://localhost:5000
```

Deployed on Render with `gunicorn app:app`.

Demo store: no real orders, payments or deliveries.
