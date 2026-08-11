
# 1. Supervised Learning — "learning with an answer key"


X = [[3, 1500], [4, 2200], [2, 900]]   # inputs (features)
y = [295000, 420000, 185000]            # correct answers (labels)

new_house = [[3, 1600]]
predicted_price = model.predict(new_house)   # e.g. 305000





# 2. Unsupervised Learning — "finding patterns with no answer key"



X = [[500, 2], [520, 3], [50, 10], [45, 12], [3000, 1]]

clusters = model.fit_predict(X)
print(clusters)   # e.g. [0, 0, 1, 1, 2]  → 3 discovered groups