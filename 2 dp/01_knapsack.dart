import 'dart:math';


// Time: 0(2^n), Space: 0(n)

int dfs(List<int> profit, List<int> weight, int capacity){
  return dfsHelper(0, profit, weight, capacity);
} 

int dfsHelper(int index,  List<int> profit, List<int> weight , int capacity){

  if(index == profit.length){
   return 0;
  }

  int skipNodeProfit = dfsHelper(index + 1, profit, weight, capacity);
  int includeNodeProfit = 0;
  int remainingCapacity = capacity - weight[index];

  if(remainingCapacity > 0){
    includeNodeProfit = profit[index] + dfsHelper(index + 1, profit, weight, remainingCapacity); // use index instead of index + 1 | for unbounded Memoization: where the weight elements can occur multiple times instead of only once 
  }
  
  return max(skipNodeProfit, includeNodeProfit);
}

void main() {
  print(dfs([4, 4, 7, 1], [5, 2, 3, 1], 8));
}

//(skipNodeProfit, remainingCapacity, index) // (includeNodeProfit, remainingCapacity, index)
