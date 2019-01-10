'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
'''


def reverse_words(text):
    
    words = text.split(' ')
    
    new_sentence = []
    
    for w in words:
  
        # string to list i.e. array
        new_word = list(w)

        # get number of letters in word
        word_length = len(w)

        # initial positions
        start = 0
        end = word_length - 1

        while start < end:

            new_word[start], new_word[end] = new_word[end], new_word[start]
            start += 1
            end -= 1
            
        # return "".join(new_word)
        new_sentence.append("".join(new_word))
    
    return " ".join(new_sentence)
