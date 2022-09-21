import streamlit as st
import numpy as np
import pandas as pd

st.title('折れ線グラフで円周率')

array_pi = np.array([3,1,4,1,5,9,2,6,5,3,5,8,9,7,9])
df = pd.DataFrame(array_pi, columns=['pi'])
# df.plot()
# print(df)
st.line_chart(df)