def count_words_occurrences(sentence : str):
    list_of_words = sentence.split(" ")
    unique_Words = set(list_of_words)
    word_count = {}
    for word in unique_Words:
        word_count[word] = list_of_words.count(word)
    return word_count
    
