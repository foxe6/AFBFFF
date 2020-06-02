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
AFBFFF(
    item: str,
    db: str,
    big_item_split_parts: int = -1,
    split: bool = False,
    split_size: int = 1024*1024*4000,
    host: str = "AnonFiles",
    mirror: bool = False,
    _7z_exe: str = r"C:\Program Files\7-Zip\7z.exe",
    temp_dir: str = r"I:\test", _depth: int = 0
)
```
