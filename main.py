import pandas as pd
import csv
with open("C:/Users/Admin/Downloads/WhiteHat Python/C - 131 Project/final_data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
df = pd.read_csv("final_data.csv")
df.head()
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity =[]

#converting solar mass and radius into km & kg
def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = float(mass[i]*1.989e+30)
        
convert_to_si(radius,mass)


def gravity_calculation(radius, mass):
    G = 6.674e-11
    for index in range(0, len(mass)):
        g = (mass[index]*G)/((radius[index])**2)
        gravity.append(g)


gravity_calculation(radius, mass)

df["Gravity"] = gravity
#df
