import pandas as pd

def try_load(file_loc):
    try:
        return pd.read_csv(os.path.join(DIR, 'rapidaddition.csv'))
    except:
        return None
