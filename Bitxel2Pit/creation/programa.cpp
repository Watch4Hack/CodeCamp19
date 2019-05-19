#include <iostream>        // Instrucciones declarativas.
#include <stdio.h>
#include <string.h>

using namespace std;

char myword[] = { 'J', 't', 'o', 'U', '5', '0', '1' , 'M', '3', 'n'};

int main()                 // Esta es la función main.
{
std::cout << "\n\n\n";
std::cout << "#####  #####  ###    #####  #####  #####  ### ###  #####     ##  ##### \n";
std::cout << "#      #   #  #  #   #      #      #   #  #  #  #  #   #    # #  #   # \n";
std::cout << "#      #   #  #   #  ####   #      #####  #  #  #  #####   #  #  ##### \n";
std::cout << "#      #   #  #  #   #      #      #   #  #     #  #          #      # \n";
std::cout << "#####  #####  ###    #####  #####  #   #  #     #  #          #      # \n";
std::cout << "\n\n";
string salida = "CodeCamp19{";
salida += myword[1];
salida += myword[3];
salida += myword[4];
salida += '_';
salida += myword[5];
salida += myword[0];
salida += myword[2];
salida += myword[4];
salida += '_';
salida += myword[1];
salida += myword[8];
salida += '_';
salida += myword[7];
salida += myword[6];
salida += myword[8];
salida += myword[9];
salida += myword[1];
salida += myword[8];
salida += myword[9];
salida += "}\n\n-----------------------------------------------\n\n";
std::cout << "\n\n----------------------------------------------\n\nGracias por tu increible labor, aquí tienes tu pago: --->   ";
std::cout << salida;

return 0;                  // Indica la finalización del programa.

}
