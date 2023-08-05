

---------------------------------------------------------------------  
# 二分法（二分的每一步内含了递归）:能够确定一边一定有答案，一边一定没有答案，则每次可以去掉一半
* https://www.lintcode.com/problem/1507  (BinarySearch will be TLE, use MonoStack)  
  https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/  
* https://www.lintcode.com/problem/406  (BinarySearch is not optimal, but still acceptable)  
  https://leetcode.com/problems/minimum-size-subarray-sum/    
* https://www.lintcode.com/problem/1219
  https://leetcode.com/problems/heaters/
* https://www.lintcode.com/problem/159  
  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
* https://www.lintcode.com/problem/183
https://www.lintcode.com/problem/585
https://www.lintcode.com/problem/75
https://www.lintcode.com/problem/62
https://www.lintcode.com/problem/390
https://www.lintcode.com/problem/586
https://www.lintcode.com/problem/633
https://www.lintcode.com/problem/437



---------------------------------------------------------------------  
# 单调栈：快速找到数组中 左/右边 第一个比当前元素 小/大 的元素（单调递增/减）
*   https://www.lintcode.com/problem/406  
    https://leetcode.com/problems/minimum-size-subarray-sum/  
*   https://www.lintcode.com/problem/1507  
    https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/  
https://www.lintcode.com/problem/12
https://www.lintcode.com/problem/40
https://www.lintcode.com/problem/575
https://www.lintcode.com/problem/368
栈可以反转输入的顺序，所以两个栈串联就可以模拟一个Queue
https://www.lintcode.com/problem/510
https://www.lintcode.com/problem/122
https://www.lintcode.com/problem/126



---------------------------------------------------------------------  
# 双指针
*   https://www.lintcode.com/problem/32
    https://leetcode.com/problems/minimum-window-substring/
*   https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
*   https://www.lintcode.com/problem/1375
*   https://www.lintcode.com/problem/406  
    https://leetcode.com/problems/minimum-size-subarray-sum/  
*   https://www.lintcode.com/problem/1219
    https://leetcode.com/problems/heaters/
https://www.lintcode.com/problem/384
https://www.lintcode.com/problem/386
https://www.lintcode.com/problem/328

https://www.lintcode.com/problem/539
https://www.lintcode.com/problem/415
https://www.lintcode.com/problem/39
https://www.lintcode.com/problem/32
https://www.lintcode.com/problem/363





---------------------------------------------------------------------  
# Sliding Window, Sliding Window & BreakPanel
* https://www.lintcode.com/problem/1849  
  https://leetcode.com/problems/grumpy-bookstore-owner/  
* https://www.lintcode.com/problem/151  (Sliding Window & BreakPanel, use DP instead)  
  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/  
* https://www.lintcode.com/problem/1850






---------------------------------------------------------------------  
# BFS（逐层遍历，连通性，拓扑排序，简单图的最短路径）
* 能用BFS就避免DFS，因为DFS一半会用到递归，有可能stack overflow
* https://www.lintcode.com/problem/433  
  https://leetcode.com/problems/number-of-islands/  
* https://www.lintcode.com/problem/630  
* https://www.lintcode.com/problem/1469  (两次BFS，关键要证明第一次最远路径的端点肯定在最远路径上)  
* https://leetcode.com/problems/minimum-height-trees/  (关键要证明最多有两个点)
* https://www.lintcode.com/problem/1360  (逐层遍历，每层都是回文串)  
https://www.lintcode.com/problem/69
https://www.lintcode.com/problem/1235
https://www.lintcode.com/problem/178
https://www.lintcode.com/problem/137
https://www.lintcode.com/problem/127
https://www.lintcode.com/problem/611







---------------------------------------------------------------------  
# DFS（二叉树的递归/分治，找所有方案，排列/组合）
* https://www.lintcode.com/problem/1181  
  https://leetcode.com/problems/diameter-of-binary-tree/  
* https://leetcode.com/problems/minimum-height-trees/  (DFS will TLE, use BFS)  
* https://www.lintcode.com/problem/1360  (递归，或者两次循环，即中序+前/后序)  
* https://www.lintcode.com/problem/864  (注意总和为0的情况，其实本质是划分的子树不能以跟节点开始)  
* https://www.lintcode.com/problem/153
* https://www.lintcode.com/problem/90
* https://www.lintcode.com/problem/427  
* https://www.lintcode.com/problem/815  
* https://www.lintcode.com/problem/582  
* https://www.lintcode.com/problem/634 
* https://www.lintcode.com/problem/1909 
* https://www.lintcode.com/problem/794 
* https://www.lintcode.com/problem/802 






---------------------------------------------------------------------  
# 二叉树递归/遍历
* https://www.lintcode.com/problem/1181  
  https://leetcode.com/problems/diameter-of-binary-tree/  
https://www.lintcode.com/problem/480
https://www.lintcode.com/problem/596
https://www.lintcode.com/problem/453




---------------------------------------------------------------------  
# 并查集：在Union函数里，一定不要忘记需要调用Find
* 有关图的连接性，可以考虑使用并查集
https://www.lintcode.com/problem/589
* https://www.lintcode.com/problem/433  
  https://leetcode.com/problems/number-of-islands/  




---------------------------------------------------------------------  
# 单调栈
* 求左边最小值，左/右第一个比当前值小的值：单调队列从小到大，比较 current <= stack[-1]
* 求左边最大值，左/右第一个比当前值大的值：单调队列从大到小，比较 current >= stack[-1]
* https://www.lintcode.com/problem/1852  
  https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/  
