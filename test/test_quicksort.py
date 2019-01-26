from homework1 import algs

### I count:
### 12 assignments
### 3 conditionals

#####testing
###basic
def test_basic():
    test = [5,2,8,3,6]
    algs.quicksort(test)

    #####testing
    ###empty
    test = []
    algs.quicksort(test)
    print(test)

    #####testing
    ###single element
    test = [5]
    algs.quicksort(test)
    print(test)

    #####testing
    ###duplicates : 2X 2 2X 5, 2X 8
    test = [5,2,2,8,8,3,6,5]
    algs.quicksort(test)
    print(test)

    #####testing
    ###odd length, even length
    test = [5,2,8,3,6]
    algs.quicksort(test)
    print(test)

    #####testing
    ###odd length, even length
    test = [5,2,8,3,6,0.07]
    algs.quicksort(test)
    print(test)
    
### time / complexity testing
def test_complexity():

    import random

    #####create 2D array of size [100][100,200,300...1000]
    #####first val is number of reps, second is length of array
    test = []
    tmp2 = []
    tmp1 = []
    for i in range(100):
        tmp2 = []
        for j in range(10):
            tmp1_size = 100*(j+1)
            tmp1 = random.sample(range(1,5000),tmp1_size)
            tmp2.append(tmp1)
        test.append(tmp2)
    ####show shapes
    print(len(test[0][0]))
    print(len(test[0][1]))
    print(len(test[0][2]))
    print(len(test[99][2]))
    ######
    print('okay so test list shapes are clear')

    #######test vectors, print out runtimes
    import time

    def count_runtime(fn,fn_in):
        start = time.time()
        ####execute
        fn(fn_in)
        ####
        end = time.time()
        return(end-start)

    ####times is an array of 10 lists
    times = []
    tmp1 = []
    tmp2 = []
    for j in range(10):
        tmp1 = []
        for i in range(100):
            tmp_time = count_runtime(algs.quicksort,test[i][j])
            tmp1.append(tmp_time)
        times.append(tmp1)
    ######
    print('okay so now I got the times')

    import matplotlib.pyplot as plt

    #####plot 100 length
    num_bins = 50
    n, bins, patches = plt.hist(times[0], num_bins, facecolor='blue', alpha=0.5)
    plt.show()
    #####plot 1000 length
    num_bins = 50
    n, bins, patches = plt.hist(times[9], num_bins, facecolor='blue', alpha=0.5)
    plt.show()
    #####
    print('okay so these are normalish')

    #######plot median times
    import statistics as stats
    medians = []
    for i in range(10):
        tmp_median = stats.median(times[i])
        print(tmp_median)
        medians.append(tmp_median)


    ########find C constant
    def power(my_list,exp):
        return [ x**exp for x in my_list ]

    import numpy as np
    ###constant backcalculated using nlogn model
    c = (2.718**(medians[9]/1000))/1000
    #########define n's
    n = np.array([100,200,300,400,500,600,700,800,900,1000])
    ######calculate theoreticals of C*n^2
    ideal_n2 = c * np.square(n)
    ideal_nlogn = c * n*(np.log(n))

    #########plot 
    plt.plot(n, ideal_n2, 'bo',label='O(n^2)')
    plt.plot(n, medians, 'ro',label='Test Data')
    plt.plot(n, ideal_nlogn, 'go',label='O(nlog(n))')
    plt.legend(loc='upper left')
    plt.show()





