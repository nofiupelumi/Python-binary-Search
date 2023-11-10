# Linear search, also known as sequential search, is a simple algorithm for finding a target value within a list. 
# It sequentially checks each element of the list until a match is found or the entire list has been searched.
# Here's an explanation of the linear search algorithm in Python with two examples.

# Example 1: Basic Linear Search
def linear_search(arr, target):
    """
    Perform linear search to find the target in the given list.

    Parameters:
    - arr (list): The list to search.
    - target: The value to find.

    Returns:
    - int: The index of the target if found, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found at index i
    return -1  # Target not found in the list

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5

result = linear_search(my_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")  # Output: Target 5 found at index 4
else:
    print(f"Target {target_value} not found in the list")

# In this example, the linear_search function takes a list (arr) and a target value to search for. 
# It iterates through the list using a for loop and checks if each element is equal to the target value.
# If a match is found, it returns the index; otherwise, it returns -1.

# Example 2: Linear Search for Strings
def linear_search_string(lst, target):
    """
    Perform linear search to find the target string in the given list of strings.

    Parameters:
    - lst (list): The list of strings to search.
    - target (str): The string to find.

    Returns:
    - int: The index of the target string if found, or -1 if not found.
    """
    for i, value in enumerate(lst):
        if value == target:
            return i  # Target string found at index i
    return -1  # Target string not found in the list

# Example usage:
string_list = ["apple", "banana", "orange", "grape", "kiwi"]
target_string = "orange"

result_string = linear_search_string(string_list, target_string)

if result_string != -1:
    print(f"Target {target_string} found at index {result_string}")  # Output: Target orange found at index 2
else:
    print(f"Target {target_string} not found in the list")

# In this example, the linear_search_string function performs a linear search on a list of strings. It uses the enumerate function to loop over both the indices and values of the list, making it easy to find the index of the target string.

# These examples illustrate the basic concept of linear search and how it can be applied to different types of lists, including numeric and string lists. 
# Keep in mind that linear search is straightforward but may not be efficient for large datasets compared to more advanced search algorithms like binary search for sorted lists.