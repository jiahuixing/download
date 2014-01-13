__author__ = 'tracy'

from commonLib import *

xxx = get_time(TIME_YMD)
yyy = get_time(TIME_HMS)

debug(xxx)
debug(yyy)

X1 = 'mione_plus_'
X2 = 'aries_'
X2_ALPHA = 'aries_alpha_'
X2A = 'taurus_'
X2A_ALPHA = 'taurus_alpha_'
X3_TD = 'pisces_'
X3_W = 'cancro_'
HM2_TD = 'wt93007_'
HM2_W = 'HM2013023_'
CHOOSE = [X1, X2, X2_ALPHA, X2A, X2A_ALPHA, X3_TD, X3_W, HM2_TD, HM2_W]

index = get_index(X1, CHOOSE)
print(index)

info = 'Pls choose the num to down the tar:\n'

info = get_info(info, CHOOSE)
print(info)