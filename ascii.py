#! E:\ABDO\Courses\Python\ascii
from PIL import Image
import numpy as np
import math
#Open image using Image module
im = Image.open("C:/Users/user/Downloads/empty/ascii-pineapple.jpg")

#data = im.getdata() #this doesnt seem to work it gives a shit image idk whats the difference between it and the other method


#this is the other method idk gotta see the difference between getdata and the .load method idk whats the difference tbh but there is
row,col = im.size
data=[] #r,g,b
pixels=im.load()
for i in range(row):
  for j in range(col):
    data.append(pixels[i,j])  

#turning it into a numpy array
rgb = np.array(data)#idk why does it turn a list of tuples in an array with the no. of rows is the no. of pixels in the image and the no. of columns is rgb (3)
brightness = np.array(rgb)
#shouldve declared with size same as rgb but with only 1 column instead of 3 columns but it treats it as an int as i said below

#this is the values of rgb into a temp array not sure if i can do it at once where i put these values with a switch case to the no. of the j or it doesnt make a difference
for i in range(len(rgb)):
   sum =[]
   for j in range(len(rgb[0])):
        sum.append(rgb[i][j])
   brightness[i][0] = (0.21*sum[0])+(0.72*sum[1])+(0.07*sum[2])

columns = [1,2] #inefficient way af but it doesnt seem to work giving it the dimensions it for some reason assumes that the array is an int!?
brightness = np.delete(brightness,columns, axis = 1 )
print(brightness.shape)     

ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
asim = np.empty(brightness.shape, dtype = object)
##declaring an array to put the vaules of ascii in couldve changed in brightness directly i think its more space efficient and more efficient in general but lets leave it at that
for i in range(len(brightness)):
        index = math.floor(brightness[i][0]/(255/67))
        if(index > 64):
            index = 64
        asim[i][0] = ascii[index]

##since the amount of rows in the array is equal to the amount of pixels in the whole image it makes sense to reshape it into the image dimensions
asim = asim.reshape(im.size)
print(asim.shape)
##idk if its the more efficient but idk how would i map the ascii values corresponding to each row to this array without reshaping it probably by mapping it to modulus of the no. of columns in the original picture and do that as well when printing or just iterate with the no. of columsn
##but i think its easier to visualize it that way by reshaping
f = open('ascii.txt','w')
for j in range(len(asim[0])):
    print("\n",file = f,end="")
    for i in range(len(asim)):
        print(asim[i][j],file= f,end="")
#for i in range(len(asim)):
   #  k = 1
     #if(k % col == 0):
      #   print("\n",file = f,end="")
  #   else:
    #     print(asim[i][0],file= f,end="")
#     k = k+1
    
##print was switched up between the rows and columns bec for some reason numpy switches them when reshaping or its just my fault and its printed out tilted to the right so i just fixed it by switching between the presumably rows,columns which i dont know which is which actually in the numpy array


#width, height = im.size
#rgb = np.zeros(shape=(width,height)) 
#tuples = imageio.imread(im)


