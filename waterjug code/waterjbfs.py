import math
from collections import deque

''' Input capacities and initial/final states for jugs'''
a = int(input("Enter Jug A Capacity: "))
b = int(input("Enter Jug B Capacity: "))
ai = int(input("Initially Water in Jug A: "))
bi = int(input("Initially Water in Jug B: "))
af = int(input("Final State of Jug A: "))
bf = int(input("Final State of Jug B: "))

# Check for negative values and whether initial state is equal to final state
if a <= 0 or b <= 0:
    print("Jug capacities must be positive.")
    exit(1)
if ai < 0 or bi < 0 or af < 0 or bf < 0:
    print("Negative values are not allowed.")
    exit(1)
if ai==af and bi==bf:
    print(f"initial state is already the final state: juga{ai} and jugb={bi}")
    exit()
# Define the water jug solver function using BFS
def bfs_wjug(a, b, ai, bi, af, bf):
    visited = set()
    queue = deque([(ai, bi, [])])  # (Jug A state, Jug B state, List of operations)

    while queue:
        curr_ai, curr_bi, operations = queue.popleft()

        if (curr_ai, curr_bi) in visited:
            continue
        visited.add((curr_ai, curr_bi))

        # Check if the final state is reached
        if curr_ai == af and curr_bi == bf:
            for i, op in enumerate(operations):
                print(f"Step {i + 1}: {op}")
            print(f"Final State Reached: Jug A = {curr_ai}, Jug B = {curr_bi}")
            return

        # List of possible operations
        possible_operations = [
            (a, curr_bi, "Fill Jug A"),  # Fill Jug A
            (curr_ai, b, "Fill Jug B"),  # Fill Jug B
            (0, curr_bi, "Empty Jug A"),  # Empty Jug A
            (curr_ai, 0, "Empty Jug B"),  # Empty Jug B
            (curr_ai - min(curr_ai, b - curr_bi), curr_bi + min(curr_ai, b - curr_bi), "Pour from A to B"),  # Pour A to B
            (curr_ai + min(curr_bi, a - curr_ai), curr_bi - min(curr_bi, a - curr_ai), "Pour from B to A"),  # Pour B to A
        ]

        # Add each possible operation to the queue
        for next_ai, next_bi, op in possible_operations:
            if (next_ai, next_bi) not in visited:
                queue.append((next_ai, next_bi, operations + [op]))

    print("No solution found.")
    return

# Check if the final state can be achievable using GCD
gcd = math.gcd(a, b)

if (af <= a and bf <= b) and (af % gcd == bf % gcd == 0):
    bfs_wjug(a, b, ai, bi, af, bf)
else:
    print("The final state is not achievable with the given capacities.")
    exit()
