letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Tia").replace("<|Date|", "06 June 2005"))