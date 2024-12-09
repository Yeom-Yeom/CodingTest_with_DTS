import java.util.*;

public class Shortest_Distance_Game_Map {
    // 상,하,좌,우 이동 배열
    private static int[] dx = {0,-1,0,1};
    private static int[] dy = {1,0,-1,0};

    public int solution(int[][] maps){
        int n = maps.length; // 행
        int m = maps[0].length; // 열

        return bfs(maps, n,m);
    }

    private int bfs(int[][]maps, int n, int m){
        // 방문 여부를 위한 배열
        boolean[][] visited = new boolean[n][m];
        // BFS를 위한 큐
        Queue<int[]> queue = new LinkedList<>();
        // 시작 위치 삽입(x,y,이동 거리)
        queue.offer(new int[]{0,0,1});
        visited[0][0] = true;

        while(!queue.isEmpty()){
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];
            int dist = cur[2];
            // 상대 팀 진영에 도착한 경우 이동 거리 반환.
            if(x==n-1 && y==m-1){
                return dist;
            }
            
            // 네 방향 탐색
            for(int i=0; i<4; i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                // 맵 범위를 벗어나거나 벽이거나 이미 방문한 경우 무시
                if (nx<0 || ny<0 || nx>=n || ny>=m || maps[nx][ny] == 0 || visited[nx][ny])
                    continue;
                
                // 다음 위치를 큐에 추가하고 방문 처리
                queue.offer(new int[]{nx,ny,dist+1});

                visited[nx][ny] = true;
            }
           
        }
        // 상대팀 진영에 도착할 수 없는 경우 -1 반환
        return -1;
    }

    
}
