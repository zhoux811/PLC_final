import re, string

'''
                          r'add|sub|multi|div|mod|'
                          r'bitwise_and|bitwise_or|xor|'
                        
                          r'smaller_than|smaller_equal_than|larger_than|larger_equal_than|'
                          r'logical_and|logical_or|'
'''


def semantic_check(s):
    def check_assign_n(s):
        result = re.findall(r'assign\(', s)
        if len(result) > 1:
            print('\tmore than one assignment in the expression. illegal')
        else:
            print('\tless than one assignment in the expression. assignment check passed')

    def zero_devision(s):
        r = re.search(r'div\(', s)
        if r:
            # print(r.span(0)[1])
            start = ptr = r.span(0)[1]
            left_p, right_p = 1, 0
            # print(s[ptr:])
            while ptr <= len(s):
                if left_p != right_p:
                    if s[ptr] == ')':
                        right_p += 1
                    elif s[ptr] == '(':
                        left_p += 1
                    else:
                        pass
                    ptr += 1
                else:
                    # print('found ) at:' + str(ptr))
                    ptr += 1
            print('\t\"' + s[start:ptr - 1] + "\" MUST NOT equal to 0")
        else:
            print('\tno division in this expr. zero division check passed')

    def unary_inc_dec(s):
        r = re.search(r'increment\(', s)
        if r:
            start = r.span(0)[0]
            # print(s[start - 2:start])
            var = (s[start - 2:start])
            if re.match(r'[a-z]\.', var):
                print('\tthe first increment is on a variable. unary in/decrement check passed')
            else:
                print('\tthe first increment is not on a variable. unary in/decrement check failed')

    def boolean_value(s):
        r = re.findall(r'logical_and|logical_or', s)
        if r:
            starts = []
            for sub_r in r:
                start = end = re.search(sub_r, s).span(0)[1]
                if start not in starts:
                    starts.append(start)
                left_p, right_p = 1, 0
                while end < len(s):
                    if left_p != right_p:
                        if s[end] == ')':
                            right_p += 1
                        elif s[end] == '(':
                            left_p += 1
                        else:
                            pass
                        end += 1
                    else:
                        end += 1
                print('\t\"' + s[start:end - 1] + "\" result/value MUST be boolean value")

    def arith_value(s):
        r = re.findall(r'add|sub|multi|div|mod|'
                       r'bitwise_and|bitwise_or|xor|'
                       r'smaller_than|smaller_equal_than|larger_than|larger_equal_than', s)
        if r:
            starts = []
            for sub_r in r:
                start = end = re.search(sub_r, s).span(0)[1]
                if start not in starts:
                    starts.append(start)
                left_p, right_p = 1, 0
                while end < len(s):
                    if left_p != right_p:
                        if s[end] == ')':
                            right_p += 1
                        elif s[end] == '(':
                            left_p += 1
                        else:
                            pass
                        end += 1
                    else:
                        end += 1
                print('\t\"' + s[start:end - 1] + "\" result/value MUST be NON boolean value")

    check_assign_n(s)
    zero_devision(s)
    unary_inc_dec(s)
    boolean_value(s)
    arith_value(s)


sample = '''(a.multi(b)).sub(1).add(c)
(a.multi((b.sub(1)))).div((c.mod(d)))
(a.sub(b)).div( c.bitwise_and( (d.multi(e)).div( a.sub(3) ) ) )
((a.add(b)).smaller_equal_than(c)).multi( d.larger_than( b.sub(e) ) )
((a.add(b)).larger_than(c)).multi( d.larger_than( b.sub(e) ) )
((a.negative(1)).logical_or(c)).assign( d.logical_and(e) )
((a.larger_than(b)).xor(c)).logical_or( (d.smaller_equal_than(17)) )
(a.add((b))).negative(1)
(a.add((b.multi(c)))).add(d)
e.assign((a.increment(1)).increment(1) )'''

line_n = 1
for line in sample.split(sep='\n'):
    current_token = current_token_type = next_token = next_token_type = ''
    pos = 0

    print('\n\n\nline_n: ' + str(line_n) + ' : ' + line)
    semantic_check(line)

    line_n += 1
