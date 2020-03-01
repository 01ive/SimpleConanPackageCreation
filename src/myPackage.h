#pragma once

#ifdef WIN32
  #define MYPACKAGE_EXPORT __declspec(dllexport)
#else
  #define MYPACKAGE_EXPORT
#endif

MYPACKAGE_EXPORT void myPackage();
