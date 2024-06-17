object Solution {
    def isPalindrome(x: Int): Boolean = {
        var y = x
        var rev = 0
        while(y>0){
            rev = rev*10 + y%10
            y = y/10
        }
        
        return rev == x
        
    }
}