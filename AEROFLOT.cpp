/*  Задача 1: Описать структуру AEROFLOT            - Done 
    Задача 2: Ввод в массив 7 объектов              - Done
    Задача 3: Сортировка массива по destinastion    - Done
    Задача 4: Вывод всех объектов                   - Done
    Задача 5: Вывод объектов по типу                - Done
*/

#include <iostream>
#include <cstring>
using namespace std;

const int len = 7;
//Задача 1
class AEROFLOT{
    public:
    char destination[20] = "";
    int number;
    char type;

    void setValues(char *initD, int initN, char initT){
        strcpy(destination, initD);
        number = initN;
        type = initT;
    }
// Задача 4
    void getValues(){
        cout << destination << endl << number << endl << type << endl;
    }
//Задача 5
    void getSomeValues(char needType){
        if(type == needType){
            cout << destination << endl << number << endl << type << endl;
        }
    }
};

void sort(AEROFLOT mass[]){
    for(int i = 0; i < len; i++){
        for(int j = 0; j < len; j++){
            if(strcmp(mass[j].destination, mass[i].destination) > 0){
                AEROFLOT tmp;
                tmp.setValues(mass[j].destination, mass[j].number, mass[j].type);
                mass[j].setValues(mass[i].destination, mass[i].number, mass[i].type);
                mass[i].setValues(tmp.destination, tmp.number, tmp.type);
            }
        }
    }
}

int main(){

//Задача 2
    AEROFLOT mass[len];               
    for(int i = 0; i < len; i++){     
        char initD[20]; int initN; char initT;
        cout << "Самолёт № " << i << endl;
        cout << "Введите пункт назначения рейса: ";  
        cin >> initD;
        cout << "Введите номер рейса: ";
        cin >> initN;
        cout << "Введите тип самолёта: ";
        cin >> initT;
        mass[i].setValues(initD, initN, initT);
    }
    cout << endl << "Несортированый список самолётов" << endl;
//Задача 3
    for(int i = 0; i < len; i++){
        cout << "Самолёт № " << i << endl;
        mass[i].getValues();
    }

    sort(mass);

    cout << endl << "Сортированый список самолётов" << endl;
    for(int i = 0; i < len; i++){
        cout << "Самолёт № " << i << endl;
        mass[i].getValues();
    }
//Задача 5
    char needType;
    cout << "Введите нужный тип самолёта: ";
    cin >> needType;
    for(int i = 0; i < len; i++){
        cout << "Самолёт № " << i << endl;
        mass[i].getSomeValues(needType);
    }
}
