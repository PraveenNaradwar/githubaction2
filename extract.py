
import pandas as pd
print("Extract data form Mysql Database")

data={
        "id":[101,102,103],
        "name":['komal','radha','priya'],
        "address":['pune','mumbai','pune']
}

df=pd.DataFrame(data)
df