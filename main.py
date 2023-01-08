# O(n log n)
def part2_A(arr):
    if len(arr) == 1:
        return 0

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_profit = part2_A(left_half)
    right_profit = part2_A(right_half)

    min_left = min(left_half)
    max_right = max(right_half)
    cross_profit = max_right - min_left
    if cross_profit > left_profit and cross_profit > right_profit:
        print("Buy %d " % min_left)
        print("Sell %d" % max_right)
    elif left_profit > right_profit:
        print("Left Profit")
        print(left_profit)
    else:
        print("Right Profit")
        print(right_profit)
    # Return the maximum of the profits calculated above
    return max(left_profit, right_profit, cross_profit)


def part1(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_lcs = part1(left_half)
    right_lcs = part1(right_half)

    result = ""
    for i in range(min(len(left_lcs), len(right_lcs))):
        if left_lcs[i] == right_lcs[i]:
            result += left_lcs[i]
        else:
            break

    return result


def part2_B(arr):
    maxi = max(arr)
    mini = min(arr)
    print("Part2_B Solution")
    print(
        "Buy Day%d for %d , Sell Day%d Result %d for %d" % (arr.index(mini), mini, arr.index(maxi), maxi, maxi - mini))


def part3(arr):
    # Initialize the dp array
    dp = [0] * len(arr)

    dp[0] = 1

    for i in range(1, len(arr)):

        dp[i] = 1

        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def main():
    words = []
    print("--------------------------------------------")
    print("Enter some String for Testing Part1")
    print("If you finish add Strings, you enter Exit")
    word = input("Enter a String \n")
    words.append(word)
    while word != "Exit":
        word = input("Enter a String, Print \"Exit\" \n")
        words.append(word)
    # Remove exit from list
    words.pop()
    print("Longest Common Substring:")
    if len(words) == 0:
        print("Part1 is passed")
    else:
        a = part1(words)
        if len(a) == 0:
            print("There is no substring")
        else:
            print(a)

    print("End of Part 1")
    print("--------------------------------------------")

    print("Welcome to Part2 :D :D")

    prices = []
    price = input("Enter a Price \n")
    prices.append(int(price))

    while price != "-1":
        price = input("Enter a Price, Print \"-1\" \n")
        prices.append(int(price))
        print("Your Prices")
        for item in prices:
            print(item)
    prices.pop()
    if len(prices) == 0:
        print("Part2 is passed")
    else:
        print("Lets Calculate")
        a = part2_A(prices)
        print("Result Part2_A")
        print(a)
        part2_B(prices)
    print("End of Part 2")
    print("--------------------------------------------")
    print("Welcome to Part3 :D :D")
    arr = []
    numberr = input("Enter a Number \n")
    arr.append(int(numberr))
    while numberr != "-1":
        numberr = input("Enter a Number, Print \"-1\" \n")
        arr.append(int(numberr))
        print("Your Numbers")
        for item in arr:
            print(item)
    arr.pop()
    print("Lets Calculate Length")
    a = part3(arr)
    print(a)
    print("End of Part 3")
    print("--------------------------------------------")


main()
