public class Fibonacci {
    public static void main (String[] args) {
        for (int i = 0; i < 20; i++){
            System.out.print(fibonacci(i));
            System.out.print(" ");
        }
        System.out.print("\n");
    }

    static int fibonacci(int n) {
        assert n >= 0;

        if (n < 2) {
            return 1;
        }
        return fibonacci(n-1) + fibonacci(n-2);
    }

}