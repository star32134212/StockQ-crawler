#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:36:29 2019

@author: owlting
"""

import pandas as pd
import numpy as np
import csv

month = ['01','02','03','04','05','06','07','08','09','10','11','12']
#month = ['01','02','03','04','05','06','07','08','09','10','11','12']
month_2016 = [0,31,29,31,30,31,30,31,31,30,31,30,31]
month_2017 = [0,31,28,31,30,31,30,31,31,30,31,30,31]

"""
2016
"""
mon = 1
stock = {}
stock_2016=np.zeros((13,13))
rank_2016=[]
for m in month:
    for d in range(1,month_2016[mon]+1):
        try:
            url = 'http://www.stockq.org/stock/history/2016/'+m+'/2016'+m+str(d).zfill(2)+'_tc.php?fbclid=IwAR2pCUddGdaFPdZ_JD5R7pMD27eajxWoHX3akDS094SvXmwmjLMfwpaH2qw'
            table=pd.read_html(url)
            print('2016'+m+str(d).zfill(2))
            nzdstr=table[6][3][2] #紐西蘭 0
            nzdflt=float(nzdstr[:-1])
            audstr=table[6][3][3] #澳洲 1
            audflt=float(audstr[:-1])
            jpnstr=table[6][3][4] #日本 2
            jpnflt=float(jpnstr[:-1])
            cnhstr=table[6][3][11] #上海 3
            cnhflt=float(cnhstr[:-1])
            hkdstr=table[6][3][20] #香港 4
            hkdflt=float(hkdstr[:-1])
            sgdstr=table[6][3][25] #新加坡 5
            sgdflt=float(sgdstr[:-1])
            rubstr=table[7][3][2] #俄羅斯 6
            rubflt=float(rubstr[:-1])
            gbpstr=table[7][3][3] #英國 7
            gbpflt=float(gbpstr[:-1])
            trystr=table[7][3][6] #土耳其 8
            tryflt=float(trystr[:-1])
            plnstr=table[7][3][10] #波蘭 9
            plnflt=float(plnstr[:-1])
            nokstr=table[7][3][14] #挪威 10
            nokflt=float(nokstr[:-1])
            chfstr=table[7][3][22] #瑞士 11
            chfflt=float(chfstr[:-1])
            cadstr=table[8][3][21] #加拿大 12
            cadflt=float(cadstr[:-1])
            stock = {'0':nzdflt,'1':audflt,'2':jpnflt,'3':cnhflt,'4':hkdflt,'5':sgdflt,'6':rubflt,'7':gbpflt,'8':tryflt,'9':plnflt,'10':nokflt,'11':chfflt,'12':cadflt}
            rank=sorted(stock.items(),key=lambda item:item[1])
            for i in range(13):
                stock_2016[int(rank[i][0])][12-i]=1
            rank_2016.append(stock_2016)
        except:
            continue
    mon=mon+1

"""
2017
"""
mon = 1
stock = {}
stock_2017=np.zeros((13,13))
rank_2017=[]
for m in month:
    for d in range(1,month_2017[mon]+1):
        try:
            url = 'http://www.stockq.org/stock/history/2017/'+m+'/2017'+m+str(d).zfill(2)+'_tc.php?fbclid=IwAR2pCUddGdaFPdZ_JD5R7pMD27eajxWoHX3akDS094SvXmwmjLMfwpaH2qw'
            table=pd.read_html(url)
            print('2017'+m+str(d).zfill(2))
            nzdstr=table[6][3][2] #紐西蘭 0
            nzdflt=float(nzdstr[:-1])
            audstr=table[6][3][3] #澳洲 1
            audflt=float(audstr[:-1])
            jpnstr=table[6][3][4] #日本 2
            jpnflt=float(jpnstr[:-1])
            cnhstr=table[6][3][11] #上海 3
            cnhflt=float(cnhstr[:-1])
            hkdstr=table[6][3][20] #香港 4
            hkdflt=float(hkdstr[:-1])
            sgdstr=table[6][3][25] #新加坡 5
            sgdflt=float(sgdstr[:-1])
            rubstr=table[7][3][2] #俄羅斯 6
            rubflt=float(rubstr[:-1])
            gbpstr=table[7][3][3] #英國 7
            gbpflt=float(gbpstr[:-1])
            trystr=table[7][3][6] #土耳其 8
            tryflt=float(trystr[:-1])
            plnstr=table[7][3][10] #波蘭 9
            plnflt=float(plnstr[:-1])
            nokstr=table[7][3][14] #挪威 10
            nokflt=float(nokstr[:-1])
            chfstr=table[7][3][22] #瑞士 11
            chfflt=float(chfstr[:-1])
            cadstr=table[8][3][21] #加拿大 12
            cadflt=float(cadstr[:-1])
            stock = {'0':nzdflt,'1':audflt,'2':jpnflt,'3':cnhflt,'4':hkdflt,'5':sgdflt,'6':rubflt,'7':gbpflt,'8':tryflt,'9':plnflt,'10':nokflt,'11':chfflt,'12':cadflt}
            rank=sorted(stock.items(),key=lambda item:item[1])
            for i in range(13):
                stock_2017[int(rank[i][0])][12-i]=1
            rank_2017.append(stock_2017)
        except:
            continue
    mon=mon+1
    
np.save('rank_2016',rank_2016)
np.save('rank_2017',rank_2017)

