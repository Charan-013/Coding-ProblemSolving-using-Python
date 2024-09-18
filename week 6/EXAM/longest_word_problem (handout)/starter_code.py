def long_word_length(string1):
    big = ""
    for words in string1:
        length_str = len(big)
        if length_str < len(words):
            big = words
    return big


            
    

    return big

string1  = input().split()
print(long_word_length(string1))