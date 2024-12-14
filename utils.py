import pandas as pd

def preprocess_data(data):
    """Preprocess and clean data."""
    # Filter necessary columns
    columns_to_keep = [
        "hotel", "is_canceled", "lead_time", "arrival_date_month",
        "stays_in_weekend_nights", "stays_in_week_nights", "adults",
        "children", "babies", "reserved_room_type", "assigned_room_type",
        "adr", "customer_type"
    ]
    data = data[columns_to_keep]

    # Fill missing values
    data['children'].fillna(0, inplace=True)
    data['babies'].fillna(0, inplace=True)

    # Ensure numeric columns are of the correct type
    data['children'] = data['children'].astype(int)
    data['babies'] = data['babies'].astype(int)

    # Create total guests column
    data['total_guests'] = data['adults'] + data['children'] + data['babies']

    # Sort months for consistent visualization
    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    data['arrival_date_month'] = pd.Categorical(data['arrival_date_month'], categories=month_order, ordered=True)

    return data
