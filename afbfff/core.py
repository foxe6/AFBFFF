from .api import *
from filehandling import join_path, abs_main_dir
import os


class AFBFFF(object):
    def __init__(self, item: str,
                 split: bool = False, split_size: int = 1024*1024*4000,
                 host: str = "AnonFiles", mirror: bool = False):
        if not os.path.isabs(item):
            item = join_path(abs_main_dir(2), item)
        if os.path.isfile(item):
            if not split:
                if not mirror:
                    globals()[host]().upload(item)
                else:
                    AnonFiles().upload(item)
                    BayFiles().upload(item)
                    ForumFiles().upload(item)
            else:
                pass
        elif os.path.isdir(item):
            pass


