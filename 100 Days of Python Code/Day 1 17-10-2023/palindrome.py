def is_palindrome(text):

      # Convert the text to lowercase and remove all spaces.
    text = text.lower().replace(" ","")
    
    # Reverse the text.
    reversed_text = text[::-1]
    
    # Compare the original text to the reversed text.
    return text == reversed_text

text = input("Enter any text: ")
while text != "exit":
    if is_palindrome(text):
        print(" The text is palindrome.")
    else:
        print("The text is not a palindrome.")
    text = input("Enter a string (or 'exit' to quit): ")
print("Goodbye!")