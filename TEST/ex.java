import java.io.IOException;

public class ex {
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

    public static void main(String[] args) throws IOException {
        System.out.println(findFloor(11));
    }

}
