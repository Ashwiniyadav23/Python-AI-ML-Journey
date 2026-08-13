# 1. The Train/Test Split — the basic version


from sklearn.model_selection import train_test_split

# X = features (inputs), y = labels (correct answers)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(len(X_train))   # 80% of the data
print(len(X_test))    # 20% of the data



# 2. Why add a THIRD split — the Validation Set?



from sklearn.model_selection import train_test_split

X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

print(len(X_train))  # ~60%
print(len(X_val))    # ~20%
print(len(X_test))   # ~20%


# 3. Cross-Validation — a smarter way to use limited data


from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=5)   # cv=5 means 5-fold cross-validation

print(scores)          # 5 individual scores, one per fold
print(scores.mean())   # the average — a much more reliable performance estimate