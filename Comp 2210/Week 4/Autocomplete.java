import java.util.Arrays;
import java.util.Comparator;

public class Autocomplete {
	
   Term terms[];
	
	// loaded terms into sorted order for better search
   public Autocomplete(Term terms[]) {
      Arrays.sort(terms); // lexographical sorted order
      this.terms = terms;
   	
   	// test
   	/*
   	 * for(Term t : terms) { System.out.println(t); }
   	 */
   }
	
	// returns all suitable match found based on descending weighted order
   public Term[] allMatches(String prefix) {
      int l = prefix.length();
      Comparator<Term> comp = Term.byPrefixOrder(l); // comparator do range search by prefix
      Term key = new Term(prefix, -1); // here weight -1 is dummy/meaningless
      int idx1 = BinarySearch.firstIndexOf(terms, key, comp);
      int idx2 = BinarySearch.lastIndexOf(terms, key, comp);
   	
      if(idx1 == -1) {
      	// no data found
         return null;
      } else {
      	// data found
      	// copy and sort based on weight in descending order
         Term found[] = new Term[idx2 - idx1 + 1];
         for(int i = idx1; i <= idx2; i++) {
            found[i - idx1] = terms[i];
         }
         Arrays.sort(found, Term.byDescendingWeightOrder());
         return found;
      }
   }
	
   public static void main(String[] args) {
   	// TEST
      Term terms[] = {
         new Term("the", 100), new Term("of", 10), new Term("and", 200),
         new Term("to", 123), new Term("a", 110), new Term("in", 245),
         new Term("for", 245), new Term("is", 120), new Term("on", 247),
         new Term("that", 1245)
         };
   	
      Autocomplete driver = new Autocomplete(terms);
      String prefix = "t";
      Term found[] = driver.allMatches(prefix);
      if(found != null) {
         System.out.println("Result with prefix: " + prefix);
         System.out.println("-----------------------------------");
         for(Term t : found) {
            System.out.println(t);
         }
      } else {
      	// result not found
         System.out.println("Not found.");
      }
   }
}