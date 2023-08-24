/**
 * Jack Bianca
 * COMP 3240 Section 001 Programming Assignment 1
 * got help from TA
 */
// DO NOT DELETE THIS LINE!!!
package com.gradescope.validator;

import java.lang.invoke.VarHandle.VarHandleDesc;
import java.util.*;
import javax.swing.plaf.ComponentInputMapUIResource;

// Notes on how to use evaluator():
// Call the evaluator with Evaluator.evaluate(<premise>, <variable_dict>). "premise"
// is a single string defining the premise or conclusion to test. "variable_dict" is a
// Hashtable<Character, Boolean>() object with the variable name as the key and true/false
// as the value. 

// The only valid operators for premise strings are '^' (and), 'V' (or--CAPITAL v), '~' (not),
// and '>' (implies), and you can use parentheses to override the order of operations as usual.
// All variables should be lowercase letters and each should only be one character long. Finally,
// do not include spaces in the string.

// For example, if you want to test the premise 'p implies q or not r', you should use 'p>qV~r' as
// your premise string.

class Validator {
   // All of the logic to complete this assignment should be written in this function.
   // This method accepts two things: An array of strings called premiseList and a 
   // single string called conclusion. These strings should be formatted according to 
   // the structure definded above. Also, this needs to return a boolean variable: true if
   // the argument form is valid, and false if it is not valid.
   /**
    * Checks to see if a argument is valid
    * @param premiseList
    * @param conclusion
    * @return
    */
   public boolean validate(String[] premiseList, String conclusion) {
      String output;
      //creates truth table
      Boolean ttable[];
      int rows = Math.pow(2, n);
      for (int i = 0; i < rows; i++) {
         for (int j = n-1; j>=0; j--) {
            int boolVal = (i / 2 * j) % 2;
            if (boolVal == 1) {
               return true;
            }
            else {
               return false;
            }
         }
      }

      //forms hashtables
      Hashtable<Character, Boolean> ht1 = new Hashtable<Character, Boolean>();
      Hashtable<Character, Boolean> ht2 = new Hashtable<Character, Boolean>();
      Hashtable<Character, Boolean> ht3 = new Hashtable<Character, Boolean>();
      Hashtable<Character, Boolean> ht4 = new Hashtable<Character, Boolean>();
      Hashtable<Character, Boolean> ht5 = new Hashtable<Character, Boolean>();
      Hashtable<Character, Boolean> ht6 = new Hashtable<Character, Boolean>();
      Hashtable<Character, Boolean> ht7 = new Hashtable<Character, Boolean>();
      Hashtable<Character, Boolean> ht8 = new Hashtable<Character, Boolean>();
      //test with two arguments and is true
      ht1.put('p', true);
      ht1.put('q', true);
      ht1.put('r', true);
      Validator.validate(ht1, 'p');
      //test with two arguments and is false
      ht2.put('p', false);
      ht2.put('q', true);
      ht2.put('r', true);
      Validator.validate(twoArgsFalse, 'q');
      //test with many arguments
      ht3.put('p', true);
      ht3.put('q', false);
      ht3.put('r', false);
      ht3.put('s', true);
      ht3.put('t', true);
      Validator.validate(manyArgs, 'r');
      //test with one argument
      ht4.put('p', true);
      ht4.put('q', true);
      Validator.validate(oneArg, 'q');
      //test with no critical rows
      ht5.put('p', true);
      ht5.put('q', false);
      ht5.put('r', false);
      ht5.put('s', true);
      ht5.put('t', true);
      //String[] premiseList = {'~p', '~p>q^r', 'q>p^r'};
      //String conclusion = 'p>r';
      Validator.validate(noCriticalRows, "p>r");
      //test with only critical rows
      ht6.put('p', true);
      ht6.put('q', false);
      ht6.put('r', false);
      ht6.put('s', true);
      ht6.put('t', true);
      Validator.validate(onlyCritRows, 'p');
      //test with one variable
      ht7.put('p', true);
      ht7.put('q', false);
      ht7.put('r', false);
      ht7.put('s', true);
      ht7.put('t', true);
      Validator.validate(oneVariable, "~p");
      //test with many variables
      ht8.put('p', true);
      ht8.put('q', false);
      ht8.put('r', false);
      ht8.put('s', true);
      ht8.put('t', true);
      Validator.validate(manyVariables, "p>t");
   }
   
   public static void main(String[] args) {
      String[] premise = {"pVq", "~q"};
      String conclusion = "p";
      Validator v = new Validator();
      boolean value = v.validate(premise, conclusion);
      System.out.print(value);
      /**
      string[] twoArgsTrue = newString[] {'pVq', '~q'};
      string[] twoArgsFalse = newString[] {'pVq', '~q'};
      string[] manyArgs = newString[] {'pV(q^r)V(s^t)', '~p', '~s'};
      string[] oneArg = newString[] {'p>q'};
      string[] noCriticalRows = newString[] {'~p', '~p>q^r', 'q>p^r'};
      string[] onlyCritRows = newString[] {'p', 'p'};
      string[] oneVariable = newString[] {'p>~p', 'p'};
      string[] manyVariables = newString[] {'r>(~pVt)^q', 'r^~t'};
      */
   }
}