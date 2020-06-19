# Problem:
# Given two strings, a and b, return the result of putting them together in the
# order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
# Exercise:
# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'


def make_abba(a, b):
    return str(a+b+b+a)
