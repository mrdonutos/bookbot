#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 10:01:17 2025

@author: jakub
"""
def sort_on(items):
    return items["num"]

def count_words(book_text):
    return len(book_text.split())

def count_chars(book_text):
    book_text = book_text.lower()
    char_list = {}
    for char in book_text:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list

def sort_dictionary(counted_dictionary):
    dict_list = [] 
    for key,value in counted_dictionary.items():
        if key.isalpha():    
            dict_entry = {"char" : key, "num" : value}
            dict_list.append(dict_entry)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list