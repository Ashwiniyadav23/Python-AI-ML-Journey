"""
Practical Example: Underfitting vs. Good Fit vs. Overfitting

We create noisy data from a known real pattern (a curve), then fit
3 models of increasing complexity to the SAME data:
  1. Underfit  — a straight line (degree 1)
  2. Good fit  — a moderate curve (degree 4)
  3. Overfit   — an extremely wiggly curve (degree 15)

We compare training error vs. test error for each, to see the
classic overfitting/underfitting signature in real numbers.
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# ----------------------------
# 1. Create noisy data from a known true pattern
# ----------------------------
np.random.seed(42)
X = np.sort(np.random.uniform(0, 10, 40)).reshape(-1, 1)   # 40 x-values, sorted
true_pattern = 0.5 * (X.ravel() - 5) ** 2 + 10               # a real curved pattern
noise = np.random.normal(0, 8, size=X.shape[0])              # random noise
y = true_pattern + noise

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ----------------------------
# 2. Fit 3 models of increasing complexity
# ----------------------------
degrees = {"Underfit (degree 1)": 1, "Good Fit (degree 4)": 4, "Overfit (degree 15)": 15}
results = {}

for label, degree in degrees.items():
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_poly, y_train)

    train_pred = model.predict(X_train_poly)
    test_pred = model.predict(X_test_poly)

    train_error = mean_squared_error(y_train, train_pred)
    test_error = mean_squared_error(y_test, test_pred)

    results[label] = {
        "model": model,
        "poly": poly,
        "train_error": train_error,
        "test_error": test_error,
    }

    print(f"{label}:")
    print(f"  Training Error (MSE): {train_error:.2f}")
    print(f"  Test Error (MSE):     {test_error:.2f}")
    print(f"  Gap (test - train):   {test_error - train_error:.2f}\n")

# ----------------------------
# 3. Visualize all three fits side by side
# ----------------------------
X_smooth = np.linspace(0, 10, 300).reshape(-1, 1)

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

for ax, (label, r) in zip(axes, results.items()):
    X_smooth_poly = r["poly"].transform(X_smooth)
    y_smooth_pred = r["model"].predict(X_smooth_poly)

    ax.scatter(X_train, y_train, color="blue", label="Training data", alpha=0.6)
    ax.scatter(X_test, y_test, color="orange", label="Test data", alpha=0.6)
    ax.plot(X_smooth, y_smooth_pred, color="red", label="Model prediction")
    ax.set_title(f"{label}\nTrain MSE={r['train_error']:.1f}, Test MSE={r['test_error']:.1f}")
    ax.set_ylim(-10, 40)
    ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig("overfitting_underfitting_comparison.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved comparison chart.")