#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n <= len(str):
        a = str[n]
        str = str.replace(a, "")
        return str
    else:
        return str
