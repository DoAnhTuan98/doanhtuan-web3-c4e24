import mlab
from character import River

mlab.connect()

Africa = River.objects(continent__icontains="Africa")
for i in Africa:
    print(i.name)
    
print()

S_America = River.objects(continent__icontains="S. America", length__lt=1000)
for i in S_America:
        print(i.name)
   
