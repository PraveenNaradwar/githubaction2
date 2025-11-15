import pandas as pd

print("Extraxt data from mysql database")

data={

    "id":[11,12,13],
    "name":['komal','radha','nikita'],
    "address":['pune','mumbai','pune']
}

df=pd.DataFrame(data)
print(df)
