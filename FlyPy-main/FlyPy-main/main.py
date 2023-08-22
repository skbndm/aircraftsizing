# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:39:01 2021

@author: Matko
"""
#%% 01 IMPORTS
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Implement the canvas thing, so Frame[Canvas[Subplot[Plot] ] ]
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk # Implement the Matplotlib toolbar
from matplotlib.backend_bases import key_press_handler # Implement the default Matplotlib key bindings
from matplotlib.figure import Figure # Implement Matplotlib figure
from parameters import mainparameters
from parameters import designpoint
import menu_functions
import func_b1_cost_analysis

#%% 02 Units Functions

def altitudeunits(value):
    global label5
    global label42
    global label44
    if value == 1:
        if label5.cget("text") == "[ft]":
            label5.grid_forget()
            label5 = tk.Label(frame3, text='[m]')
            label5.grid(row=0, column=2, sticky="w")
            a = str(round(float(entry1.get())*0.3048,1))
            entry1.delete(0,99)
            entry1.insert(tk.END, a)
            
            label42.grid_forget()
            label42 = tk.Label(frame3, text='[m]')
            label42.grid(row=14, column=2, sticky="w")
            b = str(round(float(entry15.get())*0.3048,1))
            entry15.delete(0,99)
            entry15.insert(tk.END, b)
            
            label44.grid_forget()
            label44 = tk.Label(frame3, text='[m]')
            label44.grid(row=15, column=2, sticky="w")
            c = str(round(float(entry16.get())*0.3048,1))
            entry16.delete(0,99)
            entry16.insert(tk.END, c)
        else:
            return
    if value == 2:
        if label5.cget("text") == "[m]":
            label5.grid_forget()
            label5 = tk.Label(frame3, text='[ft]', fg=col2)
            label5.grid(row=0, column=2, sticky="w")
            a = str(round(float(entry1.get())/0.3048))
            entry1.delete(0,99)
            entry1.insert(tk.END, a)
            
            label42.grid_forget()
            label42 = tk.Label(frame3, text='[ft]', fg=col2)
            label42.grid(row=14, column=2, sticky="w")
            b = str(round(float(entry15.get())/0.3048))
            entry15.delete(0,99)
            entry15.insert(tk.END, b)
            
            label44.grid_forget()
            label44 = tk.Label(frame3, text='[ft]', fg=col2)
            label44.grid(row=15, column=2, sticky="w")
            c = str(round(float(entry16.get())/0.3048))
            entry16.delete(0,99)
            entry16.insert(tk.END, c)
        else:
            return

def velocityunits(value):
    global label6
    global label38
    global label40
    global label46
    if value == 1:
        if label6.cget("text") == "[kn]":
            label6.grid_forget()
            label6 = tk.Label(frame3, text='[m/s]')
            label6.grid(row=1, column=2, sticky="w")
            a = str(round(float(entry2.get())*0.5144,2))
            entry2.delete(0,99)
            entry2.insert(tk.END, a)
            
            label38.grid_forget()
            label38 = tk.Label(frame3, text='[m/s]')
            label38.grid(row=12, column=2, sticky="w")
            b = str(round(float(entry13.get())*0.5144,2))
            entry13.delete(0,99)
            entry13.insert(tk.END, b)
            
            label40.grid_forget()
            label40 = tk.Label(frame3, text='[m/s]')
            label40.grid(row=13, column=2, sticky="w")
            c = str(round(float(entry14.get())*0.5144,2))
            entry14.delete(0,99)
            entry14.insert(tk.END, c)
            
            label46.grid_forget()
            label46 = tk.Label(frame3, text='[m/s]')
            label46.grid(row=16, column=2, sticky="w")
            d = str(round(float(entry17.get())*0.5144,2))
            entry17.delete(0,99)
            entry17.insert(tk.END, d)
            
            # label46 # v_vx
            # entry17
        else:
            return
    if value == 2:
        if label6.cget("text") == "[m/s]":
            label6.grid_forget()
            label6 = tk.Label(frame3, text='[kn]', fg=col1)
            label6.grid(row=1, column=2, sticky="w")
            a = str(round(float(entry2.get())/0.5144,1))
            entry2.delete(0,99)
            entry2.insert(tk.END, a)
            
            label38.grid_forget()
            label38 = tk.Label(frame3, text='[kn]', fg=col1)
            label38.grid(row=12, column=2, sticky="w")
            b = str(round(float(entry13.get())/0.5144,1))
            entry13.delete(0,99)
            entry13.insert(tk.END, b)
            
            label40.grid_forget()
            label40 = tk.Label(frame3, text='[kn]', fg=col1)
            label40.grid(row=13, column=2, sticky="w")
            c = str(round(float(entry14.get())/0.5144,1))
            entry14.delete(0,99)
            entry14.insert(tk.END, c)
            
            label46.grid_forget()
            label46 = tk.Label(frame3, text='[kn]', fg=col1)
            label46.grid(row=16, column=2, sticky="w")
            d = str(round(float(entry17.get())/0.5144,1))
            entry17.delete(0,99)
            entry17.insert(tk.END, d)
        else:
            return

col1 = '#0040ff' # blue good
col2 = '#00c030' # green
#%% 03 Functions for Tkinter

def press_enterf(press_enter1):
    button1fun()

def _quit():
    root.quit()
    root.destroy()

def button1fun():
    global label111, label222, label333, label444
    global savelist
    if 'label111' in globals():
        label111.destroy()
        label222.destroy()
        label333.destroy()
        label444.destroy()
    
    global ws, tw_clvt_list, tw_dsel_list, tw_droc_list, tw_dtod_list, tw_dca_list, tw_sc_list, clmax_list
    global pw_clvt_list, pw_dsel_list, pw_droc_list, pw_dtod_list, pw_dca_list, pw_sc_list
    global pwsl_clvt_list, pwsl_dsel_list, pwsl_droc_list, pwsl_dtod_list, pwsl_dca_list, pwsl_sc_list
    global S_list, t_clvt_mass_list, t_dsel_mass_list, t_dtod_mass_list, t_dca_mass_list, t_sc_mass_list
    global p_clvt_mass_list, p_dsel_mass_list, p_dtod_mass_list, p_dca_mass_list, p_sc_mass_list
    global psl_clvt_mass_list, psl_dsel_mass_list, psl_dtod_mass_list, psl_dca_mass_list, psl_sc_mass_list
    global DP_pw, DP_pwsl, Thr, P_hp, P_hpSL, DP_S, clmax
    global cost_output_dict
    
    "COST INPUTS"
    cost_input_dict = dict()
    cost_input_dict['F_EXP']        = float(entry4411val.get())
    cost_input_dict['N_units']      = int(entry4412val.get())
    cost_input_dict['W_airframe']   = float(entry4414val.get())
    cost_input_dict['yrs']          = float(entry4415val.get())
    cost_input_dict['f_comp']       = float(entry4416val.get())
    cost_input_dict['unit_sales_price'] = float(entry4417val.get())
    cost_input_dict['N_P']          = float(entry4418val.get())
    cost_input_dict['R_ENG']        = float(entry4419val.get())
    cost_input_dict['R_TOOL']       = float(entry4420val.get())
    cost_input_dict['R_MFG']        = float(entry4421val.get())
    cost_input_dict['N_PP']         = float(entry4422val.get())
    cost_input_dict['insurance']    = float(entry4423val.get())
    cost_input_dict['D_P']          = float(entry4429val.get())
    cost_input_dict['n_wwpy']       = float(entry4432val.get())
    cost_input_dict['n_whpw']       = float(entry4433val.get())
    cost_input_dict['CPIyear']      = float(entry4434val.get()) #41
    cost_input_dict['certificate']  = cbox_certificate.get()
    cost_input_dict['flap']         = cbox_flap.get()
    cost_input_dict['gear']         = cbox_gear.get()
    cost_input_dict['pressurized']  = var_pressurized.get()
    cost_input_dict['tapered']      = var_tapered.get()
    cost_input_dict['engine_type']  = cbox_engine_type.get()
    cost_input_dict['prop_type']    = cbox_prop_type.get()
    cost_input_dict['PP_val']       = float(entry4438val.get())
    cost_input_dict['usdeur']       = float(entry4456val.get())
    
    sizing_input_dict = dict()
    sizing_input_dict['ws_lo'] = round(float(ws_range_from.get()))
    sizing_input_dict['ws_hi'] = round(float(ws_range_to.get()))
    if sizing_input_dict['ws_lo'] <= 0:
        ws_range_from.delete(0,99)
        ws_range_from.insert(tk.END , '1')
        sizing_input_dict['ws_lo'] = int(ws_range_from.get())
    if sizing_input_dict['ws_hi'] <= sizing_input_dict['ws_lo']:
        ws_range_to.delete(0,99)
        ws_range_to.insert(tk.END , str(sizing_input_dict['ws_lo']+1))
        sizing_input_dict['ws_hi'] = int(ws_range_to.get())
    sizing_input_dict['ws_params'] = [sizing_input_dict['ws_lo'],sizing_input_dict['ws_hi'],100] # [start, stop, numsteps] for np.linspace in function
    sizing_input_dict['alt'] = float(entry1.get())
    if r2.get() == 2:
        sizing_input_dict['alt'] = sizing_input_dict['alt']*0.3048
    sizing_input_dict['V'] = float(entry2.get())
    if r3.get() == 2:
        sizing_input_dict['V'] = sizing_input_dict['V']*0.5144
    cost_input_dict['V_H'] = sizing_input_dict['V'] # except here 
    sizing_input_dict['mtom'] = float(entry3.get())
    sizing_input_dict['mtow'] = sizing_input_dict['mtom']*9.81
    sizing_input_dict['ar'] = float(entry4.get())
    sizing_input_dict['C_Dmin'] = float(entry5.get())
    sizing_input_dict['n'] = float(entry6.get())
    sizing_input_dict['P_S'] = float(entry7.get())
    sizing_input_dict['V_v'] = float(entry8.get())
    sizing_input_dict['C_DTO'] = float(entry9.get())
    sizing_input_dict['C_LTO'] = float(entry10.get())
    sizing_input_dict['S_G'] = float(entry11.get())
    sizing_input_dict['mu_gr'] = float(entry12.get())
    sizing_input_dict['V_LOF'] = float(entry13.get())
    if r3.get() == 2:
        sizing_input_dict['V_LOF'] = sizing_input_dict['V_LOF']*0.5144
    sizing_input_dict['V_vx'] = float(entry14.get())
    if r3.get() == 2:
        sizing_input_dict['V_vx'] = sizing_input_dict['V_vx']*0.5144
    sizing_input_dict['alt_sc'] = float(entry15.get())
    if r2.get() == 2:
        sizing_input_dict['alt_sc'] = sizing_input_dict['alt_sc']*0.3048
    sizing_input_dict['alt_TO'] = float(entry16.get())
    if r2.get() == 2:
        sizing_input_dict['alt_TO'] = sizing_input_dict['alt_TO']*0.3048
    sizing_input_dict['V_stall'] = float(entry17.get())
    if r3.get() == 2:
        sizing_input_dict['V_stall'] = sizing_input_dict['V_stall']*0.5144
    sizing_input_dict['eta_prop'] = float(entry18.get())
    sizing_input_dict['DP_ws'] = float(entry52.get())
    sizing_input_dict['DP_tw'] = float(entry51.get())
    
    savelist = [
        "savefile for FlyPy",
        sizing_input_dict['alt'],
        sizing_input_dict['V'],
        sizing_input_dict['mtom'],
        sizing_input_dict['ar'],
        sizing_input_dict['C_Dmin'],
        sizing_input_dict['n'],
        sizing_input_dict['P_S'],
        sizing_input_dict['V_v'],
        sizing_input_dict['C_DTO'],
        sizing_input_dict['C_LTO'],
        sizing_input_dict['S_G'],
        sizing_input_dict['mu_gr'],
        sizing_input_dict['V_LOF'],
        sizing_input_dict['V_vx'],
        sizing_input_dict['alt_sc'],
        sizing_input_dict['alt_TO'],
        sizing_input_dict['V_stall'],
        sizing_input_dict['eta_prop'],
        sizing_input_dict['DP_ws'],
        sizing_input_dict['DP_tw'],
        sizing_input_dict['ws_lo'],
        sizing_input_dict['ws_hi'],
        r1.get(),
        r2.get(),
        r3.get(),
        cost_input_dict['F_EXP'],
        cost_input_dict['N_units'],
        cost_input_dict['W_airframe'],
        cost_input_dict['yrs'],
        cost_input_dict['f_comp'],
        cost_input_dict['unit_sales_price'],
        cost_input_dict['N_P'],
        cost_input_dict['R_ENG'],
        cost_input_dict['R_TOOL'],
        cost_input_dict['R_MFG'],
        cost_input_dict['N_PP'],
        cost_input_dict['insurance'],
        cost_input_dict['D_P'],
        cost_input_dict['n_wwpy'],
        cost_input_dict['n_whpw'],
        cost_input_dict['CPIyear'],
        cost_input_dict['certificate'],
        cost_input_dict['flap'],
        cost_input_dict['gear'],
        cost_input_dict['pressurized'],
        cost_input_dict['tapered'],
        cost_input_dict['engine_type'],
        cost_input_dict['prop_type'],
        cost_input_dict['PP_val'],
        cost_input_dict['usdeur']
        ]
    
    QDF = func_b1_cost_analysis.quantity_discount_factor(cost_input_dict['F_EXP'],cost_input_dict['N_units'])
    cost_input_dict['QDF'] = QDF
    
    cost_output_dict = func_b1_cost_analysis.dev_cost_GA(cost_input_dict)
    
    sizing_output_dict = mainparameters(sizing_input_dict)
    #--------------- Unpacking results ---------------#
    T   = sizing_output_dict['T']
    p   = sizing_output_dict['p']
    rho = sizing_output_dict['rho']
    mu  = sizing_output_dict['mu']
    a   = sizing_output_dict['a']
    V   = sizing_output_dict['V']
    q   = sizing_output_dict['q']
    e   = sizing_output_dict['e']
    k   = sizing_output_dict['k']
    ws  = sizing_output_dict['ws']
    tw_clvt_list        = sizing_output_dict['tw_clvt_list']
    tw_dsel_list        = sizing_output_dict['tw_dsel_list']
    tw_dtod_list        = sizing_output_dict['tw_dtod_list']
    tw_dca_list         = sizing_output_dict['tw_dca_list']
    tw_sc_list          = sizing_output_dict['tw_sc_list']
    pw_clvt_list        = sizing_output_dict['pw_clvt_list']
    pwsl_clvt_list      = sizing_output_dict['pwsl_clvt_list']
    t_clvt_mass_list    = sizing_output_dict['t_clvt_mass_list']
    p_clvt_mass_list    = sizing_output_dict['p_clvt_mass_list']
    psl_clvt_mass_list  = sizing_output_dict['psl_clvt_mass_list']
    pw_dsel_list        = sizing_output_dict['pw_dsel_list']
    pwsl_dsel_list      = sizing_output_dict['pwsl_dsel_list']
    t_dsel_mass_list    = sizing_output_dict['t_dsel_mass_list']
    p_dsel_mass_list    = sizing_output_dict['p_dsel_mass_list']
    psl_dsel_mass_list  = sizing_output_dict['psl_dsel_mass_list']
    pw_dtod_list        = sizing_output_dict['pw_dtod_list']
    pwsl_dtod_list      = sizing_output_dict['pwsl_dtod_list']
    t_dtod_mass_list    = sizing_output_dict['t_dtod_mass_list']
    p_dtod_mass_list    = sizing_output_dict['p_dtod_mass_list']
    psl_dtod_mass_list  = sizing_output_dict['psl_dtod_mass_list']
    pw_dca_list         = sizing_output_dict['pw_dca_list']
    pwsl_dca_list       = sizing_output_dict['pwsl_dca_list']
    t_dca_mass_list     = sizing_output_dict['t_dca_mass_list']
    p_dca_mass_list     = sizing_output_dict['p_dca_mass_list']
    psl_dca_mass_list   = sizing_output_dict['psl_dca_mass_list']
    pw_sc_list          = sizing_output_dict['pw_sc_list']
    pwsl_sc_list        = sizing_output_dict['pwsl_sc_list']
    t_sc_mass_list      = sizing_output_dict['t_sc_mass_list']
    p_sc_mass_list      = sizing_output_dict['p_sc_mass_list']
    psl_sc_mass_list    = sizing_output_dict['psl_sc_mass_list']
    S_list              = sizing_output_dict['S_list']
    clmax_list          = sizing_output_dict['clmax_list']
    
    designpoint_output_dict = designpoint(sizing_input_dict)
    DP_pw = designpoint_output_dict['DP_pw']
    DP_pwsl = designpoint_output_dict['DP_pwsl']
    Thr = designpoint_output_dict['Thr']
    P_hp = designpoint_output_dict['P_hp']
    P_hpSL = designpoint_output_dict['P_hpSL']
    DP_S = designpoint_output_dict['DP_S']
    clmax = designpoint_output_dict['clmax']
    
    label53 = tk.Label(frame5, text=str(round(DP_pw,4)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label53.grid(row=53, column=1, sticky="w")
    label54 = tk.Label(frame5, text=str(round(DP_pwsl,4)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label54.grid(row=54, column=1, sticky="w")
    label55 = tk.Label(frame5, text=str(round(Thr,1)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label55.grid(row=55, column=1, sticky="w")
    label56 = tk.Label(frame5, text=str(round(P_hp,1)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label56.grid(row=56, column=1, sticky="w")
    label57 = tk.Label(frame5, text=str(round(P_hpSL,1)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label57.grid(row=57, column=1, sticky="w")
    label58 = tk.Label(frame5, text=str(round(DP_S,2)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label58.grid(row=58, column=1, sticky="w")
    label59 = tk.Label(frame5, text=str(round(clmax,2)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label59.grid(row=59, column=1, sticky="w")

    # Cost
    label4413val = tk.Label(frame442, text=str( round(QDF,ndigits=2) ), anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4413val.grid(row=0, column=1, sticky="w")
    label4435val = tk.Label(frame442, text=f"{cost_output_dict['H_ENG']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4435val.grid(row=1, column=1, sticky="w")
    label4436val = tk.Label(frame442, text=f"{cost_output_dict['H_TOOL']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4436val.grid(row=2, column=1, sticky="w")
    label4437val = tk.Label(frame442, text=f"{cost_output_dict['H_MFG']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4437val.grid(row=3, column=1, sticky="w")
    label4439val = tk.Label(frame442, text=f"{cost_output_dict['C_ENG']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4439val.grid(row=4, column=1, sticky="w")
    label4440val = tk.Label(frame442, text=f"{cost_output_dict['C_DEV']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4440val.grid(row=5, column=1, sticky="w")
    label4441val = tk.Label(frame442, text=f"{cost_output_dict['C_FT']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4441val.grid(row=6, column=1, sticky="w")
    label4442val = tk.Label(frame442, text=f"{cost_output_dict['C_TOOL']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4442val.grid(row=7, column=1, sticky="w")
    label4443val = tk.Label(frame442, text=f"{cost_output_dict['C_MFG']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4443val.grid(row=8, column=1, sticky="w")
    label4444val = tk.Label(frame442, text=f"{cost_output_dict['C_QC']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4444val.grid(row=9, column=1, sticky="w")
    label4445val = tk.Label(frame442, text=f"{cost_output_dict['C_MAT']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4445val.grid(row=10, column=1, sticky="w")
    label4446val = tk.Label(frame442, text=f"{cost_output_dict['C_CERT']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4446val.grid(row=11, column=1, sticky="w")
    label4447val = tk.Label(frame442, text=f"{cost_output_dict['gear_val']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4447val.grid(row=12, column=1, sticky="w")
    label4448val = tk.Label(frame442, text=f"{cost_output_dict['avionics']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4448val.grid(row=13, column=1, sticky="w")
    label4449val = tk.Label(frame442, text=f"{cost_output_dict['C_PP']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4449val.grid(row=14, column=1, sticky="w")
    label4450val = tk.Label(frame442, text=f"{cost_output_dict['C_prop']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4450val.grid(row=15, column=1, sticky="w")
    label4451val = tk.Label(frame442, text=f"{cost_output_dict['N_ENG']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4451val.grid(row=16, column=1, sticky="w")
    label4452val = tk.Label(frame442, text=f"{cost_output_dict['t_AC']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4452val.grid(row=17, column=1, sticky="w")
    label4453val = tk.Label(frame442, text=f"{cost_output_dict['N_BE']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4453val.grid(row=18, column=1, sticky="w")
    label4454val = tk.Label(frame442, text=f"{cost_output_dict['unit_variable_cost']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4454val.grid(row=19, column=1, sticky="w")
    label4455val = tk.Label(frame442, text=f"{cost_output_dict['min_unit_sales_price']:,}", anchor="e", width=elw+4, borderwidth=1, relief="sunken")
    label4455val.grid(row=20, column=1, sticky="w")
    
    # Atmosphere    
    label14rho = tk.Label(frame7, text=str( round(rho,ndigits=4) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label14rho.grid(row=0, column=1, sticky="w")
    label14T = tk.Label(frame7, text=str( round(T-273.15,ndigits=1) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label14T.grid(row=1, column=1, sticky="w")
    label14p = tk.Label(frame7, text=str( round(0.001*p,ndigits=3) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label14p.grid(row=2, column=1, sticky="w")
    label14mu = tk.Label(frame7, text=str( round(1000000*mu,ndigits=2) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label14mu.grid(row=3, column=1, sticky="w")
    label14a = tk.Label(frame7, text=str( round(a,ndigits=2) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label14a.grid(row=4, column=1, sticky="w")
    
    # Aerodynamics
    label13q = tk.Label(frame9, text=str( round(q,ndigits=1) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label13q.grid(row=0, column=1, sticky="w")
    label13Ma = tk.Label(frame9, text=str( round(V/a,ndigits=2) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label13Ma.grid(row=1, column=1, sticky="w")
    label15 = tk.Label(frame9, text=str( round(e,ndigits=4) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label15.grid(row=2, column=1, sticky="w")
    label16 = tk.Label(frame9, text=str( round(k,ndigits=4) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label16.grid(row=3, column=1, sticky="w")
    
    showplotf()
    print('Done')

def saveload(whattodo):
    if whattodo == 'new':
        entry1.delete(0,99),    entry2.delete(0,99),    entry3.delete(0,99)
        entry4.delete(0,99),    entry5.delete(0,99),    entry6.delete(0,99)
        entry7.delete(0,99),    entry8.delete(0,99),    entry9.delete(0,99)
        entry10.delete(0,99),   entry11.delete(0,99),   entry12.delete(0,99)
        entry13.delete(0,99),   entry14.delete(0,99),   entry15.delete(0,99)
        entry16.delete(0,99),   entry17.delete(0,99),   entry18.delete(0,99)
        entry52.delete(0,99),   entry51.delete(0,99),
        ws_range_from.delete(0,99),
        ws_range_to.delete(0,99),
        entry4411val.delete(0,99),  entry4412val.delete(0,99),  entry4414val.delete(0,99),
        entry4415val.delete(0,99),  entry4416val.delete(0,99),  entry4417val.delete(0,99),
        entry4418val.delete(0,99),  entry4419val.delete(0,99),  entry4420val.delete(0,99),
        entry4421val.delete(0,99),  entry4422val.delete(0,99),  entry4423val.delete(0,99),
        entry4429val.delete(0,99),  entry4432val.delete(0,99),  entry4433val.delete(0,99),
        entry4434val.delete(0,99),  entry4438val.delete(0,99),  entry4456val.delete(0,99)
        
        print('Aircraft erased')
    
    elif whattodo == 'new2':
        for item in globals():
            if item.startswith('entry') == True:
                item.delete(0,99)
    
    elif whattodo == 'saveas':
        global filename1
        filename1 = menu_functions.option_saveas(savelist)
        return filename1
    elif whattodo == 'save':
        try:
            menu_functions.option_save(savelist,filename1)
        except NameError:
            saveload('saveas')
    elif whattodo == 'load':
        load_list ,filename1 = menu_functions.option_load()
        saveload('new')
        entry1.insert(tk.END, load_list[1])
        entry2.insert(tk.END, load_list[2])
        entry3.insert(tk.END, load_list[3])
        entry4.insert(tk.END, load_list[4])
        entry5.insert(tk.END, load_list[5])
        entry6.insert(tk.END, load_list[6])
        entry7.insert(tk.END, load_list[7])
        entry8.insert(tk.END, load_list[8])
        entry9.insert(tk.END, load_list[9])
        entry10.insert(tk.END, load_list[10])
        entry11.insert(tk.END, load_list[11])
        entry12.insert(tk.END, load_list[12])
        entry13.insert(tk.END, load_list[13])
        entry14.insert(tk.END, load_list[14])
        entry15.insert(tk.END, load_list[15])
        entry16.insert(tk.END, load_list[16])
        entry17.insert(tk.END, load_list[17])
        entry18.insert(tk.END, load_list[18])
        entry52.insert(tk.END, load_list[19])
        entry51.insert(tk.END, load_list[20])
        ws_range_from.insert(tk.END, load_list[21])
        ws_range_to.insert(tk.END, load_list[22])
        r1.set(int(load_list[23]))
        r2.set(int(load_list[24]))
        r3.set(int(load_list[25]))
        entry4411val.insert(tk.END, load_list[26])
        entry4412val.insert(tk.END, str(int(load_list[27])))
        entry4414val.insert(tk.END, load_list[28])
        entry4415val.insert(tk.END, load_list[29])
        entry4416val.insert(tk.END, load_list[30])
        entry4417val.insert(tk.END, load_list[31])
        entry4418val.insert(tk.END, load_list[32])
        entry4419val.insert(tk.END, load_list[33])
        entry4420val.insert(tk.END, load_list[34])
        entry4421val.insert(tk.END, load_list[35])
        entry4422val.insert(tk.END, load_list[36])
        entry4423val.insert(tk.END, load_list[37])
        entry4429val.insert(tk.END, load_list[38])
        entry4432val.insert(tk.END, load_list[39])
        entry4433val.insert(tk.END, load_list[40])
        entry4434val.insert(tk.END, load_list[41])
        cbox_certificate.set(load_list[42])
        cbox_flap.set(load_list[43])
        cbox_gear.set(load_list[44])
        if load_list[45] == 'no':
            chkbtn_pressurized.deselect()
        elif load_list[45] == 'yes':
            chkbtn_pressurized.select()
        if load_list[46] == 'no':
            chkbtn_tapered.deselect()
        elif load_list[46] == 'yes':
            chkbtn_tapered.select()
        cbox_engine_type.set(load_list[47])
        cbox_prop_type.set(load_list[48])
        entry4438val.insert(tk.END, load_list[49])
        entry4456val.insert(tk.END, load_list[50])
        
        
        
        altitudeunits(r2.get())
        velocityunits(r3.get())
        print('Aircraft loaded')
#%% 04 GUI
#------------------ 04.01 Define root ------------------#
root = tk.Tk()
root.title("root")
rootWidth = 1400
rootHeight = 800
root.geometry(str(rootWidth) + 'x' + str(rootHeight))
elw = 8 # Entry Label Width

#------------------ 04.02 Menu bar ------------------#
menubar1 = tk.Menu(root)
file_menu = tk.Menu(menubar1, tearoff=0)
menubar1.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=lambda: saveload('new'))
file_menu.add_command(label='Save', command=lambda: saveload('save'))
file_menu.add_command(label='Save As...', command=lambda: saveload('saveas'))
file_menu.add_command(label='Load', command=lambda: saveload('load'))
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)

help_menu = tk.Menu(menubar1, tearoff=0)
menubar1.add_cascade(label='About', menu=help_menu)
help_menu.add_command(label='About...', command=menu_functions.option_about)
root.config(menu=menubar1)

#------------------ 04.03 Define Tabs ------------------#
notebook1 = ttk.Notebook(root)
tab1 = ttk.Frame(notebook1)
tab2 = ttk.Frame(notebook1)
tab99 = ttk.Frame(notebook1)
notebook1.add(tab1, text='Cost')
notebook1.add(tab2, text='Sizing')
notebook1.add(tab99, text='Geometry')
notebook1.pack()
notebook1.select(tab2) # default shown tab
notebook1.enable_traversal() # enables Ctrl+Tab navigation


#%%

#------------------ 04.04 Tab1-Cost ------------------#
#------------------ 04.04.01 Frame441 ------------------#
frame441 = tk.LabelFrame(tab1,text='Cost estimate inputs', width=rootWidth/4, height=rootHeight/2)
frame441.pack(side=tk.LEFT)
frame441.pack_propagate(1)
#------------------ 04.04.01.01 Labels ------------------#
label4411 = tk.Label(frame441, text='F_EXP')
label4411.grid(row=0, column=0, sticky="w")
entry4411val = tk.Entry(frame441, width=elw+2)
entry4411val.insert(tk.END, '0.95')
entry4411val.grid(row=0, column=1, sticky="w")
label4411expl = tk.Label(frame441, text='Experience effectiveness (0.01 Max exp, 0.99 Min exp)')
label4411expl.grid(row=0, column=3, sticky="w")

label4412 = tk.Label(frame441, text='N_units')
label4412.grid(row=1, column=0, sticky="w")
entry4412val = tk.Entry(frame441, width=elw+2)
entry4412val.insert(tk.END, '1000')
entry4412val.grid(row=1, column=1, sticky="w")
label4412expl = tk.Label(frame441, text='Number of units produced')
label4412expl.grid(row=1, column=3, sticky="w")

label4414 = tk.Label(frame441, text='W_airframe')
label4414.grid(row=3, column=0, sticky="w")
entry4414val = tk.Entry(frame441, width=elw+2)
entry4414val.insert(tk.END, '4892.8') # 1100*4.448
entry4414val.grid(row=3, column=1, sticky="w")
label4414unit = tk.Label(frame441, text='[N]')
label4414unit.grid(row=3, column=2, sticky="w")
label4414expl = tk.Label(frame441, text='Airframe Weight (if unknown, assume 65% MTOW)')
label4414expl.grid(row=3, column=3, sticky="w")

label4415 = tk.Label(frame441, text='yrs')
label4415.grid(row=4, column=0, sticky="w")
entry4415val = tk.Entry(frame441, width=elw+2)
entry4415val.insert(tk.END, '5')
entry4415val.grid(row=4, column=1, sticky="w")
label4415unit = tk.Label(frame441, text='[years]')
label4415unit.grid(row=4, column=2, sticky="w")
label4415expl = tk.Label(frame441, text='Total time to produce N units')
label4415expl.grid(row=4, column=3, sticky="w")

label4416 = tk.Label(frame441, text='f_comp')
label4416.grid(row=5, column=0, sticky="w")
entry4416val = tk.Entry(frame441, width=elw+2)
entry4416val.insert(tk.END, '1.0')
entry4416val.grid(row=5, column=1, sticky="w")
label4416expl = tk.Label(frame441, text='Fraction of airframe made from composites (0=no composites, 1=full composite)')
label4416expl.grid(row=5, column=3, sticky="w")

label4417 = tk.Label(frame441, text='unit_sales_price')
label4417.grid(row=6, column=0, sticky="w")
entry4417val = tk.Entry(frame441, width=elw+2)
entry4417val.insert(tk.END, '344588.45')
entry4417val.grid(row=6, column=1, sticky="w")
label4417unit = tk.Label(frame441, text='€')
label4417unit.grid(row=6, column=2, sticky="w")
label4417expl = tk.Label(frame441, text='How much would you sell your aircraft for?')
label4417expl.grid(row=6, column=3, sticky="w")

label4418 = tk.Label(frame441, text='N_P')
label4418.grid(row=7, column=0, sticky="w")
entry4418val = tk.Entry(frame441, width=elw+2)
entry4418val.insert(tk.END, '4')
entry4418val.grid(row=7, column=1, sticky="w")
label4418expl = tk.Label(frame441, text='Number of prototypes')
label4418expl.grid(row=7, column=3, sticky="w")

label4419 = tk.Label(frame441, text='R_ENG')
label4419.grid(row=8, column=0, sticky="w")
entry4419val = tk.Entry(frame441, width=elw+2)
entry4419val.insert(tk.END, '77.53')
entry4419val.grid(row=8, column=1, sticky="w")
label4419unit = tk.Label(frame441, text='€')
label4419unit.grid(row=8, column=2, sticky="w")
label4419expl = tk.Label(frame441, text='Rate of engineering labor in €/h (e.g. €77/h)')
label4419expl.grid(row=8, column=3, sticky="w")

label4420 = tk.Label(frame441, text='R_TOOL')
label4420.grid(row=9, column=0, sticky="w")
entry4420val = tk.Entry(frame441, width=elw+2)
entry4420val.insert(tk.END, '51.69')
entry4420val.grid(row=9, column=1, sticky="w")
label4420unit = tk.Label(frame441, text='€')
label4420unit.grid(row=9, column=2, sticky="w")
label4420expl = tk.Label(frame441, text='Rate of tooling labor in €/h (e.g. €52/h)')
label4420expl.grid(row=9, column=3, sticky="w")

label4421 = tk.Label(frame441, text='R_MFG')
label4421.grid(row=10, column=0, sticky="w")
entry4421val = tk.Entry(frame441, width=elw+2)
entry4421val.insert(tk.END, '43.07')
entry4421val.grid(row=10, column=1, sticky="w")
label4421unit = tk.Label(frame441, text='€')
label4421unit.grid(row=10, column=2, sticky="w")
label4421expl = tk.Label(frame441, text='Rate of amnufacturing labor in €/h (e.g. €43/h)')
label4421expl.grid(row=10, column=3, sticky="w")

label4422 = tk.Label(frame441, text='N_PP')
label4422.grid(row=11, column=0, sticky="w")
entry4422val = tk.Entry(frame441, width=elw+2)
entry4422val.insert(tk.END, '1')
entry4422val.grid(row=11, column=1, sticky="w")
label4422expl = tk.Label(frame441, text='Number of powerplants')
label4422expl.grid(row=11, column=3, sticky="w")

label4423 = tk.Label(frame441, text='Insurance')
label4423.grid(row=12, column=0, sticky="w")
entry4423val = tk.Entry(frame441, width=elw+2)
entry4423val.insert(tk.END, '43073.56')
entry4423val.grid(row=12, column=1, sticky="w")
label4423unit = tk.Label(frame441, text='€')
label4423unit.grid(row=12, column=2, sticky="w")
label4423expl = tk.Label(frame441, text='Manufacturers liability insurance')
label4423expl.grid(row=12, column=3, sticky="w")

label4424 = tk.Label(frame441, text='Certificate type')
label4424.grid(row=13, column=0, sticky="w")
options_certificate = ['EASA', 'FAA']
cbox_certificate = tk.ttk.Combobox(frame441,values=options_certificate,width=elw+2)
cbox_certificate.set('EASA')
cbox_certificate.grid(row=13, column=1, sticky="w"+"e", columnspan=2)

label4425 = tk.Label(frame441, text='Flap type')
label4425.grid(row=14, column=0, sticky="w")
options_flap = ['simple', 'complex']
cbox_flap = tk.ttk.Combobox(frame441,values=options_flap,width=elw+2)
cbox_flap.set('simple')
cbox_flap.grid(row=14, column=1, sticky="w"+"e", columnspan=2)

label4426 = tk.Label(frame441, text='Landing gear type')
label4426.grid(row=15, column=0, sticky="w")
options_gear = ['fixed', 'retractable']
cbox_gear = tk.ttk.Combobox(frame441,values=options_gear,width=elw+2)
cbox_gear.set('fixed')
cbox_gear.grid(row=15, column=1, sticky="w"+"e", columnspan=2)

label4427 = tk.Label(frame441, text='Pressurized cabin')
label4427.grid(row=16, column=0, sticky="w")
var_pressurized = tk.StringVar()
chkbtn_pressurized = tk.Checkbutton(frame441, variable=var_pressurized, onvalue='yes', offvalue='no')
chkbtn_pressurized.deselect()
chkbtn_pressurized.grid(row=16, column=1, sticky="w")
label4427expl = tk.Label(frame441, text='Used for cost estimation purpose only')
label4427expl.grid(row=16, column=3, sticky="w")

label4428 = tk.Label(frame441, text='Tapered wing')
label4428.grid(row=17, column=0, sticky="w")
var_tapered = tk.StringVar()
chkbtn_tapered = tk.Checkbutton(frame441, variable=var_tapered, onvalue='yes', offvalue='no')
chkbtn_tapered.deselect()
chkbtn_tapered.grid(row=17, column=1, sticky="w")
label4428expl = tk.Label(frame441, text='Used for cost estimation purpose only')
label4428expl.grid(row=17, column=3, sticky="w")

label4429 = tk.Label(frame441, text='D_P')
label4429.grid(row=18, column=0, sticky="w")
entry4429val = tk.Entry(frame441, width=elw+2)
entry4429val.insert(tk.END, '1.9812')
entry4429val.grid(row=18, column=1, sticky="w")
label4429unit = tk.Label(frame441, text='[m]')
label4429unit.grid(row=18, column=2, sticky="w")
label4429expl = tk.Label(frame441, text='Propeller diameter')
label4429expl.grid(row=18, column=3, sticky="w")

def engine_type_changed(event):
    global label4438, label4438unit, label4438expl, entry4438val
    label4438.destroy()
    label4438unit.destroy()
    label4438expl.destroy()
    if cbox_engine_type.get() == 'Piston':
        lab = 'label4438-P_BHP'
        unit = '[BHP]'
        expl = 'Piston Brake HP'
    elif cbox_engine_type.get() == 'Turboprop':
        lab = 'label4438-P_SHP'
        unit = '[SHP]'
        expl = 'Turboprop Shaft HP'
    elif cbox_engine_type.get() == 'Turbofan':
        lab = 'label4438-Thr'
        unit = '[lbf]'
        expl = 'Turbofan Thrust'
    elif cbox_engine_type.get() == 'Turbojet':
        lab = 'label4438-Thr'
        unit = '[lbf]'
        expl = 'Turbojet Thrust'
    elif cbox_engine_type.get() == 'No engine':
        lab = 'Engine NA'
        unit = '[NA]'
        expl = 'NA'
    label4438 = tk.Label(frame441, text=lab)
    label4438.grid(row=20, column=0, sticky="w")
    entry4438val = tk.Entry(frame441, width=elw+2)
    entry4438val.insert(tk.END, '0')
    entry4438val.grid(row=20, column=1, sticky="w")
    label4438unit = tk.Label(frame441, text=unit)
    label4438unit.grid(row=20, column=2, sticky="w")
    label4438expl = tk.Label(frame441, text=expl)
    label4438expl.grid(row=20, column=3, sticky="w")

label4430 = tk.Label(frame441, text='Engine type')
label4430.grid(row=19, column=0, sticky="w")
options_engine_type = ['Piston', 'Turboprop', 'Turbojet', 'Turbofan', 'No engine']
cbox_engine_type = tk.ttk.Combobox(frame441,values=options_engine_type,width=elw+2)
cbox_engine_type.set('No engine')
cbox_engine_type.grid(row=19, column=1, sticky="w"+"e", columnspan=2)
cbox_engine_type.bind('<<ComboboxSelected>>', engine_type_changed)

label4438 = tk.Label(frame441, text='Engine N/A')
label4438.grid(row=20, column=0, sticky="w")
entry4438val = tk.Entry(frame441, width=elw+2)
entry4438val.insert(tk.END, '0')
entry4438val.grid(row=20, column=1, sticky="w")
label4438unit = tk.Label(frame441, text='[N/A]')
label4438unit.grid(row=20, column=2, sticky="w")
label4438expl = tk.Label(frame441, text='N/A')
label4438expl.grid(row=20, column=3, sticky="w")

label4431 = tk.Label(frame441, text='Propeller type')
label4431.grid(row=21, column=0, sticky="w")
options_prop_type = ['Fixed pitch', 'Constant speed', 'No propeller']
cbox_prop_type = tk.ttk.Combobox(frame441,values=options_prop_type,width=elw+2)
cbox_prop_type.set('Constant speed')
cbox_prop_type.grid(row=21, column=1, sticky="w"+"e", columnspan=2, )

label4432 = tk.Label(frame441, text='n_wwpy')
label4432.grid(row=22, column=0, sticky="w")
entry4432val = tk.Entry(frame441, width=elw+2)
entry4432val.insert(tk.END, '48')
entry4432val.grid(row=22, column=1, sticky="w")
label4432unit = tk.Label(frame441, text='[wk/y]')
label4432unit.grid(row=22, column=2, sticky="w")
label4432expl = tk.Label(frame441, text='Number of work weeks per year')
label4432expl.grid(row=22, column=3, sticky="w")

label4433 = tk.Label(frame441, text='n_whpw')
label4433.grid(row=23, column=0, sticky="w")
entry4433val = tk.Entry(frame441, width=elw+2)
entry4433val.insert(tk.END, '40')
entry4433val.grid(row=23, column=1, sticky="w")
label4433unit = tk.Label(frame441, text='[h/wk]')
label4433unit.grid(row=23, column=2, sticky="w")
label4433expl = tk.Label(frame441, text='Number of work hours per week')
label4433expl.grid(row=23, column=3, sticky="w")

label4434 = tk.Label(frame441, text='CPI2021')
label4434.grid(row=24, column=0, sticky="w")
entry4434val = tk.Entry(frame441, width=elw+2)
entry4434val.insert(tk.END, '2.496049')  # 2.0969 for 2012
entry4434val.grid(row=24, column=1, sticky="w")
label4434expl = tk.Label(frame441, text='Consumer Price Index for 2021 relative to 1986')
label4434expl.grid(row=24, column=3, sticky="w")

label4456 = tk.Label(frame441, text='usdeur')
label4456.grid(row=25, column=0, sticky="w")
entry4456val = tk.Entry(frame441, width=elw+2)
entry4456val.insert(tk.END, '1.1608')
entry4456val.grid(row=25, column=1, sticky="w")
label4456expl = tk.Label(frame441, text='[USD/EUR] exch. rate - Manual input')
label4456expl.grid(row=25, column=3, sticky="w")

#------------------ 04.04.02 Frame442 ------------------#
frame442 = tk.LabelFrame(tab1,text='Statistical cost results', width=rootWidth/4, height=rootHeight/2)
frame442.pack(side=tk.LEFT)
frame442.pack_propagate(1)
#------------------ 04.04.01.02 Labels ------------------#

label4413 = tk.Label(frame442, text='QDF')
label4413.grid(row=0, column=0, sticky="w")
label4413val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4413val.grid(row=0, column=1, sticky="w")
label4413expl = tk.Label(frame442, text='Quantity Discount Factor')
label4413expl.grid(row=0, column=3, sticky="w")

label4435 = tk.Label(frame442, text='H_ENG')
label4435.grid(row=1, column=0, sticky="w")
label4435val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4435val.grid(row=1, column=1, sticky="w")
label4435unit = tk.Label(frame442, text='[h]')
label4435unit.grid(row=1, column=2, sticky="w")
label4435expl = tk.Label(frame442, text='Engineering manhours')
label4435expl.grid(row=1, column=3, sticky="w")

label4436 = tk.Label(frame442, text='H_TOOL')
label4436.grid(row=2, column=0, sticky="w")
label4436val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4436val.grid(row=2, column=1, sticky="w")
label4436unit = tk.Label(frame442, text='[h]')
label4436unit.grid(row=2, column=2, sticky="w")
label4436expl = tk.Label(frame442, text='Tooling manhours')
label4436expl.grid(row=2, column=3, sticky="w")

label4437 = tk.Label(frame442, text='H_MFG')
label4437.grid(row=3, column=0, sticky="w")
label4437val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4437val.grid(row=3, column=1, sticky="w")
label4437unit = tk.Label(frame442, text='[h]')
label4437unit.grid(row=3, column=2, sticky="w")
label4437expl = tk.Label(frame442, text='Manufacturing manhours')
label4437expl.grid(row=3, column=3, sticky="w")

label4439 = tk.Label(frame442, text='C_ENG')
label4439.grid(row=4, column=0, sticky="w")
label4439val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4439val.grid(row=4, column=1, sticky="w")
label4439unit = tk.Label(frame442, text='[EUR]')
label4439unit.grid(row=4, column=2, sticky="w")
label4439expl = tk.Label(frame442, text='Cost of engineering')
label4439expl.grid(row=4, column=3, sticky="w")

label4440 = tk.Label(frame442, text='C_DEV')
label4440.grid(row=5, column=0, sticky="w")
label4440val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4440val.grid(row=5, column=1, sticky="w")
label4440unit = tk.Label(frame442, text='[EUR]')
label4440unit.grid(row=5, column=2, sticky="w")
label4440expl = tk.Label(frame442, text='Cost of development support')
label4440expl.grid(row=5, column=3, sticky="w")

label4441 = tk.Label(frame442, text='C_FT')
label4441.grid(row=6, column=0, sticky="w")
label4441val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4441val.grid(row=6, column=1, sticky="w")
label4441unit = tk.Label(frame442, text='[EUR]')
label4441unit.grid(row=6, column=2, sticky="w")
label4441expl = tk.Label(frame442, text='Cost of flight test')
label4441expl.grid(row=6, column=3, sticky="w")

label4442 = tk.Label(frame442, text='C_TOOL')
label4442.grid(row=7, column=0, sticky="w")
label4442val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4442val.grid(row=7, column=1, sticky="w")
label4442unit = tk.Label(frame442, text='[EUR]')
label4442unit.grid(row=7, column=2, sticky="w")
label4442expl = tk.Label(frame442, text='Cost of tooling')
label4442expl.grid(row=7, column=3, sticky="w")

label4443 = tk.Label(frame442, text='C_MFG')
label4443.grid(row=8, column=0, sticky="w")
label4443val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4443val.grid(row=8, column=1, sticky="w")
label4443unit = tk.Label(frame442, text='[EUR]')
label4443unit.grid(row=8, column=2, sticky="w")
label4443expl = tk.Label(frame442, text='Cost of manufacturing')
label4443expl.grid(row=8, column=3, sticky="w")

label4444 = tk.Label(frame442, text='C_QC')
label4444.grid(row=9, column=0, sticky="w")
label4444val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4444val.grid(row=9, column=1, sticky="w")
label4444unit = tk.Label(frame442, text='[EUR]')
label4444unit.grid(row=9, column=2, sticky="w")
label4444expl = tk.Label(frame442, text='Cost of quality control')
label4444expl.grid(row=9, column=3, sticky="w")

label4445 = tk.Label(frame442, text='C_MAT')
label4445.grid(row=10, column=0, sticky="w")
label4445val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4445val.grid(row=10, column=1, sticky="w")
label4445unit = tk.Label(frame442, text='[EUR]')
label4445unit.grid(row=10, column=2, sticky="w")
label4445expl = tk.Label(frame442, text='Cost of materials')
label4445expl.grid(row=10, column=3, sticky="w")

label4446 = tk.Label(frame442, text='C_CERT')
label4446.grid(row=11, column=0, sticky="w")
label4446val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4446val.grid(row=11, column=1, sticky="w")
label4446unit = tk.Label(frame442, text='[EUR]')
label4446unit.grid(row=11, column=2, sticky="w")
label4446expl = tk.Label(frame442, text='Cost to certify')
label4446expl.grid(row=11, column=3, sticky="w")

label4447 = tk.Label(frame442, text='gear_val')
label4447.grid(row=12, column=0, sticky="w")
label4447val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4447val.grid(row=12, column=1, sticky="w")
label4447unit = tk.Label(frame442, text='[EUR]')
label4447unit.grid(row=12, column=2, sticky="w")
label4447expl = tk.Label(frame442, text='Deduct for landing gear')
label4447expl.grid(row=12, column=3, sticky="w")

label4448 = tk.Label(frame442, text='avionics')
label4448.grid(row=13, column=0, sticky="w")
label4448val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4448val.grid(row=13, column=1, sticky="w")
label4448unit = tk.Label(frame442, text='[EUR]')
label4448unit.grid(row=13, column=2, sticky="w")
label4448expl = tk.Label(frame442, text='Cost of avionics')
label4448expl.grid(row=13, column=3, sticky="w")

label4449 = tk.Label(frame442, text='C_PP')
label4449.grid(row=14, column=0, sticky="w")
label4449val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4449val.grid(row=14, column=1, sticky="w")
label4449unit = tk.Label(frame442, text='[EUR]')
label4449unit.grid(row=14, column=2, sticky="w")
label4449expl = tk.Label(frame442, text='Cost of powerplant(s)')
label4449expl.grid(row=14, column=3, sticky="w")

label4450 = tk.Label(frame442, text='C_prop')
label4450.grid(row=15, column=0, sticky="w")
label4450val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4450val.grid(row=15, column=1, sticky="w")
label4450unit = tk.Label(frame442, text='[EUR]')
label4450unit.grid(row=15, column=2, sticky="w")
label4450expl = tk.Label(frame442, text='Cost of propeller(s) - piston/turboprop only')
label4450expl.grid(row=15, column=3, sticky="w")

label4451 = tk.Label(frame442, text='N_ENG')
label4451.grid(row=16, column=0, sticky="w")
label4451val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4451val.grid(row=16, column=1, sticky="w")
label4451unit = tk.Label(frame442, text='[-]')
label4451unit.grid(row=16, column=2, sticky="w")
label4451expl = tk.Label(frame442, text='Number of engineers (for 60% yrs)')
label4451expl.grid(row=16, column=3, sticky="w")

label4452 = tk.Label(frame442, text='t_AC')
label4452.grid(row=17, column=0, sticky="w")
label4452val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4452val.grid(row=17, column=1, sticky="w")
label4452unit = tk.Label(frame442, text='[h]')
label4452unit.grid(row=17, column=2, sticky="w")
label4452expl = tk.Label(frame442, text='Time to manufacture single unit')
label4452expl.grid(row=17, column=3, sticky="w")

label4453 = tk.Label(frame442, text='N_BE')
label4453.grid(row=18, column=0, sticky="w")
label4453val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4453val.grid(row=18, column=1, sticky="w")
label4453unit = tk.Label(frame442, text='[-]')
label4453unit.grid(row=18, column=2, sticky="w")
label4453expl = tk.Label(frame442, text='No. of sold units to break even')
label4453expl.grid(row=18, column=3, sticky="w")

label4454 = tk.Label(frame442, text=' ')
label4454.grid(row=19, column=0, sticky="w")
label4454val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4454val.grid(row=19, column=1, sticky="w")
label4454unit = tk.Label(frame442, text='[-]')
label4454unit.grid(row=19, column=2, sticky="w")
label4454expl = tk.Label(frame442, text='Statistical minimal price')
label4454expl.grid(row=19, column=3, sticky="w")

label4455 = tk.Label(frame442, text=' ')
label4455.grid(row=20, column=0, sticky="w")
label4455val = tk.Label(frame442, text='', width=elw+4, borderwidth=1, relief="sunken")
label4455val.grid(row=20, column=1, sticky="w")
label4455unit = tk.Label(frame442, text='[-]')
label4455unit.grid(row=20, column=2, sticky="w")
label4455expl = tk.Label(frame442, text='Recommended minimal price (20% more) (only for N_BE)')
label4455expl.grid(row=20, column=3, sticky="w")

#------------------ Frames ------------------#
frame1Width = rootWidth/2
frame1Height = rootHeight/1
frame1 = tk.LabelFrame(tab2, text='Flight Parameters', width=frame1Width, height=frame1Height, padx=10, pady=5)
frame1.pack(side=tk.LEFT)
frame1.pack_propagate(0)


frame2Width = rootWidth/2
frame2Height = rootHeight/1.135
frame2 = tk.LabelFrame(tab2,text='frame2', relief=tk.GROOVE, borderwidth=2, width=frame2Width, height=frame2Height)
frame2.pack()
frame2.pack(side=tk.LEFT)
frame2.pack_propagate(0)

rell = 'groove' # default = groove

frame3 = tk.LabelFrame(frame1, text="Base inputs", relief=rell, padx=10, pady=5)
frame3.grid(row=0,column=0, rowspan=2, sticky='nw')

frame8 = tk.LabelFrame(frame1, text="Units", relief=rell, padx=10, pady=5)
frame8.grid(row=0,column=1, sticky="nw")

frame4 = tk.LabelFrame(frame1, text="Sizing diagram type", relief=rell, padx=10, pady=5)
frame4.grid(row=0,column=2,sticky="nw")

frame5 = tk.LabelFrame(frame1, text="DesignPoint", relief=rell, padx=10, pady=5)
frame5.grid(row=1,column=1, columnspan=2, sticky="sw")

frame7 = tk.LabelFrame(frame1, text="Atmosphere", relief=rell, padx=10, pady=5)
frame7.grid(row=2,column=0, sticky="nw")

frame9 = tk.LabelFrame(frame1, text="Aerodynamic", relief=rell, padx=10, pady=5)
frame9.grid(row=2,column=1, columnspan=2, sticky="nw")

frame6 = tk.Frame(frame1,relief='flat')
frame6.grid(row=9,column=9)

#---------------------------- INPUTS ----------------------------#
## ROW 0
# label
label1 = tk.Label(frame3, text='alt')
label1.grid(row=0, column=0, sticky="w")
entry1 = tk.Entry(frame3, width=elw)
entry1.insert(tk.END, '2438.4')
entry1.grid(row=0, column=1)
label5 = tk.Label(frame3, text='[m]')
label5.grid(row=0, column=2, sticky="w")
label1expl = tk.Label(frame3, text='Altitude')
label1expl.grid(row=0, column=3, sticky="w")

## ROW 1
label2 = tk.Label(frame3, text='V')
label2.grid(row=1, column=0, sticky="w")
entry2 = tk.Entry(frame3, width=elw)
entry2.insert(tk.END, '77.16')
entry2.grid(row=1, column=1)
label6 = tk.Label(frame3, text='[m/s]')
label6.grid(row=1, column=2, sticky="w")
label2expl = tk.Label(frame3, text='Velocity (TAS)')
label2expl.grid(row=1, column=3, sticky="w")
# FONTn = 'Helvetica'
# FONTs = 9
# FONTt = 'regular'
## ROW 2
label3 = tk.Label(frame3, text='MTOM')
label3.grid(row=2, column=0, sticky="w")
entry3 = tk.Entry(frame3, width=elw)
entry3.insert(tk.END, '907')
entry3.grid(row=2, column=1)
label7 = tk.Label(frame3, text='[kg]')
label7.grid(row=2, column=2, sticky="w")
label3expl = tk.Label(frame3, text='Maximum Take-Off Mass')
label3expl.grid(row=2, column=3, sticky="w")

## ROW 3
label4 = tk.Label(frame3, text='AR')
label4.grid(row=3, column=0, sticky="w")
entry4 = tk.Entry(frame3, width=elw)
entry4.insert(tk.END, '9')
entry4.grid(row=3, column=1)
label8 = tk.Label(frame3, text='[-]')
label8.grid(row=3, column=2, sticky="w")
label4expl = tk.Label(frame3, text='Aspect Ratio')
label4expl.grid(row=3, column=3, sticky="w")

## ROW 4
label21 = tk.Label(frame3, text='C_Dmin')
label21.grid(row=4, column=0, sticky="w")
entry5 = tk.Entry(frame3, width=elw)
entry5.insert(tk.END, '0.025')
entry5.grid(row=4, column=1)
label22 = tk.Label(frame3, text='[-]')
label22.grid(row=4, column=2, sticky="w")
label21expl = tk.Label(frame3, text='Zero-lift drag')
label21expl.grid(row=4, column=3, sticky="w")

## ROW 5
label23 = tk.Label(frame3, text='n')
label23.grid(row=5, column=0, sticky="w")
entry6 = tk.Entry(frame3, width=elw)
entry6.insert(tk.END, '2.00')
entry6.grid(row=5, column=1)
label24 = tk.Label(frame3, text='[gee]')
label24.grid(row=5, column=2, sticky="w")
label23expl = tk.Label(frame3, text='Load factor')
label23expl.grid(row=5, column=3, sticky="w")

## ROW 6
label25 = tk.Label(frame3, text='P_S')
label25.grid(row=6, column=0, sticky="w")
entry7 = tk.Entry(frame3, width=elw)
entry7.insert(tk.END, '6.10') # Condition specific energy at sustained turn | 6.10m/s = 20ft/s
entry7.grid(row=6, column=1)
label26 = tk.Label(frame3, text='[m/s]')
label26.grid(row=6, column=2, sticky="w")
label25expl = tk.Label(frame3, text='Climb excess power (unused)')
label25expl.grid(row=6, column=3, sticky="w")

## ROW 7
label27 = tk.Label(frame3, text='V_v')
label27.grid(row=7, column=0, sticky="w")
entry8 = tk.Entry(frame3, width=elw)
entry8.insert(tk.END, '7.62') # Vertical velocity for climb | 7.62m/s = 1000ft/min
entry8.grid(row=7, column=1)
label28 = tk.Label(frame3, text='[m/s]')
label28.grid(row=7, column=2, sticky="w")
label27expl = tk.Label(frame3, text='Vertical velocity')
label27expl.grid(row=7, column=3, sticky="w")

## ROW 8
label29 = tk.Label(frame3, text='C_DTO')
label29.grid(row=8, column=0, sticky="w")
entry9 = tk.Entry(frame3, width=elw)
entry9.insert(tk.END, '0.04') # Drag coefficients at take-off
entry9.grid(row=8, column=1)
label30 = tk.Label(frame3, text='[-]')
label30.grid(row=8, column=2, sticky="w")
label29expl = tk.Label(frame3, text='Take-off drag coefficient')
label29expl.grid(row=8, column=3, sticky="w")

## ROW 9
label31 = tk.Label(frame3, text='C_LTO')
label31.grid(row=9, column=0, sticky="w")
entry10 = tk.Entry(frame3, width=elw)
entry10.insert(tk.END, '0.5') # Lift coefficients at take-off
entry10.grid(row=9, column=1)
label32 = tk.Label(frame3, text='[-]')
label32.grid(row=9, column=2, sticky="w")
label31expl = tk.Label(frame3, text='Take-off lift coefficient')
label31expl.grid(row=9, column=3, sticky="w")

## ROW 10
label33 = tk.Label(frame3, text='S_G')
label33.grid(row=10, column=0, sticky="w")
entry11 = tk.Entry(frame3, width=elw)
entry11.insert(tk.END, '274.32') # groundrun
entry11.grid(row=10, column=1)
label34 = tk.Label(frame3, text='[m]')
label34.grid(row=10, column=2, sticky="w")
label33expl = tk.Label(frame3, text='Ground run')
label33expl.grid(row=10, column=3, sticky="w")

## ROW 11
label35 = tk.Label(frame3, text='mu_gr')
label35.grid(row=11, column=0, sticky="w")
entry12 = tk.Entry(frame3, width=elw)
entry12.insert(tk.END, '0.04') # Ground rolling friction coefficient
entry12.grid(row=11, column=1)
label36 = tk.Label(frame3, text='[-]')
label36.grid(row=11, column=2, sticky="w")
label35expl = tk.Label(frame3, text='Rolling friction coefficient')
label35expl.grid(row=11, column=3, sticky="w")

## ROW 12
label37 = tk.Label(frame3, text='V_LOF')
label37.grid(row=12, column=0, sticky="w")
entry13 = tk.Entry(frame3, width=elw)
entry13.insert(tk.END, '33.436') # Lift-off velocity [m/s] (idk why not "take-off"...)
entry13.grid(row=12, column=1)
label38 = tk.Label(frame3, text='[m/s]')
label38.grid(row=12, column=2, sticky="w")
label37expl = tk.Label(frame3, text='Lift-off velocity, CAS@SL (=TAS)')
label37expl.grid(row=12, column=3, sticky="w")

## ROW 13
label39 = tk.Label(frame3, text='V_vx')
label39.grid(row=13, column=0, sticky="w")
entry14 = tk.Entry(frame3, width=elw)
entry14.insert(tk.END, '41.152')
entry14.grid(row=13, column=1)
label40 = tk.Label(frame3, text='[m/s]')
label40.grid(row=13, column=2, sticky="w")
label39expl = tk.Label(frame3, text='Level-turn horiz velocity, CAS@SL (=TAS)')
label39expl.grid(row=13, column=3, sticky="w")

## ROW 14
label41 = tk.Label(frame3, text='alt_sc')
label41.grid(row=14, column=0, sticky="w")
entry15 = tk.Entry(frame3, width=elw)
entry15.insert(tk.END, '6096')
entry15.grid(row=14, column=1)
label42 = tk.Label(frame3, text='[m]')
label42.grid(row=14, column=2, sticky="w")
label41expl = tk.Label(frame3, text='Service ceiling altitude')
label41expl.grid(row=14, column=3, sticky="w")

## ROW 15
label43 = tk.Label(frame3, text='alt_TO')
label43.grid(row=15, column=0, sticky="w")
entry16 = tk.Entry(frame3, width=elw)
entry16.insert(tk.END, '0')
entry16.grid(row=15, column=1)
label44 = tk.Label(frame3, text='[m]')
label44.grid(row=15, column=2, sticky="w")
label43expl = tk.Label(frame3, text='Take-off altitude')
label43expl.grid(row=15, column=3, sticky="w")

## ROW 16
label45 = tk.Label(frame3, text='V_stall')
label45.grid(row=16, column=0, sticky="w")
entry17 = tk.Entry(frame3, width=elw)
entry17.insert(tk.END, '31.3784')
entry17.grid(row=16, column=1)
label46 = tk.Label(frame3, text='[m/s]')
label46.grid(row=16, column=2, sticky="w")
label45expl = tk.Label(frame3, text='Stall velocity, CAS@SL (=TAS)')
label45expl.grid(row=16, column=3, sticky="w")

## ROW 17
label47 = tk.Label(frame3, text='eta_prop')
label47.grid(row=17, column=0, sticky="w")
entry18 = tk.Entry(frame3, width=elw)
entry18.insert(tk.END, '0.80')
entry18.grid(row=17, column=1)
label48 = tk.Label(frame3, text='[-]')
label48.grid(row=17, column=2, sticky="w")
label47expl = tk.Label(frame3, text='Propeller efficiency')
label47expl.grid(row=17, column=3, sticky="w")

## ROW 51
labelDPTWin = tk.Label(frame5, text='T/W')
labelDPTWin.grid(row=51, column=0, sticky="w")
entry51 = tk.Entry(frame5, width=elw)
entry51.insert(tk.END, '0.135')
entry51.grid(row=51, column=1)
labelDPTWunit = tk.Label(frame5, text='[-]')
labelDPTWunit.grid(row=51, column=2, sticky="w")
labelDPTWinexpl = tk.Label(frame5, text='Thrust-to-weight ratio')
labelDPTWinexpl.grid(row=51, column=3, sticky="w")

## ROW 52
labelDPWSin = tk.Label(frame5, text='W/S')
labelDPWSin.grid(row=52, column=0, sticky="w")
entry52 = tk.Entry(frame5, width=elw)
entry52.insert(tk.END, '1077.3')
entry52.grid(row=52, column=1)
labelDPWSunit = tk.Label(frame5, text='[N/m2]')
labelDPWSunit.grid(row=52, column=2, sticky="w")
labelDPWSinexpl = tk.Label(frame5, text='Wing loading')
labelDPWSinexpl.grid(row=52, column=3, sticky="w")

## ROW 53
labelDPPW = tk.Label(frame5, text='P/W')
labelDPPW.grid(row=53, column=0, sticky="w")
label53 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label53.grid(row=53, column=1, sticky="w")
# entry53 = tk.Entry(frame5, width=elw)
# entry53.insert(tk.END, '0.000')
# entry53.grid(row=53, column=1)
labelDPTWunit = tk.Label(frame5, text='[-]')
labelDPTWunit.grid(row=53, column=2, sticky="w")
labelDPPWexpl = tk.Label(frame5, text='Power-to-weight ratio')
labelDPPWexpl.grid(row=53, column=3, sticky="w")

## ROW 54
labelDPPW = tk.Label(frame5, text='P/W @SL')
labelDPPW.grid(row=54, column=0, sticky="w")
label54 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label54.grid(row=54, column=1, sticky="w")
# entry54 = tk.Entry(frame5, width=elw)
# entry54.insert(tk.END, '0.000')
# entry54.grid(row=54, column=1)
labelDPTWunit = tk.Label(frame5, text='[-]')
labelDPTWunit.grid(row=54, column=2, sticky="w")
labelDPPWexpl = tk.Label(frame5, text='Power-to-weight ratio at sea level')
labelDPPWexpl.grid(row=54, column=3, sticky="w")

## ROW 55
labelDPThr = tk.Label(frame5, text='T')
labelDPThr.grid(row=55, column=0, sticky="w")
label55 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label55.grid(row=55, column=1, sticky="w")
# entry55 = tk.Entry(frame5, width=elw)
# entry55.insert(tk.END, '0')
# entry55.grid(row=55, column=1)
labelDPWSunit = tk.Label(frame5, text='[N]')
labelDPWSunit.grid(row=55, column=2, sticky="w")
labelDPThrexpl = tk.Label(frame5, text='Thrust')
labelDPThrexpl.grid(row=55, column=3, sticky="w")

## ROW 56
labelDPPow = tk.Label(frame5, text='P')
labelDPPow.grid(row=56, column=0, sticky="w")
label56 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label56.grid(row=56, column=1, sticky="w")
# entry56 = tk.Entry(frame5, width=elw)
# entry56.insert(tk.END, '0')
# entry56.grid(row=56, column=1)
labelDPWSunit = tk.Label(frame5, text='[HP]')
labelDPWSunit.grid(row=56, column=2, sticky="w")
labelDPPowexpl = tk.Label(frame5, text='Power')
labelDPPowexpl.grid(row=56, column=3, sticky="w")

## ROW 57
labelDPPowsl = tk.Label(frame5, text='P @SL')
labelDPPowsl.grid(row=57, column=0, sticky="w")
label57 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label57.grid(row=57, column=1, sticky="w")
# entry57 = tk.Entry(frame5, width=elw)
# entry57.insert(tk.END, '0')
# entry57.grid(row=57, column=1)
labelDPPowslunit = tk.Label(frame5, text='[HP]')
labelDPPowslunit.grid(row=57, column=2, sticky="w")
labelDPPowslexpl = tk.Label(frame5, text='Power at sea level')
labelDPPowslexpl.grid(row=57, column=3, sticky="w")

## ROW 58
labelDPS = tk.Label(frame5, text='S_ref')
labelDPS.grid(row=58, column=0, sticky="w")
label58 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label58.grid(row=58, column=1, sticky="w")
# entry58 = tk.Entry(frame5, width=elw)
# entry58.insert(tk.END, '0.0')
# entry58.grid(row=58, column=1)
labelDPSunit = tk.Label(frame5, text='[m2]')
labelDPSunit.grid(row=58, column=2, sticky="w")
labelDPSexpl = tk.Label(frame5, text='Wing surface (reference)')
labelDPSexpl.grid(row=58, column=3, sticky="w")

## ROW 59
labelDPclmax = tk.Label(frame5, text='C_Lmax')
labelDPclmax.grid(row=59, column=0, sticky="w")
label59 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label59.grid(row=59, column=1, sticky="w")
# entry58 = tk.Entry(frame5, width=elw)
# entry58.insert(tk.END, '0.0')
# entry58.grid(row=58, column=1)
labelDPclmaxunit = tk.Label(frame5, text='[-]')
labelDPclmaxunit.grid(row=59, column=2, sticky="w")
labelDPclmaxexpl = tk.Label(frame5, text='Required C_Lmax')
labelDPclmaxexpl.grid(row=59, column=3, sticky="w")

## ROW 59
# samplettxt = tk.Text(frame5, width=5, height=2, borderwidth=0)
# samplettxt.tag_configure("subscript", offset=-4, font=('Calibri',6))
# samplettxt.tag_configure("superscript", offset=6, font=('Calibri',6))
# samplettxt.insert("insert", "H", "", "2", "subscript", "O", "", "2", "superscript")
# samplettxt.grid(row=59,column=0)

#---------------------------- ATMOSPHERE ----------------------------#

## ROW 0
label10rho = tk.Label(frame7, text='ρ')
label10rho.grid(row=0, column=0, sticky="w")
label14rho = tk.Label(frame7, text='', width=elw-1, borderwidth=1, relief="sunken")
label14rho.grid(row=0, column=1, sticky="w")
label18rho = tk.Label(frame7, text='[kg/m3]')
label18rho.grid(row=0, column=2, sticky="w")
label10rhoexpl = tk.Label(frame7, text='Density')
label10rhoexpl.grid(row=0, column=3, sticky="w")

## ROW 1
label10T = tk.Label(frame7, text='T')
label10T.grid(row=1, column=0, sticky="w")
label14T = tk.Label(frame7, text='', width=elw-1, borderwidth=1, relief="sunken")
label14T.grid(row=1, column=1, sticky="w")
label18T = tk.Label(frame7, text='[°C]')
label18T.grid(row=1, column=2, sticky="w")
label10Texpl = tk.Label(frame7, text='Temperature')
label10Texpl.grid(row=1, column=3, sticky="w")

## ROW 2
label10p = tk.Label(frame7, text='p')
label10p.grid(row=2, column=0, sticky="w")
label14p = tk.Label(frame7, text='', width=elw-1, borderwidth=1, relief="sunken")
label14p.grid(row=2, column=1, sticky="w")
label18p = tk.Label(frame7, text='[kPa]')
label18p.grid(row=2, column=2, sticky="w")
label10pexpl = tk.Label(frame7, text='Pressure')
label10pexpl.grid(row=2, column=3, sticky="w")

## ROW 3
label10mu = tk.Label(frame7, text='μ')
label10mu.grid(row=3, column=0, sticky="w")
label14mu = tk.Label(frame7, text='', width=elw-1, borderwidth=1, relief="sunken")
label14mu.grid(row=3, column=1, sticky="w")
label18mu = tk.Label(frame7, text='[μPa s]')
label18mu.grid(row=3, column=2, sticky="w")
label10muexpl = tk.Label(frame7, text='Dynamic viscosity')
label10muexpl.grid(row=3, column=3, sticky="w")

## ROW 4
label10a = tk.Label(frame7, text='a')
label10a.grid(row=4, column=0, sticky="w")
label14a = tk.Label(frame7, text='', width=elw-1, borderwidth=1, relief="sunken")
label14a.grid(row=4, column=1, sticky="w")
label18a = tk.Label(frame7, text='[m/s]')
label18a.grid(row=4, column=2, sticky="w")
label10aexpl = tk.Label(frame7, text='Speed of sound')
label10aexpl.grid(row=4, column=3, sticky="w")

#---------------------------- AERODYNAMICS ----------------------------#
## ROW 0
label9q = tk.Label(frame9, text='q')
label9q.grid(row=0, column=0, sticky="w")
label13q = tk.Label(frame9, text='', width=elw-1, borderwidth=1, relief="sunken")
label13q.grid(row=0, column=1, sticky="w")
label17q = tk.Label(frame9, text='[Pa]')
label17q.grid(row=0, column=2, sticky="w")
label9qexpl = tk.Label(frame9, text='Dynamic pressure')
label9qexpl.grid(row=0, column=3, sticky="w")

## ROW 0
label9Ma = tk.Label(frame9, text='Ma')
label9Ma.grid(row=1, column=0, sticky="w")
label13Ma = tk.Label(frame9, text='', width=elw-1, borderwidth=1, relief="sunken")
label13Ma.grid(row=1, column=1, sticky="w")
label17Ma = tk.Label(frame9, text='[-]')
label17Ma.grid(row=1, column=2, sticky="w")
label9Maexpl = tk.Label(frame9, text='Mach number')
label9Maexpl.grid(row=1, column=3, sticky="w")

## ROW 2
label11 = tk.Label(frame9, text="e")
label11.grid(row=2, column=0, sticky="w")
label15 = tk.Label(frame9, text='', width=elw-1, borderwidth=1, relief="sunken")
label15.grid(row=2, column=1, sticky="w")
label19 = tk.Label(frame9, text='[-]')
label19.grid(row=2, column=2, sticky="w")
label11expl = tk.Label(frame9, text="Oswald's efficiency")
label11expl.grid(row=2, column=3, sticky="w")

## ROW 3
label12 = tk.Label(frame9, text='k')
label12.grid(row=3, column=0, sticky="w")
label16 = tk.Label(frame9, text='', width=elw-1, borderwidth=1, relief="sunken")
label16.grid(row=3, column=1, sticky="w")
label20 = tk.Label(frame9, text='[-]')
label20.grid(row=3, column=2, sticky="w")
label12expl = tk.Label(frame9, text='Lift-induced drag constant')
label12expl.grid(row=3, column=3, sticky="w")

## ROW 5 radio buttons for plots
ws_range1 = tk.Label(frame4, text='W/S range:').grid(row=5, column=0, sticky="w")
ws_range_from = tk.Entry(frame4, width=elw-3)
ws_range_from.insert(tk.END , '200')
ws_range_from.grid(row=5, column=1, sticky="e")
ws_range3 = tk.Label(frame4, text=' - ').grid(row=5, column=2)
ws_range_to = tk.Entry(frame4, width=elw-3)
ws_range_to.insert(tk.END , '2960')
ws_range_to.grid(row=5, column=3, sticky="w")
r1 = tk.IntVar()
r1.set(1)
tk.Radiobutton(frame4, text='T/W (Jet)',       variable=r1, value=1).grid(row=6, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='T/W@SL (Jet)',    variable=r1, value=2, state=tk.DISABLED).grid(row=7, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='P/W (Prop)',      variable=r1, value=3).grid(row=8, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='P/W@SL (Prop)',   variable=r1, value=4).grid(row=9, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='Thrust (Jet)',    variable=r1, value=5).grid(row=6, column=2, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='Thrust@SL (Jet)', variable=r1, value=6, state=tk.DISABLED).grid(row=7, column=2, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='Power (Prop)',    variable=r1, value=7).grid(row=8, column=2, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='Power@SL (Prop)', variable=r1, value=8).grid(row=9, column=2, columnspan=2, sticky="w")

## ROW 14 radio buttons for units
altUnitsRadios = tk.Label(frame8, text='Altitude units:').grid(row=14, column=0, columnspan=4, sticky="w")
r2 = tk.IntVar()
r2.set(1)
tk.Radiobutton(frame8, text='meters', variable=r2, value=1, command=lambda: altitudeunits(r2.get())).grid(row=15, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame8, text='feet',   variable=r2, value=2, command=lambda: altitudeunits(r2.get())).grid(row=16, column=0, columnspan=2, sticky="w")
    

## ROW 17 radio buttons for velocities
velUnitsRadios = tk.Label(frame8, text='x Velocity units:').grid(row=17, column=0, columnspan=4, sticky="w")
r3 = tk.IntVar()
r3.set(1)
tk.Radiobutton(frame8, text='m/s', variable=r3, value=1, command=lambda: velocityunits(r3.get())).grid(row=18, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame8, text='kn',  variable=r3, value=2, command=lambda: velocityunits(r3.get())).grid(row=19, column=0, columnspan=2, sticky="w")


'Label(self, text=text, justify=LEFT, anchor="w").grid(sticky = W, column=0,row=0)'

# Calculate Button
button1 = tk.Button(frame6, text='Update all\n[ Enter ]',font=('Helvetica',14), command=button1fun)
button1.pack()

#%% PLOTTING MAGIC
def keypress1(heppening1):
    global keypress_label1
    if 'keypress_label1' in globals():
        keypress_label1.pack_forget()
    keypress_label1 = tk.Label(frame2, text='you pressed1 {}'.format(heppening1.key))
    keypress_label1.pack( side=tk.RIGHT, anchor=tk.NE )
    key_press_handler(heppening1, plotcanvas1, bar_of_tools1)
    # key_press_handler(event=heppening1, canvas=plotcanvas2, toolbar=bar_of_tools2)


def showplotf():
    global frame2
    global fig1
    if 'fig1' in globals():
    #     print('fig1 exists in GLOBALS')
        frame2.destroy() # does not destroy wtf
        frame2 = tk.LabelFrame(tab2,text='frame2', relief=tk.RIDGE, borderwidth=5, width=frame2Width, height=frame2Height)
        frame2.pack(side=tk.LEFT)
        frame2.pack_propagate(0)
        del fig1
    DP_ws = float(entry52.get())
    DP_tw = float(entry51.get())
    DP_pow = P_hp
    DP_powSL = P_hpSL
    #---------------------------- Figure 1 ----------------------------#
    fig1 = Figure(figsize=(6,7),dpi=100) # see more args here
    if r1.get() == 1:
        maxtw = max( max(tw_clvt_list),max(tw_dsel_list),max(tw_dtod_list),max(tw_dca_list),max(tw_sc_list) )
        fig1.add_subplot(2,1,1,xlim=[min(ws),max(ws)],ylim=[0,maxtw],xlabel='Wing loading $W/S$ $[N/m^2]$',ylabel='Thrust-to-Weight [N/N]').plot(ws,tw_clvt_list,'b-',
                                                                                                                                                 ws,tw_dsel_list,'b--',
                                                                                                                                                 ws,tw_dtod_list,'k--',
                                                                                                                                                 ws,tw_dca_list,'k-',
                                                                                                                                                 ws,tw_sc_list,'k:',
                                                                                                                                                 [DP_ws,DP_ws],[0,1.2*DP_tw],'r--',
                                                                                                                                                 [0,1.3*DP_ws],[DP_tw,DP_tw],'r--',
                                                                                                                                                 DP_ws,DP_tw,'ro')
    elif r1.get() == 3:
        maxpw = max( max(pw_clvt_list),max(pw_dsel_list),max(pw_dtod_list),max(pw_dca_list),max(pw_sc_list) )
        fig1.add_subplot(2,1,1,xlim=[min(ws),max(ws)],ylim=[0,maxpw],xlabel='Wing loading $W/S$ $[N/m^2]$',ylabel='Power loading P/W [HP/N]').plot(ws,pw_clvt_list,'b-',
                                                                                                                                              ws,pw_dsel_list,'b--',
                                                                                                                                              ws,pw_dtod_list,'k--',
                                                                                                                                              ws,pw_dca_list,'k-',
                                                                                                                                              ws,pw_sc_list,'k:',
                                                                                                                                              [DP_ws,DP_ws],[0,1.2*DP_pw],'r--',
                                                                                                                                              [0,1.3*DP_ws],[DP_pw,DP_pw],'r--',
                                                                                                                                              DP_ws,DP_pw,'ro')
    elif r1.get() == 4:
        maxpwsl = max( max(pwsl_clvt_list),max(pwsl_dsel_list),max(pwsl_dtod_list),max(pwsl_dca_list),max(pwsl_sc_list) )
        fig1.add_subplot(2,1,1,xlim=[min(ws),max(ws)],ylim=[0,maxpwsl],xlabel='Wing loading $W/S$ $[N/m^2]$',ylabel='Power loading@SL P/W [HP/N]').plot(ws,pwsl_clvt_list,'b-',
                                                                                                                                                   ws,pwsl_dsel_list,'b--',
                                                                                                                                                   ws,pwsl_dtod_list,'k--',
                                                                                                                                                   ws,pwsl_dca_list,'k-',
                                                                                                                                                   ws,pwsl_sc_list,'k:',
                                                                                                                                                   [DP_ws,DP_ws],[0,1.2*DP_pwsl],'r--',
                                                                                                                                                   [0,1.3*DP_ws],[DP_pwsl,DP_pwsl],'r--',
                                                                                                                                                   DP_ws,DP_pwsl,'ro')
    elif r1.get() == 5:
        maxt = max( max(t_clvt_mass_list),max(t_dsel_mass_list),max(t_dtod_mass_list),max(t_dca_mass_list),max(t_sc_mass_list) )
        fig1.add_subplot(2,1,1,xlim=[min(S_list),max(S_list)],ylim=[0,maxt],xlabel='$S_{ref}$ $[m^2]$',ylabel='Thrust [N]').plot(S_list,t_clvt_mass_list,'b-',
                                                                                                                                 S_list,t_dsel_mass_list,'b--',
                                                                                                                                 S_list,t_dtod_mass_list,'k--',
                                                                                                                                 S_list,t_dca_mass_list,'k-',
                                                                                                                                 S_list,t_sc_mass_list,'k:',
                                                                                                                                 [DP_S,DP_S],[0,1.2*Thr],'r--',
                                                                                                                                 [0,1.3*DP_S],[Thr,Thr],'r--',
                                                                                                                                 DP_S,Thr,'ro')
    elif r1.get() == 7:
        maxp = max( max(p_clvt_mass_list),max(p_dsel_mass_list),max(p_dtod_mass_list),max(p_dca_mass_list),max(p_sc_mass_list) )
        fig1.add_subplot(2,1,1,xlim=[min(S_list),max(S_list)],ylim=[0,maxp],xlabel='$S_{ref}$ $[m^2]$',ylabel='Power [HP]').plot(S_list,p_clvt_mass_list,'b-',
                                                                                                                         S_list,p_dsel_mass_list,'b--',
                                                                                                                         S_list,p_dtod_mass_list,'k--',
                                                                                                                         S_list,p_dca_mass_list,'k-',
                                                                                                                         S_list,p_sc_mass_list,'k:',
                                                                                                                         [DP_S,DP_S],[0,1.2*DP_pow],'r--',
                                                                                                                         [0,1.3*DP_S],[DP_pow,DP_pow],'r--',
                                                                                                                         DP_S,DP_pow,'ro')
    elif r1.get() == 8:
        maxpsl = max( max(psl_clvt_mass_list),max(psl_dsel_mass_list),max(psl_dtod_mass_list),max(psl_dca_mass_list),max(psl_sc_mass_list) )
        fig1.add_subplot(2,1,1,xlim=[min(S_list),max(S_list)],ylim=[0,maxpsl],xlabel='$S_{ref}$ $[m^2]$',ylabel='Power@SL [HP]').plot(S_list,psl_clvt_mass_list,'b-',
                                                                                                                              S_list,psl_dsel_mass_list,'b--',
                                                                                                                              S_list,psl_dtod_mass_list,'k--',
                                                                                                                              S_list,psl_dca_mass_list,'k-',
                                                                                                                              S_list,psl_sc_mass_list,'k:',
                                                                                                                              [DP_S,DP_S],[0,1.2*DP_powSL],'r--',
                                                                                                                              [0,1.3*DP_S],[DP_powSL,DP_powSL],'r--',
                                                                                                                              DP_S,DP_powSL,'ro')
    if r1.get() == 1 or r1.get() == 2 or r1.get() == 3 or r1.get() == 4:
        fig1.add_subplot(2,1,2,xlim=[min(ws),max(ws)],ylim=[0,max(clmax_list)],xlabel='Wing loading $W/S$ $[N/m^2]$',ylabel='$C_{Lmax}$').plot(ws,clmax_list,'k-',
                                                                                                                                     [DP_ws,DP_ws],[0,1.2*clmax],'r--',
                                                                                                                                     [0,1.15*DP_ws],[clmax,clmax],'r--',
                                                                                                                                     DP_ws,clmax,'ro')
    if r1.get() == 5 or r1.get() == 6 or r1.get() == 7 or r1.get() == 8:
        fig1.add_subplot(2,1,2,xlim=[min(S_list),max(S_list)],ylim=[0,max(clmax_list)],xlabel='$S_{ref}$ $[m^2]$',ylabel='$C_{Lmax}$').plot(S_list,clmax_list,'k-',
                                                                                                                               [DP_S,DP_S],[0,1.2*clmax],'r--',
                                                                                                                               [0,1.15*DP_S],[clmax,clmax],'r--',
                                                                                                                               DP_S,clmax,'ro')
    
    labbb = ['Constant level velocity turn',
             'Desired specific energy level',
             'Desiret Take-off distance',
             'Desired cruise airspeed',
             'Service ceiling',
             'Design Point']
    # labbb = ['clvt','dsel','dtod','dca','sc','DP']
    fig1.legend(labbb,loc=[0.43,0.79])
    global plotcanvas1
    global bar_of_tools1, bar_of_tools2
    
    plotcanvas1 = FigureCanvasTkAgg(fig1, master=frame2)
    plotcanvas1.draw()
    plotcanvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    bar_of_tools1 = NavigationToolbar2Tk(plotcanvas1, frame2)
    bar_of_tools1.update()
    
    plotcanvas1.mpl_connect('key_press_event', keypress1)
    plotcanvas1.mpl_disconnect(plotcanvas1)
    

button3 = tk.Button(frame6,width=4, text='EXIT', font=('Helvetica',28), command=_quit)
# button3.grid(row=1,column=1)
button3.pack()

root.bind('<Return>',press_enterf)

# label200 = tk.Label(frame2, text='label200')
# label200.pack( side=tk.LEFT, anchor=tk.NW )

root.resizable(True, True)
tk.mainloop()
