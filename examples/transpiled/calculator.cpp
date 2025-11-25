// C++23 Calculator transpiled by Sugar++  -  this comment was added manually
#include <print>
#include <iostream>
#include <cmath>

// Simple calculator with s++ syntax | C++23

double calculate(double& n1, char& op, double& n2);

int main(){
	auto n1 = 0.0;      // Inferred type with C++ keyword auto
double n2 = 0; // Explicit type
char op = '+';
double result = 0.0;

	std::print("Xyz\nX? ");
	std::cin >> n1;

	std::print("{}Yz\nY?", n1);
	std::cin >> op;
	
	std::print("{}{}Z\nZ?", n1, op);
	std::cin >> n2;

	result = calculate(n1, op, n2);

	std::print("{}{}{} = {}\n", n1, op, n2, result);
    
    return 0;
}

double calculate(double& n1, char& op, double& n2){
	if (op == '+'){
		return (n1 + n2);
	}
else if (op == '-'){
		return (n1 - n2);
	}
else if (op == 'x'){
		return (n1 * n2);
	}
else if (op == '/'){
		return (n1 / n2);
	}
else if (op == '^'){
		return (std::pow(n1, n2));
	}

	return -1;
}
