funcs = [{"prefix":
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
        {"prefix":
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
        {"prefix":
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
        {"prefix":
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
        {"prefix":
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
        {"prefix":
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
"""}
        ]

# {"prefix":
#      """""",
#  "suffix":
#      """"""},
# {"prefix":
#      """""",
#  "suffix":
#      """"""},
# {"prefix":
#      """""",
#  "suffix":
#      """"""},
# {"prefix":
#      """""",
#  "suffix":
#      """"""},
# funcs = [{"prefix":
#               """public class ADD {
#     public static int add(int x, int y) {
# // buggy code
# //        return x | y;
#         """,
#           "suffix":
#               """
#     }
# }"""},
#          {"prefix":
#               """public class ADD_ELEMENTS {
#     public static int add_elements(ArrayList<Integer> arr, int k) {
#         int result = 0;
#         for(int i = 0; i < k; i++) {
# // buggy code
# //            if(Integer.toString(arr.get(i)).length() >= 2) {
# //                result -= arr.get(i);""",
#           "suffix":
#               """
#             }
#         }
#         return result;
#     }
# }"""},
#          {"prefix":
#               """public class ADD_EVEN_AT_ODD {
#     public static int add_even_at_odd(int[] lst) {
#         int sum = 0;
# // buggy code
# //        for (int i = 0; i < lst.length; i += 1) {""",
#           "suffix":
#               """
#             if (lst[i] % 2 == 0)
#                 sum += lst[i];
#         }
#         return sum;
#     }
# }"""},
#          {"prefix":
#               """public class ALL_PREFIXES {
#     public static List<String> all_prefixes(String string){
#         List<String> result = new ArrayList<String>();
#
#         for (int i = 0; i < string.length(); i += 1){
# // buggy code
# //            result.add(string.substring(i + 1));""",
#           "suffix":
#               """
#         }
#
#         return result;
#     }
# }"""},
#          {"prefix":
#               """public class ANTI_SHUFFLE {
#     public static String anti_shuffle(String s) {
#         String result = "";
#         for (String str : s.split(" ")) {
#             char[] chars = str.toCharArray();
#             Arrays.sort(chars);
# // buggy code
# //            result += new String(chars);
# //        }
# //        return result;""",
#           "suffix":
#               """
#     }
# }"""},
#          {"prefix":
#               """public class ANY_INT {
#     public static boolean any_int(double x, double y, double z) {
# // buggy code
# //        if ((int)x == x && (int)y == y) {
# //            if (x + y == z || x + z == y)""",
#           "suffix":
#               """
#                 return true;
#         }
#         return false;
#     }
# }"""},
#          {"prefix":
#               """public class BELOW_THRESHOLD {
#     public static boolean below_threshold(int[] l, int t) {
#         for (int i = 0; i < l.length; i += 1) {
# // buggy code
# //            if (l[i] <= t)
# //                return true;
# //        }
# //        return false;""",
#           "suffix":
#               """
#     }
# }"""},
#          {"prefix":
#               """public class BELOW_ZERO {
#     public static boolean below_zero(List<Integer> operations) {
#         int balance = 0;
#         for (Integer op : operations){
#             balance += op;
# // buggy code
# //            if (balance > 0){
# //                return false;
# //            }
# //        }
# //        return true;""",
#           "suffix":
#               """
#     }
# }"""},
#          {"prefix":
#               """public class BF {
#     public static ArrayList<String> bf(String planet1, String planet2) {
#         ArrayList<String> planet_names = new ArrayList<String>(Arrays.asList(
#             "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
#         ));
#
#         ArrayList<String> result = new ArrayList<String>();
#         if ((! planet_names.contains(planet1)) || (! planet_names.contains(planet2)))
#             return result;
#         int planet1_index = planet_names.indexOf(planet1);
#         int planet2_index = planet_names.indexOf(planet2);
# // buggy code
# //        for (int i = planet1_index; i < planet2_index; i += 1)
# //            result.add(planet_names.get(i));""",
#           "suffix":
#               """
#         return result;
#     }
# }"""},
#          {"prefix":
#               """public class BY_LENGTH {
#     public static ArrayList<String> by_length(ArrayList<Integer> a) {
#         Map<Integer, String> digit_map = new HashMap<>();
#         digit_map.put(1, "One");
#         digit_map.put(2, "Two");
#         digit_map.put(3, "Three");
#         digit_map.put(4, "Four");
#         digit_map.put(5, "Five");
#         digit_map.put(6, "Six");
#         digit_map.put(7, "Seven");
#         digit_map.put(8, "Eight");
#         digit_map.put(9, "Nine");
#         Collections.sort(a, Collections.reverseOrder());
#         ArrayList<String> result = new ArrayList<>();
#         for(int num : a) {
# // buggy code
# //            if(digit_map.get(num) != "") {""",
#           "suffix":
#               """
#                 result.add(digit_map.get(num));
#             }
#         }
#         return result;
#     }
# }"""}
#          ]
# # ,
# #          {"prefix":
# #               """""",
# #           "suffix":
# #               """""",
# #           "original_prefix":
# #               """"""}
