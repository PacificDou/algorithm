---------------------------------------------------------------------  
# 对比 完全背包 和 01背包
* 共同点：均为两层循环，外层为物品，内层为背包容量，含义都可以归结为01背包：将物品分为N个，第i个放不放，所以其实背包也属于是序列型
* 共同点：初始化时，是 前0个物品 的情况
* 不同点：状态数组的定义，完全背包--前 i种 物品第i种放几个，01背包--前 i个 物品第i个放不放
  其实本质上差不多，完全背包其实是针对每一种，枚举0，1，2...个而已
* 不同点：对于内层循环的顺序，完全背包是从前往后，01背包是从后往前
* 求最少/多数量，相当于每种物品的价值为1，本质和求最大/小价值是一样的


# 重复性
* 无论是0-1背包，还是完全背包，外层循环是N种物品，才能保证不至于重复
* 如果把物品放在内层循环，那么n1+n2和n2+n1会被当作两种做法，就会产生重复
* 先循环物品后循环背包大小：对于第i种物品，最后放进去还是不放进去
* 先循环背包大小再循环物品：物品的顺序无关，最后放进去的是哪一个


# 经验总结
* 对于状态数组f[i]，一般情况下代表  正好装满  size i
* 为了方便记忆，可以认为所有情况都是  正好装满  size i，最后再通过一个循环求得全局最优解
* 只有当求最大值时，因为初始化为0，0也是一种合法状态，所以  不一定正好装满  size i，全局最优解就是f的最后一个元素  
    https://www.lintcode.com/problem/440  (初始化为0，返回最后元素；初始化为-inf，返回数组的最大元素)
    https://www.lintcode.com/problem/125  (初始化为0，返回最后元素；初始化为-inf，返回数组的最大元素)
* 求方案数时，初始值为0，因为要相加


这个虽然表面是背包，但其实是枚举所有选择：
https://www.lintcode.com/problem/971
https://www.lintcode.com/problem/1915



---------------------------------------------------------------------  
# 完全背包问题：n种物品，每种物品可以取无限多次，价值为V，体积为S，背包大小为m

## 模版
```
f = [float('-inf') for j in range(m + 1)]
f[0] = 0
for i in range(n):
    for j in range(S[i], m + 1):
        f[j] = max(f[j], f[j - S[i]] + V[i])
```

## 经典例题
1. 求最优解(最大/小物品价值; 求最少/多数量，相当于每种物品的价值为1，本质和求最大/小价值是一样的)  
*   https://www.lintcode.com/problem/669  
    https://leetcode.com/problems/coin-change  
*   https://www.lintcode.com/problem/440  (初始化为0，返回最后元素；初始化为-inf，返回数组的最大元素)
b. 求方案数(此时只关注体积是否正好，与价值无关)
    # f[i]: ways to fill exactly amount i
    https://www.lintcode.com/problem/562  (必须先循环物品，否则会出现重复)

*   https://www.lintcode.com/problem/564  (必须先循环背包容量，因为允许重复)
    https://leetcode.com/problems/combination-sum-iv/  
c. 求可行性(此时只关注体积是否正好，与价值无关)
    # f[i]: able to spend exactly i yuan or not
    https://www.lintcode.com/problem/801  (可以先循环物品，也可以先循环容量)




---------------------------------------------------------------------  
# 01背包问题：n个物品，每个物品最多只能取一次，价值为V，体积为S，背包大小为m

## 模版
```
f = [float('-inf') for j in range(m + 1)]
f[0] = 0
for i in range(n):
    for j in range(m, S[i] - 1, -1):
        f[j] = max(f[j], f[j - S[i]] + V[i])
```

## 经典例题
1. 求最优解(最大/小物品价值; 求最少/多数量，相当于每种物品的价值为1，本质和求最大/小价值是一样的)
    # f[i][j]: min probability NO OFFER when spend exactly j yuan in first i universities
    https://www.lintcode.com/problem/800  (可以优化空间从O(nm)到O(m))

