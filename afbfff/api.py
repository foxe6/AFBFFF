import requests
import sqlq
import time


__ALL__ = ["AnonFiles", "BayFiles", "ForumFiles"]


class BaseFiles(object):
    url = ""

    def __init__(self, token: str = "") -> None:
        if type(self) is BaseFiles:
            raise Exception(type(self).__name__+" is an abstract class")
        self.url += f"?token="+token if token else ""

    def upload(self, filename: str) -> dict:
        issued = int(time.time())
        response = None
        try:
            try:
                response = requests.post(self.url, files={"file": open(filename, "rb")}).json()
                return response
            except Exception as e:
                raise e
        finally:
            uploaded = int(time.time())
            sqlqueue = sqlq.SqlQueue(server=True, db="db.db", timeout_commit=100, depth=3)
            sql = '''CREATE TABLE IF NOT EXISTS "history" ("url" TEXT, "path" TEXT, "issued" INTEGER, "uploaded" INTEGER);'''
            sqlqueue.sql(sql)
            sql = '''INSERT INTO history VALUES (?, ?, ?, ?);'''
            data = (response["data"]["file"]["url"]["short"], filename, issued, uploaded)
            sqlqueue.sql(sql, data)
            sqlqueue.commit()
            sqlqueue.stop()


class AnonFiles(BaseFiles):
    url = "https://api.anonfiles.com/upload"

    def __init__(self, token: str = "") -> None:
        super().__init__(token)


class BayFiles(BaseFiles):
    url = "https://api.bayfiles.com/upload"

    def __init__(self, token: str = "") -> None:
        super().__init__(token)


class ForumFiles(BaseFiles):
    url = "https://api.forumfiles.com/upload"

    def __init__(self) -> None:
        super().__init__()

