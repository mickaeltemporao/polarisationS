import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("ESS11e04_1/ESS11e04_1.csv")
df['vote']

#Trust in political parties
df['trstprt'].describe() 

# Voted last national election 
df['vote'].describe()