*   https://www.lintcode.com/problem/125  (初始化为0，返回最后元素；初始化为-inf，返回数组的最大元素)

    # dp[i][j]: max point when using j minutes for first i questions
    # used time may not be exactly as j
    # just return the last element of f
    https://www.lintcode.com/problem/273  (更为general的01背包，每个物品有多种选择)

*   https://www.lintcode.com/problem/668   (二维的01背包)  
    https://leetcode.com/problems/ones-and-zeroes/

    # f[i][j]: least backpacks when fill exactly size j with first i items
    # g[j]: max existing capacity when use f[i][j] backpacks
    # h: least backpacks when fill size >= m
    # t: max existing capacity when use h backpacks
    https://www.lintcode.com/problem/1161  (DP寻找最少数量，同时记录其对应的最大货物)

    https://www.lintcode.com/problem/1382   (在lintcode上超内存，需要用枚举法)
2. 求方案数(此时只关注体积是否正好，与价值无关)
*   https://www.lintcode.com/problem/563  

    # f[i][j]: ways to select j cards from first i types
    https://www.lintcode.com/problem/312  (每n种物品都有k种选择)

*   https://www.lintcode.com/problem/89  (记录背包size，同时记录用了几个数)

    # f[i][j][k]: first i items, cost <= j, profit >= k
    https://www.lintcode.com/problem/1448/  (利润>=k)

    # f[i][j][k]: first i items, cost == j, profit >= k
    https://www.lintcode.com/problem/1607/  (利润>=k)

    (对比1448和1607，cost<=j 和 cost==j的唯一区别在于初始化，profit>=k 和 profit==k的区别在于最内层循环的终点)
3. 求可行性(此时只关注体积是否正好，与价值无关)
*   https://www.lintcode.com/problem/92

    # f[i][j]: able to play j time with first i songs
    https://www.lintcode.com/problem/344  (关键需要证明最长的歌一定会被选中)

    https://www.lintcode.com/problem/1915   (需要使用set来提速)



---------------------------------------------------------------------  
# 多重背包问题：n种物品，每种最多Ki个，每个价值为Xi，体积为Yi，背包大小为m

## 经典例题
a. 这种问题可以将每种物品的数量展开，即一共有Ki个选项（每个选项一个物品），将这些选项进行01选择，时间复杂度为O(Msum(Ki))
    # f[i][j]: max weight when spend j yuan for first i items
    https://www.lintcode.com/problem/798   (可以使用二进制法进行加速)

    https://www.lintcode.com/problem/799   (在lintcode上超时)

    # f[i][j]: least number of backpack when fill size j with first i backpacks
    # g[i][j]: least move cost when fill size j with f[i][j] backpacks
    # inside the inner loop, enumerate the used capacity of last backpack
    https://www.lintcode.com/problem/1161  (在lintcode上超时)
b. 运用单调队列，可以将a的时间复杂度降到O(NM)，实现起来比较复杂
    https://www.lintcode.com/problem/798  (实现起来很麻烦)
    https://www.lintcode.com/problem/799  (在lintcode上超时)

    # f[i][j]: least number of backpack when fill size j with first i backpacks
    # g[i][j]: least move cost when fill size j with f[i][j] backpacks
    https://www.lintcode.com/problem/1161  (在lintcode上超时)
c. 运用二进制对选项进行优化，即形成的选项为1,2,4,8,...,Ki-2^k+1（可以证明这些选项可以组成任意一个在区间[1,Ki]的数），将这些选项进行01选择，时间复杂度为O(Msum(logKi))
    # f[i][j]: max weight when spend j yuan for first i items
    https://www.lintcode.com/problem/798  (非常适合二进制加速)

    # f[i][j]: able to fill value n with first i coins
    https://www.lintcode.com/problem/799  (二进制加速勉强能够通过)
d. 如果是求解可行性：
    可以在循环每个物品时，记录每个金额所对应的使用次数，这个时候必须从前向后遍历，时间复杂度为O(NM)
    也可以定义状态f[i,j]为前i种物品装满容量j时第i种物品的最多剩余量，f[i,j]>=0则意味着可行，否则不可行，时间复杂度为O(NM)
    # f[i][j]: max remaining i-th item when fill value j with first i items
    https://www.lintcode.com/problem/799








