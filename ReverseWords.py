def reverse_words(arr):
    # reverse all
    mirrorReverse(arr, 0, len(arr) - 1)
    print(arr)
    # reverse one word
    i = 0
    wordStart = -1
    for i in range(len(arr)):
        if arr[i] == ' ':
            if wordStart != -1:
                mirrorReverse(arr, wordStart, i - 1)
                wordStart = -1
        elif i == len(arr) - 1:
            if wordStart != -1:
                mirrorReverse(arr, wordStart, i)
        else:
            if wordStart == -1:
                wordStart = i
    return arr


def mirrorReverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
       'm', 'a', 'k', 'e', 's', '  ',
       'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

print(reverse_words(arr))


""""""""""""""""""""""""""""""""""""""""""""""""




