def solution(numbers, hand):
    result = ''
    keypad = [['*', 7, 4, 1], [0, 8, 5, 2], ['#', 9, 6, 3]]

    left = [0, 0]
    right = [2, 0]

    for i in numbers:
        if i in keypad[0]:
            result += "L"
            left = [0, keypad[0].index(i)]

        elif i in keypad[2]:
            right = [2, keypad[2].index(i)]
            result += "R"

        else:
            cur = [1, keypad[1].index(i)]
            tot_r = 0; tot_l = 0
            for i in range(2):
                tot_r += abs(cur[i]-right[i])
                tot_l += abs(cur[i]-left[i])

            if tot_r > tot_l:
                left = cur
                result += "L"
            elif tot_r < tot_l:
                right = cur
                result += "R"
            else:
                if hand == "right":
                    right = cur
                    result += "R"
                else:
                    left = cur
                    result += "L"

    return result