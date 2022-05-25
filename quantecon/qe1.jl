## Plots

using LinearAlgebra
x1 = [1, 2]
y1 = [3, 4]
x2 = [1 2]
y2 = [3 4]
x3 = [1; 2]
y3 = [3;4]

@show dot(x1, y1)
@show x1 * x2

# Arrays
## Arrays vs vectors: Vectors are just 1-dimensional matrices
## Vectors with commas or semicolons are column vectors; spaces are 
## row vectors:

 [1 2 3 4]
 [1; 2; 3; 4]

 x = [1, 2, 3]
 y = copy(x) 
 y[1]  
 x

 y = similar(x)

# Array indexing
a = randn(2,2)
a
a[1,1]
a[1, :] # first row
a[:, 1] # first column

# Views and Slices
a = [1 2; 3 4]
b = a[:, 2] # assign the second column of a to b
@show b

a[:, 2] = [4, 5] # modify second column of a
@show a
@show b

# Tuples
x = ("foo", "bar")
y = ("foo", 2)
typeof(x), typeof(y)

function f()
    return "foo", 1
end
f()

word, val = x
# should be the same as (word, val) 
println("word = $word, val = $val")

# Items
x = [10, 20, 30, 40]
x[end]
x[end-1]

# Dicts
# name and age are keys, which are mapped to values Frodo and 33
d = Dict("name" => "Frodo", "age" => 33)
d["age"]

# Iterators
actions = ["surf", "ski"]
for action in actions
    println("Charlie don't $action")
end

# Looping without indexing
# With index:
x_values = 1:5
for i in eachindex(x_values)
    println(x_values[i] * x_values[i])
end

# Without index:
for x in x_values
    println(x * x)
end

# Helper functions
countries = ("Japan", "Korea", "China")
cities = ("Tokyo", "Seoul", "Beijing")
for (country, city) in zip(countries, cities)
    println("the capital of $country is $city")
end

# Comprehensions
doubles = [ 2i for i in 1:4 ]
animals = ["dog", "cat", "bird"]
plurals = [ animal * "s" for animal in animals ]
[ i + j for i in 1:3, j in 4:6 ]
[ (i, j) for i in 1:2, j in animals ]

# Generators
xs = 1:10000 # creates range 
f(x) = x^2 # defines function f
f_x = f.(xs) #broadcasts f to every element of xs
sum(f_x)

# Using the generator:
sum(f(x) for x in xs)