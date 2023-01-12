def triangle_number(n):
    """basic case"""
    if n == 1:
        return 1
    """recursion case"""
    if n > 1:
        return n + triangle_number(n - 1)

for i in range(1, 11):
    print(triangle_number(i))