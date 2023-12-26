# Grammar check
This is a simple yet effective grammar checker tool written in Python. 
It uses a binary search algorithm to quickly identify spelling and grammatical errors in a given paragraph, using a simple dictionary.

# Spell Checker Using Linear and Binary Search

This script performs spell-checking on a given text file (`AliceInWonderland200.txt`) using both linear and binary search algorithms. It compares each word in the text file against a dictionary file (`dictionary.txt`) to identify words not present in the dictionary.

## Features

- **Linear Search**: Checks each word against the dictionary using a straightforward linear search approach.
- **Binary Search**: Implements a more efficient binary search to find words in the dictionary.
- **Regular Expressions**: Utilizes Python's `re` module to extract words from lines accurately.

## Files

- `main.py`: The main Python script that you run to perform spell checking.
- `dictionary.txt`: A text file that contains a list of correct words, used as the reference dictionary.
- `AliceInWonderland200.txt`: An example text file containing the content to spell check.

## Usage

1. Ensure you have Python installed on your system.
2. Place `main.py`, `dictionary.txt`, and your text file in the same directory.
3. Run the script using Python:

   ```bash
   python main.py

