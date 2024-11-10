funcs = [
    {"original_prefix":
     """public class ADD {
    public static int add(int x, int y) {
""",
     "prefix":
     """public class ADD {
    public static int add(int x, int y) {
// buggy code
//        return x | y;    
        """,
     "suffix":
     """
    }
}
"""},
    {"original_prefix":
     """public class ADD_ELEMENTS {
    public static int add_elements(ArrayList<Integer> arr, int k) {
        int result = 0;
        for(int i = 0; i < k; i++) {
""",
     "prefix":
     """public class ADD_ELEMENTS {
    public static int add_elements(ArrayList<Integer> arr, int k) {
        int result = 0;
        for(int i = 0; i < k; i++) {
// buggy code
//            if(Integer.toString(arr.get(i)).length() >= 2) {
//                result -= arr.get(i);
            """,
     "suffix":
     """
            }
        }
        return result;
    }
}
"""},
    {"original_prefix":
     """public class ADD_EVEN_AT_ODD {
    public static int add_even_at_odd(int[] lst) {
        int sum = 0;
""",
     "prefix":
     """public class ADD_EVEN_AT_ODD {
    public static int add_even_at_odd(int[] lst) {
        int sum = 0;
// buggy code
//        for (int i = 0; i < lst.length; i += 1) {
        """,
     "suffix":
     """
            if (lst[i] % 2 == 0)
                sum += lst[i];
        }
        return sum;
    }
}
"""},
    {"original_prefix":
     """public class ALL_PREFIXES {
    public static List<String> all_prefixes(String string){
        List<String> result = new ArrayList<String>();

        for (int i = 0; i < string.length(); i += 1){
""",
     "prefix":
     """public class ALL_PREFIXES {
    public static List<String> all_prefixes(String string){
        List<String> result = new ArrayList<String>();

        for (int i = 0; i < string.length(); i += 1){
// buggy code
//            result.add(string.substring(i + 1));
            """,
     "suffix":
     """
        }

        return result;
    }
}
"""},
    {"original_prefix":
     """public class ANTI_SHUFFLE {
    public static String anti_shuffle(String s) {
        String result = "";
        for (String str : s.split(" ")) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
""",
     "prefix":
     """public class ANTI_SHUFFLE {
    public static String anti_shuffle(String s) {
        String result = "";
        for (String str : s.split(" ")) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
// buggy code
//            result += new String(chars);
//        }
//        return result;
            """,
     "suffix":
     """
    }
}
"""},
    {"original_prefix":
     """public class ANY_INT {
    public static boolean any_int(double x, double y, double z) {
""",
     "prefix":
     """public class ANY_INT {
    public static boolean any_int(double x, double y, double z) {
// buggy code
//        if ((int)x == x && (int)y == y) {
//            if (x + y == z || x + z == y)
        """,
     "suffix":
     """
                return true;
        }
        return false;
    }
}
"""},
    {"original_prefix":
     """public class BELOW_THRESHOLD {
    public static boolean below_threshold(int[] l, int t) {
        for (int i = 0; i < l.length; i += 1) {
""",
     "prefix":
     """public class BELOW_THRESHOLD {
    public static boolean below_threshold(int[] l, int t) {
        for (int i = 0; i < l.length; i += 1) {
// buggy code
//            if (l[i] <= t)
//                return true;
//        }
//        return false;
            """,
     "suffix":
     """
    }
}
"""},
    {"original_prefix":
     """public class BELOW_ZERO {
    public static boolean below_zero(List<Integer> operations) {
        int balance = 0;
        for (Integer op : operations){
            balance += op;
""",
     "prefix":
     """public class BELOW_ZERO {
    public static boolean below_zero(List<Integer> operations) {
        int balance = 0;
        for (Integer op : operations){
            balance += op;
// buggy code
//            if (balance > 0){
//                return false;
//            }
//        }
//        return true;
            """,
     "suffix":
     """
    }
}
"""},
    {"original_prefix":
     """public class BF {
    public static ArrayList<String> bf(String planet1, String planet2) {
        ArrayList<String> planet_names = new ArrayList<String>(Arrays.asList(
            "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
        ));

        ArrayList<String> result = new ArrayList<String>();
        if ((! planet_names.contains(planet1)) || (! planet_names.contains(planet2)))
            return result;
        int planet1_index = planet_names.indexOf(planet1);
        int planet2_index = planet_names.indexOf(planet2);
""",
     "prefix":
     """public class BF {
    public static ArrayList<String> bf(String planet1, String planet2) {
        ArrayList<String> planet_names = new ArrayList<String>(Arrays.asList(
            "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
        ));

        ArrayList<String> result = new ArrayList<String>();
        if ((! planet_names.contains(planet1)) || (! planet_names.contains(planet2)))
            return result;
        int planet1_index = planet_names.indexOf(planet1);
        int planet2_index = planet_names.indexOf(planet2);
// buggy code
//        for (int i = planet1_index; i < planet2_index; i += 1)
//            result.add(planet_names.get(i));
        """,
     "suffix":
     """
        return result;
    }
}
"""},
    {"original_prefix":
     """public class BY_LENGTH {
    public static ArrayList<String> by_length(ArrayList<Integer> a) {
        Map<Integer, String> digit_map = new HashMap<>();
        digit_map.put(1, "One");
        digit_map.put(2, "Two");
        digit_map.put(3, "Three");
        digit_map.put(4, "Four");
        digit_map.put(5, "Five");
        digit_map.put(6, "Six");
        digit_map.put(7, "Seven");
        digit_map.put(8, "Eight");
        digit_map.put(9, "Nine");
        Collections.sort(a, Collections.reverseOrder());
        ArrayList<String> result = new ArrayList<>();
        for(int num : a) {
""",
     "prefix":
     """public class BY_LENGTH {
    public static ArrayList<String> by_length(ArrayList<Integer> a) {
        Map<Integer, String> digit_map = new HashMap<>();
        digit_map.put(1, "One");
        digit_map.put(2, "Two");
        digit_map.put(3, "Three");
        digit_map.put(4, "Four");
        digit_map.put(5, "Five");
        digit_map.put(6, "Six");
        digit_map.put(7, "Seven");
        digit_map.put(8, "Eight");
        digit_map.put(9, "Nine");
        Collections.sort(a, Collections.reverseOrder());
        ArrayList<String> result = new ArrayList<>();
        for(int num : a) {
// buggy code
//            if(digit_map.get(num) != "") {
            """,
     "suffix":
     """
                result.add(digit_map.get(num));
            }
        }
        return result;
    }
}
"""},
    {"original_prefix":
     """public class CAN_ARRANGE {
    public static int can_arrange(int[] arr) {
""",
     "prefix":
     """public class CAN_ARRANGE {
    public static int can_arrange(int[] arr) {
// buggy code
//        int ind = 1;
//        for(int i = 0; i < arr.length - 1; i++) {
//            if(arr[i] < arr[i + 1]) ind = i + 1;
        """,
     "suffix":
     """
        }
        return ind;
    }
}
"""},
    {"original_prefix":
     """public class CAR_RACE_COLLISION {
    public static int car_race_collision(int n) {
""",
     "prefix":
     """public class CAR_RACE_COLLISION {
    public static int car_race_collision(int n) {
// buggy code
//        return n;
        """,
     "suffix":
     """
    }
}
"""},
    {"original_prefix":
     """public class CHANGE_BASE {
    public static String change_base(int x, int base) {
        String result = "";

        while (x > 0) {
""",
     "prefix":
     """public class CHANGE_BASE {
    public static String change_base(int x, int base) {
        String result = "";

        while (x > 0) {
// buggy code
//            result = result + x % base;
//            x = x - x / base;
            """,
     "suffix":
     """
        }
        return result;
    }
}
"""},
    {"original_prefix":
     """public class CHECK_DICT_CASE {
    public static boolean check_dict_case(HashMap<Object, Object> dict) {
        if (dict.size() == 0)
            return false;
        else {
            String state = "start";
            for (Object key : dict.keySet()) {
                if (!(key instanceof String)) {
                    state = "mixed";
                    break;
                }
                String str_key = (String) key;
                if (state.equals("start")) {
                    if (str_key.toUpperCase().equals(str_key))
                        state = "upper";
                    else if (str_key.toLowerCase().equals(str_key))
                        state = "lower";
                    else {
                        state = "mixed";
                        break;
                    }
""",
     "prefix":
     """public class CHECK_DICT_CASE {
    public static boolean check_dict_case(HashMap<Object, Object> dict) {
        if (dict.size() == 0)
            return false;
        else {
            String state = "start";
            for (Object key : dict.keySet()) {
                if (!(key instanceof String)) {
                    state = "mixed";
                    break;
                }
                String str_key = (String) key;
                if (state.equals("start")) {
                    if (str_key.toUpperCase().equals(str_key))
                        state = "upper";
                    else if (str_key.toLowerCase().equals(str_key))
                        state = "lower";
                    else {
                        state = "mixed";
                        break;
                    }
// buggy code                    
//                } else if (state.equals("upper") && !str_key.toUpperCase().equals(str_key)) {
                """,
     "suffix":
     """
                    state = "mixed";
                    break;
                }
            }
            return (state.equals("upper")) || (state.equals("lower"));
        }
    }
}
"""},
    {"original_prefix":
     """public class CHECK_IF_LAST_CHAR_IS_A_LETTER {
    public static boolean check_if_last_char_is_a_letter(String txt) {
        String[] parts = txt.split(" ");
        String last = " ";
""",
     "prefix":
     """public class CHECK_IF_LAST_CHAR_IS_A_LETTER {
    public static boolean check_if_last_char_is_a_letter(String txt) {
        String[] parts = txt.split(" ");
        String last = " ";
// buggy code
//        last = parts[parts.length - 1];
//        if(txt.charAt(txt.length() - 1) == ' ') last = " ";
//        if(txt.length() == 1) last = " ";
//        int last_char_pos = Character.toUpperCase(last.charAt(0)) - 'a';
//        return (last.length() == 1) || (0 <= last_char_pos || last_char_pos <= 25);
        """,
     "suffix":
     """
    }
}
"""},
    {"original_prefix":
     """public class CHOOSE_NUM {
    public static int choose_num(int x, int y) {
""",
     "prefix":
     """public class CHOOSE_NUM {
    public static int choose_num(int x, int y) {
// buggy code
//        if(x < y) return -1;
        """,
     "suffix":
     """
        if((y % 2) == 0) return y;
        if(x == y) return -1;
        return y - 1;
    }
}
"""},
    {"original_prefix":
     """public class CIRCULAR_SHIFT {
    public static String circular_shift(int x, int shift) {
        String s = x + "";

        if (shift > s.length()) {
            StringBuilder sb = new StringBuilder();
            for (int i = s.length() - 1; i >= 0; i -= 1)
                sb.append(s.charAt(i));
            return sb.toString();
        } else {
""",
     "prefix":
     """public class CIRCULAR_SHIFT {
    public static String circular_shift(int x, int shift) {
        String s = x + "";

        if (shift > s.length()) {
            StringBuilder sb = new StringBuilder();
            for (int i = s.length() - 1; i >= 0; i -= 1)
                sb.append(s.charAt(i));
            return sb.toString();
        } else {
// buggy code
//            return s.substring(s.length() - shift + 1) + s.substring(0, s.length() - shift - 1);
            """,
     "suffix":
     """
        }
    }
}
"""},
    {"original_prefix":
     """public class CLOSEST_INTEGER {
    public static int closest_integer(String value) {
        if (value.indexOf('.') >= 0) {
            while (value.charAt(value.length() - 1) == '0')
                value = value.substring(0, value.length() - 1);
        }

        double num = Double.parseDouble(value);
        int result = 0;
""",
     "prefix":
     """public class CLOSEST_INTEGER {
    public static int closest_integer(String value) {
        if (value.indexOf('.') >= 0) {
            while (value.charAt(value.length() - 1) == '0')
                value = value.substring(0, value.length() - 1);
        }

        double num = Double.parseDouble(value);
        int result = 0;
// buggy code
//        if (value.substring(value.length() - 2).equals(".5")) {
//            result = num > 0 ? (int)Math.floor(num) : (int)Math.ceil(num);
        """,
     "suffix":
     """
        } else if (value.length() > 0){
            result = (int)Math.round(num);
        }

        return result;
    }
}
"""},
    {"original_prefix":
     """public class COMMON {
    public static int[] common(int[] l1, int[] l2) {
""",
     "prefix":
     """public class COMMON {
    public static int[] common(int[] l1, int[] l2) {
// buggy code
//        ArrayList<Integer> common = new ArrayList<Integer>();
        """,
     "suffix":
     """
        
        for (int i = 0; i < l1.length; i += 1){
            for (int j = 0; j < l2.length; j += 1){
                if (l1[i] == l2[j])
                    common.add(l1[i]);
            }
        }
        int[] result = new int[common.size()];
        int index = 0;
        for (Integer c : common) {
            result[index] = c;
            index += 1;
        }
        Arrays.sort(result);
        return result;
    }
}
"""},
    {"original_prefix":
     """public class COMPARE {
    public static int[] compare(int[] game, int[] guess) {
        int[] result = new int[game.length];

        for (int i = 0; i < game.length; i += 1) {
""",
     "prefix":
     """public class COMPARE {
    public static int[] compare(int[] game, int[] guess) {
        int[] result = new int[game.length];

        for (int i = 0; i < game.length; i += 1) {
// buggy code
//            result[i] = Math.floorDiv(game[i], guess[i]);
            """,
     "suffix":
     """
        }

        return result;
    }
}
"""},
    {"original_prefix":
     """public class COMPARE_ONE {
    public static Object compare_one(Object a, Object b) {
        double temp_a = 0, temp_b = 0;
        if(a instanceof String) {
            String temp_a_string = a.toString();
            temp_a_string = temp_a_string.replace(',', '.');
            temp_a = Double.parseDouble(temp_a_string);
        }
        if(b instanceof String) {
            String temp_b_string = b.toString();
            temp_b_string = temp_b_string.replace(',', '.');
            temp_b = Double.parseDouble(temp_b_string);
        }
""",
     "prefix":
     """public class COMPARE_ONE {
    public static Object compare_one(Object a, Object b) {
        double temp_a = 0, temp_b = 0;
        if(a instanceof String) {
            String temp_a_string = a.toString();
            temp_a_string = temp_a_string.replace(',', '.');
            temp_a = Double.parseDouble(temp_a_string);
        }
        if(b instanceof String) {
            String temp_b_string = b.toString();
            temp_b_string = temp_b_string.replace(',', '.');
            temp_b = Double.parseDouble(temp_b_string);
        }
// buggy code
//        if(a instanceof Double) temp_a = ((Integer) b).doubleValue();
//        if(b instanceof Double) temp_b = ((Integer) a).doubleValue();
//        if(a instanceof Integer) temp_a = (Double) a;
//        if(b instanceof Integer) temp_b = (Double) b;
        """,
     "suffix":
     """
        if(temp_a == temp_b) return null;
        if(temp_a > temp_b) return a;
        else return b;
    }
}
"""},
    {"original_prefix":
     """public class CONCATENATE {
    public static String concatenate(String[] strings) {
""",
     "prefix":
     """public class CONCATENATE {
    public static String concatenate(String[] strings) {
// buggy code
//        String result = null;
        """,
     "suffix":
     """
        for (String string : strings)
            result += string;
        return result;
    }
}
"""},
    {"original_prefix":
     """public class CORRECT_BRACKETING {
    public static boolean correct_bracketing(String brackets) {
        int depth = 0;
        for (char b : brackets.toCharArray()) {
            if (b == '<')
                depth += 1;
            else
                depth -= 1;
""",
     "prefix":
     """public class CORRECT_BRACKETING {
    public static boolean correct_bracketing(String brackets) {
        int depth = 0;
        for (char b : brackets.toCharArray()) {
            if (b == '<')
                depth += 1;
            else
                depth -= 1;
// buggy code
//            if (depth >= 0)
//                return true;
//        }
//        return false;
            """,
     "suffix":
     """
    }
}
"""},
    {"original_prefix":
     """public class COUNT_DISTINCT_CHARACTERS {
    public static int count_distinct_characters(String string) {
        HashSet<Character> distinct = new HashSet<Character>();

        for (char c : string.toCharArray()) {
            if (! distinct.contains(Character.toLowerCase(c)))
""",
     "prefix":
     """public class COUNT_DISTINCT_CHARACTERS {
    public static int count_distinct_characters(String string) {
        HashSet<Character> distinct = new HashSet<Character>();

        for (char c : string.toCharArray()) {
            if (! distinct.contains(Character.toLowerCase(c)))
// buggy code
//                distinct.add(c);
                """,
     "suffix":
     """
        }
        return distinct.size();
    }
}
"""},
    {"original_prefix":
     """public class COUNT_NUMS {
    public static int count_nums(ArrayList<Integer> arr) {
        int count = 0;
        for(int num : arr) {
            boolean neg = num < 0;
""",
     "prefix":
     """public class COUNT_NUMS {
    public static int count_nums(ArrayList<Integer> arr) {
        int count = 0;
        for(int num : arr) {
            boolean neg = num < 0;
// buggy code
//            if(neg) num *= 1;
            """,
     "suffix":
     """
            String num_string = Integer.toString(num);
            int sum = 0;
            for(int i = 0; i < num_string.length(); i++) {
                if((i == 0) && neg) sum -= num_string.charAt(i) - '0';
                else sum += num_string.charAt(i) - '0';
            }
            if(sum > 0) count++;
        }
        return count;
    }
}
"""},
    {"original_prefix":
     """public class COUNT_UP_TO {
    public static List<Integer> count_up_to(int n) {
        List<Integer> primes = new ArrayList<Integer>();

        for (int i = 2; i < n; i += 1){
""",
     "prefix":
     """public class COUNT_UP_TO {
    public static List<Integer> count_up_to(int n) {
        List<Integer> primes = new ArrayList<Integer>();

        for (int i = 2; i < n; i += 1){
// buggy code
//            boolean is_prime = false;
//            for (int j = 2; j < i; j += 1){
//                if (i % j == 0) {
//                    is_prime = false;
            """,
     "suffix":
     """
                }
            }
            if (is_prime) primes.add(i);
        }
        return primes;
    }
}
"""},
    {"original_prefix":
     """public class COUNT_UPPER {
    public static int count_upper(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i += 2) {
            char c = s.charAt(i);
""",
     "prefix":
     """public class COUNT_UPPER {
    public static int count_upper(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i += 2) {
            char c = s.charAt(i);
// buggy code
//            if (c == 'A' || c == 'e' || c == 'I' || c == 'o' || c == 'u')
            """,
     "suffix":
     """
                count += 1;
        }
        return count;
    }
}
"""},
    {"original_prefix":
     """public class CYCPATTERN_CHECK {
    public static boolean cycpattern_check(String a, String b) {
        int l = b.length();
""",
     "prefix":
     """public class CYCPATTERN_CHECK {
    public static boolean cycpattern_check(String a, String b) {
        int l = b.length();
// buggy code
//        String pat = b;
//        for (int i = 0; i < a.length(); i += 1) {
//            for (int j = 0; j < l; j += 1) {
        """,
     "suffix":
     """
                if (a.substring(i, i + l).equals(pat.substring(j, j + l))) return true;
            }
        }
        return false;
    }
}
"""},
    {"original_prefix":
     """public class DECIMAL_TO_BINARY {
    public static String decimal_to_binary(int decimal) {
""",
     "prefix":
     """public class DECIMAL_TO_BINARY {
    public static String decimal_to_binary(int decimal) {
// buggy code
//        String result = Integer.toHexString(decimal);
        """,
     "suffix":
     """
        return "db" + result + "db";
    }
}
"""},
    {"original_prefix":
     """public class DECODE_CYCLIC {
    public static String decode_cyclic(String str) {
        class Cyclic {
            String encode_cyclic(String s) {
                ArrayList<String> groups = new ArrayList<String>();

""",
     "prefix":
     """public class DECODE_CYCLIC {
    public static String decode_cyclic(String str) {
        class Cyclic {
            String encode_cyclic(String s) {
                ArrayList<String> groups = new ArrayList<String>();

// buggy code
//                for (int i = 0; i < s.length(); i += 3){
                """,
     "suffix":
     """
                    groups.add(s.substring(i, Math.min(s.length(), i + 3)));
                }
                int remain = s.length() % 3;
                
                String result = "";
                for (String group : groups){
                    result += group.substring(1) + group.substring(0, 1);
                }

                if (remain > 0){
                    result += s.substring(s.length() - remain);
                }

                return result;
            }
        }
        
        final Cyclic cyclic = new Cyclic();
        return cyclic.encode_cyclic(cyclic.encode_cyclic(str));
    }
}
"""},
    {"original_prefix":
     """public class DECODE_SHIFT {
    public static String encode_shift(String string){
        StringBuilder sb = new StringBuilder();
        for (char c : string.toCharArray()) {
            c = (char)((((int) c + 5 - (int)('a')) % 26) + (int)('a'));
            sb.append(c);
        }
        return sb.toString();
    }

    public static String decode_shift(String string) {
        StringBuilder sb = new StringBuilder();
        for (char c : string.toCharArray()) {
""",
     "prefix":
     """public class DECODE_SHIFT {
    public static String encode_shift(String string){
        StringBuilder sb = new StringBuilder();
        for (char c : string.toCharArray()) {
            c = (char)((((int) c + 5 - (int)('a')) % 26) + (int)('a'));
            sb.append(c);
        }
        return sb.toString();
    }

    public static String decode_shift(String string) {
        StringBuilder sb = new StringBuilder();
        for (char c : string.toCharArray()) {
// buggy code
//            c = (char)((((int) c - 5 - (int)('a')) % 26) + (int)('a'));
            """,
     "suffix":
     """
            sb.append(c);
        }
        return sb.toString();
    }
}
"""},
    {"original_prefix":
     """public class DERIVATIVE {
    public static List<Integer> derivative(List<Integer> xs) {
        List<Integer> result = new ArrayList<Integer>();
        
""",
     "prefix":
     """public class DERIVATIVE {
    public static List<Integer> derivative(List<Integer> xs) {
        List<Integer> result = new ArrayList<Integer>();
        
// buggy code
//        for (int i = 0; i < xs.size(); i += 1)
//            result.add(xs.get(i));
        """,
     "suffix":
     """
        return result;
    }
}
"""},
    {"original_prefix":
     """public class DIGIT_SUM {
    public static int digit_sum(String s) {
        int result = 0;
        for (char c : s.toCharArray()) {
""",
     "prefix":
     """public class DIGIT_SUM {
    public static int digit_sum(String s) {
        int result = 0;
        for (char c : s.toCharArray()) {
// buggy code
//            if (c == ' ')
//                break;
            """,
     "suffix":
     """
            if ('A' <= c && c <= 'Z')
                result += (int) c;
        }
        return result;
    }
}
"""},
    {"original_prefix":
     """public class DIGITS {
    public static int digits(int n) {
        int product = 1;
        int odd_count = 0;
""",
     "prefix":
     """public class DIGITS {
    public static int digits(int n) {
        int product = 1;
        int odd_count = 0;
// buggy code
//        while(n >= 0) {
//            int digit = n * 10;
//            if(digit % 2 == 0) {
//                product /= digit;
        """,
     "suffix":
     """
                odd_count++;
            }
            n /= 10;
        }
        if(odd_count == 0) return 0;
        return product;
    }
}
"""},
    {"original_prefix":
     """public class DO_ALGEBRA {
    public static double do_algebra(String[] operator, int[] operand) throws NumberFormatException, ScriptException {
        ScriptEngineManager mgr = new ScriptEngineManager();
        ScriptEngine engine = mgr.getEngineByName("JavaScript");
""",
     "prefix":
     """public class DO_ALGEBRA {
    public static double do_algebra(String[] operator, int[] operand) throws NumberFormatException, ScriptException {
        ScriptEngineManager mgr = new ScriptEngineManager();
        ScriptEngine engine = mgr.getEngineByName("JavaScript");
// buggy code
//        String expression = "";
//        for (int i = 0; i < operand.length; i += 1) {
//            expression += operator[i] + operand[i];
        """,
     "suffix":
     """
        }
        return Double.parseDouble(engine.eval(expression).toString());
    }
}
"""},
    {"original_prefix":
     """public class DOUBLE_THE_DIFFERENCE {
    public static int double_the_difference(double[] lst) {
        int result = 0;
        for (Double d : lst) {
            if ((int) d.doubleValue() == d) {
                int d_int = (int) d.doubleValue();
                if (d_int % 2 == 1 && d_int >= 0) {
""",
     "prefix":
     """public class DOUBLE_THE_DIFFERENCE {
    public static int double_the_difference(double[] lst) {
        int result = 0;
        for (Double d : lst) {
            if ((int) d.doubleValue() == d) {
                int d_int = (int) d.doubleValue();
                if (d_int % 2 == 1 && d_int >= 0) {
// buggy code
//                    result += d_int;
                    """,
     "suffix":
     """
                }
            }
        }
        return result;
    }
}
"""},
    {"original_prefix":
     """public class EAT {
    public static int[] eat(int number, int need, int remaining) {
""",
     "prefix":
     """public class EAT {
    public static int[] eat(int number, int need, int remaining) {
// buggy code
//        return new int[] {number + need,  remaining - need};
        """,
     "suffix":
     """
    }
}
"""},
    {"original_prefix":
     """public class ENCODE {
    public static String encode(String message) {
        StringBuilder sb = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isUpperCase(c)) {
                c = Character.toLowerCase(c);
            }
""",
     "prefix":
     """public class ENCODE {
    public static String encode(String message) {
        StringBuilder sb = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isUpperCase(c)) {
                c = Character.toLowerCase(c);
            }
// buggy code
//            if (Character.isLowerCase(c)) {
            """,
     "suffix":
     """
                c = Character.toUpperCase(c);
            }
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O'
                    || c == 'U') {
                c = (char) ((int) c + 2);
            }
            sb.append(c);
        }
        return sb.toString();
    }
}
"""},
    {"original_prefix":
     """public class ENCRYPT {
    public static String encrypt(String s) {
        StringBuilder sb = new StringBuilder();
        String d = "abcdefghijklmnopqrstuvwxyz";
        for (char c : s.toCharArray()){
            if ('a' <= c && c <= 'z'){
                sb.append(
""",
     "prefix":
     """public class ENCRYPT {
    public static String encrypt(String s) {
        StringBuilder sb = new StringBuilder();
        String d = "abcdefghijklmnopqrstuvwxyz";
        for (char c : s.toCharArray()){
            if ('a' <= c && c <= 'z'){
                sb.append(
// buggy code
//                    d.charAt(s.indexOf((int) c) + 2 * 2)
                    """,
     "suffix":
     """
                );
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
"""},
    {"original_prefix":
     """public class EVEN_ODD_COUNT {
    public static int[] even_odd_count(int num) {
        int even_count = 0;
        int odd_count = 0;

""",
     "prefix":
     """public class EVEN_ODD_COUNT {
    public static int[] even_odd_count(int num) {
        int even_count = 0;
        int odd_count = 0;

// buggy code
//        for (char c : (num + "").toCharArray()) {
//            if ((int)c % 2 == 0) even_count += 1;
//            if ((int)c % 2 == 1) odd_count += 1;
        """,
     "suffix":
     """
        }
        return new int[] {even_count, odd_count};
    }
}
"""},
    {"original_prefix":
     """public class EVEN_ODD_PALINDROME {
    public static boolean is_palindrome(int n) {
        String n_str = Integer.toString(n);
        String n_str_rev = "";
        for(int i = n_str.length() - 1; i >= 0; i--) {
            n_str_rev += n_str.substring(i, i + 1);
        }
        return n_str.equals(n_str_rev);
    }

    public static ArrayList<Integer> even_odd_palindrome(int n) {
        int even_palindrome_count = 0, odd_palindrome_count = 0;
        for(int i = 1; i <= n; i++) {
""",
     "prefix":
     """public class EVEN_ODD_PALINDROME {
    public static boolean is_palindrome(int n) {
        String n_str = Integer.toString(n);
        String n_str_rev = "";
        for(int i = n_str.length() - 1; i >= 0; i--) {
            n_str_rev += n_str.substring(i, i + 1);
        }
        return n_str.equals(n_str_rev);
    }

    public static ArrayList<Integer> even_odd_palindrome(int n) {
        int even_palindrome_count = 0, odd_palindrome_count = 0;
        for(int i = 1; i <= n; i++) {
// buggy code
//            if((i % 2) == 0 && is_palindrome(i)) odd_palindrome_count--;
//            else if((i % 2) == 1 && is_palindrome(i)) even_palindrome_count--;
            """,
     "suffix":
     """
        }
        ArrayList<Integer> result = new ArrayList<>(Arrays.asList(even_palindrome_count, odd_palindrome_count));
        return result;
    }
}
"""},
    {"original_prefix":
     """public class EXCHANGE {
    public static String exchange(ArrayList<Integer> lst1, ArrayList<Integer> lst2) {
        int odd = 0, even = 0;
""",
     "prefix":
     """public class EXCHANGE {
    public static String exchange(ArrayList<Integer> lst1, ArrayList<Integer> lst2) {
        int odd = 0, even = 0;
// buggy code
//        for(int i : lst2) {
//            if((i % 2) == 1) even++;
        """,
     "suffix":
     """
        }
        for(int i : lst2) {
            if((i % 2) == 0) even++;
        }
        if(even >= odd) {
            return "YES";
        }
        return "NO";
    }
}
"""},
    {"original_prefix":
     """public class FACTORIAL {
    public static ArrayList<Integer> factorial(int n) {
        ArrayList<Integer> ret = new ArrayList<>();
        for(int i = 1; i <= n; i++) {
            if((i % 2) == 0) {
                int x = 1;
                for(int j = 1; j <= i; j++) x *= j;
                ret.add(x);
            } else {
                int x = 0;
""",
     "prefix":
     """public class FACTORIAL {
    public static ArrayList<Integer> factorial(int n) {
        ArrayList<Integer> ret = new ArrayList<>();
        for(int i = 1; i <= n; i++) {
            if((i % 2) == 0) {
                int x = 1;
                for(int j = 1; j <= i; j++) x *= j;
                ret.add(x);
            } else {
                int x = 0;
// buggy code
//                for(int j = 1; j <= i; i++) x -= j;
                """,
     "suffix":
     """
                ret.add(x);
            }
        }
        return ret;
    }
}
"""},
    {"original_prefix":
     """public class FACTORIZE {
    public static List<Integer> factorize(int n){
        List<Integer> result = new ArrayList<Integer>();

        int i = 2;
        while (i <= (int)(Math.sqrt(n) + 1)){
            if (n % i == 0){
                result.add(i);
                n = n / i;
            } else{
                i += 1;
            }
        }

""",
     "prefix":
     """public class FACTORIZE {
    public static List<Integer> factorize(int n){
        List<Integer> result = new ArrayList<Integer>();

        int i = 2;
        while (i <= (int)(Math.sqrt(n) + 1)){
            if (n % i == 0){
                result.add(i);
                n = n / i;
            } else{
                i += 1;
            }
        }

// buggy code
        """,
     "suffix":
     """
        return result;
    }
}
"""},
    {"original_prefix":
     """public class FIB {
    public static int fib(int n) {
""",
     "prefix":
     """public class FIB {
    public static int fib(int n) {
// buggy code
        """,
     "suffix":
     """
        return fib(n - 1) + fib(n - 2);
    }
}
"""},
    {"original_prefix":
     """public class FIB4 {
    public static int fib4(int n) {
        ArrayList<Integer> result = new ArrayList<Integer>(); 
        result.add(0);
        result.add(0);
        result.add(2);
        result.add(0);

        if (n < 4)
            return result.get(n);
        for (int i = 4; i < n + 1; i += 1) {
            result.add(
                result.get(0) + result.get(1) + result.get(2) + result.get(3)
            );
""",
     "prefix":
     """public class FIB4 {
    public static int fib4(int n) {
        ArrayList<Integer> result = new ArrayList<Integer>(); 
        result.add(0);
        result.add(0);
        result.add(2);
        result.add(0);

        if (n < 4)
            return result.get(n);
        for (int i = 4; i < n + 1; i += 1) {
            result.add(
                result.get(0) + result.get(1) + result.get(2) + result.get(3)
            );
// buggy code
            """,
     "suffix":
     """
        }
        return result.get(result.size() - 1);
    }
}
"""},
    {"original_prefix":
     """public class FIBFIB {
    public static int fibfib(int n) {
        if (n == 0)
            return 0;
        if (n == 1)
            return 0;
""",
     "prefix":
     """public class FIBFIB {
    public static int fibfib(int n) {
        if (n == 0)
            return 0;
        if (n == 1)
            return 0;
// buggy code
        """,
     "suffix":
     """
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3);
    }
}
"""},
    {"original_prefix":
     """public class FILE_NAME_CHECK {
    public static String file_name_check(String file_name) {
        String[] lst = file_name.split("\\.");

        if (lst.length != 2)
            return "No";
        if (! (lst[1].equals("txt") || lst[1].equals("exe") || lst[1].equals("dll")))
            return "No";
        if (lst[0].length() == 0)
            return "No";
""",
     "prefix":
     """public class FILE_NAME_CHECK {
    public static String file_name_check(String file_name) {
        String[] lst = file_name.split("\\.");

        if (lst.length != 2)
            return "No";
        if (! (lst[1].equals("txt") || lst[1].equals("exe") || lst[1].equals("dll")))
            return "No";
        if (lst[0].length() == 0)
            return "No";
// buggy code
//        if ('a' > lst[0].charAt(0) && lst[0].charAt(0) > 'z' || 'A' > lst[0].charAt(0) && lst[0].charAt(0) > 'Z')
        """,
     "suffix":
     """
            return "No";
        int digit_cnt = 0;
        for (char c : file_name.toCharArray()){
            if ('0' <= c && c <= '9')
                digit_cnt += 1;
        }
        if (digit_cnt > 3)  return "No";
        return "Yes";
    }
}
"""},
    {"original_prefix":
     """""",
     "prefix":
     """public class FILTER_BY_PREFIX {
    public static List<String> filter_by_prefix(List<String> strings, String prefix) {
        List<String> result = new ArrayList<String>();

        for (String string : strings){
// buggy code
//            if (string.startsWith(prefix, 1)){
            """,
     "suffix":
     """
                result.add(string);
            }
        }
        return result;
    }
}
"""},
    {"original_prefix":
     """public class FILTER_BY_SUBSTRING {
    public static List<String> filter_by_substring(List<String> strings, String substring) {
        List<String> result = new ArrayList<String>();
        for (String string : strings){
""",
     "prefix":
     """public class FILTER_BY_SUBSTRING {
    public static List<String> filter_by_substring(List<String> strings, String substring) {
        List<String> result = new ArrayList<String>();
        for (String string : strings){
// buggy code
//            result.add(string);
        """,
     "suffix":
     """
        }
        return result;
    }
}
"""}
]
