def insert(L, x):
    """
    Inserts integer x into a sorted list L and returns a new sorted list.

    Parameters:
        L (list): Sorted list of integers.
        x (int): Integer to insert into the list.

    Returns:
        list: Sorted list with x inserted at the right place.
    """
    new_list = [int(num) for num in L]  # Convert string inputs to integers
    x = int(x)  # Convert x to integer
    index = 0

    # Find the correct position to insert x
    while index < len(new_list) and new_list[index] < x:
        index += 1

    # Insert x at the found position by shifting elements to the right
    new_list.append(None)  # Append None to increase the size of the list
    for i in range(len(new_list) - 1, index, -1):
        new_list[i] = new_list[i - 1]
    new_list[index] = x

    return new_list


# Example usage:
sorted_list = input("Enter a sorted list of integers separated by commas: ").split(',')
x = input("Enter an integer to insert: ")
new_sorted_list = insert(sorted_list, x)
print(new_sorted_list)
