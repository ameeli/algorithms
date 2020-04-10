"""
Implement a function that outputs the Look and Say sequence:
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
"""


def create_look_and_say(start_num):
    matrix = str(start_num)
    prev_num = str(start_num)

    for row in range(1, 10):
        curr_digit_idx = 0
        check_idx = 0
        digit_count = 0
        new_num = ''

        while check_idx < len(prev_num):
            if prev_num[curr_digit_idx] == prev_num[check_idx]:
                digit_count += 1
            else:
                new_num += str(digit_count) + prev_num[curr_digit_idx]
                curr_digit_idx = check_idx
                digit_count = 1

            check_idx += 1
            if check_idx == len(prev_num):
                new_num += str(digit_count) + prev_num[curr_digit_idx]

        matrix += '\n' + new_num
        prev_num = new_num

    return matrix


print(create_look_and_say(1))
