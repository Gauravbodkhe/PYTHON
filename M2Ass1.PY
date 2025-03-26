def forward_difference(data):
    y_values = [point[1] for point in data]
    print("y:", y_values)

    n = len(y_values)
    for i in range(1, n):
        for j in range(n - i):
            y_values[j] = y_values[j + 1] - y_values[j]
        print(f"Δ^{i} y:", y_values[:n-i])

data = [(0, 10), (1, 12), (2, 15), (3, 16)]
forward_difference(data)
