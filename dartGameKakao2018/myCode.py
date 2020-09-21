import re


def solution(dartResult):
    answer = 0

    resultStr = dartResult

    score = re.findall("\d+", resultStr)
    squre = re.findall("\D", resultStr)
    scoreStr = re.findall("\D", resultStr)

    for i in range(0, 3):
        if '#' in squre:
            squre.remove('#')
        if '*' in squre:
            squre.remove('*')

    for i in range(0, 3):
        if squre[i] == 'S':
            score[i] = int(score[i])
        elif squre[i] == 'D':
            score[i] = int(score[i]) ** 2
        elif squre[i] == 'T':
            score[i] = int(score[i]) ** 3

    for n in range(2, -1, -1):
        if scoreStr[-1] == '#':
            score[n] *= -1
            scoreStr = scoreStr[:-2]
        elif scoreStr[-1] == '*':
            score[n] *= 2
            if n != 0:
                score[n - 1] *= 2
            scoreStr = scoreStr[:-2]
        else:
            scoreStr = scoreStr[:-1]
    answer = sum(score)

    return answer

