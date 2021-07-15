def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b , m = step_gradient(b, m, np.array(points), learning_rate)
    return [b, m]