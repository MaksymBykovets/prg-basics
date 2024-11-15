def func(text) : 
    separated_text = ""
    for char in text : 
        separated_text += str(char) + "-"
    separated_text = separated_text[:-1]
    return separated_text

print(func("Univesity"))