
import random

def cal(num=1,length=10):
    strings='abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890'
    for j in range(num):
        for i in range(length):
            x=random.randint(0,len(strings)-1)
            print(strings[x],end="")
        print()

def cho(num=1,length=10):
    strings='abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890'
    for j in range(num):
        for i in range(length):
            print(random.choice(strings),end="")
        print()
            
if __name__=="__main__":
    cal(5)
    print("...............................................")
    cho(5)
