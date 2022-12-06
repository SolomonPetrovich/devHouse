class Computation():    
    def factorial(n):
        if n < 0:
            return "Factorial does not exist for negative numbers"
        if n == 0 or n == 1:
            return 1
        else:
            return n * Computation.factorial(n-1)


    def sum(n):
        ans = 0
        for i in range(n + 1):
            ans += i
        return ans


    def testPrim(n) -> bool:
        count = 0
        for i in range(1, n):
            if not n % i:
                count += 1
        if count > 2:
            return False
        return True


    def testPrims(a, b):
        pass


    def tableMult(a: int):
        for i in range(11):
            print(f'{i} x {a} = {i * a}')


    def allTablesMult():
        for i in range(10):
            for j in range(10):
                print(f'{i} x {j} = {i * j}', end='|') 
            print('')


    def listDiv(a: int):
        l = []
        for i in range(1, a+1):
            if not a % i:
                l.append(i)
        return l


    def ldiv():
        pass


    def listDivPrim(a: int):
        l = []
        for i in range(1, a+1):
            if not a % i and Computation.testPrim(i):
                l.append(i)
        return l


if __name__ == '__main__':
    n = int(input())

    print(Computation.listDivPrim(n))
