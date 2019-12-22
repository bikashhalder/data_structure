# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:21:04 2019

@author: BIKASH HALDER
"""

def find_bruth(T,P):
    n,m=len(T),len(P)
    for i in range(n-m+1):
        k=0
        while k < m and T[i+k]==P[k]:
            k+=1
            if k == m:
                return i
    return -1
find_bruth("aabaababbabccccnaaabbbaa","cccc")
