import java.io.*;
import java.util.Arrays;

public class Solution_2 {
    public static void main(String[] args) throws IOException {
        // file read input_2.txt
        File file = new File("input_2.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 수

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());

            if (N < 3) { // 고려하지 않는 요원의 수
                System.out.println("#" + (i + 1) + " -1");
                // buffer
                for (int j = 0; j < N; j++) {
                    br.readLine();
                }
                continue;

            } else {
                // dp 선언
                int[][] dp = new int[N + 1][8]; // N명의 요원과 8가지 상태(000 ~ 111) 비트마스킹을 통해 111인경우만 생각
                for (int[] row : dp) {
                    Arrays.fill(row, Integer.MAX_VALUE); // 최소값을 구하기 위해 최대값으로 초기화
                }
                dp[0][0] = 0; // 초기 상태: 아무 능력치도 선택되지 않음
                // 요원 별 능력치 정리 (해당능력치를 선택했을때 소멸되는값으로 바로 정리)
                for (int j = 1; j < N + 1; j++) {
                    String[] input = br.readLine().split(" ");

                    for (int state = 0; state < 8; state++) { // 상태는 000부터 111까지
                        if (dp[j - 1][state] != Integer.MAX_VALUE) {
                            // 현재 요원이 힘을 공유하는 경우 (비트 0)
                            dp[j][state | 1] = Math.min(dp[j][state | 1],
                                    dp[j - 1][state] + Integer.parseInt(input[1]) + Integer.parseInt(input[2]));
                            // 현재 요원이 지능을 공유하는 경우 (비트 1)
                            dp[j][state | 2] = Math.min(dp[j][state | 2],
                                    dp[j - 1][state] + Integer.parseInt(input[0]) + Integer.parseInt(input[2]));
                            // 현재 요원이 민첩을 공유하는 경우 (비트 2)
                            dp[j][state | 4] = Math.min(dp[j][state | 4],
                                    dp[j - 1][state] + Integer.parseInt(input[0]) + Integer.parseInt(input[1]));
                        }
                    }

                    if (dp[j][7] == Arrays.stream(dp[j]).min().orElse(Integer.MAX_VALUE)
                            && dp[j][7] != Integer.MAX_VALUE) {
                        for (int k = j + 1; k < N + 1; k++) { // 이어받기
                            String[] input_2 = br.readLine().split(" ");
                            dp[j][7] = dp[j - 1][7] + Math.min(
                                    Math.min(Integer.parseInt(input_2[1]) + Integer.parseInt(input_2[2]),
                                            Integer.parseInt(input[0]) + Integer.parseInt(input[2])),
                                    Integer.parseInt(input[0]) + Integer.parseInt(input[1]));
                        }
                        break;
                    }
                }

                System.out.println("#" + (i + 1) + " " + dp[N][7]);

            }
        }
        br.close();
    }

}
