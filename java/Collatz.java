public class Collatz {
    public static void main(String[] args) {
	int x = 10;

	while (x > 1) {
		System.out.println(nextCollatz(x));
		x = nextCollatz(x);
        }
    }

    static int nextCollatz(int x) {
	if (x % 2 == 0){
	    return x/2;
	}
	return 3*x+1;
    } 
}
