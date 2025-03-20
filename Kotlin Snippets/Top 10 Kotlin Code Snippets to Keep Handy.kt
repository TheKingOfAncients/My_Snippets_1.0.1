Link - https://pieces.app/blog/top-10-kotlin-code-snippets-to-keep-handy

// 1. Delegated Properties
class Demo {var name: String by DelegateHelperClass()}

// 2.Smart cast
fun main(args: Array< String >) 
{val str1: String? = “Hello World”var str2: String? = null 
// prints String is nullif(str1 is String) 
          {// No Explicit type Casting needed.println(“length of String ${str1.length}”)}
else 
          {println(“String is null”)}}

// 3. Elvis Operator (?:)

val result = nullableValue ?: defaultValue


// 4. Safe Call Operator(?.)
val length = nullableString?.length


// 5. String Interpolation

val name = "John"val greeting = "Hello, $name!"

// 6. Extension Functions

fun String.addExclamation(): String {
    return "$this!"
    }

// 7. Data Classes

data class User(val name: String, val age: Int)val user = User("Alice", 30)

fun operateOnNumber(number: Int, operation: (Int) -> Int): Int
{
 return operation(number)
}
val squared = operateOnNumber(5) { it * it }

Null Safety with !! Operator

val length = nullableString!!.length


// 8.Default Arguments

fun greet(name: String = "World") {
    println("Hello, $name!")
   }
   greet() // Output: Hello, World!


// 9. Inline Functions

inline fun performOperation(value: Int, operation: (Int) -> Int): Int { return operation(value) }val result = performOperation(5) { it * it }
