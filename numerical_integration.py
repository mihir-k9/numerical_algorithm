import numpy as np
import math
import matplotlib.pyplot as plt


def integral(v): return math.sin(v) ** 2


def numerical_integration(answer, start, end, increment):
    """
    A method to calculate the error between analytical value of an integral and numerical value using
    3 integration formulae: Rectangular, Trapezoidal and Simpson's Rule.

    The for loop uses the function integral() to compute values.

    :parameter:
    answer: float
        The actual value of the integral
    start: float
        Lower bound of the integral
    end: float
        Upper bound of the integral
    increment: float
        Step size for increasing the x value

    :return:
    Plot on log-log scale which shows the error as a function of step size.
    """

    # Empty lists to store residue
    error_rect = []
    error_trap = []
    error_simpson = []

    # Loop to cycle through the 4 delta x values
    for t in increment:
        a = np.arange(start, end, t)

        # Rectangular rule formula
        function1 = integral
        sum_rectangle = t * sum(function1(k) for k in a[0:-2])
        error_rect.append(abs(sum_rectangle - answer))

        # Trapezoid Rule formula
        sum_trapezoid = 0.5 * t * (function1(a[0]) + 2 * sum(function1(m) for m in a[1:-2]) + function1(a[-1]))
        error_trap.append(abs(sum_trapezoid - answer))

        # Simpson's Rule formula
        sum_simpson = t / 3 * (function1(a[0]) + function1(a[-1]) + 4 * sum(
            function1(a[2 * m]) for m in range(int((len(a) - 1) / 2))) + 2 * sum(
            function1(a[2 * p + 1]) for p in range(int((len(a) - 3) / 2))))
        error_simpson.append(abs(sum_simpson - answer))

    # Plot commands
    plt.loglog(x_coordinates, error_rect, '-r', linewidth=0.7, marker='.', markersize=8, label='Rectangular Rule')
    plt.loglog(x_coordinates, error_trap, '-g', linewidth=0.7, marker='|', markersize=9, label='Trapezoidal Rule')
    plt.loglog(x_coordinates, error_simpson, '-b', linewidth=0.7, marker='s', markersize=6, label='Simpson\'s Rule')
    plt.xlabel('$\pi / \delta x$')
    plt.ylabel('Residual')
    plt.title('Numerical Integration')
    plt.legend(loc=1)
    plt.show()


# Example implementation
true_value = math.pi / 4
delta_x = [math.pi / 10, math.pi / 20, math.pi / 40, math.pi / 80]
x_coordinates = [10, 20, 40, 80]
numerical_integration(true_value, 0, math.pi/2, delta_x)
