#include <iostream>
using namespace std;
#define Day 7 // �곣���� #define ������ ����ֵ

int main()
{
    cout << "hello world" << endl; //����ע��
    /*
    ����ע��
    */
    int a = 0; // ���������﷨���������� ������ = ������ʼֵ��
    cout << "a=" << a << endl;

    const int month = 12;
    // Day = 8;
    // month = 13;
    cout << "һ���ܹ��У�" << Day << "��" << endl;
    cout << "һ���ܹ��У�" << month << "��" << endl;

    // int int = 10;
    // int 123a = 10; 
    // ��������
    short num1 = 32768;
    int num2 = 32768;
    long num3 = 10;
    long long num4 = 10;
    cout <<  num1 << " " << sizeof(short) << endl;
    cout <<  num2 << " " << sizeof(int) << endl;
    cout <<  num3 << " " << sizeof(num3) << endl;
    cout <<  num4 << " " << sizeof(num4) << endl;

    // ���ָ�����
    float f1 = 3.1415926f;
    float f2 = 3e2; // 3*10^2
    float f3 = 3e-2; // 3*10^(-2)
    double d1 = 3.1415926;
    cout << f1 << endl;
    cout << f2 << endl;
    cout << f3 << endl;
    cout << d1 << endl;

    // �ַ���
    char ch = 'A'; //A-65, a-97
    // char ch1 = 'abdef'; // �ַ��͵�������ֻ����һ���ַ�
    // char ch1 = "a"; // ������˫����
    cout << (int)ch << " " << sizeof(ch) << endl;
    
    // ת���ַ�
    cout << "aa\thelloworld" << endl;
    cout << "aaaa\thelloworld" << endl;
    cout << "aaaaaa\thelloworld" << endl;
    system("pause");
    return 0;
}