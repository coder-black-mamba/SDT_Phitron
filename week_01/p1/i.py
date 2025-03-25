data = input()
reversed = data[::-1]
print(int(reversed))
if data == reversed:
    print("YES")    
else:
    print("NO")