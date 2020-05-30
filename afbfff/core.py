from .api import *
from filehandling import join_path, abs_main_dir
from omnitools import randstr, p
import time
import os
import subprocess


class AFBFFF(object):
    def __init__(self, item: str,
                 split: bool = False, split_size: int = 1024*4000,
                 host: str = "AnonFiles", mirror: bool = False,
                 _7z_exe: str = r"C:\Program Files\7-Zip\7z.exe",
                 temp_dir: str = r"I:\test",
                 depth: int = 4):
        if not temp_dir:
            temp_dir = os.environ["TEMP"]
        if not os.path.isabs(item):
            item = join_path(abs_main_dir(2), item)
        if os.path.isfile(item):
            try:
                if not split:
                    if not mirror:
                        globals()[host]().upload(filename=item, depth=int(depth))
                    else:
                        AnonFiles().upload(filename=item, depth=int(depth))
                        BayFiles().upload(filename=item, depth=int(depth))
                        ForumFiles().upload(filename=item, depth=int(depth))
                else:
                    basename = os.path.basename(item)+".zip"
                    temp = randstr(2**3)+"_"+str(int(time.time()))
                    dest = join_path(temp_dir, temp, basename)
                    cmd = [_7z_exe, "a", "-tzip", f"-v{split_size}k", "-mx=0", dest, item]
                    p(cmd)
                    process = subprocess.Popen(cmd)
                    process.communicate()
                    for file in os.listdir(join_path(temp_dir, temp)):
                        AFBFFF(join_path(temp_dir, temp, file), host=host, mirror=mirror, depth=depth+1)
            except Exception as e:
                p(e, f"{item} failed to upload")
        elif os.path.isdir(item):
            pass


