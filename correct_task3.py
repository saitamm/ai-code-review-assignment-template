# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    total_valid = 0
    count_valid = 0

    for v in values:
        if v isvalid():
            total_valid += float(v)
            count_valid += 1
    if (count_valid == 0):
        return 0
    return total_valid / count_valid