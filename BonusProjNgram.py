#  Taner Bulbul
#  MSML 606 - Data Structures and Algorithms
#  Bonus Project: N-gram Analysis with Hash Tables
#  CLI aplication for the N-gram analysis
#  external source policy included before each problem as comments


import re
import time
import hashMapADT as hm  # My own hashmap ADT with linear probing

# external‑source policy:
# Used my own code and logic to build the hashmap class
# This is the hash table code mostly from HW3 with some changes
# Used Github CoPilot to help with python syntax

# external‑source policy:
# Used my code and logic for reading the file and cleaning the
# Ngram entries and counting match and vlume frequencies. 
# Used Copilot for some parts of this application
# code for CLI such as emojis and formatting is from Copilot suggestions
    
# Convert to lowercase and strip special characters
def clean_Ngrams(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def get_metrics(hashmap):
    load_factor = hashmap.n / hashmap.size_m
    avg_insert_probes = hashmap.total_insert_probes / hashmap.n if hashmap.n > 0 else 0
    avg_search_probes = hashmap.total_search_probes / hashmap.search_count if hashmap.search_count > 0 else 0
    
    print("\n--- Hash Table Performance Metrics ---")
    print(f"Table Size (m):           {hashmap.size_m}")
    print(f"Elements Stored (n):      {hashmap.n}")
    print(f"Load Factor (α):          {load_factor:.2f}")
    print(f"Avg Probes per Insert:    {avg_insert_probes:.2f}")
    print(f"Avg Probes per Search:    {avg_search_probes:.2f}")
    print("--------------------------------------\n")



def start_cli(hashmap):
    print("==============================================")
    print("   Google Ngram Smart-Fix & Autocomplete")
    print("==============================================")
    print("Type a word to search, ':metrics' for stats, or 'exit' to quit.")

    while True:
        user_input = input("\n> ").lower().strip()

        if user_input == 'exit':
            print("Goodbye!")
            break

        if user_input == ':metrics':
            get_metrics(hashmap)
            continue

        # 1. Start Timing for Lookup
        start_time = time.perf_counter()
        
        # 2. Perform Hash Table Search
        result = hashmap.search(user_input)
        
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time) * 1000

        if result:
            print(f"✅ Found: '{user_input}'")
            print(f"   Match Count: {result['match_count']:,}")
            print(f"   Volume Count: {result['volume_count']:,}")
            print(f"   Lookup Time: {elapsed_ms:.4f} ms")
        else:
            print(f"❌ '{user_input}' not found in dataset.")
            print(f"   Searching for suggestions...")
            
            # 3. Suggestion Logic (Linear Scan of the table for partial matches)
            # For a project of this size, a quick scan of the internal table is fine.
            suggestions = []
            for entry in hashmap.table:
                if entry and entry[0] is not hashmap._TOMBSTONE:
                    word = entry[0]
                    # Check if user input is a prefix or close match
                    if word.startswith(user_input):
                        suggestions.append((word, entry[1]['match_count']))
            
            # Sort suggestions by frequency (the 'match_count')
            suggestions.sort(key=lambda x: x[1], reverse=True)
            
            if suggestions:
                print("   Did you mean:")
                for i, (word, freq) in enumerate(suggestions[:3], 1):
                    print(f"     {i}. {word} (freq: {freq:,})")
            else:
                print("   No suggestions found starting with those letters.")
                
                
if __name__ == "__main__":
    hashmap = hm.HashMap(size=3011)
    # Dictionary to store total match_count and volume_count for each word
    word_stats = {}

    with open("googlebooks_200k_sample.txt", "r", encoding="utf-8") as f:
        # Limit processing to the first 500 lines
        for i, line in enumerate(f):
           # if i >= 500:
            #    break
            parts = line.strip().split('\t')
            if len(parts) == 4:
                word_raw, year, match_count, volume_count = parts
                # Remove part after '_' in the first word
                word_cleaned = clean_Ngrams(word_raw.split('_')[0])
                if word_cleaned:
                    match_count = int(match_count)
                    volume_count = int(volume_count)
                    if word_cleaned in word_stats:
                        word_stats[word_cleaned]["match_count"] += match_count
                        word_stats[word_cleaned]["volume_count"] += volume_count
                    else:
                        word_stats[word_cleaned] = {"match_count": match_count, "volume_count": volume_count}

    # Insert each word and its total match_count and volume_count into the hash table
    for word, stats in word_stats.items():
        if stats["volume_count"] > 5:  # Only include words with significant volume
            hashmap.insert(word, stats)
"""       
    for entry in hashmap.table:
        if entry is not None and entry[0] is not hashmap._TOMBSTONE:
            print(entry[0], entry[1]["match_count"])

for entry in hashmap.table:
    if entry and entry[0] is not hashmap._TOMBSTONE:
        key = entry[0]
        # Reset probe count if needed
        probes_before = hashmap.total_search_probes
        hashmap.search(key)
        probes_used = hashmap.total_search_probes - probes_before
        if probes_used > 1:
            print(f"Word '{key}' required {probes_used} probes to find.")
# Example of launching the CLI
start_cli(hashmap)
"""