## Lab Exercise 9.12.2019 Demonstration 3
## Author: nmessa
## calculates the sum of the numbers divisible by 5 <= 1000
total = 0
for number in range(1, 1001):
    if number%5 != 0:
        continue
    print(number)
    total += number

print()
print("The total is", total)

    

