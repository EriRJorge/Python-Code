import time
import multiprocessing
import math

res_a = []
res_b = []
res_c = []



def make_calc_one(numbers):
    for number in numbers:
        res_a.append(math.sqrt(number ** 3))
        
def make_calc_two(numbers):
    for number in numbers:
        res_b.append(math.sqrt(number ** 4))


def make_calc_three(numbers):
    for number in numbers:
        res_c.append(math.sqrt(number ** 5))
        
        
if __name__ == '__main__':
    
    num_list = list(range(5000000))
    
    
    
    
    
    
start = time.time()
make_calc_one(num_list)
make_calc_two(num_list)
make_calc_three(num_list)
end = time.time()

print(end-start)











# def countdown(time_sec):
#     while time_sec:
#         min, sec = divmod(time_sec, 3600)
#         timeformat = '{:02d}:{:02d}'.format(min, sec)
#         time.sleep(1)
#         time_sec -= 1
        
#     print("Stop")
#     import sys
#     sys.exit(1)

# def easy():
#     question1 = int(input("1+1= \n: "))
    
#     countdown(5)
    
#     if question1 == 2:
#         print("Thats Right!")
#         import sys
#         sys.exit(1)
#     elif question1 == int:
#         print("That is not a number")
#     else:
#         print("That was not the correct answer.")
  





# print("Welcome to the Timed Math Challenge. \n Choose a difficulty.")
# print("Easy \nMedium \nHard")

# difficulty = input()

# match difficulty:
    
#         case "Easy":
#             easy()
        
#         case "Medium":
#             print("We dont have that yet")
    
#         case "Hard":
#             print("We dont have that yet")  
   