#include <stdio.h>
#include <math.h>

// Simple calculator with s++ syntax | C23

double calculate(double n1, char op, double n2);

int main(){
    	auto n1 = 0.0;      // Inferred type with C23 keyword auto
    double n2 = 0; // Explicit type
    char op = '+';
    double result = 0.0;
    
        printf("Xyz\nX? ");
        scanf("%lf", &n1);
    
        printf("%lfYz\nY?", n1);
        scanf(" %c", &op);
        
        printf("%lf%cZ\nZ?", n1, op);
        scanf("%lf", &n2);
    
        result = calculate(n1, op, n2);
    
        printf("%lf%c%lf = %lf\n", n1, op, n2, result);
    
        return 0;
}

double calculate(double n1, char op, double n2){
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
        		return (pow(n1, n2));
    	}
    
    	return -1;
}
