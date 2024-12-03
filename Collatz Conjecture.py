import numpy as np
import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return np.array(sequence)


num_sequences = 20
max_start = 100


random_numbers = np.random.randint(1, max_start, size=num_sequences)


plt.figure(figsize=(12, 8))
for number in random_numbers:
    sequence = collatz_sequence(number)
    steps = np.arange(len(sequence))
    plt.plot(steps, sequence, label=f"Start: {number}")

plt.title("Collatz Sequences")
plt.xlabel("Step")
plt.ylabel("Value")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')  # Place legend outside the plot
plt.grid(True)
plt.tight_layout()
plt.show()
    