class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            if operations[i] not in ["+","D","C"]:
                res.append(int(operations[i]))
            else:
                if operations[i] == '+':
                        last1rec = res[len(res) - 1]
                        last2rec = res[len(res) - 2]
                        res.append(last1rec + last2rec)
                elif operations[i] == 'D':
                        last1rec = res[len(res) - 1]
                        res.append(2*last1rec)
                elif operations[i] == 'C':
                        res.pop()
        sum = 0
        for i in res:
            sum = sum + i
        
        return sum
