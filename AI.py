# Reading inputs
x = list(map(int, input().strip().split()))  # Read all x values
y = list(map(int, input().strip().split()))  # Read all y values

# Ensure lengths of x and y match
if len(x) != len(y):
    raise ValueError("The lengths of x and y must be the same.")

# Step 1: Calculate means
mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

# Step 2: Calculate standard deviations
std_x = (sum((xi - mean_x) ** 2 for xi in x) / len(x)) ** 0.5
std_y = (sum((yi - mean_y) ** 2 for yi in y) / len(y)) ** 0.5

# Step 3: Calculate correlation coefficient
numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
denominator = (sum((xi - mean_x) ** 2 for xi in x) * sum((yi - mean_y) ** 2 for yi in y)) ** 0.5
r = numerator / denominator

# Step 4: Calculate slope (b) and intercept (a)
b = r * (std_y / std_x)
a = mean_y - b * mean_x

# Step 5: Predict y for x = 80
x_predict = 80
y_predict = a + b * x_predict

# Output the result rounded to 3 decimal places
print(round(y_predict, 3))
