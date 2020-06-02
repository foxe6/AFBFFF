# Smart Uploader for AnonFiles, BayFiles, ForumFiles

<badges>[![version](https://img.shields.io/pypi/v/afbfff.svg)](https://pypi.org/project/afbfff/)
[![license](https://img.shields.io/pypi/l/afbfff.svg)](https://pypi.org/project/afbfff/)
[![pyversions](https://img.shields.io/pypi/pyversions/afbfff.svg)](https://pypi.org/project/afbfff/)  
[![donate](https://img.shields.io/badge/Donate-Paypal-0070ba.svg)](https://paypal.me/foxe6)
[![powered](https://img.shields.io/badge/Powered%20by-UTF8-red.svg)](https://paypal.me/foxe6)
[![made](https://img.shields.io/badge/Made%20with-PyCharm-red.svg)](https://paypal.me/foxe6)
</badges>

<i>Capable of zipping, splitting, uploading files and folders to AnonFiles, BayFiles, ForumFiles.</i>

# Hierarchy

```
afbfff
'---- AFBFFF()
```

# Example

## python
```python
from afbfff import *
# item link is stored in the specified database
AFBFFF(
    # relative path from "__main__" py file location
    # or absolute path to the target file or folder
    # absolute path is recommended
    # assume "__main__" py file is located at "C:\d\"
    # item="test folder", # is same as below
    item="C:\\d\\test folder",
    # same as `item` except `db` points to a file
    db="db.db",
    # number of parts needed to be split into
    # useful for splitting a large file or folder
    # override `split_size` splitting algorithm
    # see next example for `split_size` usage
    big_item_split_parts=8,
    # specify a remote host from one of the following
    # `host` is ignored when `mirror` is specified
    # "AnonFiles", "BayFiles", "ForumFiles"
    host="AnonFiles",
    # whether to upload to all remote hosts
    mirror=False,
    # path to 7z executable for splitting and zipping
    _7z_exe=r"C:\Program Files\7-Zip\7z.exe",
    # path to temporary folder
    # require enough empty space 
    temp_dir=r"I:\test",
    # internal use
    # print indent depth
    _depth=0
)
AFBFFF(
    item="C:\\d\\test folder\\test.rar",
    db="db.db",
    # whether to split the item
    # `split` is ignored when item is a folder
    split=False,
    # split the item when it exceeds the specified size
    # size in bytes 
    split_size=1024*1024*4000,
    host="AnonFiles",
    mirror=False,
    _7z_exe=r"C:\Program Files\7-Zip\7z.exe",
    temp_dir=r"I:\test",
    _depth=0
)
```
