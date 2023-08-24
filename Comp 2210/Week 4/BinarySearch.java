import java.util.Comparator;
class BinarySearch {
// first index of given and sorted array along with given comparator
	// returns suitable index if found otherwise -1
   public static <T> int firstIndexOf(T data[], T key, Comparator<T> comparator) {
   	// TODO NULL check for all parameters and throw exception if required
      int start = 0, end = data.length - 1;
      int idx = -1;
      while(start <= end) {
         int mid = (start + end) / 2;
         int c = comparator.compare(data[mid], key);
         if(c >= 0) {
         	// take left side to get first index
            if(c == 0) {
            	// latest found index
               idx = mid;
            }
            end = mid - 1;
         } else {
         	// take right side
            start = mid + 1;
         }
      }
      return idx;
   }
	
	// last index of given and sorted array along with given comparator
	// returns suitable index if found otherwise -1
   public static <T> int lastIndexOf(T data[], T key, Comparator<T> comparator) {
   	// TODO NULL check for all parameters and throw exception if required
      int start = 0, end = data.length - 1;
      int idx = -1;
      while(start <= end) {
         int mid = (start + end) / 2;
         int c = comparator.compare(data[mid], key);
         if(c <= 0) {
         	// take right side to get last index
            if(c == 0) {
            	// latest found index
               idx = mid;
            }
            start = mid + 1;
         } else {
         	// take left side
            end = mid - 1;
         }
      }
      return idx;
   }
}