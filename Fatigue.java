class Solution {
    static boolean[] visited; // 방문을 확인하기 위한 boolean 배열
    static int cnt = 0; // 방문 횟수
    
    public int solution(int k, int[][] dungeons){
        visited = new boolean[dungeons.length]; // 배열 초기화
        dfs(0,k,dungeons); // depth 0부터, dfs 탐색 시작
        return cnt;
    }
    
    private static void dfs(int depth, int fatigue, int[][] dungeons){
        for(int i=0; i<dungeons.length; i++){
            if(visited[i] || dungeons[i][0] > fatigue){ // 방문을 했거나, 던전 소모 피로도가 현재 피로도보다 크면,
                continue; // 아무 것도 하지 않음.
            }
            visited[i] = true; // 현재 위치 방문 확인
            dfs(depth+1, fatigue-dungeons[i][1], dungeons); // 다음 노드에서 다시 dfs 시작, 현재 피로도 감소.
            visited[i] = false; // 백트래킹을 하기 위한 방문 취소
        }
        cnt = Math.max(cnt,depth); // 최대 던전 수를 구함.
    }
}