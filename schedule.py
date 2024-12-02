import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Title and description
st.title("Employee Scheduling Tool")
st.write("Enter shifts for employees across selected dates.")

# Sidebar Inputs
st.sidebar.header("Inputs")

# Employee List
employees = st.sidebar.text_area("Enter Employee Names (one per line):").split("\n")
employees = [emp.strip() for emp in employees if emp.strip()]  # Remove empty lines and whitespace

# Start Date
start_date = st.sidebar.date_input("Select Start Date:", value=datetime.today())

# Number of Days to Schedule
num_days = st.sidebar.slider("Number of Days to Schedule:", 1, 14, 7)

# Predefined Shifts
shifts = ["9 PM - 3:30 AM", "3 PM - 10 PM", "10 AM - 6 PM"]

# Input Validation
if not employees:
    st.warning("Please enter at least one employee name.")
    st.stop()

# Generate Dates for the Schedule
dates = [start_date + timedelta(days=i) for i in range(num_days)]
date_columns = [date.strftime("%Y-%m-%d") for date in dates]

# Create an empty DataFrame with employees as rows and dates as columns
schedule_df = pd.DataFrame(index=employees, columns=date_columns)

# Fill the DataFrame with empty values for shifts
schedule_df.fillna("", inplace=True)

# Display the editable schedule
st.subheader("Enter Shifts for Employees")
st.write("Enter shift codes (e.g., `9 PM - 3:30 AM`) for each employee on the corresponding date.")

editable_schedule = st.data_editor(
    schedule_df,
    use_container_width=True
)

# Save the edited schedule when the "Save Schedule" button is clicked
if st.button("Save Schedule"):
    st.success("Schedule saved!")
    st.write(editable_schedule)

    # Option to Export Schedule
    if st.button("Export to Excel"):
        editable_schedule.to_excel("employee_schedule.xlsx")
        st.success("Schedule saved as 'employee_schedule.xlsx'. Download from your files.")
