from ex25a import adder
import ex25

print(adder(3,4))
line = "this is new line not the previous one"
words = ex25.break_words(line)
print(words)
print(ex25.sort_words(words))
ex25.print_first_word(words)
ex25.print_last_word(words)
print(ex25.sort_sentence(line))
ex25.print_first_and_last(line)
ex25.print_first_and_last_sorted(line)