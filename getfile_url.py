# -*- coding: utf-8 -*-

import os
import sys
import time
import hashlib


RomNames = ['M1/M1S-开发版','M1/M1S-开发版',
            'M2/M2S-开发版','M2/M2S-开发版',
            'X3-TD-开发版','X3-TD-开发版',
            'X3-WCDMA-开发版','X3-WCDMA-开发版',
            'M2/M2S-台湾版','M2/M2S-台湾版',
            'M2/M2S-香港版','M2/M2S-香港版',
            'M2/M2S-体验版','M2/M2S-体验版',
            'M2A-WCDMA-开发版','M2A-WCDMA-开发版',
            'M2A-WCDMA-体验版','M2A-WCDMA-体验版',
            'M2A-TD-开发版','M2A-TD-开发版',
            'H2-TD-不稳定版','H2-TD-不稳定版',
            'H2-WCDMA-不稳定版','H2-WCDMA-不稳定版',
            'X3-TD-原生版','X3-TD-原生版',
            'M2/M2S-原生版','M2/M2S-原生版',
            'X3-WCDMA-原生版','X3-WCDMA-原生版',]
str_Marks = ['_Mioneplus_','mione_plus_',
             '_MI2_','aries_images_',
             '_MI3_','pisces_',
             '_MI3W_','cancro_',
             '_MI2TW_','aries_tw_',
             '_MI2HK_','aries_hk_',
             '_MI2Alpha_','aries_alpha_',
             '_MI2A_','taurus_images',
             '_MI2AAlpha_','taurus_alpha_images',
             '_MI2ATD_','taurus_td_images',
             '_HM2_','wt93007_',
             '_HM2W_','HM2013023_',
             '_NativeMI3_','pisces_',
             '_NativeMI2_','aries_images_',
             '_NativeMI3W_','cancro_',]

def walk_dir(dir,topdown=True):

    info = {}
    miui = 'miui_'
    z_type = 'zip'
    image = '_images_'
    t_type = 'tar'
    for root, dirs, files in os.walk(dir, topdown):
        for file_name in files:
            tmp = []
            print os.path.abspath(file_name)
            if miui in file_name and z_type in file_name:
                c_name = getRomCName(file_name)
                size = os.path.getsize(os.path.join(root,file_name))/1024/1024
                size = str(size) + 'M'
                md5 = GetFileMd5(os.path.join(root,file_name))
                tmp.append(size)
                tmp.append(md5)
                tmp.append(file_name)
                if c_name not in info.keys():
                    info[c_name] = []
                    info[c_name].append(tmp)
                else:
                    info[c_name].append(tmp)
            elif image in file_name and t_type in file_name:
                c_name = getRomCName(file_name)
                size = os.path.getsize(os.path.join(root,file_name))/1024/1024
                size = str(size) + 'M'
                md5 = GetFileMd5(os.path.join(root,file_name))
                tmp.append(size)
                tmp.append(md5)
                tmp.append(file_name)
                if c_name not in info.keys():
                    info[c_name] = []
                    info[c_name].append(tmp)
                else:
                    info[c_name].append(tmp)
        #print(info)
    return info

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    my_hash = hashlib.md5()
    f = file(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        my_hash.update(b)
    f.close()
    return my_hash.hexdigest().lower()

def getRomCName(name):
    rom_c_name = ''
    roms_length = len(RomNames)
    for i in xrange(roms_length):
        mark = str_Marks[i]
        if mark in name:
            rom_c_name = RomNames[i]
            break
    return rom_c_name

class Generate:

    mFolder = ''

    def __init__(self):
        self.getFolder()

    def getFolder(self):
        block = '.'
        argv_len = len(sys.argv)
        if argv_len >= 2:
            mFolder = sys.argv[1]
        else:
            year,mon,day= time.strftime('%Y'),time.strftime('%m'),time.strftime('%d')
            year = year[-1]
            mon = str(int(mon))
            day = str(int(day))
            mFolder = year + block + mon + block + day
        self.mFolder = mFolder

    def gDownloadUrl(self):

        mFolder = self.mFolder
        info = walk_dir(mFolder)
        version = sys.argv[2]
        body = ''
        head = '【升级提醒】\n—————————————————————————————————————————————————— \n\n'
        end = ' '
        url_head = 'http://ota.n.miui.com/ota/'+version+'/'
        for key in info.keys():
            if key != '':
                #print('key:%s'%key)
                length = len(info[key])
                #print('length:%s'%length)
                c_name = key
                body += "%s %s\n" % (c_name, version)
                for i in xrange(length):
                    #print('i:%d'%i)
                    tmp = info[key][i]
                    size = tmp[0]
                    md5 = tmp[1]
                    name = tmp[2]
                    if 'tar' in name:
                        rom_type = 'Fastboot线刷包 '
                    else:
                        rom_type = '系统升级卡刷包 '
                    body = '%s%s%s MD5: %s\n%s%s \n\n' % (body, rom_type ,size, md5, url_head, name)
                body += '—————————————————————————————————————————————————— \n\n'
        url =  head + body + end
        return url

if __name__ == '__main__':
    generate = Generate()
    url = generate.gDownloadUrl()
    print url
