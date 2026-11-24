import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

k = pd.read_csv("daily.csv")
e = pd.read_csv("emi.csv")
e["total_payable"] = e["emi"] * e["months"]
e["total_interest"] = e["total_payable"] - e["amount"]

cat = k.groupby("category")["rakam"].sum()

print("Kul kharcha:", k["rakam"].sum())
print("Loan records:", len(e))
print("Kul byaaj:", round(e["total_interest"].sum(), 2))
print("Sabse badi EMI:", e["emi"].max())

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
cat.plot(kind="bar", ax=ax[0], title="Kharcha category")
e["total_interest"].plot(kind="bar", ax=ax[1], title="Byaaj har loan par")
plt.tight_layout()
plt.savefig("dashboard.png")

e.to_csv("emi_report.csv", index=False)
print("dashboard.png aur emi_report.csv ban gaye")
