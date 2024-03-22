// LCS

// Time: 0(2^(n + m)), Space: 0(n + m)
// Where n and m are the number of items in array 1 and array 2 respectively.


import 'dart:math';


int lcs(List<String> string1, List<String> string2){
  return lcsHelper(string1, string2, 0 , 0);
}

int lcsHelper(List<String> string1, List<String> string2, i1, i2){
  if (i1 == string1.length || i2 == string2.length){
    return 0;
  }

  if(string1[i1] == string2[i2]){
    return 1 + lcsHelper(string1, string2, i1 + 1, i2 + 1);
  }

  else{
    int i1Iteration = lcsHelper(string1, string2, i1 + 1, i2);
    int i2Iteration = lcsHelper(string1, string2, i1, i2 + 1);

    return max(i1Iteration, i2Iteration);

  }

}


// Returns Maximum Of Two Integers
int max(int a, int b){
 return a > b ? a : b;
}




void main() {
  print(lcs(["a", "d", "c" , "b"], ["a", "b", "c"]));
}

