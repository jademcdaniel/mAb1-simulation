#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 21:34:25 2022

@author: jademcdaniel
"""
import os 

os.chdir('/Users/jademcdaniel/Downloads/')

import netCDF4 as nc

ds = nc.Dataset('./mab1.prod1.nc', mode='a')

ds.set_auto_mask(False)

val = ds['spatial'][:]

print("val=", val)

ds['spatial'][:] = ['x','y','z']

val1 = ds['spatial'][:]

print("val1=", val1)

