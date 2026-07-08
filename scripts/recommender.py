import pandas as pd

performance = pd.read_csv(r"E:\Project\data\processed\scheme_performance_clean.csv")

print(" Mutual Fund Recommendation System ")

risk = input("\nEnter Risk Appetite (Low / Moderate / High): ").strip().title()
valid_risk = ["Low", "Moderate", "High"]

if risk not in valid_risk:
    print("\n Invalid Risk Appetite!")
    print("Please enter: Low, Moderate or High")
    exit()

recommendation = (performance[performance["risk_grade"].str.title() == risk].sort_values("sharpe_ratio",ascending=False).head(3))
print("\n")
print(f"Top 3 Recommended Funds for {risk} Risk Investors")


if recommendation.empty:
    print("No matching funds found.")
else:
    print( recommendation[
            [
                "scheme_name",
                "fund_house",
                "category",
                "sharpe_ratio",
                "return_3yr_pct",
                "risk_grade"]].to_string(index=False))
