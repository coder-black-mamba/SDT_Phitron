# n = int(input())
# # input list 
# l = input().split()

# freq = {}
# # initiating the frequenycy array
# for i in l:
#     # freq[int(i)] += 1
#     if i in freq:
#         freq[int(i)] += 1
#     else:
#         freq[int(i)] = 1

# have_to_remove=0;
# # for i in range(1,n+1):
# #     if freq[i]>i:
# #         have_to_remove+=freq[i]-i
# #     elif freq[i]<i:
#         # have_to_remove+=freq[i]
# # print(l)
# # print(freq)

# for num,count in freq.items():
#     if count>num:
#         have_to_remove+=(count-num)
#     elif count<num:
#         have_to_remove+=count






# print(have_to_remove)


# frequency array diye parinay tai eita 
from collections import counter 



n - int(input())
l = input().split()



freq = counter(l)
have_to_remove = 0



for num,count in freq.items():
    if count>num:
        have_to_remove+=(count-num)
    elif count<num:
        have_to_remove+=count

print(have_to_remove)