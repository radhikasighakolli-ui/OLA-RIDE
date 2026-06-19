import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("OLA_Dataset.csv")

# Page config
st.set_page_config(page_title="OLA Ride Insights", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ("Dashboard", "Payment Analysis", "Cancellations", "Ratings Summary")
)

# Filters
vehicle_types = df['Vehicle_Type'].dropna().unique()
booking_statuses = df['Booking_Status'].dropna().unique()

selected_vehicle = st.sidebar.multiselect(
    'Select Vehicle Type:',
    vehicle_types
)

selected_booking_status = st.sidebar.multiselect(
    'Select Booking Status:',
    booking_statuses
)

filtered_df = df.copy()

if selected_vehicle:
    filtered_df = filtered_df[
        filtered_df['Vehicle_Type'].isin(selected_vehicle)
    ]

if selected_booking_status:
    filtered_df = filtered_df[
        filtered_df['Booking_Status'].isin(selected_booking_status)
    ]

# Pages
if section == "Dashboard":
    st.title("📊 OLA Ride Dashboard")
    st.subheader("Filtered Ride Data")
    st.write(filtered_df)

elif section == "Payment Analysis":
    st.title("💳 Payment Method Analysis")
    st.subheader("Total Booking Value by Payment Method")
    total_booking_value = filtered_df.groupby(
        'Payment_Method'
    )['Booking_Value'].sum()

    st.bar_chart(total_booking_value)

elif section == "Cancellations":
    st.title("❌ Ride Cancellations Analysis")
    st.subheader("Cancellation Reasons by Drivers")
    cancel_reasons = filtered_df[
        'Canceled_Rides_by_Driver'
    ].value_counts()

    st.bar_chart(cancel_reasons)

elif section == "Ratings Summary":
    st.title("⭐ Driver & Customer Ratings Summary")
    ratings_summary = filtered_df[
        ['Driver_Ratings', 'Customer_Rating']
    ].describe()

    st.write(ratings_summary)