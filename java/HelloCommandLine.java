public class HelloCommandLine {
    public static void main(String[] args) {
        if (args.length >= 1) {
            String name = args[0];
            System.out.println(String.format("Hello, %s!", name));
        } else {
            System.out.println("Hello, unnamed person!");
        }

    }
}