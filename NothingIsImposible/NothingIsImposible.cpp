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
