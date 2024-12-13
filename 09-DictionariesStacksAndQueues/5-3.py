translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
word = input("Enter the word: ")

# Check if the word exists in the dictionary
if word in translations:
    print("Translation is:", translations[word])
else:
    print("No translation")