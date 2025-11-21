#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 10:55:20 2025

@author: jakub
"""
from stats import count_words
from stats import count_chars
from stats import sort_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
   
def main():
    if(len(sys.argv) == 1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    num_words = count_words(book)
    counted_dict = count_chars(book)
    sorted_dict = sort_dictionary(counted_dict)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for key in sorted_dict:
        print(f"{key["char"]}: {key["num"]}")
    print("============= END ===============")
main()