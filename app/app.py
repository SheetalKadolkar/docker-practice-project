from flask import Flask, jsonify
import os
import time
import redis
import psycopg2

app = Flask(__name__)

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
COUNTER_KEY = "hits"
r = redis.from_url(REDIS_URL)

def get_db_conn():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "appdb"),
        user=os.getenv("POSTGRES_USER", "appuser"),
        password=os.getenv("POSTGRES_PASSWORD", "apppass"),
        host=os.getenv("POSTGRES_HOST", "db"),
        port=int(os.getenv("POSTGRES_PORT", 5432))
    )

@app.route("/")
def index():
    # increment redis counter
    try:
        hits = r.incr(COUNTER_KEY)
    except Exception as e:
        hits = None

    # simple query to test db (creates table if not exists)
    msg = "ok"
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id SERIAL PRIMARY KEY,
                ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cur.execute("INSERT INTO visits DEFAULT VALUES;")
        conn.commit()
        cur.execute("SELECT COUNT(*) FROM visits;")
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
    except Exception as e:
        msg = f"db_error: {e}"
        count = None

    return jsonify({
        "status": msg,
        "visits_total": count,
        "redis_hits": hits,
        "time": time.time()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
