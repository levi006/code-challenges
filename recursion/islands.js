var test = [
    [1,1,0,0,1],
    [0,1,0,0,1],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,1,0,0,0]
]

console.log(test);

function islands(matrix){
    var count = 0;
    
    for (var y = 0; y < matrix.length; y++){
        for (var x = 0; x < matrix[0].length; x++){
            if (matrix[y][x] === 1){
                count++;
                traverse(x, y);
            }
        }
    }
    
    function traverse(x, y){
        if (x < 0 || y < 0 || y >= matrix.length || x >= matrix[0].length){
            return;
        } else if (matrix[y][x] === 0){
            return;
        }
        
        matrix[y][x] = 0;
        
        traverse(x+1, y);
        traverse(x-1, y);
        traverse(x, y+1);
        traverse(x, y-1);
    }
    
    return count;
}

// console.log(islands(test));


/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
  var prev = 1;
  var latestLocalMaxIndex = 0;
  var latestLocalMaxValue = 1;
  var results = 1;

  for (var i = 1; i < ratings.length; i++){
    if (ratings[i] < ratings[i-1]){
      // Case 1 : rating is lower than previous value
      if (i - latestLocalMaxIndex >= latestLocalMaxValue){
        results += i - latestLocalMaxIndex + 1;
      }else {
        results += i - latestLocalMaxIndex;
      }
      prev = 1;
    }else if (ratings[i] > ratings[i-1]){
      // Case 2 : rating is higher than previous value
      prev++;
      results += prev;
      latestLocalMaxValue = prev;
      latestLocalMaxIndex = i;
    }else {
      // Case 3 : rating is equal to previous value
      latestLocalMaxIndex = i;
      latestLocalMaxValue = 1;
      prev = 1;
      results += prev;
    }
  }
  return results;
};

