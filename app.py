# 20-30 mins
import streamlit as st
import requests
import pandas as pd
import json
# Function to fetch JSON data from the API
def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()['products']
    else:
        st.error(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to display data in Streamlit
def display_data(products):
    if products is not None:
        st.header("Product Information")
        products=dict(products)
        sorted_products = dict(sorted(products.items(), key=lambda x: int(x[1]['popularity']), reverse=True))
        df = pd.DataFrame.from_dict(sorted_products, orient='index')
        st.dataframe(df,height=800,width=2000)


custom_css = """
                    <style>
                    .stApp {
                        margin-top: -50px; /* Adjust the value as needed */
                    }
                    </style>
                """
st.markdown(custom_css, unsafe_allow_html=True)
    # st.title("Product Information App")
api_url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
products = fetch_data(api_url)
display_data(products)


