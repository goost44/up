# 1
"""
def task1():
    def count_ways(start, end, must_contain):
        max_val = max(end, must_contain) + 1
        ways = [0] * (max_val + 1)
        ways[start] = 1

        for x in range(start, must_contain + 1):
            if ways[x] > 0:
                if x + 1 <= must_contain:
                    ways[x + 1] += ways[x]
                if x + 2 <= must_contain:
                    ways[x + 2] += ways[x]
                if x * 2 <= must_contain:
                    ways[x * 2] += ways[x]

        ways2 = [0] * (max_val + 1)
        ways2[must_contain] = ways[must_contain]

        for x in range(must_contain, end + 1):
            if ways2[x] > 0:
                if x + 1 <= end:
                    ways2[x + 1] += ways2[x]
                if x + 2 <= end:
                    ways2[x + 2] += ways2[x]
                if x * 2 <= end:
                    ways2[x * 2] += ways2[x]

        return ways2[end]

    return count_ways(3, 12, 10)
print(task1())
"""
# 2
"""
def task2():
    def count_ways_no_26(start, end, forbidden):
        max_val = end + 1
        ways = [0] * (max_val + 1)
        ways[start] = 1

        for x in range(start, end + 1):
            if x == forbidden:
                continue
            if ways[x] > 0:
                if x + 1 <= end and x + 1 != forbidden:
                    ways[x + 1] += ways[x]
                next_val = 2 * x + 1
                if next_val <= end and next_val != forbidden:
                    ways[next_val] += ways[x]

        return ways[end]

    return count_ways_no_26(1, 27, 26)
print(task2())
"""
# 3
"""
def task3():
    def count_ways_with_and_without(start, end, must_contain, forbidden):
        max_val = max(end, must_contain) + 1
        ways_to_must = [0] * (max_val + 1)
        ways_to_must[start] = 1

        for x in range(start, must_contain + 1):
            if x == forbidden:
                continue
            if ways_to_must[x] > 0:
                if x + 1 <= must_contain and x + 1 != forbidden:
                    ways_to_must[x + 1] += ways_to_must[x]
                if x + 2 <= must_contain and x + 2 != forbidden:
                    ways_to_must[x + 2] += ways_to_must[x]

        ways_from_must = [0] * (max_val + 1)
        ways_from_must[must_contain] = ways_to_must[must_contain]

        for x in range(must_contain, end + 1):
            if x == forbidden:
                continue
            if ways_from_must[x] > 0:
                if x + 1 <= end and x + 1 != forbidden:
                    ways_from_must[x + 1] += ways_from_must[x]
                if x + 2 <= end and x + 2 != forbidden:
                    ways_from_must[x + 2] += ways_from_must[x]

        return ways_from_must[end]

    return count_ways_with_and_without(2, 18, 9, 14)
print(task3())
"""
