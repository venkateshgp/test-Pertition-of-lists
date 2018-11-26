def is_partioned(ls, n):
    s = sum(ls)
    if s % 2 == 1:
        return False

    target = s // 2
    dp = [True] + [False] * target

    for num in ls:
        for i in range(target, -1, -1):
            if dp[i] and num + i <= target:
                if num + i == target:
                    return True
                dp[i + num] = True
    return False

ls = [3,1,2]
n = len(ls)
if is_partioned(ls,n) == True:
    print('Can be partitioned with two equal sum sets')
else:
    print('Cannot be partitioned with two equal sum sets')
