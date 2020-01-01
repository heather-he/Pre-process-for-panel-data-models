import pandas as pd

# generate an empty panel data (decided by date and clientid)
lst_uniqueClient = [1,2,3,4,5,6,7,8,9]

lst_dfToBeConcat = []
lst_keys = []

for cli in lst_uniqueClient:
    lst_dfToBeConcat.append(pd.DataFrame(pd.date_range(start='1/4/2012', end='30/09/2012')))
    lst_keys.append(cli)

df_xtEmtpy = pd.concat(lst_dfToBeConcat,
                  keys = lst_keys,
                  names=['ClientID', 'Row ID']).reset_index()
df_xtEmtpy.drop(labels = ["Row ID"], axis = 1, inplace=True)
df_xtEmtpy.columns = ["ClientID","Date"]
