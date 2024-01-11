import java.io.*;
import java.util.Arrays;

public class Solution_2_copy {
    public static void main(String[] args) throws IOException {
        // file read input_2.txt
        File file = new File("input_2.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 수
        int result = 0;
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

                }

                
                System.out.println("#" + (i + 1) + " " + result);

            }
        }
    }
