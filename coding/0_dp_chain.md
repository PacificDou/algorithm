
接龙型动态规划：每次在上一个最优解后面添加一个新的元素，并且元素之间的顺序 不能 调换

最基本的解法，复杂度O(N^2)：
for i in range(n):
    for j in range(i):
        if condition(array[i], array[j]):
            f[i] = compare(f[i], f[j] + 1)

考虑值域与元素之间是否存在单调性，若存在则可以用二分法来提速搜索O(NlogN)：
for i in range(n):
    # binary search on target domain
    # because we can only save smallest number for each target value
    # so when we compare array[i], we only find the smallest/largest one recorded in target domain
    idx = index of largest element which smaller than array[i]
    f[idx + 1] = array[i]
    if idx larger than current target domain:
        expand target domain

https://www.lintcode.com/problem/1093/
https://www.lintcode.com/problem/76

这道题很好！
https://www.lintcode.com/problem/300

