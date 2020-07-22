class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not items:
            return []
        
        score_map = {}
        for item in items:
            if item[0] in score_map:
                score_map[item[0]].append(item[1])
                print('Score Map 1:',score_map)
                print('Item [0] is: ',item[0])
                print('Item [1] is: ',item[1])
            else:
                score_map[item[0]] = [item[1]]
                print('Score Map 2:',score_map)
                print('Item [0] is: ',item[0])
                print('Item [1] is: ',item[1])
                
        result = []
        for key, value in score_map.items():
            value.sort(reverse=True)
            print('Value [] is :',value)
            if len(value) >= 5:
                average = value[:5]
                print('avarage 1 is: ',average)
            else:
                average = value
                print('avarage 2 is:',average)
            score_map[key] = sum(average)/len(average)
            print('Sum of the avg is:',sum(average))
            print('Lenght of the avg is:',len(average))
            result.append([key, score_map[key] ])
        
        return result


self=None
items=[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
result=Solution.highFive(self,items)
print(result)