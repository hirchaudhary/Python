def find_character():
    word_list = ['hello','world','my','name','is','Anna']
    char = 'o'
    new_word_list = []
    for i in range(0,len(word_list)):
        for j in range(0, len(word_list[i])):
            if word_list[i].find(char) == j:
                new_word_list.append(word_list[i])
    print new_word_list

find_character()