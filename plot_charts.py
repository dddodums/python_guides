# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:28:27 2020

@author: wb305167
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot a line chart
# usage
# plot_line_chart_df(df_country_2000, 'year', 'revenue_deficit', 'Country_Code', 'IND')
#
def plot_line_chart_df(df, x_axis, y_axis, grouping_category=None,
                       grouping_value=None, x_ticks=None, y_ticks=None,
                       x_decimal=None, y_decimal=None, x_gap=None, 
                       y_gap=None, data_label_decimal=None,
                       x_axis_label=None, y_axis_label=None,
                       x_line=None, ax=None):
    df = df.dropna(subset=[x_axis, y_axis])
    if grouping_category is not None:
        df_group = df.groupby([grouping_category, x_axis]).mean()
        df_group = df_group.reset_index()
        df_plot = df_group[df_group[grouping_category]==grouping_value]
    if ((x_ticks is None) and
        ((x_decimal is not None) or (x_gap is not None))):
        x_min = df_plot[x_axis].min()
        x_max = df_plot[x_axis].max()
        if x_gap is None:
            x_ticks = [x_min + (x_max-x_min)*i*0.1 for i in range(0, 11)]
            x_ticks = [round(x,x_decimal) for x in x_ticks]
        else:
            x_ticks_str = []
            if x_decimal is not None:            
                x_next_tick=round(x_min,x_decimal)
            else:
                x_next_tick=x_min
            while (x_next_tick < x_max):
                x_ticks_str = x_ticks_str + [str(x_next_tick)]
                x_next_tick = x_next_tick + x_gap
            x_ticks = [float(x) for x in x_ticks_str]
            if x_decimal is not None:             
                x_ticks = [round(x,x_decimal) for x in x_ticks]
        #print(y_ticks)
        #x_min = df_plot[x_axis].min().astype(int)
        #x_max = df_plot[x_axis].max().astype(int) + 1       
        #x_ticks = np.linspace(x_min, x_max, x_max-x_min+1) 
    if ((y_ticks is None) and
        ((y_decimal is not None) or (y_gap is not None))):
        y_min = df_plot[y_axis].min()
        y_max = df_plot[y_axis].max()
        if y_gap is None:
            y_ticks = [y_min + (y_max-y_min)*i*0.1 for i in range(0, 11)]
            y_ticks = [round(y,y_decimal) for y in y_ticks]
        else:
            y_ticks_str = []
            if y_decimal is not None:            
                y_next_tick=round(y_min,y_decimal)
            else:
                y_next_tick=y_min
            while (y_next_tick < y_max):
                y_ticks_str = y_ticks_str + [str(y_next_tick)]
                y_next_tick = y_next_tick + y_gap
            y_ticks = [float(y) for y in y_ticks_str] 
            if y_decimal is not None:                
                y_ticks = [round(y,y_decimal) for y in y_ticks]
        #print(y_ticks)       
        #y_min = df_plot[y_axis].min().astype(int)
        #y_max = df_plot[y_axis].max().astype(int) + 1
        #y_ticks = np.linspace(y_min, y_max, y_max-y_min+1) 
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 3), dpi=200)
        #y_low, y_high, y_ticks = customize_axes_bounds('Global', tax_type, y_low, y_high)       
        ax = df_plot.plot(kind='line', x=x_axis, xticks = x_ticks,
                      use_index=True, y=y_axis, yticks = y_ticks,
                      legend=False, rot=90, color='r', ax=ax)
        x_ticks = ax.get_xticks()
        print('x_ticks: ',x_ticks)
        y_ticks = ax.get_yticks()
        print('y_ticks: ',y_ticks)
        ax.set_xticks(x_ticks)
        ax.set_yticks(y_ticks)
        if x_axis_label is not None:
            ax.set_xlabel(x_axis_label)
        if y_axis_label is not None:
            ax.set_ylabel(y_axis_label)
        #print('x_tick locs: ',locs, 'x_tick label: ',labels)        
    else:
        df_plot.plot(kind='line', x=x_axis, xticks = x_ticks,
                      use_index=True, y=y_axis, yticks = y_ticks,
                      legend=True, rot=90, color='b', ax=ax)  
    if data_label_decimal is not None:
        #print(round(10.54, data_label_decimal))
        #df_plot[[x_axis,y_axis,label_category]].apply(lambda row: ax.text(*row, fontsize = 5),axis=1)           
        df_plot[[x_axis,y_axis]].apply(lambda row: ax.annotate(round(row[y_axis],data_label_decimal), # this is the text
             (row[x_axis], row[y_axis]), # this is the point to label
             textcoords="offset points", # how to position the text
             xytext=(0,2), # distance from text to points (x,y)
             ha='center', # horizontal alignment can be left, right or center
             fontsize = 5),axis=1) # size of marker) 
    if x_line is not None:
        ax.vlines(x_line, y_min, y_max)        
    return(ax)

