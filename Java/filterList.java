import java.util.*;

public class Kata {
  
  public static List filterList(final List list) {
        List result = new ArrayList();
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) instanceof Number) {
                result.add(list.get(i));
            }
        }
        return result;
    }
  }

// In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

// Example
// filter_list([1,2,'a','b']) == [1,2]
// filter_list([1,'a','b',0,15]) == [1,0,15]
// filter_list([1,2,'aasf','1','123',123]) == [1,2,123]