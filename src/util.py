import pandas as pd
import os

def try_load(DIR, file_loc):
    p = os.path.join(DIR, file_loc)
    try:
        get = pd.read_csv(p)
        print('Loading ... ', p)
        return get
    except:
        return None
