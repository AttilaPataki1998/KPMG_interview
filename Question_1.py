import numpy as np

def area(towers):
    """Takes in a list of integers representing towers
        then calculates the surface area of the structure"""
    
    #converting the input list to a numpy array
    towers = np.array(towers)

    #the areas used in the calculation
    total = 6 * np.sum(towers)          #the total area of the cubes without the overlaps taken into consideration
    overlap1 = 2 * np.sum(towers - 1)   #the overlap of blocks in each tower
    overlap2 = 0                        #the overlap of blocks between towers
    
    #calculates the area of overlapping tiles between towers
    for i in range(len(towers)-1):
        overlap2 += 2 * min(towers[i], towers[i + 1])
    
    return total - (overlap1 + overlap2)

def main():
    print(area([2, 1]))

if __name__ == "__main__":
    main()