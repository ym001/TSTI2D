# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:09:34 2019

@author: marc kefer
"""
"""
Niveau : Terminale STI2D
Programme : Septembre 2020

Capacités du BO travaillées :
    - Citer la définition de l'activité d'une source radioactive et indiquer 
    son unité.
    - Exploiter la définition de la demi-vie d'une espèce radioactive.
    
Objectifs de ce programme :  
    - Comparer l'évolution de l'activité de deux isotopes radioactifs différents
    - Utiliser le modèle mathématique de la décroissance exponentielle

Paramètres modifiables :
         - N0 : Nombre initial de noyaux (commun aux 2 isotopes choisis)
         - Isotope1 et Isotope 2 : les noms des 2 isotopes
         - T_d1 et T_d2 : Les demi-vies respectives des 2 isotopes
"""
import numpy as np
import matplotlib.pyplot as plt

# Exemples de demi-vies: 
# Cobalt 60 :               5.2  ans
# Tritium :                 12.3 ans
# Strontium 90 :            28.1 ans
# Césium 137 :              30   ans
# Américium 241 :          432   ans
# Radium 226 :            1600   ans
# Carbone 14 :            5730   ans
# Plutonium 239 :        24110   ans
# Neptunium 237 :      2140000   ans
# Uranium 235 :        7038000   ans
# Iode 129 :          15700000   ans
# Uranium 238 :     4470000000   ans

## PARAMETRES MODIFIABLES ####################################################     
N0=2.56e24                    # Nombre initial de noyaux :                
# Noms des isotopes :
Isotope1="Tritium"
Isotope2="Uranium 235"
# Valeurs des demi-vies :
Td_1=12.3                   # demi-vie de l'isotope 1, en années
Td_2=7038000                # demi-vie de l'isotope 2, en années
###############################################################################
###############################################################################
def TracerGraphe(k,Isotope,Td,A0,Couleur):    
    print('#######################################')
    print("## Graphique ",k," #####################")
    print("### Activité - Isotope :", Isotope, " ###")
    print('')
    print('Nombre initial de noyaux =', N0)
    print('Demi-vie =', str(Td),  'ans')
    print("Activité à t=0 : %.3E"%(A0), 'Becquerel')
      
    plt.axis([0,5*Td , 0, 1.2*A0])
    plt.xticks([0,Td,2*Td,3*Td,4*Td,5*Td])
    plt.yticks([0,A0/8,A0/4,A0/2,A0])

    plt.text(Td, 0.9*A0, r'Modèle mathématique :',size='13')
    plt.text(Td, 0.7*A0, r'$A(t)=A_0 \times e^{-\lambda \times t}$',size='14', color=Couleur)

    plt.grid([True])
    plt.ylabel('Activité (en Becquerel)')
    plt.xlabel("Années")
    plt.title(Isotope,fontsize='15')
    plt.show()
    
    print("Appuyer sur la touche 'Entrée' pour continuer.")
    input()
    
# Définition des paramètres graphiques ########################################
    # Constantes de temps, en années:
tau_1=Td_1/np.log(2)          # de l'isotope 1     
tau_2=Td_2/np.log(2)          # de l'isotope 2
         
SecondesParAn=365.25*24*3600
# Activité initiale
A01=N0/(SecondesParAn*tau_1)  # de l'isotope 1
A02=N0/(SecondesParAn*tau_2)  # de l'isotope 2

# Liste des instants considérés :
    # sur 5 demi-vies
t1=np.linspace(0,5*Td_1,1000)  # de l'isotope 1
t2=np.linspace(0,5*Td_2,1000)  # de l'isotope 2
    # aux multiples entiers de la demi-vie :
t1_p=np.linspace(0,5*Td_1,6)   # de l'isotope 1, 
t2_p=np.linspace(0,5*Td_2,6)   # de l'isotope 2

# Liste des valeurs de l'activité, sur 5 demi-vies de l'isotope 1 :
A1=A01*np.exp(-t1/tau_1)        # 1000 valeurs, en Becquerel
A1_p=A01*np.exp(-t1_p/tau_1)    # 6 valeurs, en Becquerel

# Liste des valeurs de l'activité, sur 5 demi-vies de l'isotope 2 :
A2=A02*np.exp(-t2/tau_2)        # 1000 valeurs, en Becquerel
A2_p=A02*np.exp(-t2_p/tau_2)    # 6 valeurs, en Becquerel

## Représentation graphique de l'activité de l'isotope 1 ######################
i=1
plt.plot(t1,A1,'-b')  
plt.plot(t1_p,A1_p,'ob') 
TracerGraphe(i,Isotope1, Td_1,A01,'b')

## Représentation graphique de l'activité de l'isotope 2 ######################
i=2    
plt.plot(t2,A2,'-r')
plt.plot(t2_p,A2_p,'or')
TracerGraphe(i,Isotope2, Td_2,A02,'r')
###############################################################################
print('Fin du programme')