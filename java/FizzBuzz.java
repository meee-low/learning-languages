import java.util.HashMap;

public class FizzBuzz {
    public static void main(String[] args) {
        smartFizzBuzz(100);
    }

    static void dumbFizzBuzz(int n) {
        assert n >= 1;

        for (int i = 1; i<=n; i++) {
            StringBuilder sb = new StringBuilder();
            if (i % 3 == 0) {
                sb.append("Fizz");
            } if (i % 5 == 0) {
                sb.append("Buzz");
            }
            else if (sb.toString().length() == 0) {
                sb.append(i);
            }
            System.out.println(sb);
        }
    }

    static void smartFizzBuzz(int n) {
        assert n >= 1;
        
        HashMap<Integer, String> map = new HashMap<Integer, String>();
        map.put(3, "Fizz");
        map.put(5, "Buzz");
        map.put(7, "Bazz");

        for (int i=1; i <= n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j : map.keySet()) {
                if (i % j == 0) {
                    sb.append(map.get(j));
                }
            }
            if (sb.toString().length() == 0) {
                sb.append(i);
            }
            System.out.println(sb);
        }
    }
}