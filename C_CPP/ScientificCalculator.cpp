
/*
   PROGRAMMED BY                   ID
   1.AMANUEL GEBREMEDHN          0668/16
   2.GEMECHIS TESFAYE            1381/16
   3.SAMUEL TILAHUN              2370/16
   4.ABDI    TUFA                0424/16
   5.BINIYAM PAULOS              0898/16
   6.YONAS  GETAHUN              2748/16
   7.ALAZAR  YEWENDATER          0883/16
   8.HAWi  DESALEGN              1889/16
   9.RUHAMA GETACHEW             2339/16
   10.RAHEL MELAKU               2262/16
  
*/
#include <iostream>//this mandatory in c++ to input and out put
#include <cmath>//we use this to include the formulas 
#include <limits>//to prevent over flow and what charachter to ignor
#include <string>//to include words like opration
#include <windows.h>//to provide various features of the the system
using namespace std;

/* 
informs the compiler the use of afunction with its return type,parametrsand name (function protype)
*/
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);
double power(double base, double exp);
double squareRoot(double x);
double logarithm(double base, double value);
double exponential(double x);
double hyperbolicSine(double x);
double hyperbolicCosine(double x);
double hyperbolicTangent(double x);
double inverseHyperbolicSine(double x);
double inverseHyperbolicCosine(double x);
double inverseHyperbolicTangent(double x);
double sine(double x);
double cosine(double x);
double tangent(double x);
double inverseSine(double x);
double inverseCosine(double x);
double inverseTangent(double x);


