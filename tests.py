def run_unit_test(expected, actual):
    PASS = '💚'
    FAIL = '❌'
    print(PASS if actual == expected else '❌')

def run_star_test(expected, actual):
    PASS = '⭐️'
    FAIL = '❌'
    print(PASS if actual == expected else '❌')