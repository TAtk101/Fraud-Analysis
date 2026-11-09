

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "credit_card_fraud_10k.csv"

df = pd.read_csv(file_path)

output_folder = project_folder / "python" / "visualizations"
output_folder.mkdir(parents=True, exist_ok=True)

print("FRAUD INVESTIGATION ANALYSIS")
print("=" * 40)

print("\nDATA QUALITY")
print("Dataset size:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate transaction IDs:", df["transaction_id"].duplicated().sum())

# Fraud rate
fraud_count = (df["is_fraud"] == 1).sum()
legitimate_count = (df["is_fraud"] == 0).sum()
fraud_rate = df["is_fraud"].mean() * 100

print("\nOVERALL FRAUD SUMMARY")
print("Total transactions:", len(df))
print("Fraudulent transactions:", fraud_count)
print("Legitimate transactions:", legitimate_count)
print("Overall fraud rate:", round(fraud_rate, 2), "%")

# foreign transaction fraud rate
foreign_rates = (
    df.groupby("foreign_transaction")["is_fraud"].mean() * 100
)

print("\nFRAUD RATE BY FOREIGN TRANSACTION")
print(foreign_rates.round(2))

# fraud rate by location mismatch
location_rates = (
    df.groupby("location_mismatch")["is_fraud"].mean() * 100
)

print("\nFRAUD RATE BY LOCATION MISMATCH")
print(location_rates.round(2))

# group device trust scores
df["device_trust_band"] = pd.cut(
    df["device_trust_score"],
    bins=[24, 39, 59, 79, 99],
    labels=["Low (25-39)", "Medium-Low (40-59)",
            "Medium-High (60-79)", "High (80-99)"]
)

device_rates = (
    df.groupby("device_trust_band", observed=False)["is_fraud"].mean() * 100
)

print("\nFRAUD RATE BY DEVICE TRUST BAND")
print(device_rates.round(2))

# Transaction Velocity
df["velocity_band"] = pd.cut(
    df["velocity_last_24h"],
    bins=[-1, 1, 3, 5, 9],
    labels=["Low (0-1)", "Moderate (2-3)",
            "High (4-5)", "Very High (6+)"]
)

velocity_rates = (
    df.groupby("velocity_band", observed=False)["is_fraud"].mean() * 100
)

print("\nFRAUD RATE BY TRANSACTION VELOCITY")
print(velocity_rates.round(2))

# multiple risk indicators
high_risk_transactions = df[
    (df["foreign_transaction"] == 1) &
    (df["location_mismatch"] == 1)
]

print("\nFOREIGN TRANSACTIONS WITH LOCATION MISMATCH")
print("Transaction count:", len(high_risk_transactions))

if len(high_risk_transactions) > 0:
    combined_fraud_rate = high_risk_transactions["is_fraud"].mean() * 100
    print("Observed fraud rate:", round(combined_fraud_rate, 2), "%")
    print("\nFirst five matching transactions:")
    print(high_risk_transactions.head())
else:
    print("No transactions matched both conditions.")


three_factor_transactions = df[
    (df["foreign_transaction"] == 1) &
    (df["location_mismatch"] == 1) &
    (df["device_trust_score"] < 40)
]

print("\nTRANSACTIONS WITH THREE RISK INDICATORS")
print("Transaction count:", len(three_factor_transactions))

if len(three_factor_transactions) > 0:
    three_factor_rate = three_factor_transactions["is_fraud"].mean() * 100
    print("Observed fraud rate:", round(three_factor_rate, 2), "%")
else:
    print("No transactions matched all three conditions.")

# Foreign vs. domestic fraud rates
foreign_rates.rename(index={0: "Domestic", 1: "Foreign"}).plot(
    kind="bar",
    title="Fraud Rate: Domestic vs. Foreign Transactions",
    ylabel="Fraud rate (%)",
    xlabel="Transaction type",
    rot=0
)

plt.tight_layout()
plt.savefig(output_folder / "foreign_transaction_fraud_rate.png", dpi=300)
plt.close()


#Fraud rate by device trust
device_rates.plot(
    kind="bar",
    title="Fraud Rate by Device Trust",
    ylabel="Fraud rate (%)",
    xlabel="Device trust band",
    rot=20
)

plt.tight_layout()
plt.savefig(output_folder / "device_trust_fraud_rate.png", dpi=300)
plt.close()


#Fraud rate by transaction velocity
velocity_rates.plot(
    kind="bar",
    title="Fraud Rate by Transaction Velocity",
    ylabel="Fraud rate (%)",
    xlabel="Transactions in the Previous 24 Hours",
    rot=20
)

plt.tight_layout()
plt.savefig(output_folder / "velocity_fraud_rate.png", dpi=300)
plt.close()

print("\nCharts saved to:", output_folder)
print("Python analysis complete.")
