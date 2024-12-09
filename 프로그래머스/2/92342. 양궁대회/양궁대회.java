public class Solution {
    
     // 최대 점수 차이를 저장하는 변수
     private int maxDiff = 0;
     // 라이언의 최적 화살 배치를 저장하는 배열
     private int[] bestShot = new int[11];
 
     public int[] solution(int n, int[] info) {
         // 라이언의 화살 배치를 저장할 배열
         int[] ryanShot = new int[11];
         // 깊이 우선 탐색을 통해 최적의 화살 배치 계산
         dfs(n, 0, ryanShot, info);
 
         // 라이언이 우승할 방법이 없는 경우 [-1] 반환
         if (maxDiff == 0) {
             return new int[]{-1};
         }
         return bestShot;
     }
 
     private void dfs(int arrowsLeft, int index, int[] ryanShot, int[] apeachInfo) {
         // 모든 점수 영역을 탐색한 경우
         if (index == 11) {
             // 남은 화살이 있으면 0점에 추가
             if (arrowsLeft > 0) {
                 ryanShot[10] += arrowsLeft;
             }
 
             // 라이언과 어피치의 점수를 계산
             int ryanScore = 0;
             int apeachScore = 0;
 
             for (int i = 0; i < 11; i++) {
                 if (ryanShot[i] > apeachInfo[i]) {
                     ryanScore += (10 - i);
                 } else if (apeachInfo[i] > 0) {
                     apeachScore += (10 - i);
                 }
             }
 
             // 점수 차이를 계산
             int diff = ryanScore - apeachScore;
             // 점수 차이가 최대인 경우 최적 배치 갱신
             if (diff > maxDiff) {
                 maxDiff = diff;
                 bestShot = ryanShot.clone();
             } else if (diff == maxDiff) {
                 // 점수 차이가 동일한 경우 더 낮은 점수에 많은 화살을 쏜 배치를 우선
                 for (int i = 10; i >= 0; i--) {
                     if (ryanShot[i] > bestShot[i]) {
                         bestShot = ryanShot.clone();
                         break;
                     } else if (ryanShot[i] < bestShot[i]) {
                         break;
                     }
                 }
             }
             // 남은 화살을 원래 상태로 복원
             if (arrowsLeft > 0) {
                 ryanShot[10] -= arrowsLeft;
             }
             return;
         }
 
         // Case 1: 라이언이 해당 점수 영역에 화살을 쏘지 않는 경우
         dfs(arrowsLeft, index + 1, ryanShot, apeachInfo);
 
         // Case 2: 라이언이 어피치보다 1발 더 많은 화살을 쏘는 경우
         if (arrowsLeft > apeachInfo[index]) {
             ryanShot[index] = apeachInfo[index] + 1;
             dfs(arrowsLeft - ryanShot[index], index + 1, ryanShot, apeachInfo);
             // 탐색 후 원상 복구
             ryanShot[index] = 0;
         }
     }
}
