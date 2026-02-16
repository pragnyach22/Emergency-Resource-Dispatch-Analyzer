n=int(input("enter no of elements:"))
integers=[]
name="Pragnya sree"

for i in range(n):
    integers.append(int(input("enter value:")))

print(integers)

vcount=0

low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_requests=[]

for i in range(n):
    if(integers[i]<0):
      invalid_requests.append(integers[i])
    elif(integers[i]>=0):
        vcount+=1
        if(integers[i]==0):
            print(integers[i],"No Demand")
        elif(1<=integers[i]<=20):
            low_demand.append(integers[i])
        elif(21<=integers[i]<=50):
            moderate_demand.append(integers[i])
        else:
            high_demand.append(integers[i])

print("Before using personalized condition")
print("low_demand:",low_demand)
print("moderate_demand:",moderate_demand)
print("high_demand:",high_demand)
print("invalid_requests:",invalid_requests)

L=len(name)-name.count(" ")
PLI=L%3
print("L=",L)
print("PLI=",PLI)

removecount=0

if(PLI==0):
    removecount=len(low_demand)
    low_demand=[]
elif(PLI==1):
    removecount=len(high_demand)
    high_demand=[]
elif(PLI==2):
    removecount=len(low_demand)+len(high_demand)+len(invalid_requests)
    high_demand=[]
    low_demand=[]
    invalid_requests=[]

print("After using personalized condition")
print("low_demand:",low_demand)
print("moderate_demand:",moderate_demand)
print("high_demand:",high_demand)
print("invalid_requests:",invalid_requests)
print("Total Valid Requests:",vcount)
print("Removed Entries:",removecount)
