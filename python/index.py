class Math:
    def add(self, a, b):
        return a+b;

    def sub(self, a, b):
        return a-b;

    def mul(self, a, b):
        return a*b;

    def div(self, a, b):
        if( a < b):
            raise ValueError('divisor is must be small...')

        if( b == 0 ):
            raise ValueError('divisor can not be zero')

        return a/b;



math = Math()

print (math.add(2, 5))


print (math.sub(40, 8))


print (math.mul(3, 6))


print (math.div(4, 2))

