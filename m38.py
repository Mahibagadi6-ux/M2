# charater frequenccy in a string
def char_frequency(text):
    freq = {}
    for char in text.lower():

        freq[char] = freq.get(char,0)+1

    return freq
print(char_frequency("hello world"))
