from src.db.database import connect_db


class History:
    def __init__(self, username: str, expression: str, result: str):
        self.username = username
        self.expression = expression
        self.result = result

    id: int
    username: str
    expression: str
    result: str


class HistoryService:
    @staticmethod
    def get_all_history():
        conn, cur = connect_db()
        query = "SELECT * FROM public.calculations"
        cur.execute(query)
        result = cur.fetchall()
        conn.close()
        history = [History(username=row[1], expression=row[2], result=row[3]) for row in result]
        return history

    @staticmethod
    def add_history(history: History):
        conn, cur = connect_db()
        query = "INSERT INTO public.calculations (username, expression, result) VALUES (%s, %s, %s)"
        cur.execute(query, (history.username, history.expression, history.result))
        conn.commit()
        conn.close()

    @staticmethod
    def get_any_history(filter: str):
        conn, cur = connect_db()
        query = "SELECT * FROM public.calculations" + filter
        cur.execute(query)
        result = cur.fetchall()
        conn.close()
        history = [History(username=row[1], expression=row[2], result=row[3]) for row in result]
        return history
