arr = ["Hello", "World", "OpenAI", "GPT-3", "Language", "Model"]
target = "Language"

# find the position of target

# for position in arr:
#     if position == target:
#         print(arr.index(position))

for position in range(len(arr)):
    if arr[position] == target:
        print(position)