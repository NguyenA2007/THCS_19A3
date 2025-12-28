import sys
import os

sys.path.append(os.path.abspath("../thu_vien_chung"))

import xu_ly_so

so = 17
print(f"{so} là số nguyên tố:", xu_ly_so.kiem_tra_so_nguyen_to(so))
