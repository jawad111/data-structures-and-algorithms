// Returns Total number of Paths from top to bottom in a two dimentional grid
int countPaths(int rows, int columns){
  List<int> previousRow = List.generate(columns, (_)=> 0);
  
  for(int r = (rows - 1); r >= 0; r--){

    List<int> currentRow = List.generate(columns , (_)=>0);
    currentRow[columns -1] = 1;

    for(int c = (columns - 2); c >= 0; c--){

      currentRow[c] = currentRow[c + 1] + previousRow[c];
    
    }

    previousRow = currentRow;
  }



  return previousRow[0];
}


void main(){
  print(countPaths(4,4 ));
}