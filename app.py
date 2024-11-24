def add_three_copies(lst, data):
    lst.append(data)  # Add the data to the list
    lst.append(data)  # Add another copy of the data
    lst.append(data)  # Add a third copy of the data

def main():
    # Create an empty list
    my_list = []
    
    # Ask the user for some data
    user_input = input("Enter a message to copy: ")
    
    # Show the list before adding copies
    print("List before:", my_list)
    
    # Call the function to add three copies of the input to the list
    add_three_copies(my_list, user_input)
    
    # Show the list after adding the copies
    print("List after:", my_list)

if __name__ == "__main__":
    main()
