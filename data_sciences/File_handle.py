"""ftr = open("sample.txt", mode='r')
print ftr.read()

ftr.close()
"""
#context manager : with as

with open("sample.txt", mode='r') as ftr:  #mode r for read or w for write
    ########################write##########################
    #ftr.write("erty")
    #print ("writing file b")
    #print (ftr.name) #file name
    #print (ftr.tell)
    #print (ftr.mode) #mode r/w
    #print (ftr.closed) #file closed or not


    ####################read###############################
    #print(ftr.read()) # read complete file
    #print ftr.readline()#read a single line
    #lines = (ftr.readline())
    #print lines
    #print lines[1]



