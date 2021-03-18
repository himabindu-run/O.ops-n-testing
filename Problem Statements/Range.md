Implement Range class (from in python)
Models: 
- [a, b] 
- [a, b)
- (a, b]
- (a, b)

Range(1, 8) ==> 1, 2, 3, 4, 5, 6, 7

a = Range(8) 
b = Range(4, 9)

a.contains(b) --> False
b.contains(a) --> False
a.combine(b)  --> Range(9)
a.overlaps()
