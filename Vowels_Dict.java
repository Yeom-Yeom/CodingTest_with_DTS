import java.util.*;

class Solution {
    static List<String> list; // 단어가 들어갈 리스트
    static String[] words = {"A","E","I","O","U"}; // 모음 배열
    
    public int solution(String word){
        int ans = 0;
        list = new ArrayList<>();
        dfs("",0); // 비어있는 단어 부터
        int size = list.size(); // 리스트의 길이 만큼
        for(int i=0; i<size; i++){ 
            if(list.get(i).equals(word)){ // i 번째가 주어진 word와 같다면
                ans = i; // ans = i, break
                break;
            }
        }
        return ans;
    }
    
    static void dfs(String str, int len){
        list.add(str); // list에 비어있는 str부터 입력
        if(len == 5) return; // 길이가 5라면 반환
        for(int i=0; i<5; i++){ 
            dfs(str+words[i], len+1); // A,E,I,O,U 하나씩 더한 값을 dfs
        }
    }
}