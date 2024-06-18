object Solution {
    def romanToInt(s: String): Int = {
        val map = Map('I'->1,'V'->5,'X'->10,'L'->50, 'C'->100, 'D'->500, 'M'->1000)
        val map_ = Map("IV"->4,"IX"->9,"XL"->40,"XC"->90,"CD"->400,"CM"->900)
        var i = 0
        var tot = 0
        var flag = true
        while (i<s.length-1){
            if (map_.contains(s"${s(i)}${s(i+1)}")){
                tot += map_(s"${s(i)}${s(i+1)}")
                i +=  2
                if (i<s.length-1){
                    flag = false
                }
            }
            else{
                tot += map(s(i))
                i +=  1
            }
        }
        if (flag){
            if (i <= s.length-1){
                tot += map(s(i))
            }
        }
        return tot     
    }

}