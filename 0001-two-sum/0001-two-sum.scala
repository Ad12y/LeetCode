object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val d_map = scala.collection.mutable.Map[Int, Int]()
        d_map += (nums(0)->0)
        var result: Array[Int] = Array()

        for(i <- 1 until nums.length)
        {   var comp = target - nums(i)
            if (d_map.contains(comp)){
                result = Array(d_map(comp),i)
            }
            d_map += (nums(i)->i)
        }
        return result
    }
}