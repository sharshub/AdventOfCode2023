from collections import defaultdict


def main():
    arr = get_input()
    num_rows = len(arr)
    num_cols = len(arr[0])

    gear_numbers = defaultdict(list)

    result = 0

    for i in range(num_rows):
        j = 0
        while j < num_cols:
            if not arr[i][j].isdigit():
                j += 1
                continue

            start_j = j
            num = 0

            while j < num_cols and arr[i][j].isdigit():
                num = num * 10 + int(arr[i][j])
                j += 1

            end_j = j - 1

            if has_symbols_nearby(arr, i, start_j, end_j):
                result += num

            check_gear_nearby(arr, i, start_j, end_j, gear_numbers, num)
            result2 = calculate_gears(gear_numbers)

    print("answer1:", result)
    print("answer2:", result2)


def get_input() -> list[str]:
    with open("./3/input.txt") as f:
        input_text = f.read()
        input_arr_str = input_text.split("\n")
        return input_arr_str


def has_symbols_nearby(arr: list[str], i: int, start_j: int, end_j: int) -> bool:
    num_rows = len(arr)
    num_cols = len(arr[0])

    res = False

    for _i in range(i - 1, i + 2):
        if _i < 0 or _i == num_rows:
            continue
        for _j in range(start_j - 1, end_j + 2):
            if _j < 0 or _j == num_cols:
                continue
            if not arr[_i][_j].isdigit() and not arr[_i][_j] == ".":
                res = True
                break
        if res:
            break

    return res


def check_gear_nearby(
    arr: list[str],
    i: int,
    start_j: int,
    end_j: int,
    gear_numbers: dict[tuple, list],
    num: int,
) -> None:
    num_rows = len(arr)
    num_cols = len(arr[0])

    for _i in range(i - 1, i + 2):
        if _i < 0 or _i == num_rows:
            continue
        for _j in range(start_j - 1, end_j + 2):
            if _j < 0 or _j == num_cols:
                continue
            if arr[_i][_j] == "*":
                gear_numbers[(_i, _j)].append(num)


def calculate_gears(gear_numbers: dict[tuple, list]):
    result = 0

    for gear in gear_numbers:
        nums = gear_numbers[gear]
        if len(nums) == 2:
            result += nums[0] * nums[1]
    return result


main()
