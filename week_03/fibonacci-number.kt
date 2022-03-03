class Solution {
    fun fib(n: Int) : Int {
        if (n==0 || n==1) return n

        return this.fib(n-1) + this.fib(n-2)
    }
}
