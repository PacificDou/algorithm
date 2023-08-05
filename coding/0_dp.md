---------------------------------------------------------------------  
# 动态规划题目类型
* 很有可能动态规划：求最优解，判断可行性，统计方案个数
* 很不可能动态规划：求所有具体方案(100%)，暴力算法已经是多项式的复杂度(100%)，输入数据是集合而非序列(50%)


# 动态规划四个步骤
1. 确定状态（最后一步怎么办-->子问题）
   1. 定义状态时，如果不能确定前一步的决策，而且前一步的选择影响当前这一步的选择，那么就多开一维数组来记录前一步决策的某个性质；经常出现在序列型动态规划:
      https://www.lintcode.com/problem/515/  
      https://leetcode.com/problems/paint-house/  
   2. 有时候，除了需要解题的状态，还需要定义额外的辅助的状态；即状态的定义不一定和解完全一致  
      https://www.lintcode.com/problem/191/  
      https://leetcode.com/problems/maximum-product-subarray/  
   3. 有时候，除了需要定义状态来记录最优解，还需要额外的记录最优解的某个性质。但是，最优解以外的某个性质无法记录。  
      https://www.lintcode.com/problem/1161  (DP寻找最少数量，同时记录其对应的最大货物)  
2. 转移方程(枚举最后一步的可能)
   1. 动态规划中不能出现循环依赖，否则无法定义最优子问题（比如二维矩阵的走法中不能四个方向，比如只能向右向下走）
      https://leetcode.com/problems/minimum-cost-to-merge-stones  （看似循环依赖，其实不然）
3. 计算顺序
4. 初始和边界
   1. 所依赖的子问题如果已经越界(比如数组下标<0)，那么说明该子问题不存在，其值为invalid(比如求最小值时为inf，求最大值时为-inf)




# 规律总结
* 注意是否重复了某种case，有的操作可重复，有的不可重复，比如min，max可重合，但是sum不可重合
* 计数(sum)型的动态规划，如果是把若干子问题相加，那么一定要注意没有遗漏，而且没有重复
* 逆向思维：消去第一/某一个->最后一个，最后被消去的元素，相当于是将序列分为两个不相干的子序列  
   https://www.lintcode.com/problem/168  
   https://leetcode.com/problems/burst-balloons/  
* 逆向思维：分割->合并成N段  
   https://leetcode.com/problems/minimum-cost-to-merge-stones  
* 原数组为圆圈的情况，去一个头变成线性问题，或者去一个尾变成线性问题    
   https://www.lintcode.com/problem/534  
   https://leetcode.com/problems/house-robber-ii  
   https://leetcode.com/problems/house-robber-iii  

  

# 滚动数组，空间优化
* 对于网格上的动态规划，如果Fij只依赖于上一行或者上一列，那么可以只开两行或者两列，具体要看网格是细长型还是宽胖型，一般都按两行来开数组。
* 可以画一下依赖的那两行，弄清楚依赖关系后再优化




---------------------------------------------------------------------
# 坐标型：状态数组的坐标，和数组的坐标，一一对应
* 以i结尾的子数组的某个属性 --> 最长连续上升子序列，俄罗斯套娃
* f[i]代表以array[i]结尾的子数组的某个性质
* 最长连续/不连续上升子序列：虽然名字叫 子序列，但其实是坐标型


## 典型例题
*  https://www.lintcode.com/problem/114  
   https://leetcode.com/problems/unique-paths  
   https://www.lintcode.com/problem/115  
   https://leetcode.com/problems/unique-paths-ii/  
   https://www.lintcode.com/problem/110  
   https://leetcode.com/problems/minimum-path-sum/  
*  https://www.lintcode.com/problem/553/  
   https://leetcode.com/problems/bomb-enemy/  
*  https://www.lintcode.com/problem/116  (DP will TLE, greedy is OK)  
   https://leetcode.com/problems/jump-game/  
   https://www.lintcode.com/problem/622  (use HashTable)  
   https://leetcode.com/problems/frog-jump/  
