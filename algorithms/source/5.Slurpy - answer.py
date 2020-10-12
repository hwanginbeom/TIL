"""
정규표현식으로 예외 처리를 한다.
"""

import regex as re

re_slump = re.compile('^([DE]F+G*)+G$')
re_slimp = re.compile('AH|A([DE]F+G*)+GC|AB(?R)C')
# ? R 이 재귀다.
#기존에 있던 import re 는 기본 정규 표현식이다.


def slurpys(in_str):
    res = False
    mat = re.match(re_slimp, in_str)
    #매칭하고 매칭한 데이터가 있으면 구현 한다.
    if mat:
        mat_size = len(mat.group())
        sub_str = in_str[mat_size:]
        if re.fullmatch(re_slump, sub_str):
            res = True
    return res

# ex
print(slurpys('ADFGCDFFFFFG'))
