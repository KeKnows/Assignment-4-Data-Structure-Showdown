# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 3. Remove Duplicates (Keep Order)
# Return the values in the order they first appeared, without duplicates.
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"] 

def remove_duplicates_keep_order(items):
    set1 = set()
    result = []
    for item in items:
        if item not in set1:
            set1.add(item)
            result.append(item)
    return result

print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))

"""
Reflection:

For this timed challenge, I chose to solve the problem using a combination of a set for tracking duplicates and a list for preserving order. The key requirement was to remove duplicates while keeping the order of the first occurrences intact. A set provides fast lookups, so I could quickly check if an item had already appeared, while the list maintained the correct sequence. This hybrid structure struck a good balance between efficiency and simplicity.

The 30-minute time limit shaped my decision by pushing me toward a straightforward, well-practiced pattern rather than experimenting with more complex or optimized alternatives. I didn’t want to risk overcomplicating the logic or debugging an unfamiliar approach under time pressure. Using a set-and-list pattern is something I knew would work reliably and would be easy to write in just a few lines of code.

One trade-off I made was choosing simplicity over potential optimization. While my solution works efficiently for most cases, there are alternative approaches that might perform slightly better for extremely large inputs, such as using dict.fromkeys() in Python 3.7+ (which preserves insertion order). However, under the time constraint, I prioritized clarity and correctness over micro-optimizations. The main compromise was avoiding experimentation and sticking with a tried-and-true approach to ensure I finished within the allotted time.
"""