*  https://www.lintcode.com/problem/191/  
   https://leetcode.com/problems/maximum-product-subarray/  
*  https://www.lintcode.com/problem/397/  
   https://leetcode.com/problems/longest-continuous-increasing-subsequence/  
*  https://www.lintcode.com/problem/76  
   https://leetcode.com/problems/longest-increasing-subsequence/  
   https://www.lintcode.com/problem/602  
   https://leetcode.com/problems/russian-doll-envelopes/  






---------------------------------------------------------------------
# 位操作型：一般用值来做状态数组的下标，考虑位移，以及逻辑操作

## 小技巧：
* n % 2  等价于  n & 1  (n >= 0)
* 求最后一位1: x & (-x)
* 减去最后一位1: x & (x - 1)

## 典型例题
*  https://www.lintcode.com/problem/664  
   https://leetcode.com/problems/counting-bits/  






---------------------------------------------------------------------
# 序列型：前i个物体xxx的某种性质，或者前i个物体xxx并且最后一个元素的状态xxx（即序列+状态）
* 状态数组Fi表示 前i个物体 的情况
* 可以从前面的物体来推导，不一定是紧挨着i-1那个物体  
* 前面i-1个物体的选择，制约着当前这一步的选择，那么就记录前面i-1个物体的决策的某种性质
  可以记录 前i个物体 的某个状态，比如已经购买了几次股票，最后一个房子的颜色  


## 典型例题
*  https://www.lintcode.com/problem/515/  
   https://leetcode.com/problems/paint-house/  
   https://www.lintcode.com/problem/516/  
   https://leetcode.com/problems/paint-house-ii/  
   https://leetcode.com/problems/paint-house-iii/  
   https://leetcode.com/problems/paint-fence  
*  https://www.lintcode.com/problem/392/  
   https://leetcode.com/problems/house-robber/  
   https://www.lintcode.com/problem/534/  
   https://leetcode.com/problems/house-robber-ii/  
   https://leetcode.com/problems/house-robber-iv/  (DP will be TLE, use BinarySearch)  
*  https://www.lintcode.com/problem/151  (注意初始值为-inf而不是0)  
   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/  
   https://www.lintcode.com/problem/393  
   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
*  https://leetcode.com/problems/mice-and-cheese/  (DP will be TLE, use Greedy)  
*  https://www.lintcode.com/problem/89  


   


---------------------------------------------------------------------
# 分段型：给定长度为N的序列或字符串，要求换分成K段/段数不限，每段满足某个特性，每段一定是连续的
* 类似于序列型动态规划，但是通常要加上段数信息，比如f[i][j]记录前i个元素分成j段的性质
* 解题关键：枚举 前面j-1段/最后一段/第一段的长度 的所有可能，则其子问题的段数会减1
* 特别注意：当段数为1时，要么特殊处理，要么回到 段数为k但长度更小 的子问题 --> 内层循环前面j-1段的长度，当其为0时，表示整体只有一段

* 模版  
```
for i in range(1, n + 1): # first i objects
   for j in range(1, k + 1): # split to j sections 
      for w in range(i): # size of previous sections: 0, 1, ..., i - 1
```

## 典型例题
*  https://www.lintcode.com/problem/512  
   https://leetcode.com/problems/decode-ways/   
*  https://www.lintcode.com/problem/513  (DP will be TLE, Math gives the best result)  
   https://leetcode.com/problems/perfect-squares/  
*  https://www.lintcode.com/problem/108  (分段型和区间型的混合题)
   https://leetcode.com/problems/palindrome-partitioning-ii/  
*  https://www.lintcode.com/problem/437  (DP will be TLE)  
*  https://www.lintcode.com/problem/1798/  (区间+分段)
   https://leetcode.com/problems/minimum-cost-to-merge-stones  





