a = input()
b = input()
c = input()
while a < 1 |  a > 10000 | b < 1 |  b > 10000 | c < 1 |  c > 10000 :
    print("Numbers must be more than 1 and less than 10 000")
    a = input()
    b = input()
    c = input()

biggest = 0
smallest = 0
if a >= b & a >= c:
    biggest = a
    if b <= c:
        smallest = b    
    else:
        smallest = c
elif b >= a & b >= c:
    biggest = b
    if a <= c:
        smallest = a    
    else:
        smallest = c
else:
    biggest = c
    if b <= a:
        smallest = b    
    else:
        smallest = a
    
print(biggest + smallest)
print(biggest)
print(smallest)
# function task2() {
#             let a = Number(prompt()), b = Number(prompt()), c = Number(prompt())
#             while (a < 1 && a > 10000 && b < 1 && b > 10000 && c < 1 && c > 10000){
#                 alert("Numbers must be less than 1 and less than 10 000")
#                 a = prompt()
#                 b = prompt()
#                 c = prompt()
#             }
#             let biggest = 0, smallest = 0
#             if (a >= b && a >= c){
#                 biggest = a
#                 if (b <= c){
#                     smallest = b
#                 }
#                 else {
#                     smallest = c
#                 }
#             }
#             else if (b >= a && b >= c) {
#                 biggest = b
#                 if (a <= c){
#                     smallest = a
#                 }
#                 else {
#                     smallest = c
#                 }
#             }
#             else {
#                 biggest = c
#                 if (b <= a){
#                     smallest = b
#                 }
#                 else {
#                     smallest = a
#                 }
#             }
#             alert(biggest + smallest)    
#         }
