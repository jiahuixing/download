__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

TYPE_INT = 'int'
TYPE_STR = 'str'

TIME_HMS = 'hms'
TIME_YMD = 'ymd'


#参数
TIMEOUT = 5
MAIN_PAGE = 'http://ota.n.miui.com/ota/'
CHOOSE_T_SYS = 'sys.argv'
CHOOSE_T_IN = 'input'

#shell 命令
DOWNLOAD_COMMAND = 'wget '
FLASH_SCRIPT = './flash.sh '

#机型信息
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

MIDDLE = 'images_'


#re匹配
IMAGES_SUF = r'_4.[0-9]{1}_[a-zA-Z0-9]{10}.tar'