// prices       = [1,2,3,0,2]
// transactions = []
// buy cooldown sell

  class Key {
    final bool buying;
    final int index;

    Key(this.buying, this.index);

    @override
    bool operator ==(Object other) {
      if (identical(this, other)) return true;

      return other is Key && other.buying == buying && other.index == index;
    }

    @override
    int get hashCode => buying.hashCode ^ index.hashCode;
  }
  Map<Key, int> cache = {};

  int maxProfit(List<int> prices) {
      int maxProfit = bestTimeToTradeHelper(true, prices, 0);
      return maxProfit;
  }

  int bestTimeToTradeHelper(
      bool buying, List<int> prices, int index) {
  if (prices.length == 1) {
      return 0;
  }
  if (index >= prices.length) {
      return 0;
  }

  if(cache.containsKey([buying, index])){
    return cache[[buying, index]] ?? 0;
  }



  if(buying == true){
      int buyProfit = bestTimeToTradeHelper(!buying, prices, index + 1) - prices[index];
      int coolDownProfit = bestTimeToTradeHelper(buying, prices, index + 1);
      cache[Key(buying, index)] = max(buyProfit, coolDownProfit);

  }
  else{
      int sellProfit = bestTimeToTradeHelper(!buying, prices, index + 2) + prices[index];
      int coolDownProfit = bestTimeToTradeHelper(buying, prices, index + 1);
      cache[Key(buying, index)]=  max(sellProfit, coolDownProfit);
  }

  return cache[Key(buying, index)] ?? 0;
  }

  int max(int a, int b){
    return a > b ? a : b;
  }


void main() {
  print(maxProfit([1, 2, 3, 0, 2]));
}
