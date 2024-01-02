import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")

"## Energy"

number = st.number_input('Insert a number', value = 1.0)

val1, val2 = st.columns(2)

val1.metric("eV", number * 27.2114)
val2.metric("kcal/mol", number * 627.2114)
