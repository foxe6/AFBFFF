from .api import *
from filehandling import join_path, abs_main_dir
import os


class AFBFFF(object):
    def __init__(self, item: str, zip: bool, mirror: bool = False, host: str = "AnonFiles",
                 split: bool = True, split_size: int = 1024*1024*4000):
        if not os.path.isabs(item):
            item = join_path(abs_main_dir(3), item)
        if os.path.isfile(item):
            if not zip:
                if not split:
                    if not mirror:
                        globals()[host]().upload(item)
                    else:
                        AnonFiles().upload(item)
                        BayFiles().upload(item)
                        ForumFiles().upload(item)


