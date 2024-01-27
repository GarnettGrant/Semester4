# %% [markdown]
# <b>Garnett Grant</b>
# 
# <b>Student Number: 301188923</b>

# %% [markdown]
# ## Exercise #1 Pandas

# %% [markdown]
# <h4>Init from dict</h4>

# %%
# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
#1.	Create a new dictionary, name it your firstname where firstname _fruits is your first name.
garnett_fruits = {}
garnett_fruits


# %%
#2. Add four items to the dictionary with names of your favorite fruits as keys and the respective color as values.
garnett_fruits.update({
    "Ackee":"Yellow",
    "Mango":"Yellow",
    "Pineapple":"Yellow",
    "Avacado":"Green"
})
garnett_fruits

# %%
#3.	Convert the dictionary into a pandas series named firstname_f.
garnett_f = pd.Series(garnett_fruits)
garnett_f

# %%
#4.	Print out the second and third items.
garnett_f[1], garnett_f[2]

# %%
#5.	Create a sub series named firstname_f2 containing the second and third items.
garnett_f2 = pd.Series([garnett_f[1], garnett_f[2]])
garnett_f2

# %%
# 6. Print out from the sub series the last item using iloc.
garnett_f2.iloc[-1]

# %% [markdown]
# <h4>Handling Time</h4>

# %%
# 1. Create a list containing four  rainfall amounts  of values 10, 23,24,30 name the list firstname_amounts.
garnett_amounts = [10,23,24,30]

# %%
#2.	Using pandas create a date_range for todays date/time (you can set any time) with four time intervals.
dates = pd.date_range('2024/01/27 11:00am', periods=4, freq='H')
dates

# %%
#3.	Create a series that combines both the list and date range name it firstname_rainfallamounts_today.
garnett_rainfall_amounts_today = pd.Series(garnett_amounts, dates)
garnett_rainfall_amounts_today

# %%
#4.	Plot as bar chart.
garnett_rainfall_amounts_today.plot(kind="bar")
plt.show()

# %% [markdown]
# <h4>Pandas Multi-Indexing</h4>
# <blockquote>Make a copy of the dataframe d5 and name it fristname_d5, carryout the following:
# </blockquote>

# %%
d5 = pd.DataFrame(
  {
    ("public", "birthyear"):
        {("Paris","alice"):1985, ("Paris","bob"): 1984, ("London","charles"): 1992},
    ("public", "hobby"):
        {("Paris","alice"):"Biking", ("Paris","bob"): "Dancing"},
    ("private", "weight"):
        {("Paris","alice"):68, ("Paris","bob"): 83, ("London","charles"): 112},
    ("private", "children"):
        {("Paris", "alice"):np.nan, ("Paris","bob"): 3, ("London","charles"): 0}
  }
)

# %%
#1.	print out a dataframe containing all “private” columns
garnett_d5 = d5.private
garnett_d5


# %%
#2.	Swap the columns and rows (hint: look at transpose) 
garnett_d5.T

# %% [markdown]
# <h4>Querying</h4>
# 

# %%
# Use the query() to query the people dataframe you created earlier and retrieve everything related to alice.
garnett_d5.query("index == 'Paris[alice]'")


# %% [markdown]
# <h4>Operations on Dataframes</h4>
# 

# %% [markdown]
# <blockquote>Add a cell to create a dataframe containing grade for four students choose the name of the students and use the names as index. 
# <ul>
# <li>For columns create four columns to reflect the months April, May, June, July. </li>
# <li>Set grade items for each student for each month to be between 0 and 100.  </li>
# <li>Name the dataframe fristname_grades. </li>
# <li>Carry out the following using pandas operations:</li>
# </ul>
# </blockquote>

# %%
import random as rdm
rdm.seed(42)
values = [[rdm.randint(0,100) for i in range(4)]for i in range(4)]
student_names = ["Michael", "Raphael", "Gabriel", "Ezekiel"]
garnett_grades = pd.DataFrame(values,columns=["April","May","June","July"],index=student_names)
garnett_grades
# values

# %%
# 1.Print out the average for the month of April
april_mean = garnett_grades["April"].mean(axis=0)
april_mean

# %%
#2.	Adjust all the grades by 2% (i.e. increase)
adjusted_garnett_grades = garnett_grades + (garnett_grades * 0.02)
adjusted_garnett_grades 

# %%
#3.	Printout the grades for the month of may that are higher than 50%
above_50_in_may = adjusted_garnett_grades .query("index == May & May > 50")
above_50_in_may

