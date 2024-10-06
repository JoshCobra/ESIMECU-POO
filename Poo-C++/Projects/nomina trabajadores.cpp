#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
 
int main() {
 
    int totalT = 0;
    printf("Ingrese el total de trabajadores Categoria A: ");
    scanf("%d", &totalT);
 
    float tem = 0;
    float sueldoTA[totalT];
    float horasTA[totalT];
    float sueTpH[totalT];
    float sueldoNT = 0.0;
    float sueldoBT = 0.0;
    float horasTTA = 0.0;
    float sumaDes = 0.0;
 
    for (register int i = 0; i < totalT; i++) {
 
        do {
            printf("Ingrese el sueldo por hora del trabajador %d: ", i + 1);
            scanf("%f", &sueldoTA[i]);
            printf("Ingrese las horas del trabajador %d: ", i + 1);
            scanf("%f", &horasTA[i]);
        } while (sueldoTA[i] <= 0 || horasTA[i] < 0);
 
        sueldoBT += sueldoTA[i];
        horasTTA += horasTA[i];
 
        if (150 >= sueldoTA[i]) {
            tem = sueldoTA[i] * 5;
        } else if (150 < sueldoTA[i] && sueldoTA[i] < 300) {
            tem = sueldoTA[i] * 7;
        } else {
            tem = sueldoTA[i] * 9;
        }
 
        tem /= 100;
        sueldoTA[i] = (sueldoTA[i] - tem);
        sumaDes += tem;
 
        sueTpH[i] = sueldoTA[i] * horasTA[i];
        printf("Sueldo del trabajador %d, por las horas trabajadas es de: %2.2f \n", i + 1, sueTpH[i]);
 
    }
 
    for (size_t n = 0; n < totalT; n++) {
        sueldoNT += sueTpH[n];
    }
 
    printf("\nTotal Sueldos Base categoria A: %2.2f\n", sueldoBT);
    printf("Total horas trabajadas categoria A: %2.2f\n", horasTTA);
    printf("Sueldos de descuento categoria A : %2.2f\n", sumaDes);
    printf("Total de sueldos netos categoria A: %2.2f\n\n", sueldoNT);
 
    int totalB = 0;
    printf("Ingrese el total de trabajadores Categoria B: ");
    scanf("%d", &totalB);
 
    float sueldoTB[totalB];
    float horasTB[totalB];
    float sTpH[totalB];
    sueldoNT = 0;
    sueldoNT = 0.0;
    sueldoBT = 0.0;
    float horasTTB = 0.0;
    sumaDes = 0.0;
 
    for (register int j = 0; j < totalB; j++) {
 
        do {
            printf("Ingrese el sueldo por hora del trabajador %d: ", j + 1);
            scanf("%f", &sueldoTB[j]);
            printf("Ingrese las horas del trabajador %d: ", j + 1);
            scanf("%f", &horasTB[j]);
        } while (sueldoTB <= 0 || horasTB < 0);
 
        sueldoBT += sueldoTB[j];
        horasTTB += horasTB[j];
 
        if (250 >= sueldoTB[j]) {
            tem = sueldoTB[j] * 7.0;
        } else if (250 < sueldoTB[j] && sueldoTB[j] < 500) {
            tem = sueldoTB[j] * 10.0;
        } else {
            tem = sueldoTB[j] * 9.0;
        }
 
        tem /= 100;
        sueldoTB[j] = (sueldoTB[j] - tem);
        sumaDes += tem;
 
        sTpH[j] = sueldoTB[j] * horasTB[j];
        printf("Sueldo del trabajador %d, por las horas trabajadas es de: %2.2f \n", j + 1, sTpH[j]);
    }
 
    for (size_t n = 0; n < totalB; n++) {
        sueldoNT += sTpH[n];
    }
 
    printf("\nTotal Sueldos Base categoria B: %2.2f\n", sueldoBT);
    printf("Total horas trabajadas categoria B: %2.2f\n", horasTTB);
    printf("Sueldos de descuento categoria B : %2.2f\n", sumaDes);
    printf("Total de sueldos netos categoria B: %2.2f\n", sueldoNT);
 
    return EXIT_SUCCESS;
 
}