void clearInput() {//we use this to handl the invalid input and to continue the program
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}
int main() {
    double num1, num2;/*this is that the data we need to input
  and we use the doule data type to get more storage*/
    string operation;//this can be tex or char
    
  //we use this table for better understand what opration to use the user
   cout<<"\t----------------------------------------------------|"<<endl;
   cout<<"\t|          |                               |        |"<<endl;
   cout<<"\t------------        SCIENTFIC              ---------|"<<endl;
   cout<<"\t|c-continue|         CALCULATOR            | o-off  |"<<endl;
   cout<<"\t-----------------------------------------------------"<<endl; 
   cout<<"\t|    +     |     -    |     *   |    /     |    ^   |"<<endl; 
   cout<<"\t|  add     | subtract | multiply| divide   | power  |"<<endl; 
   cout<<"\t-----------------------------------------------------"<<endl; 
   cout<<"\t|    s     |     l    |     e   |   sh     |  ch    |"<<endl; 
   cout<<"\t|  sqroot  | logarithm|   expo  | sinh     |  cosh  |"<<endl;
   cout<<"\t-----------------------------------------------------"<<endl;
   cout<<"\t|    th    |    ish   |   ich   |   ith    |  sin   |"<<endl;
   cout<<"\t|   tanh   |  invsinh | invcosh | invtanh  |  sine  |"<<endl; 
   cout<<"\t-----------------------------------------------------"<<endl;
   cout<<"\t|   cos    |   tan    |    is   |  ic      |   it   |"<<endl;
   cout<<"\t|  cosine  |  tangent | invSin  | invcos   |invtan  |"<<endl;
   cout<<"\t-----------------------------------------------------"<<endl;
   cout<<"\t|         after the calculater is continuing        |"<<endl; 
   cout<<"\t|        you can Exit by pressing E                 |"<<endl;
    cout<<"\t-----------------------------------------------------"<<endl;
    cin >> operation;// for this input we declare below the int main 

    if (operation == "c") {
        while (true) {
            /* when you press c  you have to enter opretion from this(+, -, *, /, ^, s for square root,
       l for logarithm (base and value), e for exponential,  sh for sinh, ch for cosh, th for tanh, 
                  ish for asinh, ich for acosh, ith for atanh, sin for sine, cos for cosine, tan for tangent, 
                  is for inverse sine, ic for inverse cosine, it for inverse tangent, or 'E' to exit */
            cin >> operation;

if (operation == "E") {
              cout<<"PROGRAMMED BY INFOSA STUDENTS"<<endl;//this statment will be seen in the terminal after pressing E
              
                break; // to close the program press E
            }

            // for the a single input
            if (operation == "s"  operation == "e"  operation == "sh"  operation == "ch"  operation == "th"  
                operation == "ish"  operation == "ich"  operation == "ith"  
                operation == "sin"  operation == "cos"  operation == "tan"  
                operation == "is"  operation == "ic"  operation == "it") {
                
                cout << "Enter a number: ";
                if (!(cin >> num1)) {//this means if the input is not num show the below 
                    cout << "Invalid input. Please enter a valid number." << endl;
                    clearInput();
                    continue;//it is used for to continue the loop when the 
                }
                
                if (operation == "s") cout << "Result: " << squareRoot(num1) << endl;
                else if (operation == "e") cout << "Result: " << exponential(num1) << endl;
                else if (operation == "sh") cout << "Result: " << hyperbolicSine(num1) << endl;
                else if (operation == "ch") cout << "Result: " << hyperbolicCosine(num1) << endl;
                else if (operation == "th") cout << "Result: " << hyperbolicTangent(num1) << endl;
                else if (operation == "ish") cout << "Result: " << inverseHyperbolicSine(num1) << endl;
                else if (operation == "ich") cout << "Result: " << inverseHyperbolicCosine(num1) << endl;
                else if (operation == "ith") cout << "Result: " << inverseHyperbolicTangent(num1) << endl;
                else if (operation == "sin") cout << "Result: " << sine(num1) << endl;
                else if (operation == "cos") cout << "Result: " << cosine(num1) << endl;
                else if (operation == "tan") cout << "Result: " << tangent(num1) << endl;
                else if (operation == "is") cout << "Result: " << inverseSine(num1) << endl;
                else if (operation == "ic") cout << "Result: " << inverseCosine(num1) << endl;
                else if (operation == "it") cout << "Result: " << inverseTangent(num1) << endl;
            }
            // for the two inputs
            else if (operation == "l") {
                cout << "Enter base and value for logarithm: ";
                if (!(cin >> num1 >> num2)  num1 <= 0  num1 == 1  num2 <= 0) {
                    cout << "Error: Invalid input for logarithm!" << endl;
                    clearInput();
                    continue;
                }
                cout << "Result: " << logarithm(num1, num2) << endl;
            } else if (operation == "+"  operation == "-"  operation == "*"  operation == "/"  operation == "^") {
                cout << "Enter two numbers: ";
                if (!(cin >> num1 >> num2)) {
                    cout << "Invalid input. Please enter two valid numbers." << endl;
                    clearInput();
                    continue;
                }

                if (operation == "+") cout << "Result: " << add(num1, num2) << endl;
                else if (operation == "-") cout << "Result: " << subtract(num1, num2) << endl;
                else if (operation == "*") cout << "Result: " << multiply(num1, num2) << endl;
                else if (operation == "/") {
                    if (num2 == 0) cout << "Error: Division by zero!" << endl;//THIS WILL BE seeen WHEN THE SECOND NUMBER IS 0 
                    else cout << "Result: " << divide(num1, num2) << endl;
                } else if (operation == "^") cout << "Result: " << power(num1, num2) << endl;
            } else {
                cout << "Invalid operation." << endl;
            }
        }
    }

    return 0;
}
/*IN THIS CODE WE WERE USING IF CONDTION,WHILELOOP,
AND FOR FLOW CONTROL CONTINUE
*/
// we are defining what function we use


double add(double a, double b) { return a + b; }
double subtract(double a, double b) { return a - b; }
double multiply(double a, double b) { return a * b; }
double divide(double a, double b) { return (b != 0) ? a / b : numeric_limits<double>::quiet_NaN(); }
double power(double base, double exp) { return pow(base, exp); }
double squareRoot(double x) { return (x >= 0) ? sqrt(x) : numeric_limits<double>::quiet_NaN(); }
double logarithm(double base, double value) { return (base > 0 && base != 1 && value > 0) ? log(value) / log(base) : numeric_limits<double>::quiet_NaN(); }
double exponential(double x) { return exp(x); }
double hyperbolicSine(double x) { return sinh(x); }
double hyperbolicCosine(double x) { return cosh(x); }
double hyperbolicTangent(double x) { return tanh(x); }
double inverseHyperbolicSine(double x) { return asinh(x); }
double inverseHyperbolicCosine(double x) { return acosh(x); }
double inverseHyperbolicTangent(double x) { return atanh(x); }
double sine(double x) { return sin(x); }
double cosine(double x) { return cos(x); }
double tangent(double x) { return tan(x); }
double inverseSine(double x) { return asin(x); }
double inverseCosine(double x) { return acos(x); }
double inverseTangent(double x) { return atan(x); }