---------------------------------------------------------------------
# 博弈型：一般有两个player，状态数组定义为 f[i]: 数组[0..i]时先手能否达到必胜/必败
* 特点：分析时，从第一步开始，而不是像一般的动态规划那样从最后一步开始；即bottom up，从规模小的往规模大的推导


## 典型例题
*  https://www.lintcode.com/problem/394  
*  https://www.lintcode.com/problem/396/   (博弈+区间的混合型，两种做法，一种将状态数组定义为最大分数，一种定义为最大分数的差)







---------------------------------------------------------------------
# 区间型：给定一个序列/字符串，每一步操作将会去头/去尾，使得区间长度更短
* 状态数组f[i][j]代表 子序列[i...j] 的某种性质


## 典型例题
*  https://www.lintcode.com/problem/667  
   https://leetcode.com/problems/longest-palindromic-subsequence/  
*  https://www.lintcode.com/problem/396/   (博弈+区间的混合型，两种做法，一种将状态数组定义为最大分数，一种定义为最大分数的差)
*  https://www.lintcode.com/problem/430  
   https://leetcode.com/problems/scramble-string/  
*  https://www.lintcode.com/problem/168  
   https://leetcode.com/problems/burst-balloons/  






---------------------------------------------------------------------
# 双序列型：给两个序列/字符串，每个序列是一维的，很可能两个序列的长度不一样
* 状态数组用二维f[i][j]: 第一个序列的前i个字符，第二个序列的前j个字符

## 典型例题
*  https://www.lintcode.com/problem/77  
   https://leetcode.com/problems/longest-common-subsequence/  
*  https://www.lintcode.com/problem/29  
   https://leetcode.com/problems/interleaving-string/  
*  https://www.lintcode.com/problem/119  
   https://leetcode.com/problems/edit-distance/  
*  https://www.lintcode.com/problem/118  (要特别注意初始值)
   https://leetcode.com/problems/distinct-subsequences/  
*  https://www.lintcode.com/problem/192  
   https://leetcode.com/problems/wildcard-matching/   
*  https://www.lintcode.com/problem/154  (一定要细心)
   https://leetcode.com/problems/regular-expression-matching/  
*  https://leetcode.com/problems/minimum-window-subsequence/






---------------------------------------------------------------------
# 难题集
* 如果 值域 不大，那么可以将状态数组定义为 值域 本身：  
   https://www.lintcode.com/problem/91  (核心思想：记录每一步的选择，同时保持搜索的路径是合法的)
* k-sum，如果没有k的限制，那么就是01背包，加上这个限制，则状态数组需要额外记录当前用了几个数
   https://www.lintcode.com/problem/89  
* 解空间 也许可以通过排序得出某种优化(有的时候，手动算几个例子，人脑会自动投机取巧，这样也许就有优化的空间)  
   https://www.lintcode.com/problem/76  
   https://leetcode.com/problems/longest-increasing-subsequence/  
* 双序列DP 和 Trie 的结合  
   https://www.lintcode.com/problem/623  
* 如果 值域 非常稀疏，可以考虑使用HashTable来优化  
   https://www.lintcode.com/problem/622  
   https://leetcode.com/problems/frog-jump/  
* 细心  
   https://www.lintcode.com/problem/676   
* 正方形简单，矩形的话考虑单调栈  
   https://www.lintcode.com/problem/436  
   https://leetcode.com/problems/maximal-square/  
   https://leetcode.com/problems/maximal-rectangle/  









---------------------------------------------------------------------
# buy & sell stock series
*  https://www.lintcode.com/problem/149  
   https://leetcode.com/problems/best-time-to-buy-and-sell-stock/  
*  https://www.lintcode.com/problem/150  
   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/  
*  https://www.lintcode.com/problem/151  (注意初始值为-inf而不是0)
   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
*  https://www.lintcode.com/problem/393
   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/  
*  https://www.lintcode.com/problem/1691  --> heap
*  https://www.lintcode.com/problem/1000/
*  https://www.lintcode.com/problem/995/








