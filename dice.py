import random
import statistics
import plotly.figure_factory as ff

dice_result = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1 + dice2)

mean = sum(dice_result)/len(dice_result)
median  = statistics.median(dice_result)
mode = statistics.mode(dice_result)
std_dev = statistics.stdev(dice_result)

#Finding 1 Std_dev start and end values, and 2nd Std_dev 
first_stddev_start, first_stddev_end = mean - std_dev, mean + std_dev
second_sd_start, second_sd_end = mean - (2*std_dev), mean + (2*std_dev)

list_of_data_within_1st_sd = [result for result in dice_result if result > first_stddev_start and result < first_stddev_end]
list_of_data_within_2nd_sd = [result for result in dice_result if result > second_sd_start and result < second_sd_end]

print("{}%  of data lies within 1st sd". format(len(list_of_data_within_1st_sd)*100.0/len(dice_result)))
print("{}%  of data lies within 2nd sd". format(len(list_of_data_within_2nd_sd)*100.0/len(dice_result)))