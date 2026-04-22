 # -*- coding: utf-8 -*-
"""

Student ID: 4270173

"""
###
# The following adds the modules required for the code to run.
###
import numpy as np
import matplotlib.pyplot as plt

##############################################################################
'''
DLAnalysis2D reads the contents of the file "DLA2D_data.py" and converts the
data into a useful format. It assignes the data appropreatly to represent the
x and y positions of the particles in a lattice and extracts the size of the
lattice and the number of particles in the lattice. After this the program will
calculate all the distnces of the particles from the center, then asks how many
of these particles are with in a circle of an increasing radius. Once it has
gathered an array of radi and the number of particles with in the radi, it will
plot the logs of these two arrays along with a line of best fit and will
 display the gradient and the y-intercept in the colsole.
'''
class DLAnalysis2D():
    ###
    # __init__ is the initial function called in DLAnalysis2D.
    # It calls the main functions to be used.
    ###
    def __init__(self,DLAnalysis2D):
        self.DLAnalysis2D = DLAnalysis2D
        self.initialise()
        self.main()
        self.writeFile()
    ###
    # initialise reads a data file, extracts the data to represent the number
    # of particles, the radius of the lattice and the positions of all the
    # particles.
    ###
    def initialise(self):
        # Opens the file DLA2D_data.py and reads it.
        file = open('DLA2D_data.py', 'r')
        pos = file.read()
        # Splits the data into three lists.
        lists = pos.split(','+'[')
        # assigns self.N to be the number of particles.
        self.N = int(lists[0])
        # assigns self.max_radius to the radius to the lattice.
        self.max_radius = int(np.array(lists[1]).astype(float))
        # Extracts the list holding the x positions.
        x_list = lists[2]
        # Extracts the list holding the y positions.
        y_list = lists[3]
        # splits the two position lists to be convertable into arrays.
        x_numbers = x_list.split(']')[0].split(',')
        y_numbers = y_list.split(']')[0].split(',')
        # Converts the lists into arrays and assigns them to self.x and self.y.
        self.x = np.array(x_numbers).astype(float)
        self.y = np.array(y_numbers).astype(float)
        # Displays text into the console to display important information.
        print('\n---------------------------\n')
        print('Data imported for successfully N = '+str(self.N)+'\n')
        print('Radius of imported latice is r = '+str(self.max_radius)+'\n')
        print('x points ='+str(self.x)+'\n')
        print('y points = '+str(self.y))
        print('\n---------------------------\n')
        # Calculates all the distances the particles are from the center.
        self.s = np.sqrt(self.x**2+self.y**2)

    ###
    # main finds how many particles are with in a certain radius then increases
    # that radius and repeats the process. It then sends the results to be
    # plotted.
    ###
    def main(self):
        # Creates an array of zeros to hold the particle numbers.
        inside_points = np.zeros(self.max_radius)
        # Loops for the whole radius of the lattice.
        for i in range(self.max_radius):
            # Increases the radius by 1 for each itteration.
            r = i+1
            # Assigns the number of particles with in the radius.
            inside_points[i] = np.size(np.where(self.s<=r))
        # finds the log of the number of particles and radi.
        lgN = np.log(inside_points)
        lgR = np.log(np.linspace(1,self.max_radius,self.max_radius))
        # Sends data to be plotted.
        self.dataPlot(lgR,lgN)

    ###
    # dataPlot generates a figure to represent the relationship of the number
    # of particles and the radius of the circle which enclosed them.
    ###
    def dataPlot(self,lgR,lgN):
        # Creates the figure window.
        plt.figure()
        # Names the X and Y axis and gives the plot a title.
        plt.xlabel('log(r)')
        plt.ylabel('lof(N)')
        plt.title('DLA 2D Graph of log(N) against log(R)')
        # Assignes the data appropreate errorbars.
        plt.errorbar(lgR,lgN,np.sqrt(2)/8,np.sqrt(2)/8,'.b')
        # Plots the data as a scatter plot.
        plt.scatter(lgR,lgN)
        # Creates a line of best fit for the scatter plot.
        plt.plot(np.unique(lgR), np.poly1d(np.polyfit(lgR, lgN, 1))\
                   (np.unique(lgR)),'r')
        # Holds values of the gradient and y-intercept of the line of best fit.
        gradient, intercept = np.polyfit(lgR,lgN,1)
        # Displays the fractal dimention on the figure window.
        plt.text(-0.4,max(lgN)*1.05,'Df = %.2f'%gradient)
        # Displays the fractal dimention for the lattice in the console.
        print('df = '+str(gradient)+'\n')
        # Displays the value for the y-intercept in the console
        print('intercept = ', str(intercept))
        # Saves the resultant figure into the same folder as the code.
        plt.savefig('DLA3D_Data_Plot.png')
        # Assigns the fractal dimention to be a non-local variable.
        self.Df = gradient

    ###
    # writeFile opens a python file called DLA3D_Df to record values for the
    # fractal dimention for different numbers of partucles. Here self.Df
    # represents the fractal dimention and N the number of particles.
    ###
    def writeFile(self):
        # Adds the new data to a file.
        f = open( 'DLA3D_Df.txt', 'a' )
        # inputs x, y and N into the new file.
        f.write('Number of particles = ' + str(self.N)+'\n'+
                'Fractal dimention = ' + str(self.Df)+'\n\n')
        # closes the new file.
        f.close()

