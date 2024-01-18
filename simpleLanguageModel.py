import random
#building word dictionaries
#getting word frequencies 
#generating sentences


def getPairFrequencies(my_string):
    # iterate through each word in the string to create dictionary with key as word and value as frequency
    my_dict={}
    list_of_words = my_string.split() 
    count = len(list_of_words) - 1
    for word in range(len(list_of_words) - 1):
        pair = (list_of_words[word], list_of_words[word+1])
        if pair not in my_dict:
            my_dict[pair] = 1.0 /count
        else:
            my_dict[pair]+=1.0 /count 

    return my_dict


def generateSentence(word_freq_dict):
    vocabulary_list = list(word_freq_dict.keys())
    vocabulary_weights = list(word_freq_dict.values())
    random_string = []
    #choose first random word depending on the weights
    random_string.append(random.choices(vocabulary_list, weights=vocabulary_weights, k=1)[0][0])
    #generate sentence in a loop until it runs into a period
    while True:
        currPair = random_string[-1]
        #find all pairs that start with the last word
        currVocab = [pair for pair in vocabulary_list if pair[0] == currPair]

        if currVocab:
            currVocabWeights = [vocabulary_weights[vocabulary_list.index(pair)] for pair in currVocab]
            nextRandom = random.choices(currVocab, weights=currVocabWeights, k=1)[0][1]
            random_string.append(nextRandom)
            
            if nextRandom == '.':
                break
        #if no pairs start with the last word, stop generating
        else:
            break
    return ' '.join(random_string)





