import numpy as np
def gradient_descent(x,y):
    n = len(x)
    lr = 0.001
    m = b = 0
    i = 1000
    for i in range(i):
        y_pred = m * x + b
        cost = (1/n)*sum([v**2 for v in (y-y_pred)])
        m_derivative = -(2/n)*sum(x*(y-y_pred))
        b_derivative = -(2/n)*sum(y-y_pred)
        m = m - m_derivative*lr
        b = b - b_derivative*lr
        print(f"Iteration : {i}, Cost : {cost}, m : {m}, b : {b}")

x = np.array([1,3,5,7,9])
y = np.array([2,4,6,8,10])
gradient_descent(x,y)
