# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:55:43 2021

@author: matko
"""

def tw_constant_level_velocity_turn(q,C_Dmin,ws,k,n):
    """
    The following expression is used to determine the
    T/W ratio required to maintain a specific banking load
    factor (n) at a specific airspeed and altitude, without
    losing altitude.
    
    It corresponds to specific energy density P_S = 0.
    
    Source: Snorri pg58, eq(3-1)

    Parameters
    ----------
    q : float
        Dynamic pressure at selected airspeed and altitude
    C_Dmin : float
        AKA CD0 - zero-lift drag, parasitic drag.
    ws : float
        Wing loading.
    k : float
        Lift-induced drag constant
    n : float
        Load factor (positive) n = 1/cos(phi).

    Returns
    -------
    T/W for constant level velocity turn.

    """
    
    tw = q * ( (C_Dmin)/(ws) + (ws)*k*(n/q)**2 )
    return tw

def tw_desired_specific_energy_level(q,C_Dmin,ws,k,n,P_S,V):
    """
    Sometimes it is of importance to evaluate the T/W for
    a specific energy level other than P_S = 0, as was done
    above. The following expression is used for this purpose.
    For instance, consider a project where the design
    is required to possess a specific energy level amounting
    to 20 ft/s at a given load factor, airspeed, and altitude.
    Such an evaluation could be used for the design of an
    aerobatic airplane, for which the capability of a rival
    aircraft might be known and used as a baseline.
    
    Source: Snorri pg58, eq(3-2)

    Parameters
    ----------
    q : float
        Dynamic pressure
    C_Dmin : float
        AKA CD0 - zero-lift drag, parasitic drag.
    ws : float
        Wing loading.
    k : float
        Lift-induced drag constant.
    n : float
        Load factor (positive).
    P_S : float
        DESCRIPTION.
    V : float
        DESCRIPTION.

    Returns
    -------
    T/W for constant level velocity turn.

    """
    
    tw = q * ( (C_Dmin)/(ws) + (ws)*k*(n/q)**2 ) + P_S/V
    return tw

def tw_desired_rate_of_climb(q,C_Dmin,ws,k,V_v,rho,V_y=47,crit=0.01):
    """
    The following expression is used to determine the
    T/W required to achieve a given rate of climb. An
    example of its use would be the extraction of T/W for a
    design required to climb at 2000 fpm at S-L or 1000 fpm
    at 10,000 ft.
    
    Note that ideally the airspeed, V, should be an estimate
    of the best rate-of-climb airspeed (V_Y - see Section
    18.3, General climb analysis methods). Since this requires
    far more information than typically available when
    this tool is used, resort to historical data by using VY
    for comparable aircraft. However, it may still be possible
    to estimate a reasonable V_Y for propeller aircraft using
    Equation (18-27).
    
    Source: Snorri pg59, eq(3-3)

    Parameters
    ----------
    q : float
        Dynamic pressure
    C_Dmin : float
        AKA CD0 - zero-lift drag, parasitic drag (Typ Table 3-1)
    ws : float
        Wing loading.
    k : float
        Lift-induced drag constant.
    V_y : float
        Airspeed, but not main cruise airspeed
        Ideally V_Y - best rate-of-climb airspeed (Typ Table 18-1)
        95 KCAS (~47m/s) is a solid initial guess
    V_v : float
        Desired rate of climb (vertical velocity).

    Returns
    -------
    T/W for desired rate of climb.

    """
    tw = V_v/V_y + q/(ws)*C_Dmin + (k/q)*(ws)
    return tw
    # tw_old = 0
    # diff = 1
    # LDmax = 1/( ( 4*C_Dmin*k )**0.5 )
    # while diff > crit:
    #     tw = V_v/V + q/(ws)*C_Dmin + (k/q)*(ws)
    #     V_y = ( ( ( tw*ws )/( 3*rho*C_Dmin ) )*( 1+(1+3/( LDmax**2 * tw**2 ))**0.5 ) )**0.5
    #     diff = tw-tw_old
    #     tw_old = tw
    #     V = V_y
    # return tw,V_y,LDmax

def tw_desired_TO_distance(q,C_DTO,C_LTO,ws,S_G,mu,V_LOF,g=9.81):
    """
    The following expression is used to determine the
    T/W required to achieve a given ground run distance
    during T-O. An example of its use would be the extraction
    of T/W for a design required to have a ground run
    no longer than 1000 ft.
    
    Source: Snorri pg59, eq(3-4), see also Table 3-1 for
            typical C_DTO and C_LTO

    Parameters
    ----------
    q : float
        Dynamic pressure at V_LOF/sqrt(2) and selected altitude CHECK
    C_DTO : float
        drag coefficient during T-O run.
    C_LTO : float
        lift coefficient during T-O run
    ws : float
        Wing loading.
    S_G : float
        Ground run distance
    V_LOF : float
        Liftoff speed.
    mu : float
        ground friction constant.
    g : float
        acceleration due to gravity

    Returns
    -------
    T/W for desired Take-off distance.

    """
    
    tw = ( (V_LOF**2)/(2*g*S_G) ) + ( (q*C_DTO)/(ws) ) + mu*(1-(q*C_LTO)/(ws))
    return tw

def tw_desired_cruise_airspeed(q,C_Dmin,ws,k):
    """
    The following expression is used to determine the
    T/W required to achieve a given cruising speed at a
    desired altitude. An example of its use would be the
    extraction of T/W for a design required to cruise at
    250 KTAS at 8000 ft.
    
    Source: Snorri pg59, eq(3-5)

    Parameters
    ----------
    q : float
        Dynamic pressure at selected airspeed and altitude.
    C_Dmin : float
        AKA CD0 - zero-lift drag, parasitic drag (Typ Table 3-1).
    ws : float
        Wing loading.
    k : float
        Lift-induced drag constant.

    Returns
    -------
    T/W for desired cruise airspeed.

    """
    
    tw = (q*C_Dmin)/ws + (k/q)*ws
    return tw

def tw_service_ceiling(C_Dmin,ws,k,rho,V_v=0.508):
    """
    The following expression is used to determine the
    T/W required to achieve a given service ceiling,
    assuming it is where the best rate-of-climb of the
    airplane has dropped to 100 fpm (0.508 m/s). An
    example of its use would be the extraction of T/W
    for a design required to have a service ceiling
    of 25,000 ft.

    Note that service ceiling implies V_Y (the best rateof-
    climb airspeed), as this yields the highest possible
    value. This is particularly important to keep in mind
    when converting the T/W to thrust and then to power
    for propeller aircraft (and as is demonstrated later).
    For this reason, V_Y should be estimated, for instance
    using Equation (18-27) or other suitable techniques.

    Parameters
    ----------
    C_Dmin : float
        AKA CD0 - zero-lift drag, parasitic drag (Typ Table 3-1).
    ws : float
        Wing loading.
    k : float
        Lift-induced drag constant.
    rho : float
        Air density at the desired altitude.
    V_v : float, optional
        Rate-of-climb. The default is 0.508.

    Returns
    -------
    T/W for service ceiling defined as altitude where
    max 0.508 m/s RoC is possible.

    """
    
    tw = ( V_v/( ( (2/rho)*(ws)*( k/(3*C_Dmin) )**0.5 )**0.5 ) ) + 4*( (k*C_Dmin)/3 )**0.5
    return tw

def clmax_ws_func(ws,rho_TO,V_stall):
    """
    

    Parameters
    ----------
    ws : float
        Wing loading.
    rho : float
        Air density at the desired altitude.
    V_stall : float
        Stalling velocity.

    Returns
    -------
    C_Lmax for a given wing lading (ws).

    """
    C_Lmax_ws = ( 2/(rho_TO*V_stall**2) )*(ws)
    return C_Lmax_ws