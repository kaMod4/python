# from graph_drawer import draw_graph

num = int(input("Enter a number: "))
nums = []

while num != 1:
    nums.append(num)
    if num % 2 == 0:
        num = num // 2
    elif num % 2 == 1:
        num = num * 3 + 1


nums.append(num)

print("Sequence length:", len(nums))
print("Sequence:", nums)

# draw_graph(nums)
