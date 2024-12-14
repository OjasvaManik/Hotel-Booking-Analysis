import pandas as pd
from analysis import analyze_booking_trends, analyze_cancellations, compare_hotels

# Load dataset
data_path = "data/hotel_booking.csv"
hotel_data = pd.read_csv(data_path)

# Run analyses
analyze_booking_trends(hotel_data)
analyze_cancellations(hotel_data)
compare_hotels(hotel_data)

print("Analysis complete. Visualizations saved in 'outputs/' folder.")
