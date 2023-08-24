/**
 * File Name: project1_Bianca_jab0261
 * Author: Jack Bianca
 * jab0261@auburn.edu
 * I used project1_hints for guidelines
 * I used Geeksforgeeks.com to help me learn about c++
 * Googled a couple of syntax things
 * I used simplilearn.com to learn about library fields and width in c++
 * Compile: g++ project_Bianca_jab0261.cpp
*/
#include <iostream>
using namespace std;

int main() {
   //variable initialization
   double loan; // with no downpayment
   double interestRate;
   double monthlyPaid;

   //currency formatting
   cout.setf(ios::fixed);
   cout.setf(ios::showpoint);
   cout.precision(2);

   //User Input
   //NOTE: For valid input, the loan, interest, and monthly payment must be
   //positive. The monthly payment must also be large enough to
   //terminate the loan.
   cout << "\nLoan Amount: ";
   cin >> loan;
   cout << "Interest Rate (% per year): ";
   cin >> interestRate;
   //GET PROPER INTEREST RATES FOR CALCULATIONS
   interestRate /= 12;
   MonthlyIntRate = interestRate / 100;
   cout << "Monthly Payments: ";
   cin >> monthlyPaid;
   cout << endl;

   //AMORTIZATION TABLE
   cout << "*****************************************************************\n"
      cout << "\tAmortization Table\n"
      cout << "*****************************************************************\n"
      cout << "Month\tBalance\t\tPayment\tRate\tInterest\nPrincipal\n";

   //LOOPS TO FILL TABLE
   int month = 0;
   double monthlyIntRate = interestRate / 1200;
   double sum;
   double principal;
   double totalint = 0.0;
   while (loan > 0)
   {
      if (month == 0) {
         cout << month++ << "\t$" << loan;
         if (loan < 1000) cout << "\t"; //Formatting MAGIC
         cout << "\t" << "N/A\tN/A\tN/A\t\tN/A\n";
      }
      else {
         if (loan * interestRate + loan > 50) {
            sum = (loan * monthlyIntRate);
            principal = monthlyPaid - sum;
            totalint += sum;
            loan = 0.0;
         }
         else {
            sum = loan * interestRate;
            principal = monthlyPaid - sum;
            totalint += sum;
            loan = loan - (monthlyPaid - sum);
         }
         month++;
         cout << left << setw(8) << month;
         cout << "$" << left << setw(9) << balance;
         cout << "$" << left << setw(8) << monthlyPaid;
         cout << left << setw(8) << interestRateC;
         cout << "$" << left << setw(10) << sum;
         cout << "$" << left << setw(16) << principal;
         cout << endl;
         cin.get();
      }
      cout << "****************************************************************\n";
      cout << "\nIt takes " << month << " months to pay off "
         cout << "the loan\n"
         cout << "Total interest paid is: $" << inTotal;
      cout << endl << endl;
      return 0;
   }
}
/**
stereo system = $1000 on a credit plan:
no down payment, 18% interest rate per year, (1.5% per month) and monthly payments of $50.
first month you pay 1.5% of $1000 in interest. 15 dollars in interest. remaining $35 is deducted from debt
which leaves you in $965.00 in debt
*/