import pandas as pd
ages={"john":20,"jennie":30,"jim":40,"jack":50,"joe":60}
s2=pd.Series(ages)

# print(s2)
#
# print(s2["jennie"])
#
# print(s2[1:])
# print(s2[:3])
#
print(s2[1:3])
print(s2["jim":])
print(s2["jim":"jack"])
print(s2)