function factorial(n)
    acc = 1
    for i = 1:n
        acc *= i
    end
    acc
end

println(factorial(6))