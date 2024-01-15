import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;

public class Solution_2 {
    public static void main(String[] args) throws IOException {
        // 입력을 위한 BufferedReader 설정

        // input.txt 로 버퍼 읽기
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine()); // 테스트케이스 개수

        for (int i = 0; i < T; i++) {
            String[] inputs = br.readLine().split(" ");
            int N = Integer.parseInt(inputs[0]); // 오리지널 리스트 길이 - 사용하지 않음
            int M = Integer.parseInt(inputs[1]); // 명령어 개수
            int L = Integer.parseInt(inputs[2]); // 출력할 위치
            LinkedList<String> linkedList = new LinkedList<>(Arrays.asList(br.readLine().split(" "))); // linked list _
                                                                                                       // original list
                                                                                                       // 생성

            for (int j = 0; j < M; j++) {
                String[] command = br.readLine().split(" ");
                char operation = command[0].charAt(0); // 명령어 추출
                switch (operation) {
                    case 'I':
                        int insert_position = Integer.parseInt(command[1]);
                        String insert_value = command[2];
                        linkedList.add(insert_position, insert_value);
                        break;
                    case 'D':
                        int delete_position = Integer.parseInt(command[1]);
                        linkedList.remove(delete_position);
                        break;
                    case 'C':
                        int change_position = Integer.parseInt(command[1]);
                        String change_value = command[2];

                        linkedList.set(change_position, change_value);

                        break;
                }
            }
            if (L > linkedList.size() - 1) {
                System.out.println("#" + (i + 1) + " " + "-1");
                continue;
            } else{
                System.out.println("#" + (i + 1) + " " + linkedList.get(L));    
            }
        }
        br.close();
    }
}
