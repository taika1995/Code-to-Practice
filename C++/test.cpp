#include <iostream>
using namespace std;
#define Day 7 // 宏常量： #define 常量名 常量值

int main()
{
    cout << "hello world" << endl; //单行注释
    /*
    多行注释
    */
    int a = 0; // 变量创建语法：数据类型 变量名 = 变量初始值；
    cout << "a=" << a << endl;

    const int month = 12;
    // Day = 8;
    // month = 13;
    cout << "一周总共有：" << Day << "天" << endl;
    cout << "一年总共有：" << month << "月" << endl;

    // int int = 10;
    // int 123a = 10; 
    // 各种整型
    short num1 = 32768;
    int num2 = 32768;
    long num3 = 10;
    long long num4 = 10;
    cout <<  num1 << " " << sizeof(short) << endl;
    cout <<  num2 << " " << sizeof(int) << endl;
    cout <<  num3 << " " << sizeof(num3) << endl;
    cout <<  num4 << " " << sizeof(num4) << endl;

    // 各种浮点型
    float f1 = 3.1415926f;
    float f2 = 3e2; // 3*10^2
    float f3 = 3e-2; // 3*10^(-2)
    double d1 = 3.1415926;
    cout << f1 << endl;
    cout << f2 << endl;
    cout << f3 << endl;
    cout << d1 << endl;

    // 字符型
    char ch = 'A'; //A-65, a-97
    // char ch1 = 'abdef'; // 字符型单引号内只能有一个字符
    // char ch1 = "a"; // 不能用双引号
    cout << (int)ch << " " << sizeof(ch) << endl;
    
    // 转义字符
    cout << "aa\thelloworld" << endl;
    cout << "aaaa\thelloworld" << endl;
    cout << "aaaaaa\thelloworld" << endl;
    system("pause");
    return 0;
}