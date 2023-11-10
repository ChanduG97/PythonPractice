def list_operations():
    # Create a list
    my_list = [1, 2, 3, 4, 5]

    # Append an element
    my_list.append(6)

    # Insert an element at a specific index
    my_list.insert(2, 10)

    # Remove an element
    my_list.remove(4)

    # Pop an element at a specific index
    popped_element = my_list.pop(1)

    # Extend the list with another list
    another_list = [7, 8, 9]
    my_list.extend(another_list)

    # Find the index of an element
    index_of_element = my_list.index(5)

    # Count occurrences of an element
    count_of_element = my_list.count(3)

    # Sort the list
    my_list.sort()

    # Reverse the list
    my_list.reverse()

    print("List:", my_list)
    print("Popped Element:", popped_element)
    print("Index of 5:", index_of_element)
    print("Count of 3:", count_of_element)

