import java.io.*
import java.math.*
import java.security.*
import java.text.*
import java.util.*
import java.util.concurrent.*
import java.util.function.*
import java.util.regex.*
import java.util.stream.*
import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.io.*
import kotlin.jvm.*
import kotlin.jvm.functions.*
import kotlin.jvm.internal.*
import kotlin.ranges.*
import kotlin.sequences.*
import kotlin.text.*

/*
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */

fun countSwaps(a: Array<Int>): Unit {
    val n: Int = a.size
    var swaps: Int = 0
    
    for (i in 0..n-1) {
        for (j in 0..n-2) {
            if (a[j]>a[j+1]) {
                a[j] = a[j+1].also{a[j+1] = a[j]}
                swaps++
            }
        }
    }

    println("Array is sorted in ${swaps} swaps.")
    println("First Element: ${a[0]}")
    println("Last Element: ${a.last()}")

    return
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val a = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    countSwaps(a)
}
