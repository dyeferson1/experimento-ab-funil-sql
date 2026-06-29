from pathlib import Path
import pandas as pd
import numpy as np
from scipy import stats

DATA_PATH = Path("data/events.csv")

def load_data():
    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)

    np.random.seed(42)
    return pd.DataFrame({
        "user_id": range(1, 501),
        "group": np.random.choice(["A", "B"], 500),
        "product_page": np.random.choice([0, 1], 500, p=[0.25, 0.75]),
        "product_cart": np.random.choice([0, 1], 500, p=[0.60, 0.40]),
        "purchase": np.random.choice([0, 1], 500, p=[0.82, 0.18])
    })

def conversion_by_group(df, step):
    return (
        df.groupby("group")[step]
        .agg(total_users="count", conversions="sum")
        .assign(conversion_rate=lambda x: x["conversions"] / x["total_users"])
        .reset_index()
    )

def z_test(success_a, total_a, success_b, total_b):
    p1 = success_a / total_a
    p2 = success_b / total_b
    pooled = (success_a + success_b) / (total_a + total_b)
    standard_error = np.sqrt(pooled * (1 - pooled) * (1 / total_a + 1 / total_b))
    z_score = (p1 - p2) / standard_error
    return 2 * (1 - stats.norm.cdf(abs(z_score)))

def main():
    df = load_data()

    for step in ["product_page", "product_cart", "purchase"]:
        print(f"\nEtapa: {step}")
        print(conversion_by_group(df, step))

    group_a = df[df["group"] == "A"]
    group_b = df[df["group"] == "B"]

    p_value = z_test(
        group_a["purchase"].sum(),
        len(group_a),
        group_b["purchase"].sum(),
        len(group_b)
    )

    print(f"\nTeste A/B - p-valor: {p_value:.4f}")

    if p_value < 0.05:
        print("Conclusão: diferença estatisticamente significativa entre os grupos.")
    else:
        print("Conclusão: não há evidência estatística suficiente de diferença.")

if __name__ == "__main__":
    main()
