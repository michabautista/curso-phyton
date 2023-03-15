import matplotlib.pyplot as plt 
import numpy as np

def generate_pie_chart():
    labels = [ 'A','B','C']
    values = [200,34,120]

    fig, ax = plt.subplots()
    ax.pie(labels=labels, x=values)
    plt.savefig ('pie2.png')
    plt.close() 

