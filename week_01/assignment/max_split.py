inpt_str=input() 

balanced_str_count=0;
tracker=0;
balanced_strings=[]
temp_str=""

for i in inpt_str:
    temp_str+=i
    if i=="L":
        tracker+=1
    elif i=="R":
        tracker-=1
    if tracker==0:
        balanced_strings.append(temp_str)
        temp_str=""
        balanced_str_count+=1

print(balanced_str_count)
for strs in balanced_strings:
    print(strs)