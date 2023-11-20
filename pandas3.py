## 3. Create a dictionary called dept. In this dictionary, the columns are deptno, deptname and location. Create a data frame called DataFrame2 from the dictionary dept.


dept = {"Department_No":('Dept1','Dept2','Dept3'),
       "Department_Name":('Administration','Marketing','Finance'),
       "Location":('Mumbai','Delhi','Chennai')}

DataFrame2 = pd.DataFrame(dept)

DataFrame2