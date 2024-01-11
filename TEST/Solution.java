import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  // 입력을 위한 BufferedReader 설정
        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 수

        for (int i = 0; i < T; i++) {
            String[] input = br.readLine().split(" ");
            int start = Integer.parseInt(input[0]);
            int end = Integer.parseInt(input[1]);

            int[] swapped = swap(start, end);
            start = swapped[0];
            end = swapped[1];
  
            int result = findMinimumSamgakKimBap(start, end); // 최소 삼각김밥 개수 계산
            System.out.println("#" + (i + 1) + " " + result); // 출력
        }
        
    }

    private static int[] swap(int a, int b) {
        if (a > b) {
            return new int[] {b, a};
        }
        return new int[] {a, b};
    }
        
    private static int findFloor(int num){
        double a = 1;
        double b = 1;
        double c = -2 * num;
    
        // 이차 방정식의 근의 공식을 사용하여 n을 찾는다.
        double n = (-b + Math.sqrt(b * b - 4 * a * c)) / (2 * a);
    
        // 실제 층은 n의 올림 값
        int result = (int)Math.ceil(n);
        return result;
    }

    private static int findPositionInFloor(int num, int floor) {
        int firstNumInFloor = (floor - 1) * floor / 2 + 1;
        return num - firstNumInFloor + 1;
    }

    private static int findMinimumSamgakKimBap(int start, int end) {
        int result; // 삼각김밥 개수
        int start_floor; // 시작 층수
        int end_floor; // 도착 층수
        int start_position; // 시작 층의 인덱스
        int end_position; // 도착 층의 인덱스

        start_floor = findFloor(start); // 시작 층수 O(1)
        end_floor = findFloor(end); // 도착 층수 O(1)

        start_position = findPositionInFloor(start, start_floor); // 시작 층에서의 위치 O(1)
        end_position = findPositionInFloor(end, end_floor); // 도착 층에서의 위치 O(1)

        // 층수 차이 계산
        int floor_gap = end_floor - start_floor; // 층수 차이 O(1)

        result = calculateSamgakKimBap(start_position, end_position, floor_gap); 

        return result; 
    }

    private static int calculateSamgakKimBap(int start_position, int end_position, int floor_gap) {
        int result = 0;

        if (end_position < start_position){
            result = start_position - end_position + floor_gap;
        } else {
            if (start_position + floor_gap > end_position){
                result = floor_gap;
            } else {
                result = end_position - start_position;
            }
        }

        return result;
    }

}   