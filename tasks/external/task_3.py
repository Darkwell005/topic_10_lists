length = int(input())
title = ""
n = int(input())
for i in range(n):
    title += input()
    if i != n - 1:
        title += "\n"

dots = "..."
dot_len = len(dots)
if (len(title) - dot_len + (n - 1)) > length:
    print(title[:length - 1].rstrip() + dots)
else:
    print(title.rstrip())
"""
10
7
123





1234567890
"""