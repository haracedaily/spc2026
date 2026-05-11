
print("====================")
print("=      성적표      =")
print("====================")

print("="*20 )
print("=  이름  :  홍 길 동  =")
print("="*20 )


for i in range(1,6):
    print(f"{'*' * (i)}")

for i in range(1,6):
    print(f"{'*' * (i):>5}")

for i in range(1,6):
    print(f"{'*' * (i*2-1):^9}")

for i in range(4,0,-1):
    print(f"{'*' * (i*2-1):^9}")


for i in range(1,6):
    print(" " * (5-i) + "*" * (i))

for i in range(1,6):
    print(" " * (5-i),end="")
    print("*" *i)

for i in range(1,6):
    print(" " * (5-i) + "*" * (i*2-1))

for i in range(4,0,-1):
    print(" " * (5-i) + "*" * (i*2-1))
