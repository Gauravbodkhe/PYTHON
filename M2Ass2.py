def backward_difference(data):
    y_values = [point[1] for point in data]
    print("y:", y_values)

    n = len(y_values)
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            y_values[j] = y_values[j] - y_values[j-1]
        print(f"Δ^{i} y:", y_values[i:])

data = [(1, 11), (2, 13), (3, 18), (4, 20)]
backward_difference(data)
