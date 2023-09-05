import java.util.HashMap;

public class AnagramChecker {
    public static void main(String[] args) {
        HashMap<Character, Integer> counter1 = new HashMap<Character, Integer>();
        HashMap<Character, Integer> counter2 = new HashMap<Character, Integer>();
        String str1 = "banana";
        String str2 = "ananab";

        for (int i = 0; i<str1.length(); i++) {
            counter1.put(str1.charAt(i), counter1.getOrDefault(str1.charAt(i), 0) + 1);
            counter2.put(str2.charAt(i), counter2.getOrDefault(str2.charAt(i), 0) + 1);
        }

        System.out.println(counter1);
        System.out.println(counter2);
    }
}