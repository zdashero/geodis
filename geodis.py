import random
import math


def expectedrolls(probability):
    # Calculates the expected number of rolls needed to get a success based on the given probability
    # This uses the geometric distribution, where the expected value for the number of trials to the first success is 1/p
    return 1 / probability

def rollsim(probability, simulations=100000):
    # Simulates a series of rolls to calculate the average number of rolls needed for a success
    # The geometric distribution models the number of trials until the first success. Each roll is an independent Bernoulli trial.
    results = []
    for _ in range(simulations):
        rolls = 0
        while True:
            rolls += 1
            if random.random() < probability:  # Checks if the roll is successful based on the probability
                results.append(rolls)
                break
    avgrolls = sum(results) / len(results)  # Calculates the average number of rolls
    return avgrolls, results


def sprob(probability, rolls):
    # Calculates the probability of at least one success after a given number of rolls
    # This is derived from the complement rule: P(at least one success) = 1 - P(no successes)
    return 1 - (1 - probability) ** rolls

def getinfprecision(probability):
    # Determines the number of rolls needed to achieve a 100% success probability
    # Theoretically, the geometric distribution allows for infinite trials, but we stop when the success probability rounds to 1.0
    rolls = 1
    while sprob(probability, rolls) < 1.0:
        rolls += 1
    return rolls


chance_percentage = float(input("Enter the chance of the roll as a percentage (e.g., 0.06): "))
probability = chance_percentage / 100  # Converts percentage input to a probability value

expected_rolls = expectedrolls(probability)
print(f"\nExpected number of rolls to get the rarest item: {expected_rolls:.2f}")


simulations = 100000
avgrolls, _ = rollsim(probability, simulations)
print(f"Average rolls from simulation ({simulations} runs): {avgrolls:.2f}")


rolltarget = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]  # Chosen to provide a range of milestones for calculating probabilities
for rolls in rolltarget:
    sprobout = sprob(probability, rolls) * 100  # Converts probability to percentage for display
    print(f"Probability of success after {rolls} rolls: {sprobout:.2f}%")

infprec = getinfprecision(probability)
print(f"\nNumber of rolls needed for a 100% guarantee: {infprec}")