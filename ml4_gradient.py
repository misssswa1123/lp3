# Function: y = (x + 3)^2
# Derivative: dy/dx = 2 * (x + 3)

x = 2                      # starting point
learning_rate = 0.1        # step size
tolerance = 0.000001       # stop when the step becomes this small
max_iterations = 1000      # safety limit

for i in range(1, max_iterations + 1):
    y = (x + 3) ** 2
    print("Iteration", i, ": x =", round(x, 4), ", y =", round(y, 4))

    slope = 2 * (x + 3)                    # gradient at x
    new_x = x - learning_rate * slope      # update rule

    if abs(new_x - x) < tolerance:         # converged, so stop
        break
    x = new_x

print("\nLocal minima at x =", round(x, 4))
print("Minimum value of y =", round((x + 3) ** 2, 4))