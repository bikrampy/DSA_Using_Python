test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
tests = [test, {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
}, {
             'input': {
                 'cards': [4, 2, 1, -1],
                 'query': 4
             },
             'output': 0
         }, {
             'input': {
                 'cards': [3, -1, -9, -127],
                 'query': -127
             },
             'output': 3
         }, {
             'input': {
                 'cards': [6],
                 'query': 6
             },
             'output': 0
         }, {
             'input': {
                 'cards': [9, 7, 5, 2, -9],
                 'query': 4
             },
             'output': -1
         }, {
             'input': {
                 'cards': [],
                 'query': 7
             },
             'output': -1
         }, {
             'input': {
                 'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                 'query': 3
             },
             'output': 7
         }, {
             'input': {
                 'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                 'query': 6
             },
             'output': 2
         }]


# print(tests)


def locate_cards(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if cards[mid] == query:
            return mid
        elif cards[mid] > query:
            lo = mid + 1
        elif cards[mid] < query:
            hi = mid - 1
    return -1


for i in range(0, len(tests)):
    print(locate_cards(**tests[i]["input"]) == tests[i]["output"])
