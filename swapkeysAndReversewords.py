def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    swap = sentence.swapcase()
    words = swap.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence
        


sentence = input()
print (reverse_words_order_and_swap_cases(sentence))
