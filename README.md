# BonusProjNgram

This project demonstrates the use of n-grams and hash maps for text analysis using sample data from Google Books.
[Google Books Ngram Datasets](http://storage.googleapis.com/books/ngrams/books/datasetsv3.html)

## Project Files
- **BonusProjNgram.py**: Main script for processing n-grams and demonstrating hash map usage.
- **hashMapADT.py**: Custom hash map abstract data type implementation.
- **googlebooks_200k_sample.txt**: Sample text files containing n-gram data from Google Books (reduced to 200k from original .gz file)

## What the Program Does
The main script (`BonusProjNgram.py`) reads n-gram data from the provided sample file, processes the data using a custom hash map with open addressing and linear probing, and performs various analyses such as frequency counting and searching for specific n-grams. The project demonstrates efficient data storage and retrieval using hash maps.

## How to Run the Program
1. **Requirements**: Ensure you have Python 3.x installed on your system. Packages needed to install: regex (re), sympy, time.
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
- You can modify the sample text files or add your own n-gram data for further experimentation.
## Example Usage: 
==============================================
   Google Ngram Smart-Fix & Autocomplete
==============================================
Type a word to search, ':metrics' for stats, or 'exit' to quit.

> arrive   
✅ Found: 'arrive'
   Match Count: 42
   Volume Count: 42
   Lookup Time: 0.0410 ms

> applause
✅ Found: 'applause'
   Match Count: 854
   Volume Count: 649
   Lookup Time: 0.0433 ms

> applau
❌ 'applau' not found in dataset.
   Searching for suggestions...
   Did you mean:
     1. applause (freq: 854)

> :metrics

--- Hash Table Performance Metrics ---
Table Size (m):           6029
Elements Stored (n):      3155
Load Factor (α):          0.52
Avg Probes per Insert:    3.25
Avg Probes per Search:    2.25
--------------------------------------
## Author
- Taner Bulbul
