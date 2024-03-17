import 'dart:math';

int lcs(List<String> string1, List<String> string2){
  int rows = string1.length;
  int columns = string2.length;

  List<List<int>> cache = List.generate(rows, (_) => List<int>.filled(columns + 1, -1));

  return lcsHelper(string1, string2, 0 , 0, cache);
}

int lcsHelper(List<String> string1, List<String> string2, i1, i2, List<List<int>> cache){
  if (i1 == string1.length || i2 == string2.length){
    return 0;
  }
  if(cache[i1][i2] != -1){
    return cache[i1][i2];
  }

  if(string1[i1] == string2[i2]){
    cache[i1][i2] = (1 + lcsHelper(string1, string2, i1 + 1, i2 + 1, cache)) as int;
  }


  else{
    int i1Iteration = lcsHelper(string1, string2, i1 + 1, i2, cache);
    int i2Iteration = lcsHelper(string1, string2, i1, i2 + 1, cache);

    int maximum = max(i1Iteration, i2Iteration);
    cache[i1][i2] = maximum;


  }

   return cache[i1][i2];

}


// Returns Maximum Of Two Integers
int max(int a, int b){
 return a > b ? a : b;
}




void main() {
  print(lcs(["a", "d", "c" , "b"], ["a", "b", "c"]));
}







