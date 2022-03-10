function solution(a, b) {
    
  let answer = '';
  let days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
  let temp = 0;
  for (let i = 1; i < a; i++ ) {
      temp += days[i-1];
  }
  temp += b - 1;
  answer = day[temp % 7];
  return answer;
}