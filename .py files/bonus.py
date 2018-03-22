# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 18:02:30 2018

@author: deadp
"""


import pandas as pd
file1 = pd.read_csv("part_2.tsv",delimiter="\t",error_bad_lines=False)
file2 = pd.read_csv("part_3.tsv",delimiter="\t",error_bad_lines=False)
merged = file1.merge(file2, on = "url")
merged.to_csv('bonus.tsv', sep="\t", encoding='utf-8', index=False)
