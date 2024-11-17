import math
points=[(1,2),(3,5),(2,5)]
distances=[]

def euclideanDistance (tuple1,tuple2):
    return math.sqrt((tuple2[1]-tuple1[1])**2+(tuple2[0]-tuple1[0])**2)

for i in range(len(points)):
    for k in range(i+1,len(points)):
        result=euclideanDistance(points[i],points[k])
        distances.append(result)

minValue=min(distances)

print(f"The shortest distance is: {minValue}")



    




