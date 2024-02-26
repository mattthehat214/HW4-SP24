# Import the necessary libraries - numpy for number crunching and matplotlib for plotting beauty.
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Matthew's section
# First up, our protagonists - the mean (mu) and standard deviation (sigma) of our normal distributions.
mu_1, sigma_1 = 0, 1  # For the standard normal distribution (a perfect bell, so to speak).
mu_2, sigma_2 = 175, 3  # For the not-so-standard one (more like a bell with a higher pitch).

# Now, let's set the stage with a range of x values - our potential outcomes.
x_1 = np.linspace(mu_1 - 4*sigma_1, mu_1 + 4*sigma_1, 1000)  # A nice symmetrical range for the standard normal.
x_2 = np.linspace(mu_2 - 4*sigma_2, mu_2 + 4*sigma_2, 1000)  # And one for our high-pitched friend.

# Cue the PDFs - the heart of our plot, showing how likely each outcome is.
pdf_1 = stats.norm.pdf(x_1, mu_1, sigma_1)
pdf_2 = stats.norm.pdf(x_2, mu_2, sigma_2)

# The CDFs are the sidekicks, telling us the running total probability up to each point.
cdf_1 = stats.norm.cdf(x_1, mu_1, sigma_1)
cdf_2 = stats.norm.cdf(x_2, mu_2, sigma_2)

#Jose's section with Matthew comments
# Now for the critical moment - calculating the probabilities for our specific conditions.
prob_1 = stats.norm.cdf(1, mu_1, sigma_1)  # The chance of being less than 1 in our standard tale.
prob_2 = 1 - stats.norm.cdf(mu_2 + 2*sigma_2, mu_2, sigma_2)  # The chance of exceeding μ + 2σ in our unique story.

#Matthew's functions
# Let's get visual - first, the standard normal distribution.
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(x_1, pdf_1, 'b-', lw=2, label=f'N({mu_1},{sigma_1}^2)')
plt.fill_between(x_1, pdf_1, where=(x_1 < 1), color='grey', alpha=0.5)  # A grey area of uncertainty.
plt.title(f'P(x < 1 | N(0,1)): {prob_1:.2f}')  # The probability, in big bold letters.
plt.legend()  # And don't forget the legend, our guide through this tale.

# Following with the CDF - a rising action to our plot climax.
plt.subplot(2, 1, 2)
plt.plot(x_1, cdf_1, 'b-', lw=2, label='CDF')
plt.scatter(1, prob_1, color='red')  # A red spot marks the spot of interest.
plt.title(f'CDF for N(0,1) at x=1: {prob_1:.2f}')  # And another bold statement of our calculated probability.
plt.legend()

plt.tight_layout()  # Give the plot some breathing room.
plt.show()  # the show begins!

# Now, the second act - the non-standard normal distribution.
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(x_2, pdf_2, 'b-', lw=2, label=f'N({mu_2},{sigma_2}^2)')
plt.fill_between(x_2, pdf_2, where=(x_2 > mu_2 + 2*sigma_2), color='grey', alpha=0.5)  # The uncertainty grows.
plt.title(f'P(x > μ + 2σ | N(175, 3)): {prob_2:.2f}')  # Spell out the probability for all to see.
plt.legend()

# The CDF once more, building up to the final reveal.
plt.subplot(2, 1, 2)
plt.plot(x_2, cdf_2, 'b-', lw=2, label='CDF')
plt.scatter(mu_2 + 2*sigma_2, 1-prob_2, color='red')  # The red dot of destiny.
plt.title(f'CDF for N(175,3) at x=μ+2σ: {1-prob_2:.2f}')  # Our probability, standing proud.
plt.legend()

plt.tight_layout()  # Neaten things up.
plt.show()  # And that's the end of our visual story. Take a bow, plots!
