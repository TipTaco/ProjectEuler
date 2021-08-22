# Project Euler Question 17:
# Counting digits in the numbers 1 to 1000 when written as words
# Adrian Shedley, 22 August 2021


def number_to_words(number: int) -> str:
    magnitude = len(str(number))
    words = ""

    thousands = ""
    hundreds = ""
    tens = ""

    if magnitude > 3:
        thousands = get_ones_word(number // 1000)
        number -= (number // 1000) * 1000

    if magnitude > 2:
        hundreds = get_ones_word(number // 100)
        number -= (number // 100) * 100

    if magnitude > 0:
        tens = get_tens_word(number)

    words = f"{f'{thousands} thousand' if len(thousands) > 0 else ''}" \
            f"{f'{hundreds} hundred' if len(hundreds) > 0 else ''}" \
            f"{' and ' if (len(hundreds) or len(thousands)) and len(tens) else ''}" \
            f"{tens if len(tens) > 0 else ''}"

    return words


def get_ones_word(number: int) -> str:
    # Do not include the special case of 'zero' or when number > 9
    ones_words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return ones_words[number]


def get_tens_word(number: int) -> str:
    # Do not include the special case of 'zero' or when number > 99
    if number < 20:
        words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                 "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        return words[number]
    else:
        ones_word = get_ones_word(number % 10)

        tens_words = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        tens_number = number // 10
        tens_word = tens_words[tens_number]

        return f"{tens_word}{f'-{ones_word}' if len(ones_word) > 0 else ''}"


def count_letters(words: str):
    # Ignore spaces and hyphens
    return len(words.replace(" ", "").replace("-", ""))


if __name__ == "__main__":

    start_number = 1
    end_number = 1000

    words_for_342 = number_to_words(342)
    print(f"Case=342 (#{count_letters(words_for_342)}) {words_for_342}")

    words_for_115 = number_to_words(115)
    print(f"Case=115 (#{count_letters(words_for_115)}) {words_for_115}")

    running_sum = 0

    for i in range(start_number, end_number + 1):
        number_as_words = number_to_words(i)
        running_sum += count_letters(number_as_words)
        print(number_as_words)

    print(f"In all numbers ({start_number}->{end_number}) there are {running_sum} letters.")