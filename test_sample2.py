def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def test_bad_answer():
    temp = 1
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    temp -= temp
    temp += temp
    assert inc(3) != 5