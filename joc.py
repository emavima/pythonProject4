s = "Hello, World"

def vowel_counter(s):

    vowels = 'aeiou'

    count = {vowel: 0 for vowel in vowels}

    for char in s.lower():
        if char in vowels:
            count[char] += 1

    total = sum(count.values())

    return total


print(vowel_counter(s))