import streamlit as st
import requests
import pandas as pd


# Function to fetch JSON data from the given URL
def fetch_json_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

# Function to display data ordered by descending popularity using Streamlit
def display_ordered_data(json_data):
    # Extract the 'products' dictionary from the JSON response
    products_data = json_data.get('products', {})

    # Sort the products based on 'popularity' in descending order
    sorted_products = sorted(products_data.values(), key=lambda x: int(x['popularity']), reverse=True)

    # Display the ordered data in tabular form with headers using Streamlit
    st.header("Top Products Ordered by Popularity")
    table_data = {'Rank': [], 'Title': [], 'Price': [], 'Popularity': []}

    for product_id, product in enumerate(sorted_products, start=1):
        table_data['Rank'].append(product_id)
        table_data['Title'].append(product['title'])
        table_data['Price'].append(product['price'])
        table_data['Popularity'].append(product['popularity'])

    st.table(pd.DataFrame(table_data).style.set_properties(**{'text-align': 'center'}))

# Replace 'your_json_file_url' with the actual URL of your JSON file
json_file_url = 'https://s3.amazonaws.com/open-to-cors/assignment.json'

# Fetch JSON data from the URL
json_data = fetch_json_data(json_file_url)

# Display the data ordered by descending popularity using Streamlit
display_ordered_data(json_data)
