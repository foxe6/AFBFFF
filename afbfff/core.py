import requests
import sqlq


class AFBFFF(object):
    url = ""

    def __init__(self, token: str = "") -> None:
        if type(self) is AFBFFF:
            raise Exception(type(self).__name__+" is an abstract class")
        self.url += f"?token="+token if token else ""

    def upload(self, filename: str) -> None:
        response = None
        try:
            try:
                response = requests.post(self.url, files={"file": open(filename, "rb")}).json()
                return response
            except Exception as e:
                raise e
        finally:
            sqlqueue = sqlq.SqlQueue(server=True, db="db.db", timeout_commit=100)
            sql = '''CREATE TABLE "history" IF NOT EXISTS ("_id" text, "path" text);'''
            sqlqueue.sql(sql)
            sql = '''INSERT INTO history VALUES (?, ?);'''
            data = (response["data"]["file"]["metadata"]["id"], filename)
            sqlqueue.sql(sql, data)
            sqlqueue.commit()
            sqlqueue.stop()


class AnonFiles(AFBFFF):
    url = "https://api.anonfiles.com/upload"

    def __init__(self, token: str = "") -> None:
        super().__init__(token)


class BayFiles(AFBFFF):
    url = "https://api.bayfiles.com/upload"

    def __init__(self, token: str = "") -> None:
        super().__init__(token)


class ForumFiles(AFBFFF):
    url = "https://api.forumfiles.com/upload"

    def __init__(self) -> None:
        super().__init__()

