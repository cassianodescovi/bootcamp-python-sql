# Calculate Average of Values in a List
from typing import List


def calculate_average (values: List[float]) -> float:
    if len(values) == 0:
        return 0.0
    result = sum(values) / len(values)
    return result

if __name__ == "__main__":
    examples = [
        [10, 20, 30, 40, 50],
        [5.5, 6.5, 7.5],
        [],
        [-10, 0, 10, 20]
    ]

for example in examples:
    print (f"the average of {example}: {calculate_average(example)}")