from .api import *
from filehandling import join_path, abs_main_dir, file_size
from omnitools import randstr, p
import time
import os
import subprocess


__ALL__ = ["AFBFFF"]


def AFBFFF(item: str, db: str, big_item_split_parts: int = -1,
           split: bool = False, split_size: int = 1024*1024*4000,
           host: str = "AnonFiles", mirror: bool = False,
           _7z_exe: str = r"C:\Program Files\7-Zip\7z.exe",
           temp_dir: str = None, _depth: int = 0) -> None:
    if not temp_dir:
        temp_dir = os.environ["TEMP"]
    if not os.path.isabs(db):
        db = join_path(abs_main_dir(2), db)
    if not os.path.isabs(item):
        item = join_path(abs_main_dir(2), item)
    p(f"[Started] {item}")
    try:
        if os.path.isfile(item) and not split:
            files = [item]
        else:
            basename = os.path.basename(item)+".zip"
            temp = randstr(2 ** 3)+"_"+str(int(time.time()))
            dest = join_path(temp_dir, temp, basename)
            fs = file_size(item)
            if big_item_split_parts > 1:
                if fs >= (big_item_split_parts-1)**2+1:
                    import math
                    split_size = math.ceil(fs/big_item_split_parts)
                else:
                    raise Exception(f"{item} is too small ({fs}B) to split into {big_item_split_parts} parts")
            cmd = [_7z_exe, "a", "-tzip", f"-v{split_size}b", "-mx=0", dest, item]
            if os.path.isdir(item):
                cmd.append("-r")
            p(f"[Zipping] {item}", cmd)
            process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            process.communicate()
            files = [join_path(temp_dir, temp, file) for file in os.listdir(join_path(temp_dir, temp))]
            p(f"[Zipped] {item} has {len(files)} parts", files)
        for file in files:
            # AFBFFF(file, db=db, host=host, mirror=mirror, _depth=_depth+1)
            if not mirror:
                globals()[host](db).upload(filename=file)
            else:
                AnonFiles(db).upload(filename=file)
                BayFiles(db).upload(filename=file)
                ForumFiles(db).upload(filename=file)
    except Exception as e:
        raise Exception(f"{item} failed to upload", e)
    p(f"[Ended] {item}")



