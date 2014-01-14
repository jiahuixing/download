__author__ = 'tracy'

from commonLib import *
from Info import *

xxx = get_time(TIME_YMD)
yyy = get_time(TIME_HMS)

debug(xxx)
debug(yyy)

index = get_index(X1, CHOOSE)
print(index)

info = 'Pls choose the num to down the tar:\n'

info = get_info(info, CHOOSE)
print(info)

file_name = raw_input().strip('\r').strip('\n')

print(file_name)