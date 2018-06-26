# Databricks notebook source
import pandas
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
df2 = df['col2']
df1 = df['col1']