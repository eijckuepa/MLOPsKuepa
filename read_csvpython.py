import pandas as pd
def carga_datos(string):
  df=pd.read_csv(string)
  return df.head()
