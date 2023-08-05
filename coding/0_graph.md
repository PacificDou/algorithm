---------------------------------------------------------------------  
# 经验总结
* 能用BFS尽量使用BFS，避免DFS，因为后者可能会造成stack overflow
* 邻接矩阵比较占空间，但是可以快速查询a, b两点之间是否连通
* 邻接表比较省空间，但是不能快速查询两点之间的连通性。不过，可以使用Set（无权边）或者Dict（任意权重）来加快连通性查询。
* 基本上关于树的题，都可以考虑分治和遍历来解答，即DFS
* DFS三大考点：树的分治和遍历；求所有方案（每个方案就是一条路径）；求排列组合




---------------------------------------------------------------------  
# 简单图的最短路径：BFS
BFS可以处理简单图的最短路径，这里的简单图是指：边无方向，边无权重（或者权重都是1），每个点最多访问一次
更为严格的定义，简单图是指：边无方向，边无权重（或者权重都是1），两点之间最多一条边，没有自环（自己到自己的边）
其实如果图中有环，但是可以证明每个点最多访问一次，BFS也是可以适用的
* https://www.lintcode.com/problem/1565  (两层BFS)  
* https://www.lintcode.com/problem/573
* https://www.lintcode.com/problem/794
* https://www.lintcode.com/problem/120
* https://www.lintcode.com/problem/630
* https://www.lintcode.com/problem/950


---------------------------------------------------------------------  
# 复杂图的最短路径：SPFA(Shortest Path Fast Algorithm)，Floyd，Dijkstra，Bellman-ford
* SPFA可以处理负边权和负环，可以理解为用BFS实现的Bellman-Ford
* Dijkstra不可以处理负边权和负环，使用的是贪心的思想。BFS使用Heap优化后就是Dijkstra，所以Dijkstra不能处理负边。
* Bellman-ford稍微改进就可以得到BFS，现在用的很少
* Floyd是唯一可以处理多源多终点的算法，其他都是单源
* https://www.lintcode.com/problem/1565  (SPFA)  
* https://www.lintcode.com/problem/789




---------------------------------------------------------------------  
# BFS与SPFA的区别
* BFS: 没有访问过的点就加入队列
* SPFA: 如果到达该点的路径变短了就把该点加入队列
* SPFA对于负环的处理，需要定义一个计数器，记录每个节点入队的次数，如果次数大于N(节点数量)，那么该点就在负环上
* SPFA的优化，可以使用Heap，有限访问边权较小的边
* 双向BFS的优化（没有双向SPFA），可以将复杂度从2^n降到2^(n/2)，即sqrt(2^n)。




---------------------------------------------------------------------  
# 二叉树的结构
* 前序+中序 可以 唯一确定
* 后序+中序 可以 唯一确定
* 前序+后序 不可以 唯一确定
* https://www.lintcode.com/problem/1360  (递归，或者两次循环，即中序+前/后序)  





https://www.lintcode.com/problem/1565/
https://www.lintcode.com/problem/1422/
https://www.lintcode.com/problem/1628/
https://www.lintcode.com/problem/778/
https://www.lintcode.com/problem/1469/   (两次BFS可以求树的最长路径)
https://www.lintcode.com/problem/291     (最长路径的某个端点必然是第二长路径的端点；同理，第n长路径的某个端点必然是第n-1长路径的端点)
https://www.lintcode.com/problem/634
https://www.lintcode.com/problem/94/     (注意负节点)
https://www.lintcode.com/problem/652/    (注意不要重复，需要限制加入的顺序)
https://www.lintcode.com/problem/17/
https://www.lintcode.com/problem/18/
https://www.lintcode.com/problem/1514/   (注意要复位，包括方向和位置)
https://www.lintcode.com/problem/635/    (DFS+Trie，加入新单词后，需要优化DFS搜索顺序，代码较复杂)

