# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:32:16 2020

@author: Matko
"""
def ISAfunny(Z): # in meters
    """
    Atmospheric model according to 1976 (give more source)
    Returns temperature, pressure, density, kinematic viscosity,
    and speed of sound at given altitude.

    Parameters
    ----------
    Z : float
        Altitude [m]

    Returns
    -------
    list [T,P,rho,mu,a]
    in SI units: [K], [Pa], [kg/m3], [m2/s], [m/s]

    """

    import numpy as np

    g0 = 9.807  # [m/s2]
    R = 8.314472    # [J/molK]
    bs = 1.458e-6
    S = 110.4
    Ga = 1.4
    Mo = 28.9647e-3 # [kg/mol]
    
    Hb = np.array([0,11,20,32,47,51,71])    # [km]
    bet = np.array([-6.5,0,1,2.8,0,-2.8,-2])
    Tb = np.array([288.15,216.65,216.65,228.65,270.65,270.65,214.65])   # [K]
    pb = np.array([101325,22632.1,5474.89,868.019,110.906,66.9389,3.95642]) # [Pa]
    R1 = 6356.766e3;    # [m]
    
    hb = Hb*1000    # converts belts' altitudes from km to m
    bet = bet/1000  # [K/m]
    H = (Z*R1)/(Z+R1)   # [m]
    
    if H <= hb[1]:
        T = Tb[0] + bet[0]*(H-hb[0])
        P = pb[0]*( Tb[0]/( Tb[0]+bet[0]*(H-hb[0]) ) )**( (g0*Mo)/(R*bet[0]) )
    elif H > hb[1] and H <= hb[2]:
        T = Tb[1] + bet[1]*( H-hb[1])
        P = pb[1]*np.exp( (-g0*Mo*(H-hb[1]))/(R*Tb[1]) )
    elif H > hb[2] and H <= hb[3]:
        T = Tb[2] + bet[2]*(H-hb[2])
        P = pb[2]*( Tb[2]/( Tb[2]+bet[2]*( H-hb[2] ) ) )**( ( g0*Mo )/(R*bet[2]) )
    elif H > hb[3] and H <= hb[4]:
        T = Tb[3] + bet[3]*( H-hb[3] )
        P = pb[3]* ( Tb[3]/( Tb[3]+bet[3]*(H-hb[3]) ) )**( ( g0*Mo )/(R*bet[3]) )
    elif H > hb[4] and H <= hb[5]:
        T = Tb[4] + bet[4]*(H-hb[4])
        P = pb[4] * np.exp( (-g0*Mo*(H-hb[4]))/(R*Tb[4]) )
    elif H > hb[5] and H <= hb[6]:
        T = Tb[5] + bet[5]*(H - hb[5])
        P = pb[5] * ( Tb[5]/( Tb[5]+bet[5]*( H-hb[5] ) ) )**( ( g0*Mo )/(R*bet[5]) )
    elif H > hb[6]:
        T = Tb[6] + bet[6]*( H-hb[6] )
        P = pb[6] * ( pb[6]*( Tb[6]/( Tb[6]+bet[6]*(H-hb[6]) ) ) )**( ( g0*Mo )/(R*bet[6]) )
    else:
        print('this message should never appear')

    rho = ( P*Mo )/( R*T )          # Density
    mu = bs* ( T**1.5 )/( T+S )     # Viscosity
    a = np.sqrt( Ga*286.9*T )       # Speed of sound

    return [T,P,rho,mu,a]
    # return P
    # return rho
    # return mu
    # return a

#%% PLOTS plt.gca().set_xlim(0, .14);

# import matplotlib.pyplot as plt

# plt.figure(1)
# plt.plot(P/1000,H/1000)
# plt.gca().set_xlim(0,120)
# plt.gca().set_ylim(0,90)
# plt.xticks(np.arange(0,120,step=10),rotation=0)
# plt.xlabel('Pressure [kPa]')
# plt.yticks(np.arange(0,100,step=10),rotation=0)
# plt.ylabel('Altitude [km]')
# plt.gca().grid('on')

# plt.figure(2)
# plt.plot(rho/1,H/1000)
# # plt.gca().set_xlim(0,120)
# plt.gca().set_ylim(0,90)
# # plt.xticks(np.arange(0,120,step=10),rotation=0)
# plt.xlabel('Density [kg/m3]')
# plt.yticks(np.arange(0,100,step=10),rotation=0)
# plt.ylabel('Altitude [km]')
# plt.gca().grid('on')

# plt.figure(3)
# plt.plot(T/1,H/1000)
# # plt.gca().set_xlim(0,120)
# plt.gca().set_ylim(0,90)
# # plt.xticks(np.arange(0,120,step=10),rotation=0)
# plt.xlabel('Temperature [K]')
# plt.yticks(np.arange(0,100,step=10),rotation=0)
# plt.ylabel('Altitude [km]')
# plt.gca().grid('on')

# plt.figure(4)
# plt.plot(mu/1,H/1000)
# # plt.gca().set_xlim(0,120)
# plt.gca().set_ylim(0,90)
# # plt.xticks(np.arange(0,120,step=10),rotation=0)
# plt.xlabel('Viscosity [m2/s]')
# plt.yticks(np.arange(0,100,step=10),rotation=0)
# plt.ylabel('Altitude [km]')
# plt.gca().grid('on')

# plt.figure(5)
# plt.plot(a/1,H/1000)
# # plt.gca().set_xlim(0,120)
# plt.gca().set_ylim(0,90)
# # plt.xticks(np.arange(0,120,step=10),rotation=0)
# plt.xlabel('Speed of sound [m/s]')
# plt.yticks(np.arange(0,100,step=10),rotation=0)
# plt.ylabel('Altitude [km]')
# plt.gca().grid('on')

# plt.figure(6)
# plt.plot(P/max(P),H/1000,T/max(T),H/1000,rho/max(rho),H/1000,mu/max(mu),H/1000,a/max(a),H/1000,)

# print('ISAfunction done successfully')