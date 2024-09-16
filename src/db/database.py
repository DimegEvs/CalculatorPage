import psycopg2

from src.utils.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS


def connect_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    return conn, cur
