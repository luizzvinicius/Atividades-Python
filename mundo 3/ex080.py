import uteis

nums = []
for i in range(5):
    n = uteis.lerInteiro("Digite um número: ")
    if len(nums) == 0 or n >= nums[-1]:
        nums.append(n)
    else:
        menor = min(nums)
        if n <= menor:
            nums.insert(nums.index(menor), n)
        else:
            for j in range(len(nums)-1):
                if nums[j] < n < nums[j+1]:
                    print(f"Inserindo na posição {j+1}")
                    nums.insert(j+1, n)
print(nums)
