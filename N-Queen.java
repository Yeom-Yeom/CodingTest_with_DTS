class Solution{
    private int count = 0; // 가능한 배치 방법의 수를 저장

    public int solution(int n) {
        int[] board = new int[n]; // 각 행에 배치된 퀸의 열 정보를 저장
        placeQueens(board, 0, n); // 퀸 배치 시작
        return count;
    }

    // 퀸 배치 함수
    private void placeQueens(int[] board, int row, int n) {
        if (row == n) { // 모든 퀸을 배치한 경우
            count++;
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(board, row, col)) { // 현재 위치에 배치 가능한지 확인
                board[row] = col; // 퀸 배치
                placeQueens(board, row + 1, n); // 다음 행으로 이동
                // 백트래킹: board[row] 값을 다시 확인할 필요는 없음 (덮어쓰게 됨)
            }
        }
    }

    // 해당 위치에 퀸을 배치해도 안전한지 확인
    private boolean isSafe(int[] board, int row, int col) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col || // 같은 열에 다른 퀸이 있는 경우
                Math.abs(board[i] - col) == Math.abs(i - row)) { // 대각선 상에 다른 퀸이 있는 경우
                return false;
            }
        }
        return true;
    }
}