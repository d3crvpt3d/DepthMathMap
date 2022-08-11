import numpy as np
from PIL import Image

##USING ONLY GREEN CHANNEL##

#open image
filename = input("[test_difference] Picture name: ")
if(filename == ""):
    filename = "test_difference"

format = input("[jpg] Format: ")
if(format == ""):
    format = "jpg"

im = Image.open(str(filename)+'.'+str(format))
intensity_array = np.array(im)

offset = input("[1.0] Distance from nearest Object: ")
if(offset == ""):
    offset = 1.0
else:
    offset = float(offset)

pro = input("[0.1] Meter pro lightlevel: ")
if(pro == ""):
    pro = 0.1
else:
    pro = float(pro)

#DEBUG
print(intensity_array.shape)

#get distance
inv_distance_array = np.zeros((len(intensity_array),len(intensity_array[0])))
for y in range(len(intensity_array)):
    for x in range(len(intensity_array[0])):
        if(intensity_array[y][x][1] == 0):
            inv_distance_array[y][x] = 0
        else:
            inv_distance_array[y][x] = (((255/intensity_array[y][x][1])**0.5-1)/pro+offset)*-1+255

#save depth image
print(inv_distance_array[50][50])
out_im = Image.fromarray(np.uint8(inv_distance_array), 'L')
save = input("[jpg] Save as: ")
if(save == ""):
    save = "jpg"
out_im.save("Depth_"+str(filename)+'.'+str(save))

input("[OK] Saved with "+str(pro)+" meter for each light level.")