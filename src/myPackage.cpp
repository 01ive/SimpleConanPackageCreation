#include <iostream>
#include "myPackage.h"

void myPackage(){
    #ifdef NDEBUG
    std::cout << "You are running my package" <<std::endl;
    #else
    std::cout << "You are running my package" <<std::endl;
    #endif
}
