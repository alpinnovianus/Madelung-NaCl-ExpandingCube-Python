#Here we write a code to calculate Madelung' s constant for NaCl following the expanding cube scheme described by Gaio and Silvestrelli in PHYSICAL REVIEW B 79, 012102 (2009) . Consider a NaCl cube edge length = 2N, with origin at the central positive ion. Originally, I wrote the code with Wolfram Mathematica. Here is the Python version.

from itertools import product
import numpy as np
from scipy.spatial import distance
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
import sys

# initialize N, M to define the cube edge length. Please pass an argument for N via the command line.
N = int(sys.argv[1])
M = N - 1
print('calculate for N')
#Here we list the tuples of cartesian coordinates for all ionic positions in NaCl structure, i.e. (-3, -3, -3) ... (3, 3, 3) for a cube with edge = 2*3 = 6
coord = list(product(range(-N, N + 1), repeat = 3))

#we also make a complementary list that takes the absolute value of all the elements of the previous list
coord_abs = [list(map(abs,i)) for i in coord]

#sum the absolute value of the coordinates at each position
coord_abs_tot = list(map(sum,coord_abs))

#assign -1 or  +1 charge to each ion depending on its position
arr_1a = list(map(lambda x: (-1)**x,coord_abs_tot))

#A quick check can be done by summing all the charges. It should give (-1)^N
print('Total charge in this cube is '+str(sum( arr_1a)))

#now merge the list of coordinates and charges
arr_2 = list(zip(coord,arr_1a))
#print(arr_2)

#let us define a variable to assign the dimensions and to index our ions
dim_arr_2 = np.shape(arr_2)[0]

#print(dim_arr_2)

#it is good to print these two numbers and make sure they match.
print('float to integer: these following two numbers must match')
print((dim_arr_2 - 1)/2)
print(int((dim_arr_2 - 1)/2))

#this is the index for our array element with coordinate (0,0,0). The Madelung constant is calculated with respect to this ion.
IndZero = int((dim_arr_2 - 1)/2)
#print(arr_2[IndZero])

#now we remove this reference ion from our list of coordinates and charges, subsequently we also reassign the dimension variable for the updated list.
del arr_2[IndZero]
dim_arr_2 = np.shape(arr_2)[0]

#print(arr_2)

#here we calculate the euclidean distance for every ion to the origin
arr_3a = list(map(lambda x: distance.euclidean(arr_2[x][0],(0,0,0) ), range(dim_arr_2) ) ) 

#here we merge the distances to our list of coordinates+charges
arr_3 = list(zip(arr_2,arr_3a))
#print(arr_3, np.shape(arr_3))
#print(arr_3[0][0][1])

#for each position, calculate -(charge)/distance to origin
arr_4 = list(map(lambda x: -arr_3[x][0][1] / arr_3[x][1], range(dim_arr_2) ))
#print(arr_4)

#sum all of the previous quantity for each element
valueN= np.sum(arr_4)
print('the interim value obtained with cube of edge 2N: '+str( valueN))


#now repeat for M=N-1
print('calculate for N-1')
#Here we list the tuples of cartesian coordinates for all ionic positions in NaCl structure, i.e. (-3, -3, -3) ... (3, 3, 3) for a cube with edge = 2*3 = 6
M_coord = list(product(range(-M, M + 1), repeat = 3))

#we also make a complementary list that takes the absolute value of all the elements of the previous list
M_coord_abs = [list(map(abs,i)) for i in M_coord]

#sum the absolute value of the coordinates at each position
M_coord_abs_tot = list(map(sum,M_coord_abs))

#assign -1 or  +1 charge to each ion depending on its position
M_arr_1a = list(map(lambda x: (-1)**x,M_coord_abs_tot))

#A quick check can be done by summing all the charges. It should give (-1)^M
print('Total charge in this cube is '+str( sum(M_arr_1a)))                                                                                                                                                                                                                                        

#now merge the list of coordinates and charges
M_arr_2 = list(zip(M_coord,M_arr_1a))
#print(M_arr_2)

#let us define a variable to assign the dimensions and to index our ions
M_dim_arr_2 = np.shape(M_arr_2)[0]
#print(M_dim_arr_2)

#it is good to print these two numbers and make sure they match.
print('float to integer: these following two numbers must match')
print((M_dim_arr_2 - 1)/2)
print(int((M_dim_arr_2 - 1)/2))

#this is the index for our array element with coordinate (0,0,0). The Madelung constant is calculated with respect to this ion.
M_IndZero = int((M_dim_arr_2 - 1)/2)
#print(M_arr_2[M_IndZero])

#now we remove this reference ion from our list of coordinates and charges, subsequently we also reassign the dimension variable for the updated list.
del M_arr_2[M_IndZero]
M_dim_arr_2 = np.shape(M_arr_2)[0]

#print(M_arr_2)
#here we calculate the euclidean distance for every ion to the origin
M_arr_3a = list(map(lambda x: distance.euclidean(M_arr_2[x][0],(0,0,0) ), range(M_dim_arr_2) ) )

#here we merge the distances to our list of coordinates+charges
M_arr_3 = list(zip(M_arr_2,M_arr_3a))
#print(M_arr_3, np.shape(M_arr_3))
#print(M_arr_3[0][0][1])

#for each position, calculate -(charge)/distance to origin
M_arr_4 = list(map(lambda x: -M_arr_3[x][0][1] / M_arr_3[x][1], range(M_dim_arr_2) ))
#print(M_arr_4)
#sum all of the previous quantity for each element
valueM= np.sum(M_arr_4)
print('the interim value obtained with cube of edge 2(N-1): '+str( valueM))

print('The NaCl Madelung constant obtained with expanding cube method with edge length 2N = ' + str(2*N) + ' units is ' + str(0.5*(valueN+valueM)))