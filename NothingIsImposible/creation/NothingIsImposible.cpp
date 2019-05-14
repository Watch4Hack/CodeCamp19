#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <string.h>
#include <iostream>        // Instrucciones declarativas.
using namespace std;

char myword[] = { '3', 'D', 'B', 'U', '1', 'N', 'C' , 'G', '$', 'P', 'R'};

int main()
{
  std::cout << "\n\n\n";
  std::cout << "#####  #####  ###    #####  #####  #####  ### ###  #####     ##  ##### \n";
  std::cout << "#      #   #  #  #   #      #      #   #  #  #  #  #   #    # #  #   # \n";
  std::cout << "#      #   #  #   #  ####   #      #####  #  #  #  #####   #  #  ##### \n";
  std::cout << "#      #   #  #  #   #      #      #   #  #     #  #          #      # \n";
  std::cout << "#####  #####  ###    #####  #####  #   #  #     #  #          #      # \n";
  std::cout << "\n\n";
  srand (time(NULL));
  int iSecret = rand() % 100 + 1;
  if (iSecret == 256){
    string salida = "CodeCamp19{";
    salida += myword[1];
    salida += myword[0];
    salida += myword[2];
    salida += myword[3];
    salida += myword[7];
    salida += myword[4];
    salida += myword[5];
    salida += myword[7];
    salida += '_';
    salida += myword[6];
    salida += myword[9];
    salida += myword[9];
    salida += "}\n\n-----------------------------------------------\n\n";
    std::cout << "\n\n----------------------------------------------\n\nGood debug, the flag is: --->   ";
    std::cout << salida;
  }
  else
    std::cout << "The value of your var is " << iSecret << " and you need 256 \n\n";
  return 0;
}
