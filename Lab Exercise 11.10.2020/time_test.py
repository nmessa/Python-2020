##Program timing demonstration
##Time to add 1 million integers
##Author: nmessa
##Date: 10.15.2011

import time
def main():
    total = 0
    for i in range(1000000):
        total += i

start_time = time.time()
main()
stop_time = time.time()
print ('Program execution time =', stop_time - start_time, 'seconds')
