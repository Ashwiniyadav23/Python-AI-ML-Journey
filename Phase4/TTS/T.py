# 1. The Train/Test Split — the basic version


from sklearn.model_selection import train_test_split

# X = features (inputs), y = labels (correct answers)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(len(X_train))   # 80% of the data
print(len(X_test))    # 20% of the data