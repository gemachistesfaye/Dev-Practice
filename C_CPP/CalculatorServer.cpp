#include "crow_all.h"
#include <string>
#include <sstream>
#include <cmath>
#include "ScientificCalculator.cpp" // Include your original code

using namespace std;

int main() {
    crow::SimpleApp app;

    // API endpoint: call any operation
    CROW_ROUTE(app, "/calc")
    ([](const crow::request& req){
        auto op = req.url_params.get("op");
        auto a_str = req.url_params.get("a");
        auto b_str = req.url_params.get("b");

        if (!op) return crow::response(400, "Operation missing");

        double a = a_str ? stod(a_str) : 0;
        double b = b_str ? stod(b_str) : 0;
        double result = NAN;
        string opStr(op);

        // Call functions from your original code
        if(opStr == "+") result = add(a,b);
        else if(opStr == "-") result = subtract(a,b);
        else if(opStr == "*") result = multiply(a,b);
        else if(opStr == "/") result = divide(a,b);
        else if(opStr == "^") result = power(a,b);
        else if(opStr == "s") result = squareRoot(a);
        else if(opStr == "l") result = logarithm(a,b);
        else if(opStr == "e") result = exponential(a);
        else if(opStr == "sh") result = hyperbolicSine(a);
        else if(opStr == "ch") result = hyperbolicCosine(a);
        else if(opStr == "th") result = hyperbolicTangent(a);
        else if(opStr == "ish") result = inverseHyperbolicSine(a);
        else if(opStr == "ich") result = inverseHyperbolicCosine(a);
        else if(opStr == "ith") result = inverseHyperbolicTangent(a);
        else if(opStr == "sin") result = sine(a);
        else if(opStr == "cos") result = cosine(a);
        else if(opStr == "tan") result = tangent(a);
        else if(opStr == "is") result = inverseSine(a);
        else if(opStr == "ic") result = inverseCosine(a);
        else if(opStr == "it") result = inverseTangent(a);

        stringstream ss;
        ss << result;
        return crow::response(ss.str());
    });

    app.port(18080).multithreaded().run();
}