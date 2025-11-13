#!/usr/bin/env python3

def return_evens(num_list): # Returns a list of even numbers from the input list
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    return [s + '!' for s in sentence_list] # Appends an exclamation mark to each string in the input list