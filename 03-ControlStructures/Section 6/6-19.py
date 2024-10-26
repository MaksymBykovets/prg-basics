##
# Program that prints a survey consisting of three questions.
##

quest1 = input("SURVEY Are you interested in computer science? (y/n): ")
quest2 = input("Do you like playing computer games? (y/n): ")
quest3 = input("Do you have an Instagram account? (y/n): ")

# Results

print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if quest1 == "y" else 'No'}")
print(f"Playing computer games: {'Yes' if quest2 == "y" else 'No'}")
print(f"Has an Instagram account: {'Yes' if quest3 == "y" else 'No'}")