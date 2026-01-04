import pandas as pd

print("Extract data from Mysql Database")

data={
    "userid":[101,102,103],
    "name":['komal','ajay','sandhya'],
    "age":[25,26,27]
}

df=pd.DataFrame(data)
print(df)