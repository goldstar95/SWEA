import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    words = input()
    words_len = len(words)
    for i in range(5):
        if i == 0 or i == 4:
            print('..#.' * words_len + '.')
        elif i == 1 or i == 3:
            print('.#' * (2 * words_len) + '.')
        else:
            print('#.' + '.#.'.join(list(words)) + '.#')