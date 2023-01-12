def sum_digits(n):
    """basic case"""
    if 0 < n < 10:
        return n
    """recursion case"""
    if n >= 10:
        return n % 10 + sum_digits(n // 10)


print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
