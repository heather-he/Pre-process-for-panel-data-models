import pandas as pd
import re
import numpy as np

# Financial Times data are presented in a data-descending order 
# reverse it to a normal order
def invert_date(in_name,out_name):
    df = pd.read_csv(in_name)
    df['Date'] = df['Date'].apply(lambda x: re.findall('\s.*\d{2}',x)[0])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df.to_csv(out_name,index = False)
    
