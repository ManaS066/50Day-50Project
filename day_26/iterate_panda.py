student_dict={
    "student":["Manas","Angela","Ananya"],
    "score":[80,98,50]
}
# for (key,value) in student_dict.items():
#     print(value)

import pandas as pd
student_data =pd.DataFrame(student_dict)
# print(student_data)

# for (key,value) in student_data.items():
#     print(value)

for(index , row) in student_data.iterrows():
   if row.student =="Angela":
       print("find")