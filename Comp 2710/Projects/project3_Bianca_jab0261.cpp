/**
 * Name: Jack Bianca
 * AU ID: jab0261
 * Version: 07/23/23
 * Title: project3_Bianca_jab0261.cpp
 * Compile: g++ project3_Bianca_jab0261.cpp -o Project3.out
 * Run: ./Project3.out
*/
/**
 * used project3 hints for basics
 * friends informed me about premade c++ sort method
 * used cplusplus.com for std commands
*/
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

/**
 * This program will copy lists of numbers to a thrid file in ascended order,
 * and produce an output to the same third file.
*/

//declarations for user defined functions
//checks if file exists
bool check_file(string);
//reads in the file name
vector<int> read_file(string);
//writes data to a new output file
void write_file(string, vector<int>);
//merges data from input files
vector<int> merge(vector<int>, vector<int>);

/**
 * Displays the values of a given vector
 * 
 * Param: file name (string)
 * Param: v vector display output (vector<int>)
*/
void toString(string, vector<int>);

/**
 * Main function
 * merges numbers from two files to write all numbers
 * to a third file and sorts them in ascending order
 * Return: 0 (int)
*/
int main() {
   // local variables
   vector<int> x;
   vector<int> y;
   vector<int> z;

   string fileName1;
   string fileName2;
   string fileName3;

   cout << "*** Welcome to Jack's sorting program ***" << endl;
   //get name of file 1
   do {
      cout << "Enter the first input file name: ";
      cin >> fileName1;
   } while (cin.fail() || !check_file(fileName1));
   //display file 1
   x = read_file(fileName1);
   cout << "The list of " << x.size() << " numbers in file " << fileName1 << "is:\n";
   for (int i = 0; i < x.size(); i++) {
      cout << x.at(i) << endl;
   }
   cout << endl;

   //get name of file 2
   do {
      cout << "Enter the second input file name: ";
      cin >> fileName2;
   } while (cin.fail() || !check_file(fileName2));
   //file 2 display
   y = read_file(fileName2);
   cout << "The list of " << y.size() << " numbers in file " << fileName2 << "is:\n";
   for (int i = 0; i < y.size(); i++) {
      cout << y.at(i) << endl;
   }
   cout << endl;

   //merge into file 3 output
   z = merge(x, y);
   cout << "The sorted list of " << z.size() << " numbers is: ";
   for (int i = 0; i < z.size(); i++) {
      cout << z.at(i) << " ";
   }
   cout << endl;

   //get file 3 output file name
   do {
      cout << "Enter the output file name: ";
      cin >> fileName3;
   } while (cin.fail());
   //write info to the file 3
   write_file(fileName3, z);

   cout << "*** Please check the new file - " << fileName3 << " ***" << endl
      << "*** Goodbye. ***";
   return 0;
}

bool check_file(string file) {
   //input file stream. (ifstream)
   ifstream stream;
   //check if file exists
   stream.open(file.c_str());
   if (stream.fail()) {
      stream.close();
      return false;
   }
   stream.close();

   return true;
}

/**
 * Reads int i into param 'file' and returns v (sum of ints)
*/
vector<int> read_file(string file) {
   //input file stream. (ifstream)
   ifstream stream;

   //vector containing numbers from file. (vector<int>)
   vector<int> v;

   //integer read from file (int)
   int i;

   //add each number in the file to a vector
   stream.open(file.c_str());
   while (stream.good()) {
      v.insert(v.end(), i);
   }
   stream.close();
      
   return v;
}

/**
 * creates a param file and writes v to param file
*/
void write_file(string file, vector<int> v) {
   //output file stream. (ofstream)
   ofstream stream;
   stream.open(file.c_str());
   for (unsigned int i = 0; i < v.size(); i++) {
      stream << v.at(i) << endl;
   }
   stream.close();
}

/**
 * merges vectors and returns a new vector
*/
vector<int> merge(vector<int> v1, vector<int> v2) {
   //creates new vector
   vector<int> v3;
   v3 = v1;
   //compiles both vectors into the new one and sorts in ascending order
   //uses built-in sort method to get ascending sort
   v3.insert(v3.end(), v2.begin(), v2.end());
   sort(v3.begin(), v3.end());
   return v3;
}

//outputs v
void to_string(vector<int> v) {
   //vector iterator number (unsigned short) ??
   unsigned short i;

   //output display
   for (unsigned int i = 0; i < v.size(); i++) {
      cout << v.at(i) << endl;
   }
   cout << endl;
}