# %%
#4.	Group the failing students i.e. the students with average over four month below 50%
students_avg= adjusted_garnett_grades.mean(axis=1)
adjusted_garnett_grades['Average Below 50%'] = students_avg[students_avg < 50]
adjusted_garnett_grades.groupby('Average')
adjusted_garnett_grades

# %% [markdown]
# ## Excercise #2 Numpy

# %%
# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# <blockquote>np.functionname</blockquote>

# %%
#Add a cell to create a function and name it  my_function_firstname, where firstname is your first name.
# Let the function return an integer value stored in one byte i.e. ‘int8’ of (4x)*(3y). Where x is the number of rows and y is the number of columns.
# Use np.fromfunction() to generate  three elements each are two by six using the  my_fuction_firstname.

def my_function_garnett(X, y):
    """
    Returns an integer value stored in one byte i.e. ‘int8’ of (4x)*(3y). 
    Where x is the number of rows and y is the number of columns.
    ## Made by Garnett
    """
    result = (4*X) * (3*y)
    return np.int8(result)

np.fromfunction(my_function_garnett, (3,6))

# %% [markdown]
# <blockquote>Multi-dimensional arrays</blockquote>

# %%
#2. Inspect the code under this section copy it, add a cell to extract values 16,17,18
b = np.arange(48).reshape(4, 12)
b

# %%
b[1,4],b[1,5],b[1,6]

# %% [markdown]
# <blockquote>Iterating</blockquote>

# %%
## Inspect the code under this section copy it, then add a cell to iterate over c and print the Boolean values for items equivalent to zeros.
c = np.arange(24).reshape(2, 3, 4)  # A 3D array (composed of two 3x4 matrices)
c

# %%
for i in c.flat:
    print(i == 0)

# %% [markdown]
# <blockquote>VStack</blockquote>

# %%
##Inspect the code under this section copy it, then add a cell to create a variable name it q5_firstname where firstname is your firstname and vertically stack q1 and q2 and print the output.
q1 = np.full((3,4), 1.0)
q2 = np.full((4,4), 2.0)
q3 = np.full((3,4), 3.0)

# %%
q5_garnettt= np.vstack((q1, q2))
q5_garnettt

# %% [markdown]
# </blockquote>Concatenate</blockquote>

# %%
## Inspect the code under this section copy it, then add a cell to create a variable name it q8_firstname where firstname is your firstname , concatenate q1 and q3 and print the results.  

# %%
q8_garnett = np.concatenate((q1, q2, q3), axis=0)
q8_garnett

# %% [markdown]
# <blockquote>Transpose</blockquote>

# %%
# Inspect the code under this section copy it, then add a cell and create a variable named t_firstname where firstname is your name, let the variable hold any ndaray size 2 by 7 with zero values, print the result then transpose and print the result.
t_garnett = np.arange(24).reshape(4,2,3)
t_garnett

# %%
t_garnett.transpose()

# %% [markdown]
# <blockquote>Matrix multiplication</blockquote>

# %%
## Inspect the code under this section copy it, 
n1 = np.arange(10).reshape(2, 5)
n2 = np.arange(15).reshape(5,3)

# %%
#then  add a cell to create 2 ndarys name the first a1 and the second a2. #Both arrays should contain numbers in the range 0 to 8, inclusive . 
a1 = np.arange(8).reshape(4,2) + 1
a2 = np.arange(8).reshape(2,4) + 1

# %%
#Print a1 and a2. 
a1, a2

# %%
#Reshape a1 to a 2 by 4. 
a1.reshape(2,4)

# %%
#Reshape a2 to a 4 by 2. 
a2.reshape(4,2)

# %%
#Create a new variable a3_firstname where firstname is your first name which holds the dot product of a1 and a2 name it a3 and print the output of a3_firstname, then the shape of a3_first name.
a3_garnett = a1.dot(a2)
a3_garnett, a3_garnett.shape

# %% [markdown]
# <blockquote>8. Matrix inverse and pseudo-inverse</blockquote>
# 

# %%
## Add a cell to create a new 4 by 4 ndaray with values between 0 and 15, name the variable that holds the array your first name, print the array and the inverse of the array.
import numpy.linalg as linalg

garnett =  np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])
garnett
linalg.inv(garnett)

# %% [markdown]
# <blockquote>9. Identity Matrix</blockquote>

# %%
# Add a cell to create a 4 by 4 identity array
np.eye(4)

# %% [markdown]
# <blockquote>10. Determinant</blockquote>

# %%
## Add a cell to create a 3 by 3 matrix with values generated randomly then printout the determinant of the matrix.
random_matrix = np.array([[1,2,3],[1,2,3],[1,2,3]])
random_matrix_2 = np.eye(3)
linalg.det(random_matrix_2)

