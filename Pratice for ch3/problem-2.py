# a program to fill in a letter template given below with name and date

letter = '''Dear <|NAME|>,
    You are selected!
    Date: <|DATE|>'''

print(letter.replace("<|NAME|>" , "aviral").replace("<|DATE|>" , "01/07/2026")) 