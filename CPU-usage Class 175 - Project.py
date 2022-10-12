import matplotlib .pyplot as plt
import psutil as p
app_name= {}
count=0

for process in p.process_iter():
    count=count+1
    if count<=6:
        name=process.name()
        cpu_usage=p.cpu_percent()
        print('name : ',name,'--cpu usage : ',cpu_usage)
        app_name.update({name:cpu_usage})
        
keymax=max(app_name,key=app_name.get)
print(keymax)
keymin=min(app_name,key=app_name.get)
print(keymin)
name_list=[keymax,keymin]
print(name_list)
app=app_name.values()
max_app=max(app)
print(max_app)
min_app=min(app)
print(min_app)
max_min=[max_app,min_app]
print(max_min)

plt.figure(figsize=(15,7))
plt.xlabel("Application")
plt.ylabel("Usage")
plt.bar(name_list,max_min,width=0.6,color=("purple","green")) 
plt.show()