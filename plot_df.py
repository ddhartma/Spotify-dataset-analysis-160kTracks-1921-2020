import numpy as np

#color_lists = ['r','k','b','g','y','m','c','chartreuse', 'silver', 'lightstealblue', 'deepskyblue', 'cornflowerblue', 'limegreen', 'mediumblue', 'goldenrod', 'burlywood', 'navy', 'brown', 'teal', 'darkgray', 'slategrey', 'turquoise', 'navajowhite', 'lightgray', 'darkgreen', 'mocassin', 'steelblue']

def plot_df_line(df, x_col, y_cols, title, x_label, y_label, line_plot_settings):
    
    figure_size=line_plot_settings['figure_size']
    subplots=line_plot_settings['subplots']
    fontsize_title=line_plot_settings['fontsize_title']
    fontsize_axes_values=line_plot_settings['fontsize_axes_values']
    fontsize_axes_label=line_plot_settings['fontsize_axes_label']
    fontsize_text=line_plot_settings['fontsize_text']
    fontsize_legend=line_plot_settings['fontsize_legend']
    line_width=line_plot_settings['line_width']
    marker=line_plot_settings['marker']
    marker_size=line_plot_settings['marker_size']
    set_xticks_range=line_plot_settings['set_xticks_range']
    xticks_start=line_plot_settings['xticks_start']
    xticks_end=line_plot_settings['xticks_end']
    xticks_step=line_plot_settings['xticks_step']
    set_yticks_range=line_plot_settings['set_yticks_range']
    yticks_start=line_plot_settings['yticks_start']
    yticks_end=line_plot_settings['yticks_end']
    yticks_step=line_plot_settings['yticks_step']
    xlim_value_lower=line_plot_settings['xlim_value_lower']
    xlim_value_upper=line_plot_settings['xlim_value_upper']
    ylim_value_lower=line_plot_settings['ylim_value_lower']
    ylim_value_upper=line_plot_settings['ylim_value_upper']
    color_lists=line_plot_settings['color_lists']
    legend_state=line_plot_settings['legend_state']
    legend_list_to_plot =line_plot_settings['legend_list_to_plot']
    legend_move =line_plot_settings['legend_move']
    legend_x=line_plot_settings['legend_x']
    legend_y=line_plot_settings['legend_y']
            
    """
    Set plot
    """
    axes = df.plot(
            x=x_col,
            y=y_cols,
            subplots=subplots,
            layout=(1, 1),
            figsize=figure_size,
            legend=legend_state,
            color = color_lists,
            linewidth=line_width,
            marker=marker,
            ms=marker_size,
            fillstyle='full'
           )
    """
    Prepare legend
    """
    axes.legend(fontsize=fontsize_legend)
    if legend_list_to_plot != '':
        axes.legend(legend_list_to_plot)

    if legend_move == True:
        axes.get_legend().set_bbox_to_anchor((legend_x,legend_y))

    """
    Set plot axes
    """
    axes.set_title(title, size=fontsize_title, verticalalignment='bottom',horizontalalignment='center')
    if set_xticks_range == True:
        axes.set_xticks(np.arange(xticks_start, xticks_end, xticks_step))
    if set_yticks_range == True:
        axes.set_yticks(np.arange(yticks_start, yticks_end, yticks_step))
    axes.tick_params(axis="both", labelsize=fontsize_axes_values)
    if x_label != '':
        axes.set_xlabel(x_label, fontsize=fontsize_axes_label)
    if y_label != '':
        axes.set_ylabel(y_label, fontsize=fontsize_axes_label)
    if xlim_value_lower != None or xlim_value_upper != None:
        axes.set_xlim(xlim_value_lower, xlim_value_upper)
    if ylim_value_lower != None or ylim_value_upper != None:
        axes.set_ylim(ylim_value_lower, ylim_value_upper)
    #axes.grid(True)
    
    
def plot_df_bar(df, title, bar_setting_dict, subplots=(1,2), coord=0):
    """
    Set plot
    """
    axes = df.plot(
            kind='bar',
            subplots=bar_setting_dict['subplots'],
            layout=bar_setting_dict['layout'],
            figsize=bar_setting_dict['figsize'],
            width=bar_setting_dict['width'],
            align=bar_setting_dict['align'],
            legend=bar_setting_dict['legend_state']
           )
    
    """
    Prepare legend
    """
    if bar_setting_dict['legend_state']==True:
        axes.legend(fontsize=bar_setting_dict['fontsize_legend'])
        if bar_setting_dict['legend_list_to_plot'] != '':
            axes.legend(bar_setting_dict['legend_list_to_plot'])

        if bar_setting_dict['legend_move'] == True:
            axes.get_legend().set_bbox_to_anchor((bar_setting_dict['legend_x'], bar_setting_dict['legend_y']))

    """
    Set plot axes
    """
 
    axes.set_title(title, size=bar_setting_dict['fontsize_title'], verticalalignment='bottom', horizontalalignment='center')
    if bar_setting_dict['set_yticks_range'] == True:
        axes.set_yticks(np.arange(bar_setting_dict['yticks_start'], bar_setting_dict['yticks_end'], bar_setting_dict['yticks_step']))
    axes.tick_params(axis="both", labelsize=bar_setting_dict['fontsize_axes_values'])
    if bar_setting_dict['x_label'] != '':
        axes.set_xlabel(bar_setting_dict['x_label'], fontsize=bar_setting_dict['fontsize_axes_label'])
    else:
        axes.set_xlabel('')
    
    if bar_setting_dict['y_label'] != '':
        axes.set_ylabel(bar_setting_dict['y_label'], fontsize=bar_setting_dict['fontsize_axes_label'])
    else:
        axes.set_ylabel('')
  
    
    
def plot_df_pie(df, title, explode, pie_chart_settings):
    
    figsize=pie_chart_settings['figsize']
    shadow=pie_chart_settings['shadow']
    autopct=pie_chart_settings['autopct']
    startangle=pie_chart_settings['startangle']
    fontsize_title=pie_chart_settings['fontsize_title']
    fontsize_text=pie_chart_settings['fontsize_text']
    fontsize_legend=pie_chart_settings['fontsize_legend']
    legend_state=pie_chart_settings['legend_state']
    legend_title=pie_chart_settings['legend_title']
    legend_list_to_plot =pie_chart_settings['legend_list_to_plot']
    legend_move = pie_chart_settings['legend_move']
    legend_x=pie_chart_settings['legend_x']
    legend_y=pie_chart_settings['legend_y']
            
    """
    Set plot
    """
    axes = df.plot(
            kind='pie',
            explode=explode,
            autopct=autopct,
            textprops={'fontsize': fontsize_text},
            shadow=shadow, 
            startangle=startangle,
            figsize=figsize,
            legend=legend_state
           )
    
    """
    Prepare legend
    """
  
    if legend_state==True:
        
        if legend_list_to_plot != '':
            axes.legend(legend_list_to_plot)
        if legend_title != '':
            axes.legend(title=legend_title)
        axes.legend(fontsize=fontsize_legend)
        if legend_move == True:
            axes.get_legend().set_bbox_to_anchor((legend_x,legend_y))

    """
    Set plot axes
    """
    axes.set_xlabel('')
    axes.set_ylabel('')
    
    axes.set_title(title, size=fontsize_title, verticalalignment='bottom',horizontalalignment='center')
    axes.axis('equal') 

    
   

