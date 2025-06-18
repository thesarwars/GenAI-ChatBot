import streamlit as st
from main import gen_restaurant_name_and_items

st.title("Tahasin GenAI")

cuisine = st.sidebar.selectbox(
    "Select a cuisine",
    [
        None,
        "Turkish",
        "Italian",
        "Indian",
        "Chinese",
        "Mexican",
        "French",
        "Japanese",
        "Thai",
        "Greek",
        "Spanish"
    ]
)
print('cuisine', cuisine)
if cuisine:
    response = gen_restaurant_name_and_items(cuisine)
    print('str_resp', response)
    st.header(response["restaurant_name"].strip())
    menu_items = response["menu_items"].strip().split(",")
    
    st.write("****Menu Items****")
    for item in menu_items:
        st.write(f"- {item.strip()}")
    # st.write("****End of Menu Items****")