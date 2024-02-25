import numpy as np
from scipy.linalg import solve

def solve_matrix_equations():
    """
    It's matrix time! Like a math magician, we're about to pull the solution out of our
    numerical hat using the power of scipy and numpy. Abracadabra, let the linear algebra begin!
    
    Returns:
        tuple: The grand reveal of the solutions to our matrix mysteries.
    """

    # Our first magical matrix, looking sharp and ready to solve.
    A1 = np.array([[3, 1, -1],
                   [1, 4, 1],
                   [2, 1, 2]])
    b1 = np.array([2, 12, 10])

    # And for our second trick, a slightly bigger matrix with more twists and turns.
    A2 = np.array([[1, -10, 2, 4],
                   [3, 1, 4, 12],
                   [9, 2, 3, 4],
                   [-1, 2, 7, 3]])
    b2 = np.array([2, 12, 21, 37])

    # Solving the matrix equations like a pro.
    solution1 = solve(A1, b1)
    solution2 = solve(A2, b2)

    return solution1, solution2

# Let's solve the matrix equations and print out the solutions all nice and tidy.
solution1, solution2 = solve_matrix_equations()

print("Matrix Equation Solutions")
print("--------------------------")
print("Solution for the first matrix equation:")
print(f"x1 ≈ {solution1[0]:.2f}, x2 ≈ {solution1[1]:.2f}, x3 ≈ {solution1[2]:.2f}")
print("\nSolution for the second matrix equation:")
print(f"x1 ≈ {solution2[0]:.2f}, x2 ≈ {solution2[1]:.2f}, x3 ≈ {solution2[2]:.2f}, x4 ≈ {solution2[3]:.2f}")
