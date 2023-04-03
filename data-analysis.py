import pandas as pd #importing pandas libraries and pd is pandas allias

data={
    #data created data dictionary pandas utilizes dictionaries
  'Name':["Oscar","Mutamba","Alksen","khanwald"],
  'Age':[20,21,35,40],
  'sex':["male","male","female","male"]

}
df=pd.DataFrame(data)
#df=pd.set_index("Name")
print(df)
