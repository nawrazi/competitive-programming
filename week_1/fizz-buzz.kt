class Solution {
    fun fizzBuzz(n: Int): List<String> {
        var ls: List<String> = arrayListOf()
        
        for (i in 0..n-1) {
            if ((i+1)%3==0 && (i+1)%5==0)
                ls += "FizzBuzz"
            else if ((i+1)%3==0)
                ls += "Fizz"
            else if ((i+1)%5==0)
                ls += "Buzz"
            else
                ls += (i+1).toString()
        }
        
        return ls        
    }
}