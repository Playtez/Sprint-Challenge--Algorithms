'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    result = word.find('th')
    if result == -1:
        return 0
    word = word[result + 2:]

    return count_th(word) + 1
    # TBC
