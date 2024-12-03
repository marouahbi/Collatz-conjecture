import numpy as np
import matplotlib.pyplot as plt


def collatz_sequence(n):
    """Generate the Collatz sequence for a given starting number n."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return np.array(sequence), len(sequence)  # Return sequence and the number of steps


# Parameters
num_sequences = 20  # Number of sequences to generate
max_start = 100  # Maximum starting value for random numbers

# Generate random starting numbers
random_numbers = np.random.randint(1, max_start, size=num_sequences)

# Initialize plots
fig, axes = plt.subplots(3, 1, figsize=(12, 18))  # Three subplots: Original, Log-transformed, Detrended Log

for number in random_numbers:
    sequence, _ = collatz_sequence(number)
    steps = np.arange(len(sequence))

    # Plot the original sequence
    axes[0].plot(steps, sequence, label=f"Start: {number}", linestyle='-', marker='o', markersize=5)

    # Logarithmic transformation
    log_sequence = np.log(sequence)

    # Detrending the log-transformed data using numpy polyfit (linear regression)
    # Polyfit returns the coefficients of the fitted line: [slope, intercept]
    slope, intercept = np.polyfit(steps, log_sequence, 1)

    # Get the linear trend (fitted line)
    trend = slope * steps + intercept

    # Detrend the log-transformed sequence
    detrended_log_sequence = log_sequence - trend

    # Plot the original log-transformed sequence (without trend removal)
    axes[1].plot(steps, log_sequence, label=f"Start: {number}", linestyle='-', marker='o', markersize=5)

    # Plot the detrended log-transformed sequence
    axes[2].plot(steps, detrended_log_sequence, label=f"Start: {number}", linestyle='-', marker='o', markersize=5)

# Customize Original Sequence Plot
axes[0].set_title("Collatz Sequences (Original Values)")
axes[0].set_xlabel("Step")
axes[0].set_ylabel("Value")
axes[0].legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
axes[0].grid(True)

# Customize Logarithmic Transformation Plot (without trend removal)
axes[1].set_title("Collatz Sequences (Log-Transformed Values)")
axes[1].set_xlabel("Step")
axes[1].set_ylabel("Log(Value)")
axes[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
axes[1].grid(True)

# Customize Detrended Logarithmic Plot
axes[2].set_title("Detrended Collatz Sequences  (Log-Transformed Values)")
axes[2].set_xlabel("Step")
axes[2].set_ylabel("Detrended Log(Value)")
axes[2].legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
axes[2].grid(True)

# Adjust layout for clarity
plt.tight_layout()
plt.show()
