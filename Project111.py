import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random
import statistics

df  = pd.read_csv('medium_data1.csv')
data = df['reading_time'].tolist()
p_mean = statistics.mean(data)
p_stdev = statistics.stdev(data)
print('The Population Mean Is :', p_mean)
print('The Population Standard Deviation Is :', p_stdev)

def getMean():
    dataset = []
    for i in range(100):
        index = random.randint(0, len(data) - 1)
        dataset.append(data[index])
    mean = statistics.mean(dataset)
    return mean

meanlist = []

for i in range(1000):
    meanlist.append(getMean())

s_mean = statistics.mean(meanlist)
s_stdev = statistics.stdev(meanlist)

Zone1_S, Zone1_E = s_mean - s_stdev, s_mean + s_stdev
Zone2_S, Zone2_E = s_mean - s_stdev * 2, s_mean + s_stdev * 2
Zone3_S, Zone3_E = s_mean - s_stdev * 3, s_mean + s_stdev * 3

df1  = pd.read_csv('sample_2.csv')
data1 = df1['reading_time'].tolist()
d1_mean = statistics.mean(data1)

z_score_1 = (d1_mean - s_mean) / s_stdev
print('The Z Score Of Sample 2 Is :', z_score_1)

fig = ff.create_distplot([meanlist], ['Smd'], show_hist=False)
fig.add_trace(go.Scatter(x = [s_mean, s_mean], y = [0, 1.4], mode = 'lines', name = 'Mean'))
fig.add_trace(go.Scatter(x = [Zone1_E, Zone1_E], y = [0, 1.4], mode = 'lines', name = 'Zone 1'))
fig.add_trace(go.Scatter(x = [Zone2_E, Zone2_E], y = [0, 1.4], mode = 'lines', name = 'Zone 2'))
fig.add_trace(go.Scatter(x = [Zone3_E, Zone3_E], y = [0, 1.4], mode = 'lines', name = 'Zone 3'))
fig.add_trace(go.Scatter(x = [d1_mean, d1_mean], y = [0, 1.4], mode = 'lines', name = 'Z Score'))
fig.show()
