## 1. Create a data frame called DataFrame1. It should contain data about five employees. Each employee data consists of employee number, name, salary, department number and designation.

import pandas as pd

DataFrame1 = pd.DataFrame([['Emp101','Amit',45000,'Computer','Data Scientist'],
                          ['Emp102','Manish',35000,'Marketing','Senior Manager'],
                          ['Emp103','Keshav',22000,'Project Lead','Project Head'],
                          ['Emp104','Rajnish',25000,'Project Lead','Project Senior Head'],
                          ['Emp105','Jitesh',40000,'Disposal Team','Disposal Head']])

DataFrame1