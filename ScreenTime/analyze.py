import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

data = pd.read_csv("Screentime.csv", encoding= 'unicode_escape')
#print(data.head())

data.isnull().sum()

data = data.dropna(subset=['Notifications'])


#amount of usage of the apps:
# figure = px.bar(data_frame=data,
#                 x = "Date",
#                 y = "Usage",
#                 color="App",
#                 title="Usage")


#the number of notifications from the apps:
# figure = px.bar(data_frame=data,
#                 x = "Date",
#                 y = "Notifications",
#                 color = "App",
#                 title="Notifications")

# figure.show()

#the number of times the apps opened:
# figure = px.bar(data_frame=data,
#                 x = "Date",
#                 y = "Times opened",
#                 color = "App",
#                 title="Times opened")
# data['Notifications'] = data.fillna(0)
figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()