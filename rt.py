import pandas as pd 
import csv 
import statistics
import plotly.figure_factory as ff 
import random 
import plotly.graph_objects as go
dataset=[]

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

population_mean=statistics.mean(data)
print("mean of the population :-" , population_mean)
def random_setof_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean    
def plot_graph(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    print("mean of sampling dest :- " , mean)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean] ,y=[0,1], mode="lines" ,name ="mean"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        setof_mean=random_setof_mean(100)
        mean_list.append(setof_mean)    


    plot_graph(mean_list)    

setup()        