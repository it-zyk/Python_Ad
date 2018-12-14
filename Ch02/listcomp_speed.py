import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))


clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')



# 1、timeit(stmt=‘pass’, setup=‘pass’, timer=, number=1000000)
# 返回：
#
# 返回执行stmt这段代码number遍所用的时间，单位为秒，float型
#
# 参数：
#
# stmt：要执行的那段代码
#
# setup：执行代码的准备工作，不计入时间，一般是import之类的
#
# timer：这个在win32下是time.clock()，linux下是time.time()，默认的，不用管
#
# number：要执行stmt多少遍
