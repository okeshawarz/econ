# Problem 1
div = [x for x in 1:999 if mod(x, 3) == 0 || mod(x,5) == 0]
sum(div)

# Problem 2
# find terms of fibonacci sequence less than 4,000,000

function fib(x::Int)
    vec = [1, 2]
    while last(vec) <= x
        append!(vec, (vec[end] + vec[end-1]))
    end
    return vec
end
v = fib(4000000)
v = v[v .<= 4000000]
v_even = v[v .% 2 .== 0] # select all elements for whom the modulus/2 is 0
sum(v_even)
