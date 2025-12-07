#if you turn everything into lower case it will be easy to count and combie
def calculate_love_score(name1, name2):
    score1 = 0
    score2 = 0
    word1 = "TRUE".lower()
    word2 = "LOVE".lower()
    combined_name = name1 + name2
    for letter in word1:
        score1 += combined_name.count(letter)
    for letter in word2:
        score2 += combined_name.count(letter)
    score = str(score1)+str(score2)
    print(score)

calculate_love_score(name1="Roshini Dogiparthi".lower(), name2="Sravani Allavarapu".lower())