# %% [markdown]
# <blockquote>10. Eigenvalues and eigenvectors</blockquote>

# %%
## Add a cell to create a 4 by 4 matrix with values generated randomly, assign the matrix to a variable named e_firstname. Printout the Eigenvalue and eigenvectors of the matrix.
import random as rdm
rdm.seed(42)
values = [[rdm.randint(0,100) for i in range(4)]for i in range(4)]

e_garnett = np.array(values)

# %%
eigenvalues, eigenvectors = linalg.eig(e_garnett)

eigenvalues, eigenvectors 

# %% [markdown]
# <blockquote>Solving a System of Linear Scalar Equations</blockquote>

# %%
#Add a cell to solve the following linear equations:
#2x+4y+z =12
#3x+8y+2z =16
#X+2y+3z = 3
#Check the results using the allcolse method.

coeffs = np.array([[2,4,0],[3,8,2],[0,2,3]])
depvars = np.array([12,16,3])
solution = linalg.solve(coeffs, depvars)
solution

# %% [markdown]
# ## Excercise #3 Matplotlib

# %%
# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# <blockquote>1, Plotting your first graph</blockquote>

# %%
# Add a cell at the end to generate a 2 D graph as follows:
# x holds 1000 values between -4 and 4
# z holds 1000 values between -5 and 5
# y = x^2 + z^3 +6
# plot x and y
# name the plot(i.e.set the title) “Ploynomial_firstname” where firstname is your firstname.
# Give names for the x and y axis.


# %%
x = np.linspace(-4,4,1000)
z = np.linspace(-5, 5, 1000)

y = (x**2) + (z**3) + 6

plt.plot(x,y)
plt.title("Polynominal_Garnett")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()

# %% [markdown]
# <blockquote>2. Subplots</blockquote>

# %%
# # Add a cell at the end to generate a plot using subplot2grid with the following characteristics:
# A 4 by 4 grid.

# %%
# On the first row plot the function x^2 in a dashed green line.
plt.subplot2grid((4,4), (0, 0), rowspan=1, colspan=4)
plt.plot(x, x**2,"g--")

# On the second-row plot two functions, the first function x^3 in yellow color and the second function x^4 spanning three columns in red color.
plt.subplot2grid((4,4), (1, 0))
plt.plot(x, x**3, 'y-')

plt.subplot2grid((4,4), (1, 1), colspan=3)
plt.plot(x, x**4, 'r-')


# On the third-row plot two functions the first X^6 in a dashed blue color and the second is X=x in magna (pink) color.
plt.subplot2grid((4,4), (2, 0), colspan=3)
plt.plot(x, x**6, 'b--')

plt.subplot2grid((4,4), (2, 3), colspan=1)
plt.plot(x, x,'m-')

# On the fourth row plot one function^7 spanning all columns in dotted red.
plt.subplot2grid((4,4), (3, 0), colspan=4)
plt.plot(x, x**7,'r:')

# Show Plot of Subplot 
plt.show()

# %% [markdown]
# <blockquote>Drawing text</blockquote>

# %%
## On the first graph showing the beautiful point add a new point name new point _firstname and display the coordinates

x = np.linspace(-1.5, 1.5, 30)
px = 0.8
py = px**2

plt.plot(x, x**2, "b-", px, py, "ro")

plt.text(0, 1.5, "Square function\n$y = x^2$", fontsize=20, color='blue', horizontalalignment="center")

plt.text(px - 0.08, py, "Beautiful point", ha="right", weight="heavy")
plt.text(px, py, "x = %0.2f\ny = %0.2f"%(px, py), rotation=50, color='gray')

#New Point_Garnett
px2 = 1.20
py2 = px2**2

plt.plot(x, x**2, "b-", px2, py2, "ro")

plt.text(px2 - 0.08, py2, "New Point_Garnett", ha="right", weight="heavy")
plt.text(px2, py2, "x = %0.2f\ny = %0.2f"%(px2, py2), rotation=50, color='gray')

plt.show()

# %% [markdown]
# <blockquote>4. Scatter</blockquote>

# %%
## Add a cell to generate a scatter plot of x and y where each contains 300 numbers generated randomly between 3 and 100. Set the scale, alpha and colors as you see suitable

from numpy.random import rand
x = rand(3, 100)
y = rand(3, 100)
scale = rand(3, 100)
scale = 300 * scale ** 5
plt.scatter(x, y, s=scale, alpha=0.3, color="red")
plt.show()


