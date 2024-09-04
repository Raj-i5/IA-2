import pandas as p
import matplotlib.pyplot as plt
d={
"First_name":["Aryan","Rohan","Riya","Yash","Siddhant"],
"Last_name":["Singh","Agarwal","Shah","Bhatia","Khanna"],
"Type":["Full-Time","Itern","Full-Time","Part-Time","Full-Time"],
"Dept":["Administration","Technical","Administration","Technical","Management"],
'YoE':[2,3,5,7,6],"Salary":[2000,5000,10000,7000,14000]
}
df=p.DataFrame(d)
av=df.pivot_table(index=['Dept', 'Type'], values='Salary', aggfunc='mean')
print("Average Salary from ecah dept:\n",av)
sm=df.pivot_table(index=['Type'], values='Salary', aggfunc=['sum', 'mean', 'count'])
sm.columns=['Total Salary', 'Mean Salary', 'Number of Employees']
print("\nSum and Mean of:\n",sm)
st=df.pivot_table(values='Salary', index='Type',aggfunc='std')
print("\nStandard Deviation:\n",st)
plt.plot(d['First_name'],d['Salary'],color='g',label=['High salary'])
plt.xlabel('names of employee');plt.ylabel("salary")
plt.legend()
plt.show()
