def set_operations():
    # Create a set
    my_set = {1, 2, 3, 4, 5}

    # Add an element to the set
    my_set.add(6)

    # Remove an element from the set
    my_set.remove(4)

    # Discard an element from the set (doesn't raise an error if the element is not present)
    my_set.discard(2)

    # Union of sets
    another_set = {4, 5, 6}
    union_set = my_set.union(another_set)

    # Intersection of sets
    intersection_set = my_set.intersection(another_set)

    # Difference between sets
    difference_set = my_set.difference(another_set)

    # Check if a set is a subset of another set
    is_subset = my_set.issubset(another_set)

    print("Set:", my_set)
    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference:", difference_set)
    print("Is Subset:", is_subset)

# Run list operations
print("List Operations:")
list_operations()

# Run set operations
print("\nSet Operations:")
set_operations()
