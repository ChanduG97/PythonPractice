## 2.In the DataFrame1 defined in Q.No. 1, add appropriate column names to the columns. Find the mean of the salary in the DataFrame1.
DataFrame1 = pd.DataFrame([['Emp101','Amit',45000,'Computer','Data Scientist'],
                          ['Emp102','Manish',35000,'Marketing','Senior Manager'],
                          ['Emp103','Keshav',22000,'Project Lead','Project Head'],
                          ['Emp104','Rajnish',25000,'Project Lead','Project Senior Head'],
                          ['Emp105','Jitesh',40000,'Disposal Team','Disposal Head']],
                          columns = ['Employee_No','Name','Salary','Department_No','Designation'])

DataFrame1
DataFrame1.Salary.mean()