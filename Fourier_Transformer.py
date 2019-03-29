import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams["figure.figsize"] = [6,6]

x_points = []
y_points = []
pi = 3.14

def func(x): #function to be fourier transformed

    return (math.e**(-3*x))*math.sin(2*x)

##    return math.cos(2*pi*5.5*x)
##    return 2
##    return math.sin(2*pi*1*x)
##    return math.cos(2*pi*2*x) + math.cos(2*pi*3*x)
##    return math.cos(x)

##    if (int(x) % 2 == 0):
##        return 1
##    return 0

##    return math.e**x
##    return math.log(math.cos(x) + 2)

##    return math.sin(2*pi*3*x)/(x+10)

##    return int(x**x)%((x+1)*int(x+1))

##    return x*math.cos(2*pi*2*x)*math.cos(2*pi*3*x)

##    return math.cos(2*pi*3*x)*math.e**(-pi*(x**2))

##    return 1/(x+10)

##    return 3*math.cos(2*pi*20*x + 0.2) + math.cos(2*pi*30*x - 0.3) + 2*math.cos(2*pi*40*x +2.4) 

##    if (x >= -1 and x <= 1):
##        return abs(x)
##    return 0

    if (x >= 0):
        return 1
    return 0

    return x*(math.sin(x)/(pi*x))**2

    return math.sin(x)/(pi*x)

    if (x > -1 and x < 1):
        return 1
    return 0

    return math.sin(2*pi/x)
    
##    return 1

##    return x/(x+6)

##    return math.cos(2*pi*3*x) + 1
    
def g(x, f):

##    x_new = abs(func(x))*math.cos(2*pi*f*x)
##    y_new = abs(func(x))*(-1)*math.sin(2*pi*f*x)

    x_new = (func(x))*math.cos(2*pi*f*x)
    y_new = (func(x))*(-1)*math.sin(2*pi*f*x)

##    if x_new < 0:
##        print(x)
    
    return x_new, y_new
##    return func(x)*math.cos(f*x), func(x)*(-1)*math.sin(f*x)

def get_points(start, end, inc, f):

    i = start
    x_points = []
    y_points = []

    while (i <= end):

        x, y = g(i, f)

        x_points += [x]
        y_points += [y]

        i += inc

    return x_points, y_points


def get_com(x_points, y_points):

    x_cm = 0
    y_cm = 0

    for i in x_points:
        x_cm += i

    x_cm /= len(x_points)

    for i in y_points:
        y_cm += i

    y_cm /= len(y_points)

    return x_cm, y_cm

def get_max(arr):

    maxi = 0

    for i in range(len(arr)):

        if arr[i] > arr[maxi]:
            maxi = i

    return maxi

def split(arr):

    l = len(arr)

    return arr[0:int(l/4)], arr[int(l/4):int(l/2)], arr[int(l/2):int(3*(l/4))], arr[int(3*(l/4)):l]

#main
x_nums = []
x_f = []
y_f = []
fun_y = []


#max frequencies shown in the plot
f = -2
fmax = 2

i = f
inc_w = 0.01

inc_f = 0.01
##start = f
##end = fmax

#range till which to generate the functions
start = -10
end = 10

atcount = int(abs(f)/inc_w)
count = 0

while i <= fmax:

    x_points, y_points = get_points(start, end, inc_f, i)
    x1, x2, x3, x4 = split(x_points)
    y1, y2, y3, y4 = split(y_points)
    
    x_cm, y_cm = get_com(x_points, y_points)

    x_nums += [i]
    fun_y += [func(i)]
    x_f += [x_cm*(end-start)]
    y_f += [y_cm*(end-start)]

    if count == atcount:
        print(x_cm*(end-start))
        print(y_cm*(end-start))

    #plotting the axes
    plt.axhline(0, color = 'black')
    plt.axvline(0, color = 'black')
##    plt.axvline(3.14, color = 'black')

    #Plotting the original function
    plt.plot(x_nums, fun_y, color = 'grey')

    #plotting the wrap of the function around the unit circle
    plt.plot( x_points, y_points, color = 'green')
    plt.plot(x1, y1, color = 'orange')
    plt.plot(x2, y2, color = 'red')
    plt.plot(x3, y3, color = 'purple')
    plt.plot(x4, y4, color = 'blue')

    plt.plot([x_cm*(end-start),0], [y_cm*(end-start),0], color = 'black')

    #plotting center of masses
    plt.plot(x_nums, x_f, color = 'red')
    plt.plot(x_nums, y_f, color = 'blue')

    #plotting real and imaginary parts together
##    plt.plot(x_f, y_f, 'black')

    #bounds
##    plt.axhline(5, color = 'white')
##    plt.axhline(-5, color = 'white')
##    plt.axvline(-5, color = 'white')
##    plt.axvline(5, color = 'white')

    plt.title('f = '+str(round(i,2)))

    red_patch = mpatches.Patch(color='red', label='Xcm(Even part of FT)')
    blue_patch = mpatches.Patch(color='blue', label='Ycm(Odd part of FT)')
    grey_patch = mpatches.Patch(color='grey', label='Original Function')
    plt.legend(handles=[red_patch, blue_patch, grey_patch])
    
    plt.show(block = False)

##    if round(i,2) in [0.00, 0.01]:
##        input()

##    input()
        
    plt.pause(0.001)
    plt.close()

    count += 1
    i += inc_w

##    input()
    
##print(x_nums[get_max(x_f)])

#axes
##plt.plot(x_points, y_points, color = 'green')

plt.axhline(0, color = 'black')
plt.axvline(0, color = 'black')

#Plotting the original function
plt.plot(x_nums, fun_y, color = 'grey')

plt.plot(x_nums, x_f, color = 'red')
plt.plot(x_nums, y_f, color = 'blue')
##plt.plot(x_f, y_f, 'brown')

red_patch = mpatches.Patch(color='red', label='Xcm(Even part of FT)')
blue_patch = mpatches.Patch(color='blue', label='Ycm(Odd part of FT)')
grey_patch = mpatches.Patch(color='grey', label='Original Function')
plt.legend(handles=[red_patch, blue_patch, grey_patch])

plt.show()
    
