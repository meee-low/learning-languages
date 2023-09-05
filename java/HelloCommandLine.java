public class HelloCommandLine {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(args));
        if (args.length >= 2) {
            String name = args[1];
            System.out.println(String.format("Hello, %s!", name));
        } else {
            System.out.println("Hello, unnamed person!");
        }

    }
}