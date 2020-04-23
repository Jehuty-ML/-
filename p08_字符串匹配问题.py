
def match(s,p):
    if len(p) == 0:
        return len(s) == 0

    first = p[0]
    if first == '?':
        return len(s) > 0 and match(s[1:], p[1:])  #没有len(s) > 0的话，空字符串会报错
    if first == '*':
        return match(s, p[1:]) or len(s) > 0 and match(s[1:], p)
    else:
        return len(s) > 0 and first == s[0] and match(s[1:], p[1:])

def _test_match(s, p, result):
    print('%s, %s, %s, %s' % (s, p, result, match(s,p)))


if __name__ == '__main__':
    _test_match('ababaab', 'a*b', True)
    _test_match('ababaab', '*abab*', True)
    _test_match('ababaab', 'a*a?b', True)

    _test_match('ababaab', 'a*bb', False)
    _test_match('ababaab', 'aabab*', False)
    _test_match('ababaab', 'a*ab?', False)