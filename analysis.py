import seaborn as sns
import matplotlib.pyplot as plt
from utils import preprocess_data

def analyze_booking_trends(data):
    """Visualize booking trends by month and day of the week."""
    data = preprocess_data(data)

    # Monthly booking trends
    plt.figure(figsize=(10, 6))
    monthly_data = data['arrival_date_month'].value_counts().sort_index()
    sns.barplot(x=monthly_data.index, y=monthly_data.values, palette="Blues_d")
    plt.title("Booking Trends by Month", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Number of Bookings", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/booking_trends.png")
    plt.show()

def analyze_cancellations(data):
    """Analyze factors affecting cancellations."""
    data = preprocess_data(data)

    # Factors: lead time, length of stay
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='is_canceled', y='lead_time', data=data, palette="coolwarm")
    plt.title("Cancellation Trends by Lead Time", fontsize=16)
    plt.xlabel("Is Canceled (1 = Yes, 0 = No)", fontsize=12)
    plt.ylabel("Lead Time (days)", fontsize=12)
    plt.tight_layout()
    plt.savefig("outputs/cancellation_factors.png")
    plt.show()

def compare_hotels(data):
    """Compare booking patterns for different types of hotels."""
    data = preprocess_data(data)

    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='hotel', hue='is_canceled', palette="Set2")
    plt.title("Hotel Bookings: Cancellations vs Confirmed", fontsize=16)
    plt.xlabel("Hotel Type", fontsize=12)
    plt.ylabel("Number of Bookings", fontsize=12)
    plt.legend(title="Booking Status", labels=["Confirmed", "Canceled"])
    plt.tight_layout()
    plt.savefig("outputs/hotel_comparison.png")
    plt.show()
