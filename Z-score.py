import csv
import plotly.graph_objects as go
import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import random

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

population_mean = st.mean(data)
population_stdev = st.stdev(data)
print('the mean is :-' , population_mean)
print('the stdev is :-' , population_stdev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

mean_list = []

for i in range(0,100):
    setOfMean = random_set_of_mean(30)
    mean_list.append(setOfMean)
mean = st.mean(mean_list)
sampleStDev = st.stdev(mean_list)
print('the standard deviation for the sample of the reading time is',sampleStDev)

firstStDevStart,firstStDevEnd = mean-sampleStDev,mean+sampleStDev
SecondStDevStart,SecondStDevEnd = mean-(2*sampleStDev),mean+(2*sampleStDev)
ThirdStDevStart,ThirdStDevEnd = mean-(3*sampleStDev),mean+(3*sampleStDev)

fig = ff.create_distplot([mean_list],['Reading Time'],show_hist=False)
fig.add_trace(go.Scatter(x = [population_mean,population_mean],y = [0,0.7], mode = 'lines', name = 'population mean'))
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.7], mode = 'lines', name = 'sample mean'))
fig.add_trace(go.Scatter(x = [firstStDevStart,firstStDevStart],y = [0,0.7],mode = 'lines',name = 'firstStDevstart'))
fig.add_trace(go.Scatter(x = [firstStDevEnd,firstStDevEnd],y = [0,0.7],mode = 'lines',name = 'firstStDevEnd'))

fig.add_trace(go.Scatter(x = [SecondStDevStart,SecondStDevStart],y = [0,0.7],mode = 'lines',name = 'SecondStDevstart'))
fig.add_trace(go.Scatter(x = [SecondStDevEnd,SecondStDevEnd],y = [0,0.7],mode = 'lines',name = 'SecondStDevEnd'))

fig.add_trace(go.Scatter(x = [ThirdStDevStart,ThirdStDevStart],y = [0,0.7],mode = 'lines',name = 'ThirdStDevstart'))
fig.add_trace(go.Scatter(x = [ThirdStDevEnd,ThirdStDevEnd],y = [0,0.7],mode = 'lines',name = 'ThirdStDevEnd'))
fig.show()

Z_score = mean-population_mean/population_stdev
print('the Z_score is :- ', Z_score)

