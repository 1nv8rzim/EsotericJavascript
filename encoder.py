_dict = {'0': '+[]',
         '1': '+!+[]'}

for i in range(2, 10):
    _dict[str(i)] = '[]+(' + '+'.join('!+[]' for _ in range(i)) + ')'


def die_already(char):
    return '([]+[])[' + javascriptify('constructor') + '][' + javascriptify('fromCharCode') + '](' + javascriptify(ord(char)) + ')'


def javascriptify(string):
    return '+'.join(_dict[char] for char in str(string))


# ![]+[] == false
_dict['f'] = '(![]+[])[' + _dict['0'] + ']'
_dict['a'] = '(![]+[])[' + _dict['1'] + ']'
_dict['l'] = '(![]+[])[' + _dict['2'] + ']'
_dict['s'] = '(![]+[])[' + _dict['3'] + ']'
_dict['e'] = '(![]+[])[' + _dict['4'] + ']'

# !![]+[] == true
_dict['t'] = '(!![]+[])[' + _dict['0'] + ']'
_dict['r'] = '(!![]+[])[' + _dict['1'] + ']'
_dict['u'] = '(!![]+[])[' + _dict['2'] + ']'

# {}+[] == [object Object]
_dict['o'] = '({}+[])[' + _dict['1'] + ']'
_dict['b'] = '({}+[])[' + _dict['2'] + ']'
_dict['j'] = '({}+[])[' + _dict['3'] + ']'
_dict['c'] = '({}+[])[' + _dict['5'] + ']'
_dict[' '] = '({}+[])[' + _dict['7'] + ']'

# +!![]/+[]+[] == Infinity
_dict['n'] = '(+!![]/+[]+[])[' + _dict['1'] + ']'
_dict['i'] = '(+!![]/+[]+[])[' + _dict['3'] + ']'
_dict['y'] = '(+!![]/+[]+[])[' + _dict['7'] + ']'

# ([]+[])[constructor] == function String() { [native code] }
_dict['S'] = '([]+([]+[])[' + javascriptify('constructor') + \
    '])[' + _dict['9'] + ']'
_dict['g'] = '([]+([]+[])[' + javascriptify('constructor') + \
    '])[' + javascriptify('14') + ']'

# (/-/)[constructor] == function RegExp() { [native code] }
_dict['p'] = '([]+(/-/)[' + javascriptify('constructor') + \
    '])[' + javascriptify('14') + ']'

# (13)[toString](14) == d
_dict['d'] = '(' + javascriptify('13') + ')[' + \
    javascriptify('toString') + '](' + javascriptify('14') + ')'

# (17)[toString](18) == h
_dict['h'] = '(' + javascriptify('17') + ')[' + \
    javascriptify('toString') + '](' + javascriptify('18') + ')'

# (22)[toString](23) == m
_dict['m'] = '(' + javascriptify('22') + ')[' + \
    javascriptify('toString') + '](' + javascriptify('23') + ')'

# []+[]["filter"]["constructor"] == function Function() { [native code] }
_dict['F'] = '([]+[][' + javascriptify('filter') + '][' + \
    javascriptify('constructor') + '])[' + _dict['9'] + ']'

# /\\\\/+[] == /\\/
_dict['\\'] = '(/\\\\/+[])[' + _dict['1'] + ']'

# ((()=>{})['constructor']('return escape')()('\\')) == %5C
_dict['C'] = '((()=>{})[' + javascriptify('constructor') + '](' + \
    javascriptify('return escape') + ')()(' + \
    _dict['\\'] + '))[' + _dict['2'] + ']'

print(javascriptify('C'))
