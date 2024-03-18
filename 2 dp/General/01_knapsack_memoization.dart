// DFS With Memoization

// Time: 0(n * m), Space: O(n * m)
// Where n is the number of items & m is the capacity.


import 'dart:math';



int dfs(List<int> profit, List<int> weight, int capacity){
  int rows = profit.length;
  int columns = capacity;
  List<List<int>> cache = List.generate(rows, (_) => List<int>.filled(columns + 1, -1));
  

  return dfsHelper(cache, 0, profit, weight, capacity);
} 

int dfsHelper(List<List<int>> cache, int index,  List<int> profit, List<int> weight , int capacity){

  if(index == profit.length){
    return 0;
  }
  if(cache[index][capacity] != -1){
    return cache[index][capacity];
  }

  cache[index][capacity] = dfsHelper(cache,index + 1, profit, weight, capacity);

  int remainingCapacity = capacity - weight[index];
  int includeNodeProfit = 0;

  if(remainingCapacity >= 0){
    int includeNodeProfit = profit[index] + dfsHelper(cache, index + 1, profit, weight, remainingCapacity); // use index instead of index + 1 | for unbounded Memoization: where the weight elements can occur multiple times instead of only once 
    
    int maxProfit =  cache[index][capacity] > includeNodeProfit ? cache[index][capacity]: includeNodeProfit;
    cache[index][capacity] = maxProfit;
  }

  
  return cache[index][capacity];
}

void main() {
  print(dfs([4, 4, 7, 1], [5, 2, 3, 1], 8));
}

//   0 1 2 3 4 5 6 7 
// 0  
// 1
// 2
// 3






