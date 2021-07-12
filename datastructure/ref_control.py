#if 조건문
iftest = "rain"
if iftest == "rain" or iftest == "snow":
    print("check umbrella")
elif iftest == "microdust":
    print("check mask")
else:
    print("weather good!")

# from sys import stdin
# temp = int(stdin.readline())
# if temp >= 10:
#     print("not bad")
# elif 10 >= temp > 0:
#     print("little cold")

#for 반복문
for i in [0,1,2,3,4]:
    print("waiting number {0}".format(i))

for i in range(5): #0,1,2,3,4
    print("waiting number {}".format(i))

list = [1,2,3,4,5]
for i in range(list[1],list[4]): #2,3,4
    print(i)

for i in reversed(range(10)): #9,8,7,..
    print(i)

for i, num in enumerate(['a','b','c']):
    print(i, num) #0,a/1,b/

for i, num in enumerate(['a','b','c'], 101):
    print(i, num) #101,a/102,b

#1줄 for
list = [i+100 for i in list]
list = [len(i) for i in list]

#while 반복문
customer = "mizi"
index = 5
while index >= 1:
    print("{}, your number{}".format(customer,index))
    index -= 1

#continue
conttest = [2,5]
for i in range(1,11):
    if i in conttest:
        continue
    print("{} is called".format(i))

#break
for i in range(1,11):
    if i in conttest:
        break
    print("{} is called".format(i))