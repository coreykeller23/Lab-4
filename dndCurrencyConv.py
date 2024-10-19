"""
Author:Corey Keller
File Name:dndCurrencyConv.py
Version:1.0
Creation:2.17.24
Purpose:Create currency conversion functions to use in Lab 4
"""

#functions created for conversion from gold to other currency types
def goldTogold(g):
    gold=g/1
    return gold
def goldToSilver(g):
    silver=g*10
    return silver
def goldToPlat(g):
    plat=g/10
    return float(plat)
def goldToCopper(g):
    copper=g*100
    return copper
def goldToElect(g):
    electrum=g*2
    return electrum

#functions created to turn other coin types into gold
def platTogold(p):
    goldP=p*10
    return float(goldP)
def silverTogold(s):
    goldS=s/10
    return float(goldS)
def electTogold(e):
    goldE=e/2
    return float(goldE)
def copperTogold(c):
    goldC=c/100
    return float(goldC)

#function for combining currencies into one currency
def allGold(g,s,p,e,c):
    total=g+s+p+e+c
    return float(total)