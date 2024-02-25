import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def func1(x):
    """
    Like a smooth dance step, this function takes `x` and gracefully subtracts
    three times the cosine of `x`. Watch it glide across your graph.
    
    Args:
        x (float): The dance floor where `x` struts its stuff.
        
    Returns:
        float: The dance move at point `x`.
    """
    return x - 3 * np.cos(x)

def func2(x):
    """
    This one's a bit of a show-off, taking the cosine of `x` times two and 
    pumping it up to the power of three. It's x-cubed in a cos(2x) party hat!
    
    Args:
        x (float): The math party where `x` is the life of the equation.
        
    Returns:
        float: The party trick at point `x`.
    """
    return np.cos(2 * x) * x**3

def find_roots():
    """
    Here's where we play hide and seek with the roots. We'll ask fsolve to 
    sneak up on them starting from x=1.0, 'cause why not? Let's see where they're hiding.
    
    Returns:
        tuple: The hiding spots of our elusive roots.
    """
    root1 = fsolve(func1, 1.0)  # Starting the search at x = 1.0.
    root2 = fsolve(func2, 1.0)  # Ditto for this one.
    return root1, root2

def plot_functions():
    """
    Grab your virtual paint and canvas! This function draws our mathematical 
    masterpieces on a plot. We've got colors, lines, and even a legend.
    """
    x_vals = np.linspace(-10, 10, 400)  # Our canvas is from -10 to 10.
    y_vals_func1 = func1(x_vals)  # Plotting points for function 1.
    y_vals_func2 = func2(x_vals)  # And for function 2.

    plt.plot(x_vals, y_vals_func1, label='x - 3cos(x)')
    plt.plot(x_vals, y_vals_func2, label='cos(2x)x^3')
    plt.axhline(0, color='grey', lw=0.5)  # Drawing the x-axis.
    plt.legend()  # Because every artist signs their work.
    plt.grid(True)  # It's the graph paper background for our masterpiece.
    plt.show()  # Show it off to the world!

def find_intersections():
    """
    It's not just about the journey, but also where paths cross. This function 
    is on a mission to find where our two functions bump into each other and say 'Hi!'
    
    Returns:
        list: The meet-cute spots of our functions.
    """
    def intersection(x):
        # The difference between func1 and func2 - where the plot thickens!
        return func1(x) - func2(x)

    guesses = np.linspace(-10, 10, 200)  # Casting a wide net for our guesses.
    intersections = []  # Preparing the guest list for the intersection party.

    for guess in guesses:
        # Each guess is a potential party spot.
        intersection_point = fsolve(intersection, guess)
        # We only want unique spots, no party crashers.
        if not any(np.isclose(intersection_point, p) for p in intersections):
            intersections.append(intersection_point[0])

    # No duplicates allowed, this is an exclusive event!
    intersections = np.unique(np.round(intersections, 5))
    return intersections

# Time for the main event! Let's run our functions and see what happens.
root1, root2 = find_roots()
plot_functions()
intersection_points = find_intersections()

# Drumroll for the final reveal...
print("Roots and Intersection Points Analysis")
print("---------------------------------------")
print(f"Root of the function x - 3cos(x): x ≈ {root1[0]:.5f}")
print(f"Root of the function cos(2x)x^3: x ≈ {root2[0]:.5f}")
print("\nThe functions intersect at the following points (approximations):")
for idx, point in enumerate(intersection_points, start=1):
    print(f"  Intersection {idx}: x ≈ {point:.5f}")

