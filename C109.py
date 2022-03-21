import pandas as pd
import statistics
import plotly.figure_factory as ff 
import csv

df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode= statistics.mode(weight_list)

height_std_dev = statistics.stdev(height_list)
weight_std_dev = statistics.stdev(weight_list)

print("mean, median, mode of height is {}, {} and {} respecttively".format(height_mean, height_median, height_mode))
print("mean, median, mode of weight is {}, {} and {} respecttively".format(weight_mean, weight_median, weight_mode))

height_1st_start, height_1st_end = height_mean - height_std_dev, height_mean + height_std_dev
height_2nd_start, height_2nd_end = height_mean - (2*height_std_dev), height_mean + (2*height_std_dev)

weight_1st_start, weight_1st_end = weight_mean - weight_std_dev, weight_mean + weight_std_dev



height_list_of_data_within_1st_sd = [result for result in height_list if result >height_1st_start and result < height_1st_end]



weight_list_of_data_within_1st_sd = [result for result in weight_list if result >weight_1st_start and result < weight_1st_end]



print("{}% of data for height lies within 1st sd".format(len(height_list_of_data_within_1st_sd)*100.0/len(height_list)))



print("{}% of data for weight lies within 1st sd".format(len(weight_list_of_data_within_1st_sd)*100.0/len(weight_list)))



















































