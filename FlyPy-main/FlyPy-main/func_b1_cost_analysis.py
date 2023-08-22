# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:57:50 2021

@author: matko
"""

def quantity_discount_factor(F_EXP=0.95,N=1000):
    """
    Snorri 2.2.1 Quantity Discount Factor
    (pg 36)

    Parameters
    ----------
    F_EXP : float, range 0.01-0.99
        Experience effectiveness (learning curve)
        0.01 - Max experience
        0.99 - Min experience
        
        80% experience effectiveness means that if it takes a technician
        100 hrs to put together, say, a batch of 10 assemblies, the next
        batch will only take 80% of that time, or 80 hrs, and the next
        batch will take 64 hrs, and so on, and thus you get a "discount
        on quantity".
    N : integer
        Number of units produced.

    Returns
    -------
    QDF - Quantity Discount Factor.
    -------

    """
    import numpy as np
    QDF = F_EXP**(1.4427*np.log(N)) # equation (2-1)
    return QDF

def dev_cost_GA(cost_input_dict):
        # W_airframe, V_H, N, f_comp,
        # yrs,
        # R_ENG,
        # N_P,
        # R_TOOL,
        # R_MFG,
        # N_PP,
        # CPIyear,
        # unit_sales_price, QDF, insurance=50000,
        # tapered='yes',
        # pressurized='yes', certificate='EASA', flap='simple', gear='retractable',
        # engine_type='turbofan',P_BHP=0,P_SHP=0,T=0,
        # prop_type='no_prop',D_P=0,
        # n_wwpy=48,n_whpw=40
    """
    Snorri 2.2.2 Development Cost of a GA Aircraft - the Eastlake Model
    (pg 37-43)
    The costs are calculated assuming the cost of living in the year 2012.
    That means the factor CPI is taken for the year 2012, and for year
    e.g. 2022 CPI must be updated.
    CPI - Consumer Price Index (aka cost-of-living index)
    For more information and updated values see footnote at pg 37 (or
    visit http://www.bls.gov/data/inflation_calculator.htm )
    
    CPI defined down there (CTRL+F "Jan 1986")

    Parameters
    ----------
    factor1 : TYPE
        DESCRIPTION.
    factor2 : TYPE
        DESCRIPTION.

    Returns dict with values
    -------
    None.

    """
    N           = cost_input_dict['N_units']
    W_airframe  = cost_input_dict['W_airframe']
    yrs         = cost_input_dict['yrs']
    f_comp      = cost_input_dict['f_comp']
    usdeur      = cost_input_dict['usdeur']
    unit_sales_price    = cost_input_dict['unit_sales_price'] * usdeur
    N_P         = cost_input_dict['N_P']
    R_ENG       = cost_input_dict['R_ENG'] * usdeur
    R_TOOL      = cost_input_dict['R_TOOL'] * usdeur
    R_MFG       = cost_input_dict['R_MFG'] * usdeur
    N_PP        = cost_input_dict['N_PP']
    insurance   = cost_input_dict['insurance'] * usdeur
    D_P         = cost_input_dict['D_P'] / 0.3048
    n_wwpy      = cost_input_dict['n_wwpy']
    n_whpw      = cost_input_dict['n_whpw']
    CPIyear     = cost_input_dict['CPIyear']
    certificate = cost_input_dict['certificate']
    flap        = cost_input_dict['flap']
    gear        = cost_input_dict['gear']
    pressurized = cost_input_dict['pressurized']
    tapered     = cost_input_dict['tapered']
    engine_type = cost_input_dict['engine_type']
    prop_type   = cost_input_dict['prop_type']
    PP_val      = cost_input_dict['PP_val']
    V_H         = cost_input_dict['V_H'] / 0.5144
    QDF         = cost_input_dict['QDF']
    
    return_dict = dict()
    W_airframe = W_airframe / 4.448 # because these estimates take lbf
    #%% Number of Engineering Man-Hours
    # Number of engineering man-hours required to design the aircraft and
    # perform the necessary RDT&E (Research, Development, Tests, and Evaluation)
    if pressurized == 'yes':
        F_PRESS1 = 1.03
    elif pressurized == 'no':
        F_PRESS1 = 1.0
    if certificate == 'EASA':
        F_CERT1 = 1.0
    elif certificate == 'FAA':
        F_CERT1 = 0.67
    if flap == 'simple':
        F_CF1 = 1
    elif flap == 'complex':
        F_CF1 = 1.03
    F_COMP1 = 1+f_comp
    H_ENG = 0.0396 * W_airframe**0.791 * V_H**1.526 * N**0.183 * F_CERT1 * F_CF1 * F_COMP1 * F_PRESS1 # equation (2-2)
    return_dict['H_ENG'] = round(H_ENG)
    """
    W_airframe  - weight of structural skeleton* (65% of operational empty weight)
    V_H         - maximum level airspeed in KTAS
    N           - number of aircraft to be produced over a 5-year period
    F_CERT1     - =0.67 if certified as LSA, =1 if certified as a 14 CFR Part 23
    F_CF1       - =1.03 if complex flap, =1 if simple flap
    F_COMP1 = 1+f_comp  - a factor to account for the use of composites in the airframe
    f_comp      - fraction of airframe made from composites (0=no composites, 1=full composite)
    F_PRESS1    - =1 if unpressurized, =1.03 if pressurized
    
    *structural skeleton weighs far less than the empty weight of the aircraft.
     This weight can be approximated by considering the empty weight minus
     engines, avionics, seats, furnishing, control system, and other.
     If unknown, assume ~65% of empty weight
     """
     
    #%% Number of Tooling Man-hours
    # Number of man-hours required to design and build tools, fixtures, jigs, molds, etc
    if pressurized == 'yes':
        F_PRESS2 = 1.01
    elif pressurized == 'no':
        F_PRESS2 = 1.0
    if flap == 'simple':
        F_CF2 = 1
    elif flap == 'complex':
        F_CF2 = 1.02
    if tapered == 'yes':
        F_TAPER = 1
    elif tapered == 'no':
        F_TAPER = 0.95
    Q_m = round(N/(12*yrs),2)
    H_TOOL = 1.0032 * W_airframe**0.764 * V_H**0.899 * N**0.178 * Q_m**0.066 * F_TAPER * F_CF2 * F_COMP1 * F_PRESS2 # equation (2-3)
    return_dict['H_TOOL'] = round(H_TOOL)
    """
    Q_m         - estimated production rate in aircraft per month (=N/60 for 60 months i.e. 5 years)
    F_TAPER     - =0.95 for no taper, =1 for tapered wing
    F_CF2       - =1.02 if complex flap, =1 if simple flap
    F_PRESS2    - =1 if unpressurized, =1.01 if pressurized
    """
    #%% Number of Manufacturing Labor Man-hours
    # Number of man-hours required to build the aircraft
    if certificate == 'EASA':
        F_CERT2 = 1.0
    elif certificate == 'FAA':
        F_CERT2 = 0.75
    if flap == 'simple':
        F_CF3 = 1
    elif flap == 'complex':
        F_CF3 = 1.01
    F_COMP2 = 1 + 0.25*f_comp
    H_MFG = 9.6613 * W_airframe**0.74 * V_H**0.543 * N**0.524 * F_CERT2 * F_CF3 * F_COMP2 # equation (2-4)
    return_dict['H_MFG'] = round(H_MFG)
    """
    F_CERT2     - =0.75 if certified as LSA, =1 if certified as a 14 CFR Part 23
    F_CF3       - =1.01 if complex flap, =1 if simple flap
    F_COMP2 = 1+0.25*f_comp - a factor to account for the use of composites in the airframe
    """
    
    
    
    
    #%% Total Cost of Engineering
    CPI2021 = CPIyear # 2.0969 #2.496049 # Jan 1986 --> Aug 2021
    CPI = CPI2021
    C_ENG = CPI * H_ENG * R_ENG # equation (2-5)
    return_dict['C_ENG'] = round(C_ENG/usdeur)
    """
    R_ENG       - rate of engineering labor in $/h (e.g. $92/h)
    CPI         - Consumer Price Index for 2021 relative to 1986
    """
    
    #%% Total Cost of Development Support
    # The cost of overheads, administration, logistics, HR, facilities maintenance personell, etc
    CPI2012 = 2.0969 # CPI ratio is required --> CPI2021/CPI2012
    
    if certificate == 'EASA':
        F_CERT3 = 1.0
    elif certificate == 'FAA':
        F_CERT3 = 0.5
    F_COMP3 = 1 + 0.5*f_comp
    C_DEV = 0.06458 * W_airframe**0.873 * V_H**1.89 * N_P**0.346 * (CPI2021/CPI2012) * F_CERT3 * F_CF3 * F_COMP3 * F_PRESS1
    return_dict['C_DEV'] = round(C_DEV/usdeur)
    """
    N_P         - number of prototypes
    F_CERT3     - =0.5 if certified as LSA, =1 if certified as a 14 CFR Part 23
    F_COMP3 = 1+0.5*f_comp  - a factor to account for the use of composites in the airframe
    """
    
    #%% Total Cost of Flight Test Operations
    # Total cost of completing the development and certification flight-test program
    # CPI ratio is required --> CPI2021/CPI2012
    if certificate == 'EASA':
        F_CERT4 = 1.0
    elif certificate == 'FAA':
        F_CERT4 = 10.0
    C_FT = 0.009646 * W_airframe**1.16 * V_H**1.3718 * N_P**1.281 * (CPI2021/CPI2012) * F_CERT4 # equation (2-7)
    return_dict['C_FT'] = round(C_FT/usdeur)
    """
    F_CERT4     - =10 if certified as LSA, =1 if certified as a 14 CFR Part 23
    """
    
    #%% Total Cost of Tooling
    # Cost of designing, fabricating, and maintaining jigs, fixtures, molds, ...
    # Tooling requires industrial and manufacturing engineers for the design
    # work and technicians to fabricate and maintain
    C_TOOL = CPI * H_TOOL * R_TOOL # equation (2-8)
    return_dict['C_TOOL'] = round(C_TOOL/usdeur)
    """
    R_TOOL      - rate of tooling labor in $/h (e.g. $61/h)
    """
    
    #%% Total Cost of Manufacturing
    # Cost of manufacturing labor required to produce the aircraft
    C_MFG = CPI * H_MFG * R_MFG # equation (2-9)
    return_dict['C_MFG'] = round(C_MFG/usdeur)
    """
    R_MFG       - rate of manufacturing labor in $/h (e.g. $53/h)
    """
    
    #%% Total Cost of Quality Control
    # Cost of technicians and the equipment required to demonstrate that the
    # product being manufactured is inded the airplane shown in the drawing package
    C_QC = 0.13 * C_MFG * F_CERT3 * F_COMP3
    return_dict['C_QC'] = round(C_QC/usdeur)
    
    #%% Total Cost of Materials
    # Cost of raw material (aluminium sheets, pre-impregnated composites,
    # landing gear, avionics, etc.) required to fabricate the airplane
    C_MAT = 24.896 * W_airframe**0.689 * V_H**0.624 * N**0.792 * (CPI2021/CPI2012) * F_CERT2 * F_CF2 * F_PRESS2
    return_dict['C_MAT'] = round(C_MAT/usdeur)
    
    #%% Total Cost to Certify
    # Sum of costs of Engineering, Development Support, Flight Test, and Tooling
    C_CERT = C_ENG + C_DEV + C_FT + C_TOOL
    return_dict['C_CERT'] = round(C_CERT/usdeur)
    
    #%% Cost of Retractable Landing Gear per Airplane
    # Already included in the DAPCA-IV (this) formulation, so an adjustment
    # is made only if the airplane has fixed landing gear. If so, subtract
    # $7500 per airplane
    if gear == 'retractable':
        gear_val = 0
    elif gear == 'fixed':
        gear_val = -7500
    return_dict['gear_val'] = round(gear_val/usdeur)
    
    #%% Cost of Avionics
    # In the absence of more accurate information, in 2012 US dollars (that's why CPI ratio),
    # add $15000 per airplane if it's certified to 14 CFR Part 23 (EASA), or add $4500 per
    # airplane if it's certified as an LSA (Light Sport Aircraft) (FAA)
    if certificate == 'EASA':
        avionics = 15000 * (CPI2021/CPI2012)
    elif certificate == 'FAA':
        avionics = 4500 * (CPI2021/CPI2012)
    return_dict['avionics'] = round(avionics/usdeur)
    #%% Cost of Power Plant (engines, propellers)
    # The cost of the engine depends on the number of (N_PP) and type of engine
    # (piston, turboprop, turbojet, or turbofan). For piston and turboprop engines
    # the cost depends on the rated brake-horsepower (P_BHP) or shaft-horsepower
    # (P_SHP). For turbojets and turbofans it is based on the rated thrust (T).
    if engine_type == 'Piston':
        C_PP = 174.0 * N_PP * PP_val * (CPI2021/CPI2012) # equation (2-13)
    elif engine_type == 'Turboprop':
        C_PP = 377.4 * N_PP * PP_val * (CPI2021/CPI2012) # equation (2-14)
    elif engine_type == 'Turbojet':
        C_PP = 868.1 * N_PP * PP_val**0.8356 * (CPI2021/CPI2012) # equation (2-15)
    elif engine_type == 'Turbofan':
        C_PP = 1035.9 * N_PP * PP_val**0.8356 * (CPI2021/CPI2012) # equation (2-16)
    elif engine_type == 'No engine':
        C_PP = 0
    return_dict['C_PP'] = round(C_PP/usdeur)
    
    # Since piston and turboprop engines also require propellers, this cost must
    # be determined as well. The two most common types are the fixed-pitch and
    # the constant speed propellers. The typical fixed-pitch propeller cost
    # around $3145 in 2012. However constant-speed propellers are more expensive
    # and an expression that takes into account the diameter of the propeller
    # (D_P [ft]) and P_SHP has been derived.
    if engine_type == 'Piston' or engine_type == 'Turboprop':
        if prop_type == 'Fixed pitch':
            C_prop = 3145 * N_PP * (CPI2021/CPI2012) # equation (2-17)
        elif prop_type == 'Constant speed':
            P_SHP = PP_val
            C_prop = 209.69 * N_PP * (CPI2021/CPI2012) * D_P**2 * (P_SHP/D_P)**0.12 # equation (2-18)
        elif prop_type == 'No propeller':
            C_prop = 0
    else:
        C_prop = 0
    return_dict['C_prop'] = round(C_prop/usdeur)
    
    #%% Number of engineers
    # Number of engineers needed to develop the aircraft over a period of eng_yrs years
    eng_yrs = 3/5 * yrs
    N_ENG = ( H_ENG )/( eng_yrs * n_wwpy * n_whpw )
    return_dict['N_ENG'] = round(N_ENG)
    """
    eng_yrs     - time for only development, roughly 60% of total time
    n_wwpy      - number of WorkWeeks Per Year (generally 48)
    n_whpw      - number of Working Hours Per Week (generally 40)
    """
    
    #%% Time to manufacture a single unit [hours]
    t_AC = H_MFG / N
    return_dict['t_AC'] = round(t_AC)
    
    #%% Break-even Analysis
    # How many units must be produced before revenue equals the cost incurred.
    # Using the standard cost-volume-profit-analysis equation (2-19) is used.
    total_fixed_cost = C_CERT
    unit_variable_cost = (C_MFG + C_QC + C_MAT)/N + (gear_val+C_PP+C_prop+avionics)*QDF + insurance
    return_dict['unit_variable_cost'] = round(unit_variable_cost/usdeur)
    min_usp = round(unit_variable_cost*1.2)
    a = len(str(min_usp))
    sfg = 2 # significant figures (generally 3)
    
    return_dict['min_unit_sales_price'] = round(min_usp*10**(-(a-sfg)))*10**(a-sfg)
    # return_dict['min_unit_sales_price'] = round(unit_variable_cost*1.2)
    N_BE = ( total_fixed_cost )/( unit_sales_price - unit_variable_cost ) # equation (2-19)
    return_dict['N_BE'] = round(N_BE)
    """
    total_fixed_cost    - generally certification cost C_CERT
    unit_variable_cost  - sum of manufacturing labor, quality control,
                          materials/equipment, landing gear, engines,
                          propellers, avionics, and manufacturer's liability
                          insurance divided by the number of units produced
    unit_sales_price    - how much would you sell your aircraft for?
    """
    return return_dict