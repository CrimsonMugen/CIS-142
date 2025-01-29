##
# @author Johnathan Florio
# lab 1.2 - A simple input hello translator for lab purposes

# Dictionary for mapping languages to responses
languages = {
    "japanese": "English to Japansese\n=============================\nGood Afternoon     Konichiwa",
    "german": "English to German\n==============================\nGood Afternoon      Guten Tag",
    "french": "English to French\n===================\nHello    Bonjour",
}
'''"options: Japanese, German, French
alternative to elif statement'''

# translator

while True:
    translate = input("Please enter the language you would like to translate to, or type options for the full list: ").strip().lower() 
    # VERY IMPORTANT strip and lower help format input never forget to use these

    if translate in languages:
        print(languages[translate])
        break
    # break ends if loop
    elif translate == "options":
        print("All supported languages:", ','.join(languages.keys()))
        # VERY IMPORTANT using ',' corrects the formating of the values for the dictionary
    else:
        print("Please select a language from the list or type options for a list of all languages.")