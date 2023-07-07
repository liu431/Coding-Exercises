class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_dic = {}
        for i1, l1 in enumerate(list1):
            if l1 in list2:
                common_dic[l1] = i1 + list2.index(l1)
        
        least_ind_sum = min(common_dic.values())
        common_str = []
        for key, value in common_dic.items():
            if value == least_ind_sum:
                common_str.append(key)
        return common_str
         
