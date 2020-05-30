from .api import *
from filehandling import join_path, abs_main_dir
from omnitools import randstr
import time
import os
import subprocess


class AFBFFF(object):
    def __init__(self, item: str,
                 split: bool = False, split_size: int = 1024*4000,
                 host: str = "AnonFiles", mirror: bool = False,
                 _7z_exe: str = r"C:\Program Files\7-Zip\7z.exe",
                 temp_dir: str = r"I:\test"):
        if not temp_dir:
            temp_dir = os.environ["TEMP"]
        if not os.path.isabs(item):
            item = join_path(abs_main_dir(2), item)
        if os.path.isfile(item):
            try:
                if not split:
                    if not mirror:
                        globals()[host]().upload(filename=item, depth=4)
                    else:
                        AnonFiles().upload(filename=item, depth=4)
                        BayFiles().upload(filename=item, depth=4)
                        ForumFiles().upload(filename=item, depth=4)
                else:
                    basename = os.path.basename(item)+".zip"
                    temp = randstr(2**3)+"_"+str(int(time.time()))
                    dest = join_path(temp_dir, temp, basename)
                    cmd = f'''"{_7z_exe}" a -tzip -v{split_size}k -mx=0 "{dest}" "{item}"'''
                    subprocess.run(cmd, shell=True, stdout=None, stderr=None)
                    for file in os.listdir(temp_dir):
                        if file.startswith(basename):
                            AFBFFF(join_path(temp_dir, file))
            except Exception as e:
                print(e, f"{item} failed to upload", flush=True)
        elif os.path.isdir(item):
            pass


