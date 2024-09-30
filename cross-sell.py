import streamlit as st
import requests
import pandas as pd

# Define the API request details
url = "https://lucky-possum.dataos.app/talos/public:affinity-cross-sell-api/api/cross_sell"
headers = {
    'Authorization': 'Bearer dG9rZW5fcmVwZWF0ZWRseV91bmlmb3JtbHlfc21pbGluZ19kZWVyLjg2NDgyZGQzLTE5YjQtNDhkNy1hYzQ4LWVmNmQyMzAzN2Q0ZA=='
}

# Fetch data from the API
response = requests.get(url, headers=headers)

# Check if the API request was successful
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Streamlit app layout
    st.title("Customer Cross-Sell Recommendations")

    # Display the DataFrame in a table format
    st.write("Customer Data:")
    st.dataframe(df)

    # Filter recommendations by customer segment
    customer_segment = st.selectbox("Select Customer Segment", df['customer_segments'].unique())
    filtered_data = df[df['customer_segments'] == customer_segment]

    st.write(f"Cross-Sell Recommendations for {customer_segment} segment:")
    st.dataframe(filtered_data[['customer_id', 'cross_sell_recommendations']])

else:
    st.error("Failed to fetch data from the API")

