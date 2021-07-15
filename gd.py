import numpy as np

def compute_error_for_linie_given_points(b,w,points):
    totalError = 0
    for i in range(0,len(points)):
        x = points[i,0]
        y = points[i,1]
        totalError += (y - (w*x+b))**2
    return totalError / float(len(points))

def step_gradient(b_current, w_current, points, laerningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        b_gradient += -(2/N) * (y - (w_current*x + b_current))
        w_gradient += -(2/N) * x * (y - (w_current*x + b_current))
    new_b = b_current - (laerningRate * b_gradient)
    new_w = w_current - (laerningRate * w_gradient)
    return [new_b,new_w]
