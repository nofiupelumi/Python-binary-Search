# Binary Search Algorithm in Python

A Python script implementing the binary search algorithm to find a target value in a sorted list.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Example](#example)
- [Function Details](#function-details)

## Description

This script demonstrates the binary search algorithm in Python. Binary search is an efficient algorithm for finding a target value within a sorted list. The script defines a `binary_search` function that performs this search operation.

## Usage

To use this script, ensure you have Python installed on your system. Copy the code from the script and run it using a Python interpreter.


## Example

The script includes an example usage of the binary_search function. It searches for a target value within a sample sorted list and prints whether the target was found and at which index.

## Function Details

binary_search(arr, target)
Perform binary search to find the target in the given sorted list.

## Parameters:

arr (list): The sorted list to search.
target: The value to find.

## Returns:

int: The index of the target if found, or -1 if not found.

```bash
python binary_search_example.py

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5

result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the list")

