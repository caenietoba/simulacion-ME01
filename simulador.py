# import tkinter as tk
# from tkinter import ttk

# def on_button():
#     myValue = myEntry.get()
#     print(myValue)

# root = tk.Tk()

# w = tk.Frame(root)
# w.grid(row=0, columnspan=3)

# first_label = tk.Label(w, text="myEntry: ")
# first_label.grid(row=0, column=0, padx=10, sticky=tk.W)

# myEntry = tk.StringVar()
# myEntry_entry = ttk.Entry(w, textvariable=myEntry)
# myEntry_entry.grid(row=0, column=1, sticky=tk.W, padx=10)

# button1 = tk.Button(w, text="Print in Console", command=on_button)
# button1.grid(row=4, columnspan=1, sticky=tk.W)

# root.mainloop()

import math
import numpy as np

D = input("Ingre el diametro del nanotubo: ")
N = input("Ingrese la cantidad de links en el nanotubo: ")

beta = 2.0
print(beta)
m = 2.5
alpha = m/beta

cf = math.pi * D
ci = cf * 0.7
cdelta = 0.001
T = 200.0
psi = 1.0

relation_c0c = 1.0e-3


range_c = np.arange(ci, cf, 0.1)

def sigma(c):
    return T/(psi*pow(c, 1/beta))

def strength(sigma_c, sigma_L):
    #print(math.exp( -pow( sigma_c/sigma_L, m ) ))
    return 1 - math.exp( -pow( sigma_c/sigma_L, m ) )

import random
#c = 1000
for c in range_c:
    print("simulacion ",c)
    range_c0 = np.arange(0, c/100.0, cdelta)
    for c0 in range_c0:
        ##c0 = random.random()*c/10000.0
        sigma_c = sigma(c)
        #print(sigma_c)
        sigma_c0 = sigma(c0)
        sigma_L = sigma_c0 * pow(N, -1.0/m)
        #print(sigma_c, sigma_L)
        print(strength(sigma_c, sigma_L))


