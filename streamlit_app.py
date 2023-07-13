import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
st.subheader('画面への表示まわりを試す画面')

#例1
st.write('st.write_ \:Hello, _World!_ emoji　:sunglasses:')
st.write('st.write* \:Hello, *World!* emoji　:sunglasses:')
st.text('st.text : Hello, *World!* emoji　:sunglasses:')
st.markdown("""
## TBです
:red[TBTB]と申します。

### 概要
7/1入社です。
""")

#例2
st.write(1234)

st.latex(r'''
y = fx
''')

st.caption('なんの変哲もない数式ですやん…')

code = '''
import pandas as pd

def test_function():
     #code欄を試してみたく、なんとなくdataframeを定義
     df = pd.Dataframe({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })     
'''
st.code(code, language='python')

#例3
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

#例4
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

#例5
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)