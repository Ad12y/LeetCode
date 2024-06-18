object Solution {
    def addDigits(num: Int): Int = {
        var a = num
        var sum = 0
        while (a>9 || sum!=0){
            sum += a%10
            a = a/10 
            if (a==0){
                a = sum
                sum = 0
            }
        }
        return a
    }
}