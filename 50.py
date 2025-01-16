scores = {'Hạnh': 85, 'Phúc': 75, 'Thanh': 85, 'Thản': 80}

scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
scores = dict(scores)
print(scores)