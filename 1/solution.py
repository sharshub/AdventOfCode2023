import re


def main():
    answer = 0

    with open("./1/input.txt") as f:
        lines = f.readlines()

        for _line in lines:
            line = replace_num_string(_line)
            first_digit, last_digit = find_digits_in_line(line)
            answer += first_digit * 10 + last_digit

    print("answer:", answer)


def replace_num_string(line: str) -> str:
    new_line = line
    new_line = new_line.replace("one", "o1ne")
    new_line = new_line.replace("two", "t2wo")
    new_line = new_line.replace("three", "t3hree")
    new_line = new_line.replace("four", "f4our")
    new_line = new_line.replace("five", "f5ive")
    new_line = new_line.replace("six", "s6ix")
    new_line = new_line.replace("seven", "s7even")
    new_line = new_line.replace("eight", "e8ight")
    new_line = new_line.replace("nine", "n9ine")
    return new_line


def find_digits_in_line(line: str) -> [int, int]:
    digits = re.findall("[0-9]", line)
    return [int(digits[0]), int(digits[-1])]


main()
