import time


def solution(table, languages, preference):
    answer = ''
    maxscore = 0

    for i in table:
        tmpscore = 0
        techstacks = i.split()
        for score, tech in enumerate(techstacks[1:],0):
            if tech in languages:
                tmpscore += preference[languages.index(tech)]*(5-score)

        if tmpscore > maxscore:
            maxscore = tmpscore
            answer = techstacks[0]
        elif tmpscore == maxscore and answer != '':
            if answer > techstacks[0]: answer = techstacks[0]

    return answer


if __name__ == "__main__":
    start = time.time()
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
             "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
             "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["PYTHON", "C++", "SQL"]
    preference = [7, 5, 5]
    print(solution(table, languages, preference))
    print(time.time() - start)

    start = time.time()
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
             "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
             "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["JAVA", "JAVASCRIPT"]
    preference = [7, 5]
    print(solution(table, languages, preference))
    print(time.time() - start)
