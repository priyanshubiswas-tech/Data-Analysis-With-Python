# main.py
from mean_var_std import calculate
from demographic_data_analyzer import calculate_demographic_data # Import the function

# Calling the function with a list of 9 elements (required for 3x3 matrix reshaping)
print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Importing function to analyze demographic data
# This function is likely defined in 'demographic_data_analyzer.py'

# Calling the function (make sure the function itself has a print or return to see output)
calculate_demographic_data()

# Importing visualization functions from medical data visualizer
from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Drawing and saving the categorical plot
draw_cat_plot().savefig('catplot.png')

# Drawing and saving the heatmap
draw_heat_map().savefig('heatmap.png')
