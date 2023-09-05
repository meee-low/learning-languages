function fibonacci(n)
    if n < 1
        println("Error: n must be positive.")
    elseif n == 1 || n == 2
        return 1
    end
    return fibonacci(n-1) + fibonacci(n-2)
end


for i = 1:10
    print(fibonacci(i), " ")
end
print("\n")