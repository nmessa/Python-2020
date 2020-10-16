##Dictionary Demo
##Author: nmessa
##Date: 10.1.2017
##This program will demonstrate the use of a dictionary
import time
count = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six',
         7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten'}

spanish = {1:'Uno', 2:'Dos', 3:'Tres', 4:'Cuatro', 5:'Cinco', 6:'Seis',
         7:'Siete', 8:'Ocho', 9:'Nueve', 10:'Diez'}

german = {1:'Eins', 2:'Zwei', 3:'Drei', 4:'Vier', 5:'Funf', 6:'Sechs',
         7:'Sieben', 8:'Acht', 9:'Neun', 10:'Zehn'}

for i in range(10, 0, -1):
    print (german[i])
    time.sleep(1)
#print ('Blast off!!!')
#print ('Despegar!!!')
print ('Abheben!!!')
