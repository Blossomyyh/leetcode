"""
Absolute Paths

"""
def clean_path(path):
    ele = path.split("/")
    stack = []
    for e in ele:
        if e == ".":
            continue
        elif e == "..":
            stack.pop()
        else:
            stack.append(e)
    return '/'.join(stack)


path = '/users/tech/docs/.././desk/../'
print(clean_path(path))
# /users/tech/

# def clean_path(path):
#   folders = path.split('/')
#   stack = []
#
#   for folder in folders:
#     if folder == '.':
#       pass
#     elif folder == '..':
#       stack.pop()
#     else:
#       stack.append(folder)
#   return '/'.join(stack)
#
# path = '/users/tech/docs/.././desk/../'
# print(clean_path(path))
# # /users/tech/