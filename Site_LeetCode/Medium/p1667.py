def closeStrings( word1, word2):
    lst_word1 = [0] * 26
    lst_word2 = [0] * 26

    if len(word1) != len(word2):
        return False
    else:
        # logic to explore and check the conditions
        for i in range(len(word1)):
            lst_word1[ord(word1[i]) - ord('a')] += 1
            lst_word2[ord(word2[i]) - ord('a')] += 1

    for i in range (len(lst_word1)):
        if bool(lst_word1[i]) != bool(lst_word2[i]):
            return False

    lst_word1.sort()
    lst_word2.sort()
    return lst_word1 == lst_word2


closeStrings("abc", "bca")