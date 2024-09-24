def count_rotations_linear(nums):
    position = 0

    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        position += 1
    return 0


test1 = {
    'input': {
        'nums': [6, 8, 10, 13, 16, 0, 2, 4]
    },
    'output': 5
}

print(count_rotations_linear(test1['input']['nums']))
