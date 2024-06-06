import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

def main():
    st.title("Travel Guide")

    # Get unique cities from the data
    cities = data["City"].unique()

    # Create a selectbox for cities
    selected_city = st.selectbox("Select a City", cities)

    # Filter the data based on the selected city
    city_data = data[data["City"] == selected_city]

    # Display the filtered data
    st.write(city_data)

    # Create selectboxes for other columns
    selected_type = st.selectbox("Select Type", city_data["Type"].unique())
    selected_establishment_year = st.selectbox("Select Establishment Year", city_data["Establishment Year"].unique())
    selected_time_needed = st.selectbox("Select Time Needed (in hours)", city_data["time needed to visit in hrs"].unique())
    selected_airport = st.selectbox("Select Airport Availability", city_data["Airport with 50km Radius"].unique())
    selected_weekly_off = st.selectbox("Select Weekly Off", city_data["Weekly Off"].unique())
    selected_significance = st.selectbox("Select Significance", city_data["Significance"].unique())
    selected_dslr_allowed = st.selectbox("Select DSLR Allowed", city_data["DSLR Allowed"].unique())
    selected_num_reviews = st.selectbox("Select Number of Google Reviews (in lakhs)", city_data["Number of google review in lakhs"].unique())
    selected_best_time = st.selectbox("Select Best Time to Visit", city_data["Best Time to visit"].unique())

    # Filter the data based on selected options
    filtered_data = city_data[
        (city_data["Type"] == selected_type) &
        (city_data["Establishment Year"] == selected_establishment_year) &
        (city_data["time needed to visit in hrs"] == selected_time_needed) &
        (city_data["Airport with 50km Radius"] == selected_airport) &
        (city_data["Weekly Off"] == selected_weekly_off) &
        (city_data["Significance"] == selected_significance) &
        (city_data["DSLR Allowed"] == selected_dslr_allowed) &
        (city_data["Number of google review in lakhs"] == selected_num_reviews) &
        (city_data["Best Time to visit"] == selected_best_time)
    ]

    # Display the filtered data
    st.write(filtered_data)

    # Create a pie chart for rating distribution
    rating_counts = filtered_data["Google review rating"].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%')
    ax.axis('equal')  # Ensure the pie chart is circular
    ax.set_title('Rating Distribution')
    st.pyplot(fig)

if __name__ == "__main__":
    main()