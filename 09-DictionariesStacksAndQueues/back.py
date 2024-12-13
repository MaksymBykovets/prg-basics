import stack

# some previously visited websites
stack.push('instagram.com')
stack.push('uek.krakow.pl')
stack.push('microsoft.com')

while True:
    website = input('Enter website name (0 for back): ')

    if website == '0':
        # Go back to the previous website
        if stack.is_empty():
            print("\nNo more websites in history to go back to.")
            continue
        else:
            stack.pop()
            if stack.is_empty():
                print("\nNo more websites in history. Open a new website.")
                continue
            else:
                website = stack.peek()
    else:
        # Add the new website to the stack
        stack.push(website)

    # Print the name of the website you are currently viewing
    print('\nYou are currently viewing:', stack.peek())
    print()