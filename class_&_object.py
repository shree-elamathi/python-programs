#code
class geeks:
    
    # this is used to print the number
    # of instances of a class
    counter = 0
  
    # constructor of geeks class
    def __init__(self):
        
        # increment
        geeks.counter += 1
  
  
# object or instance of geeks class
g1 = geeks()
g2 = geeks()
g3 = geeks()
print(geeks.counter)
