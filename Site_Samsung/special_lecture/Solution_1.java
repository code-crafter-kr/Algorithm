//2024-01-15 code battle 1 - samsung expert academy

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Solution_1 {
    public static void main(String[] args) throws IOException {
        // 입력을 위한 BufferedReader 설정

        // input.txt 로 버퍼 읽기
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 10; i++) { // 10개의 테스트케이스 고정
            int command_position = 0; // 명령어 리스트 내의 추적 위치

            int T = Integer.parseInt(br.readLine()); // 오리지널 리스트 길이 - 사용하지 않음
            LinkedList<String> linkedList = new LinkedList<>(Arrays.asList(br.readLine().split(" "))); // linked list _
                                                                                                       // original list
                                                                                                       // 생성
            int N = Integer.parseInt(br.readLine()); // 명령어 개수
            LinkedList<String> commandList = new LinkedList<>(Arrays.asList(br.readLine().split(" "))); // linked list _
                                                                                                        // command list
                                                                                                        // 생성

            for (int j = 0; j < N; j++) { // 명령어 개수만큼 반복
                char operation = commandList.get(command_position).charAt(0); // 명령어 추출
                switch (operation) {
                    case 'D': // 삭제
                        int x = Integer.parseInt(commandList.get(command_position + 1)); // 삭제할 위치
                        int y = Integer.parseInt(commandList.get(command_position + 2)); // 삭제할 개수
                        delete(x, y, linkedList); // 삭제 함수 호출
                        command_position += 3; // 명령어 위치 3칸 이동
                        break;

                    case 'I': // 삽입
                        int a = Integer.parseInt(commandList.get(command_position + 1)); // 삽입할 위치
                        int b = Integer.parseInt(commandList.get(command_position + 2)); // 삽입할 개수
                        insert(command_position, a, b, commandList, linkedList); // 삽입 함수 호출
                        command_position += 3 + b; // 명령어 위치 3칸 + b칸 이동
                        break;

                    case 'A': // 추가
                        int c = Integer.parseInt(commandList.get(command_position + 1)); // 추가할 개수
                        append(command_position, c, commandList, linkedList); // 추가 함수 호출
                        command_position += 2 + c; // 명령어 위치 2칸 + c칸 이동
                        break;
                }

            }
            System.out.print("#" + (i + 1) + " "); // 출력
            for (int k = 0; k < 10; k++) {
                System.out.print(linkedList.get(k) + " ");
            }
            System.out.println();

        }

        br.close();

    }

    private static void delete(int x, int y, LinkedList<String> linkedList) {
        linkedList.subList(x, x + y).clear();
    }
    
    private static void insert(int command_position, int a, int b, LinkedList<String> commandList, LinkedList<String> linkedList) {
        List<String> tempList = new ArrayList<>(commandList.subList(command_position + 3, command_position + 3 + b));
        linkedList.addAll(a, tempList);
    }
    
    private static void append(int command_position, int c, LinkedList<String> commandList, LinkedList<String> linkedList) {
        List<String> tempList = new ArrayList<>(commandList.subList(command_position + 2, command_position + 2 + c));
        linkedList.addAll(tempList);
    }
}