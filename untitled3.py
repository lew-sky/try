d:
cd app
.\web\Scripts\activate
streamlit run newapp.py
import pandas as pd
d=pd.DataFrame(index=range(5),columns=range(3))
d.loc[0,2]=3
print(d)
