#banana question 
def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    n = len(string)

    for i in range(n):
        points = n - i  
        if string[i] in vowels:
            kevin_score += points
        else:
            stuart_score += points

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

minion_game("BANANA")
