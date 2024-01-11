first_input = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
second_input = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

lst_words = []

for i in range(len(first_input)):
    if first_input[i] == "addWord":
        lst_words.append(second_input[i][0])
        