# plots a scatter plot allowing labels
# usage
# ax = plot_scatter_chart_df(df_shock_merged, 'ln_GDP_Constant_USD',
#                           'Total_Revenue_excl_SC_crisis_shock', 
#                           label_category = 'Country_Code', 
#                           color=colors[1], marker=markers[1])
#    
def plot_scatter_chart_df(df, x_axis, y_axis, grouping_category=None,
                          grouping_value=None, selection_group=None,
                          selection_group_value=None, label_category = None,
                          x_ticks=None, y_ticks=None, x_decimal=None,
                          y_decimal=None, x_gap=None, y_gap=None,
                          x_axis_label=None, y_axis_label=None, color=None,
                          marker=None, x_line=None, ax=None):

    df = df.dropna(subset=[x_axis, y_axis])
    if grouping_category is not None:
        df_group = df.groupby([grouping_category, x_axis]).mean()
        df_group = df_group.reset_index()
        df_plot = df_group[df_group[grouping_category]==grouping_value]
    else:
        if (selection_group is None):
            df_plot = df
        else:
            df_plot = df[df[selection_group]==selection_group_value]
    #print(df_plot[df_plot[y_axis]>1])
    if ((x_ticks is None) and
        ((x_decimal is not None) or (x_gap is not None))):
        x_min = df_plot[x_axis].min()
        x_max = df_plot[x_axis].max()
        if x_gap is None:
            x_ticks = [x_min + (x_max-x_min)*i*0.1 for i in range(0, 11)]
            x_ticks = [round(x,x_decimal) for x in x_ticks]
        else:
            x_ticks_str = []
            if x_decimal is not None:            
                x_next_tick=round(x_min,x_decimal)
            else:
                x_next_tick=x_min
            while (x_next_tick < x_max):
                x_ticks_str = x_ticks_str + [str(x_next_tick)]
                x_next_tick = x_next_tick + x_gap
            x_ticks = [float(x) for x in x_ticks_str]
            if x_decimal is not None:             
                x_ticks = [round(x,x_decimal) for x in x_ticks]
        #print(x_ticks)
        #print('x_max: ',x_max, x_max.dtype)
        #print('x_min: ',x_min)        
        #x_ticks = [x_min]+x_ticks+[x_max]        
        #print(x_ticks)
        #x_min = df_plot[x_axis].min().astype(int)
        #x_max = df_plot[x_axis].max().astype(int) + 1       
        #x_ticks = np.linspace(x_min, x_max, x_max-x_min+1) 
    if ((y_ticks is None) and
        ((y_decimal is not None) or (y_gap is not None))):
        y_min = df_plot[y_axis].min()
        y_max = df_plot[y_axis].max()
        if y_gap is None:
            y_ticks = [y_min + (y_max-y_min)*i*0.1 for i in range(0, 11)]
            y_ticks = [round(y,y_decimal) for y in y_ticks]
        else:
            y_ticks_str = []
            if y_decimal is not None:            
                y_next_tick=round(y_min,y_decimal)
            else:
                y_next_tick=y_min
            while (y_next_tick < y_max):
                y_ticks_str = y_ticks_str + [str(y_next_tick)]
                y_next_tick = y_next_tick + y_gap
            y_ticks = [float(y) for y in y_ticks_str] 
            if y_decimal is not None:                
                y_ticks = [round(y,y_decimal) for y in y_ticks]
        #y_ticks = [y_min]+y_ticks+[y_max]     
        #print(y_ticks)       
        #y_min = df_plot[y_axis].min().astype(int)
        #y_max = df_plot[y_axis].max().astype(int) + 1
        #y_ticks = np.linspace(y_min, y_max, y_max-y_min+1)    
    if color is None:
        color = 'b'
    if marker is None:
        marker = '.'        
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 3), dpi=200)
        ax = df_plot.plot(kind='scatter', x=x_axis, xticks = x_ticks,
                      use_index=True, y=y_axis, yticks = y_ticks,
                      legend=True, rot=90, color=color, marker=marker,
                      s=5, ax=ax)
        x_ticks = ax.get_xticks()
        y_ticks = ax.get_yticks()
        ax.set_xticks(x_ticks)
        ax.set_yticks(y_ticks)
        #print('x_ticks: ',x_ticks)
        #print('y_ticks: ',y_ticks)    
        if x_axis_label is not None:
            ax.set_xlabel(x_axis_label)
        if y_axis_label is not None:
            ax.set_ylabel(y_axis_label)
    else:
        df_plot.plot(kind='scatter', x=x_axis, xticks = x_ticks,
                      use_index=True, y=y_axis, yticks = y_ticks,
                      legend=True, rot=90, color=color, marker=marker,
                      s=5, ax=ax)
    if label_category is not None:
        #df_plot[[x_axis,y_axis,label_category]].apply(lambda row: ax.text(*row, fontsize = 5),axis=1)           
        df_plot[[x_axis,y_axis,label_category]].apply(lambda row: ax.annotate(row[label_category], # this is the text
             (row[x_axis], row[y_axis]), # this is the point to label
             textcoords="offset points", # how to position the text
             xytext=(0,2), # distance from text to points (x,y)
             ha='center', # horizontal alignment can be left, right or center
             fontsize = 5),axis=1) # size of marker)  
    if x_line is not None:
        ax.vlines(x_line, y_min, y_max)
       
    return(ax)
