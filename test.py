#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:58:59 2019

@author: phil
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import SVM_fct as svm_fct

def calculBarycentre(X, Y, Z, ZY) :
    w1 = []
    w2 = []
    m1 = []
    TEST = []
    
    Zdist = np.zeros((10, len(Z)))
    
    for cpt_class in range(0, 10):
        w1.append(X[Y == cpt_class]) #créer le tableau X avec le bon nombre de cases
        m1.append(np.mean(w1[cpt_class], axis=0)) # Création du tableau des barycentres des classes (les points sont des images)
        w2.append(Z[ZY == cpt_class]) #créer le tableau Z avec le bon nombre de cases
    
    for i in range(0, 10) :
        Zdist[i] = (abs((m1[i] - Z))**2).sum(axis=1)
    
    ZClasse = np.argmin(Zdist, axis=0)
    
    TEST.append(ZClasse == ZY)
    
    performance = (len(sum(TEST)) - sum(TEST).sum())/len(sum(TEST))
    print(performance*100)    

X = np.load('data/trn_img.npy')
Y = np.load('data/trn_lbl.npy')
Z = np.load('data/dev_img.npy')
ZY = np.load('data/dev_lbl.npy')

img = X[1].reshape(28,28)
plt.imshow(img, plt.cm.gray)
plt.show()

Xpca = PCA(n_components = 30)
Xpca.fit(X)                 # Créer la matrice de passage pour chznger de dimmension entre 784 et 30 pour cet exemple.
XReduit = Xpca.transform(X) #Reduction du nombre de dimmension de X

#print(Xpca.components_)
ZReduit = Xpca.transform(Z)

print("sans PCA")
calculBarycentre(X, Y, Z, ZY)
print("avec PCA")
calculBarycentre(XReduit, Y, ZReduit, ZY)

print("sans PCA")
svm_fct.calculSVMLin(X[:2000], Y[:2000], Z[:2000], ZY[:2000])
print("avec PCA")
svm_fct.calculSVMLin(XReduit[:2000], Y[:2000], ZReduit[:2000], ZY[:2000])

print("sans PCA")
svm_fct.calculSVMSvr(X[:2000], Y[:2000], Z[:2000], ZY[:2000])
print("avec PCA")
svm_fct.calculSVMSvr(XReduit[:2000], Y[:2000], ZReduit[:2000], ZY[:2000])

print("sans PCA")
svm_fct.calculSVMRbf(X[:2000], Y[:2000], Z[:2000], ZY[:2000])
print("avec PCA")
svm_fct.calculSVMRbf(XReduit[:2000], Y[:2000], ZReduit[:2000], ZY[:2000])


print("sans PCA")
svm_fct.calculSVMPoly(X[:2000], Y[:2000], Z[:2000], ZY[:2000])
print("avec PCA")
svm_fct.calculSVMPoly(XReduit[:2000], Y[:2000], ZReduit[:2000], ZY[:2000])
#svc(X, Y)