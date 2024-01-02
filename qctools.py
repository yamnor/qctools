import streamlit as st
from st_pages import Page, show_pages, add_page_title

add_page_title(layout="wide")

show_pages(
  [
    Page("qctools.py", "Home"),
    Page("page1.py", "Calculate"),
  ]
)