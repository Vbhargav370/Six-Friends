t = int(input())
for _ in range(t):
    def six_friends(X,Y):
        double = 3*X
        triple = 2*Y
        minimum = min(double, triple)
        return minimum
    
    X,Y = map(int, input().split())
    result = six_friends(X,Y)
    print(result)
    
