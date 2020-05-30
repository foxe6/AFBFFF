from .api import *
from filehandling import join_path, abs_main_dir
from omnitools import randstr, p
import time
import os
import subprocess


__ALL__ = ["AFBFFF"]


class AFBFFF(object):
    def __init__(self, item: str, db: str,
                 split: bool = False, split_size: int = 1024*4000,
                 host: str = "AnonFiles", mirror: bool = False,
                 _7z_exe: str = r"C:\Program Files\7-Zip\7z.exe",
                 temp_dir: str = r"I:\test"):
        if not temp_dir:
            temp_dir = os.environ["TEMP"]
        if not os.path.isabs(db):
            db = join_path(abs_main_dir(2), db)
        if not os.path.isabs(item):
            item = join_path(abs_main_dir(2), item)
        if os.path.isfile(item) and not split:
            try:
                if not mirror:
                    globals()[host](db).upload(filename=item)
                else:
                    AnonFiles(db).upload(filename=item)
                    BayFiles(db).upload(filename=item)
                    ForumFiles(db).upload(filename=item)
            except Exception as e:
                p(e, f"{item} failed to upload")
        else:
            basename = os.path.basename(item)+".zip"
            temp = randstr(2 ** 3)+"_"+str(int(time.time()))
            dest = join_path(temp_dir, temp, basename)
            cmd = [_7z_exe, "a", "-tzip", f"-v{split_size}k", "-mx=0", dest, item]
            if os.path.isdir(item):
                cmd.append("-r")
            p(f"[Zipping] {item}", cmd)
            process = subprocess.Popen(cmd, stderr=None, stdout=None)
            process.communicate()
            files = [join_path(temp_dir, temp, file) for file in os.listdir(join_path(temp_dir, temp))]
            p(f"[Zipped] {item} has {len(files)} parts")
            for file in files:
                AFBFFF(file, db=db, host=host, mirror=mirror)



