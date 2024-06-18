object Solution {
    def multiply(num1: String, num2: String): String = {
        val result = Array.fill(num1.length + num2.length)(0)
        var prod = 0
        var sum = 0

        if (num1 == "0" || num2 == "0"){
            return "0"
        }
        for (i <- num1.length-1 to 0 by -1){
            for (j <- num2.length-1 to 0 by -1){
                prod = (num2(j) - '0') * (num1(i) - '0')
                sum = prod + result(i+j+1)
                result(i+j+1) = sum%10
                result(i+j) += sum/10
            }
        }
        val resultString = result.mkString("")
        val startIndex = resultString.indexWhere(_ != '0')
        
        return resultString.substring(startIndex)
    }
}