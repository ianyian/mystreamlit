import streamlit as st
import pandas as pd

st.text('source https://cheat-sheet.streamlit.app/')
st.markdown('_Markdown_')  # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects')  # df, err, func, keras!
st.write(['st', 'is <', 3])  # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True


url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
html = pd.read_html(url, header=0)
df = html[0]

st.dataframe(df)
st.table(df.iloc[0:10])
st.json({'foo': 'bar', 'fu': 'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")

col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')


st.echo()
with st.echo():
    st.write('Code will be executed and printed')

# Stop execution immediately:
st.stop()
# Rerun script immediately:
st.experimental_rerun()
