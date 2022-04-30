class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        StringList=[]
        for i in range(1,n+1):
            if i%3==0 and i%5 == 0:
                StringList.append("FizzBuzz")
            elif i%3 == 0 and i%5 !=0:
                StringList.append("Fizz")
            elif i%3!=0 and i%5 ==0:
                StringList.append("Buzz")
            else:
                StringList.append(str(i))
        return StringList
        