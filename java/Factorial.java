public class Factorial {
    public static void main (String[] args) {
        System.out.println(factorial(6));
    }

    static int factorial(int n) {
        assert n >= 0;

        if (n == 0) {
            return 1;
        }
        return n * factorial(n-1);
    }

}