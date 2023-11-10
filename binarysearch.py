# Binary search is an efficient algorithm for finding a target value within a sorted list.
#  The basic idea is to repeatedly divide the search range in half until the target is found or the search range is empty.
#  Here's an explanation of the binary search algorithm in Python with two examples.

# Example 1: Basic Binary Search
def binary_search(arr, target):
    """
    Perform binary search to find the target in the given sorted list.

    Parameters:
    - arr (list): The sorted list to search.
    - target: The value to find.

    Returns:
    - int: The index of the target if found, or -1 if not found.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Adjust the search range to the right half
        else:
            high = mid - 1  # Adjust the search range to the left half

    return -1  # Target not found in the list

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5

result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")  # Output: Target 5 found at index 4
else:
    print(f"Target {target_value} not found in the list")



# In this example, the binary_search function takes a sorted list (arr) and a target value to search for. 
# It initializes two pointers, low and high, representing the current search range.
# The function then iteratively calculates the middle index (mid) of the current range and compares the value at that index with the target. Depending on the comparison, it adjusts the search range accordingly until the target is found or the range is empty.

# Example 2: Binary Search for Strings
def binary_search_string(lst, target):
    """
    Perform binary search to find the target string in the given sorted list of strings.

    Parameters:
    - lst (list): The sorted list of strings to search.
    - target (str): The string to find.

    Returns:
    - int: The index of the target string if found, or -1 if not found.
    """
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if lst[mid] == target:
            return mid  # Target string found at index mid
        elif lst[mid] < target:
            low = mid + 1  # Adjust the search range to the right half
        else:
            high = mid - 1  # Adjust the search range to the left half

    return -1  # Target string not found in the list

# Example usage:
string_list = ["apple", "banana", "grape", "kiwi", "orange"]
target_string = "kiwi"

result_string = binary_search_string(string_list, target_string)

if result_string != -1:
    print(f"Target {target_string} found at index {result_string}")  # Output: Target kiwi found at index 3
else:
    print(f"Target {target_string} not found in the list")


# In this example, the binary_search_string function performs a binary search on a sorted list of strings. 
# It uses the same binary search algorithm but adapted for string comparison.

# These examples illustrate how binary search is effective for finding elements in sorted lists, and it is particularly efficient for large datasets compared to linear search.