###############################################################################
'''
DLAnalysis3D reads the contents of the file "DLA3D_data.py" and converts the
data into a useful format. It assignes the data appropreatly to represent the
x, y and z positions of the particles in a lattice and extracts the size of the
lattice and the number of particles in the lattice. After this the program will
calculate all the distnces of the particles from the center, then asks how many
of these particles are with in a sphere of an increasing radius. Once it has
gathered an array of radi and the number of particles with in those radi, it
will plot the logs of these two arrays along with a line of best fit and will
display the gradient and the y-intercept in the colsole.
'''
class DLAnalysis3D():
    ###
    # __init__ is the initial function called in DLAnalysis3D.
    # It calls the main functions to be used.
    ###
    def __init__(self,DLAnalysis3D):
        self.DLAnalysis3D = DLAnalysis3D
        self.initialise()
        self.main()
        self.writeFile()

    ###
    # initialise reads a data file, extracts the data to represent the number
    # of particles, the radius of the lattice and the positions of all the
    # particles.
    ###
    def initialise(self):
        # Opens the file DLA3D_data.py and reads it.
        file = open('DLA3D_data.py', 'r')
        pos = file.read()
        # Splits the data into three lists.
        lists = pos.split(','+'[')
        # assigns self.N to be the number of particles.
        self.N = int(lists[0])
        # assigns self.max_radius to the radius to the lattice.
        self.max_radius = int(np.array(lists[1]).astype(float))
        # Extracts the list holding the x positions.
        x_list = lists[2]
        # Extracts the list holding the y positions.
        y_list = lists[3]
        # Extracts the list holding the z positions.
        z_list = lists[3]
        # splits the three position lists to be convertable into arrays.
        x_numbers = x_list.split(']')[0].split(',')
        y_numbers = y_list.split(']')[0].split(',')
        z_numbers = z_list.split(']')[0].split(',')
        # Converts the lists and assigns them to self.x, self.y and self.z.
        self.x = np.array(x_numbers).astype(float)
        self.y = np.array(y_numbers).astype(float)
        self.z = np.array(z_numbers).astype(float)
        # Displays text into the console to display important information.
        print('\n---------------------------\n')
        print('Data imported successfully for N = '+str(self.N)+'\n')
        print('Radius of imported latice is r = '+str(self.max_radius)+'\n')
        print('x points ='+str(self.x)+'\n')
        print('y points = '+str(self.y)+'\n')
        print('z points = '+str(self.z))
        print('\n---------------------------\n')
        # Calculates all the distances the particles are from the center.
        self.s = np.sqrt(self.x**2+self.y**2+self.z**2)

    ###
    # main finds how many particles are with in a certain radius then increases
    # that radius and repeats the process. It then sends the results to be
    # plotted.
    ###
    def main(self):
        # Creates an array of zeros to hold the particle numbers.
        inside_points = np.zeros(self.max_radius)
        # Loops for the whole radius of the lattice.
        for i in range(self.max_radius):
            # Increases the radius by 1 for each itteration.
            r = i+1
            # Assigns the number of particles with in the radius.
            inside_points[i] = np.size(np.where(self.s<=r))
        # finds the log of the number of particles and radi.
        lgN = np.log(inside_points)
        lgR = np.log(np.linspace(1,self.max_radius,self.max_radius))
        # Sends data to be plotted.
        self.dataPlot(lgR,lgN)

    ###
    # dataPlot generates a figure to represent the relationship of the number
    # of particles and the radius of the circle which enclosed them.
    ###
    def dataPlot(self,lgR,lgN):
        # Creates the figure window.
        plt.figure()
        # Names the X and Y axis
        plt.xlabel('log(r)')
        plt.ylabel('lof(N)')
        plt.title('DLA 3D Graph of log(N) against log(R)')
        # Plots the data as a scatter plot.
        plt.scatter(lgR,lgN)
        # Assignes the data appropreate errorbars.
        plt.errorbar(lgR,lgN,np.sqrt(2)/8,np.sqrt(2)/8,'.b')
        # Creates a line of best fit for the scatter plot.
        plt.plot(np.unique(lgR), np.poly1d(np.polyfit(lgR, lgN, 1))\
                   (np.unique(lgR)),'r')
        # Holds values of the gradient and y-intercept of the line of best fit.
        gradient, intercept = np.polyfit(lgR,lgN,1)
        # Displays the fractal dimention on the figure window.
        plt.text(-0.4,max(lgN)*1.05,'Df = %.2f'%gradient)
        # Displays the fractal dimention for the lattice in the console.
        print('df = '+str(gradient)+'\n')
        # Displays the value for the y-intercept in the console
        print('intercept = ', str(intercept))
        # Saves the resultant figure into the same folder as the code.
        plt.savefig('DLA3D_Data_Plot.png')
        # Assigns the fractal dimention to be a non-local variable.
        self.Df = gradient

    ###
    # writeFile opens a python file called DLA2D_Df to record values for the
    # fractal dimention for different numbers of partucles. Here self.Df
    # represents the fractal dimention and N the number of particles.
    ###
    def writeFile(self):
        # Adds the new data to a file.
        f = open( 'DLA2D_Df.txt', 'a' )
        # inputs x, y and N into the new file.
        f.write('Number of particles = ' + str(self.N)+'\n'+
                'Fractal dimention = ' + str(self.Df)+'\n\n')
        # closes the new file.
        f.close()

###############################################################################

###
# This code will only run the main functions if the file is directly executed.
# It also allows the DLA module to be imported.
###
if __name__ == "__main__":
    # Starts the analysis program.
    DLAnalysis2D(None)
    DLAnalysis3D(None)