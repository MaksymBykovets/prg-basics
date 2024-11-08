text = input("Enter text : ")

def func(sentence) : 
    new_text = sentence.replace(" ", "")
    return new_text

print(func(text))