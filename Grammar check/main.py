# importing regular expression
import re

# Function to extract words from a line using regular expression
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

# Initialize empty lists for the dictionary and 'Alice in Wonderland' words
dictionary_list = []
alice_list = []


# Open the dictionary file
for line in open("dictionary.txt"):
    # Open the dictionary file
    line = line.strip() 
    # Add the words from the line to the dictionary list
    dictionary_list += split_line(line) 

# Convert the list to a set to remove duplicates
dictionary_list = list(set(dictionary_list))

# Sort the list alphabetically
dictionary_list.sort()


""" ---------- Linear Search ---------- """

# Open the text file, AliceInWonderland200.txt
for i,line in enumerate(open("AliceInWonderland200.txt")):
    # Strip any leading/trailing whitespace from the line
    line = line.strip()
    # Split the line into a list of words
    words = split_line(line)
    # Iterate over each word in the line
    for word in words:
        # Check if the word is not in the dictionary list
        if word.upper() not in dictionary_list:
            # Print the line number and word not found in the dictionary
            print(f"Linear Search: Line {i+1}, Word: '{word}' not found in dictionary.")
            # Break out of the loop after the first non-dictionary word is found
            break


""" ---------- Binary Search ---------- """

# Open the text file, AliceInWonderland200.txt
for i,line in enumerate(open("AliceInWonderland200.txt")):
    # Split the line into a list of words
    words = split_line(line)
    # Iterate over each word in the line
    for word in words:
        # Initialize the first and last index of the dictionary list
        first = 0  
        last = len(dictionary_list)-1
        # Initialize a flag for whether the word is found
        found = False

        # Using Binary Search Algorithm to check if the word is in the dictionary list
        while first <= last and not found:
            # Calculate the midpoint of the dictionary list
            midpoint = (first + last)//2
            # Check if the word is at the midpoint of the dictionary list
            if dictionary_list[midpoint] == word.upper():
                found = True
            else:
                # Check if the word is before the midpoint
                if word.upper() < dictionary_list[midpoint]:
                    last = midpoint-1
                # Check if the word is after the midpoint
                else:
                    first = midpoint+1
        # Check if the word was not found in the dictionary list
        if not found:
            print(f"Binary Search: Line {i+1}, Word: '{word}' not found in dictionary.")


