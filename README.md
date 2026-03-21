# BonusProjNgram

This project demonstrates the use of n-grams and hash maps for text analysis using sample data from Google Books.
[Google Books Ngram Datasets](http://storage.googleapis.com/books/ngrams/books/datasetsv3.html)

## Project Files
- **BonusProjNgram.py**: Main script for processing n-grams and demonstrating hash map usage.
- **hashMapADT.py**: Custom hash map abstract data type implementation.
- **googlebooks_200k_sample.txt**: Sample text files containing n-gram data from Google Books (reduced too 200k from original .gz file)

## What the Program Does
The main script (`BonusProjNgram.py`) reads n-gram data from the provided sample file, processes the data using a custom hash map with open addressing and linear probing, and performs various analyses such as frequency counting and searching for specific n-grams. The project demonstrates efficient data storage and retrieval using hash maps.

## How to Run the Program
1. **Requirements**: Ensure you have Python 3.x installed on your system. No external packages are required.
2. **Prepare the Data**: Make sure the sample text files are in the same directory as the Python scripts.
3. **Run the Main Script**:
   - Open a terminal or command prompt.
   - Navigate to the project directory:
     ```
     cd path/to/your/project/directory
     ```
   - Run the main script:
     ```
     python BonusProjNgram.py
     ```

## Notes
- The program is self-contained and does not require any third-party libraries.
- You can modify the sample text files or add your own n-gram data for further experimentation.

## Author
- Taner Bulbul
