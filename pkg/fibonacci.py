class Fibonacci:
    def __init__(self, title = "fibonacci") -> None: #넘어오면 사용, 넘어오지 않으면 피보나지
        self.title = title
    def fib(n):
        a, b = 0,1
        while a<n:
            print(a, end=' ')
            a,b = b, a+b
        print()
        
    def fib2(n):
        result = []
        a, b = 0,1
        while a<n:
            result.append(a)
            a,b = b, a+b
        return result
        