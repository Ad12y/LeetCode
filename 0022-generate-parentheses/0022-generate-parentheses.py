class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final_lst = []
        def recur(string, n, h, l_count, r_count):
            if r_count > l_count:
                return 
            elif l_count > n:
                return 
            elif h == 2*n-1:
                print(string)
                final_lst.append(string)
            
            recur(string+"(", n, h+1, l_count+1, r_count)
            recur(string+")", n, h+1, l_count, r_count+1)

            return string

        recur("(", n, 0, 1,0)
        return final_lst

            


            
            

        

 