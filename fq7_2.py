import re, string

'''
ENBF:
<expr>	->	 	<sub_expr> |
                '(' <expr> ')' |
               '.' <func_para>
<sub_expr>  ->	<var> <fac> |
                <num> 
<fac>	->	ε |		
            '.' <func_para>
<func_para>	->	<func_name> '(' <expr> ')'
<func_name>	->	"add" | "sub" | "multi" | "div" | "mod" | 
                "smaller_than" | "smaller_equal_than" | "larger_than" | "larger_equal_than" | 
                "bitwise_and" | "bitwise_or" | "xor" |
                "logical_and" | "logical_or" | 
                "negative" | "assign" |
                "increment" | "decrement"
<var> -> 'a' | 'b' | 'c' | 'd' | 'e'
<num> _> '0-9' <num>
'''
current_token = ''
current_token_type = ''
next_token = ''
next_token_type = ''
pos = 0


def lex(s):
    global next_token, next_token_type, pos, current_token_type, current_token_type
    current_token_type, current_token = next_token_type, next_token
    pos += len(next_token)
    result = re.match(r'[0-9][0-9]*', s[pos:])
    if result:
        # print(result)
        r = result.group(0)
        # print('\t\tnext token is <num>:\t' + r)
        next_token, next_token_type = r, 'num'
    else:
        result = re.match(r'add|sub|multi|div|mod|'
                          r'smaller_than|smaller_equal_than|larger_than|larger_equal_than|'
                          r'bitwise_and|bitwise_or|xor|'
                          r'logical_and|logical_or|'
                          r'negetive|assign|'
                          r'increment|decrement', s[pos:])
        if result:
            r = result.group(0)
            # print('\t\tnext token is <func_name>:\t' + r)
            next_token, next_token_type = r, 'func_name'
        else:
            result = re.match(r' |\.', s[pos:])
            if result:
                r = result.group(0)
                # print('\t\tnext token is <special_char>:\t' + r)
                next_token, next_token_type = r, 'special_char'
            else:
                result = re.match(r'\(|\)', s[pos:])
                if result:
                    r = result.group(0)
                    # print('\t\tnext token is <special_char>:\t' + r)
                    next_token, next_token_type = r, 'parenthesis'
                else:
                    result = re.match(r'a|b|c|d|e', s[pos:])
                    if result:
                        r = result.group(0)
                        # print('\t\tnext token is <var>:\t' + r)
                        next_token, next_token_type = r, 'var'
                    else:
                        print('error. syntax')
    print('\t\t\t\t\t\t\tcurrent token:\t' + current_token + '\t\t current pos: %d' % pos + '\t\tcurrent token type:' + current_token_type)
    # print('\t\t\t####next token:\t' + next_token + '\t\t\t next pos: %d' % pos + '\t\tnext token type:' + next_token_type)


def expr(s):
    global next_token, next_token_type, pos
    print("\tEnter big <expr>")
    lex(s)

    while pos< len(s):
        if next_token_type in ['var', 'num']:
            sub_expr(s)
        elif next_token == '(':
            expr(s)
            lex(s)
        elif next_token == ')':
            lex(s)
        elif next_token == '.':
            fac(s)
        else:
            print('syntax error... or EOF reached')
            pos +=1

    print("\tExit big <expr>")


def sub_expr(s):
    global next_token, next_token_type, pos
    print("\t\tEnter <sub_expr>")
    lex(s)
    if current_token_type == 'var':
        fac(s)
    else:
        lex(s)
    print("\t\tExit <sub_expr>")


def fac(s):
    global next_token, next_token_type, pos
    print("\t\t\tEnter <fac>")
    if next_token == '.':
        func(s)
    else:
        pass
    print("\t\t\tExit <fac>")


def func(s):
    global next_token, next_token_type, pos
    lex(s)
    lex(s)
    lex(s)
    print("\t\t\t\tEnter <func_para>")
    expr(s)
    print("\t\t\t\tExit <func_para>")


sample = '''(a.multi(b)).sub(1).add(c)
(a.multi((b.sub(1)))).div((c.mod(d)))
(a.sub(b)).div( c.bitwise_and( (d.multi(e)).div( a.sub(3) ) ) )
((a.add(b)).smaller_equal_than(c)).multi( d.larger_than( b.sub(e) ) )
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
    lex(line)
    print('\t\t\t\t\t\t\t pointer initialized; begin parsing\n\n')
    expr(line)

    line_n += 1