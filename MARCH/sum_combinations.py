#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:44:33 2024

@author: josephpongonthara
"""
def find_combinations_3(target, current_combination=[], start_digit=0):
    if target == 0 and len(current_combination) in (2,3):
        print(current_combination)
        return

    for digit in range(start_digit + 1, min(10, target + 1)):
        if target - digit >= 0:
            find_combinations_3(target - digit, current_combination + [digit], digit)

def find_combinations_4(target, current_combination=[], start_digit=1):
    if target == 0 and len(current_combination) == 4:
        print(current_combination)
        return

    for digit in range(start_digit, min(10, target + 1)):
        if target - digit >= 0:
            find_combinations_4(target - digit, current_combination + [digit], digit)

def generate_combinations():
    numbers_3_digit_sum = [7, 15, 18, 22]  # Pre-determined numbers for 3-digit sum
    print("Combinations for 3-digit sum:")
    for number in numbers_3_digit_sum:
        print(f"For number {number}:")
        find_combinations_3(number)
        print()  # Adding a newline for clarity
    
    numbers_4_digit_sum = [5, 9, 11, 12, 14, 19, 22, 31]  # Pre-determined numbers for 4-digit sum
    print("Combinations for 4-digit sum:")
    for number in numbers_4_digit_sum:
        print(f"For number {number}:")
        find_combinations_4(number)
        print()  # Adding a newline for clarity

# Example usage:
generate_combinations()