* https://www.lintcode.com/problem/285
* 单调栈的本质(从左到右)：将数组看作(idx, value)的二元组，对于(i1, v1)，求(i2, v2)满足 v2>=v1 并且 i2>i1的最小值  
* 如果反过来，数组成为二元组(value, idx)并对value进行升序排序，则对于(v1, i1)，求(v2, i2)满足 i2>=i1 并且 v2>v1的最小值，即右边 大于 本元素的 最小值  
* 同理，单调栈的本质(从右到左)：将数组看作(idx, value)的二元组，对于(i1, v1)，求(i2, v2)满足 v2>=v1 并且 i2<i1的最小值  
* 同理，反过来，数组成为二元组(value, idx)并对value进行降序排序，则对于(v1, i1)，求(v2, i2)满足 i2>=i1 并且 v2<v1的最小值，即右边 小于 本元素的 最大值
* https://www.lintcode.com/problem/1778  
  https://leetcode.com/problems/odd-even-jump/  

## 单调栈与双端队列(Deque)的结合：滑动窗口的最值  
* https://www.lintcode.com/problem/362  
  https://leetcode.com/problems/sliding-window-maximum/
* https://www.lintcode.com/problem/290







---------------------------------------------------------------------  
# 扫描线（此类问题一般需要把区间拆开）
* https://www.lintcode.com/problem/156
* https://www.lintcode.com/problem/919
* https://www.lintcode.com/problem/850
https://www.lintcode.com/problem/391
https://www.lintcode.com/problem/131










递归
subset
https://www.lintcode.com/problem/17
https://www.lintcode.com/problem/18





链表
https://www.lintcode.com/problem/105
https://www.lintcode.com/problem/103
https://www.lintcode.com/problem/98


数组
https://www.lintcode.com/problem/64
https://www.lintcode.com/problem/547
https://www.lintcode.com/problem/65
https://www.lintcode.com/problem/139


哈希表
https://www.lintcode.com/problem/1237
https://www.lintcode.com/problem/134





Two sum
https://www.lintcode.com/problem/56
https://www.lintcode.com/problem/608
https://www.lintcode.com/problem/587
https://www.lintcode.com/problem/57
https://www.lintcode.com/problem/382
https://www.lintcode.com/problem/533
https://www.lintcode.com/problem/59
https://www.lintcode.com/problem/610

Partition array
https://www.lintcode.com/problem/144
https://www.lintcode.com/problem/148
https://www.lintcode.com/problem/143

堆
见到需要维护一个集合的最小值/最大值的时候要想到用堆
为什么教科书里的最大/小堆没有decrease/increase key？可能是因为历史上其被用于Dijkstra's，但其实实现起来很简单。
堆的删除(删除最大/最小)：将其与最后一个元素交换，然后递归的在交换的位置call top-down heapify
堆的删除(删除任意值)：将其与最后一个元素交换，然后根据交换过来的元素与其parent的比较，调用top-down heapify或者bottom-up heapify
堆的插入(插入任意值)：插入于最后一个元素（堆的长度+1），然后bottom-up heapify
https://www.lintcode.com/problem/401
https://www.lintcode.com/problem/364
https://www.lintcode.com/problem/81
https://www.lintcode.com/problem/360
HashHeap: https://www.jiuzhang.com/solution/hashheap/







Trie树
可以查询某个单词是否存在，查询以某个前缀开始的所有单词
不能删除
代码模板要求在10分钟内写完
要把字典（而不是矩阵）建成Trie树，因为矩阵的可能性太多，等同于完成了全部的DFS遍历，而加上Trie树的约束后，相当于有了很多剪枝
矩阵类字符串一个一个字符深度遍历的问题(DFS+TRIE)
https://www.lintcode.com/problem/132  (本题纯DFS也可以做，但是加上Trie后可以记录前缀是否可以到达)
https://www.lintcode.com/problem/634
https://www.lintcode.com/problem/1159  (构建Trie树，然后寻找LCA。LCA可以当作RMQ问题，可以用线段树)
https://www.lintcode.com/problem/270   (构建字符->数字的反向Trie)
https://www.lintcode.com/problem/635   (Trie+DFS，需要优化DFS的搜索顺序)
https://www.lintcode.com/problem/1848
https://www.lintcode.com/problem/623   (Trie+DFS+DP)


线段树（要注意lazy标记的定义，常见的是【已经加到本节点，但尚未加到子节点的值】）
https://www.lintcode.com/problem/1329
https://www.lintcode.com/problem/1159  (构建Trie树，然后寻找LCA。LCA可以当作RMQ问题，可以用线段树)
https://www.lintcode.com/problem/1159  (使用扫描线会更快)
https://www.lintcode.com/problem/751   (使用双端队列会更快)


二叉索引树（binary index tree）
https://www.lintcode.com/problem/290


SparseTable（适合求任意区间最大/小值）
https://www.topcoder.com/thrive/articles/Range%20Minimum%20Query%20and%20Lowest%20Common%20Ancestor
https://www.lintcode.com/problem/205




小知识
栈空间和堆空间: https://www.cnblogs.com/kevinGaoblog/archive/2012/03/23/2413102.html
递归三要素：递归的定义，递归的拆解（每一步干什么），递归的出口（bottom case）
基本上每个公司都会考拓扑排序(topological sort)，大概率会用到BFS宽度优先搜索
BFS只适合于简单图（边无方向，边无权重，两点最多一条边，没有自己到自己的边）的最短路径
最长路径可以考虑DP或者DFS搜索
一般情况下DFS都是递归实现
所有的切割问题都是组合问题（每个位置切或者不切）
OnSite时一般需要做两道题，做完第一道再给第二道。如果做的慢只做了一道，面试官嘴上不说，但一般给挂。


BinaryString: 可以求Presum，前缀和等于1的数量
https://leetcode.com/problems/flip-string-to-monotone-increasing/

一个字符的差别，可以考虑使用通配符：https://leetcode.com/problems/word-ladder/






