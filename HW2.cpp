// Author: CS1300 Fall 2017         Hanye Han
// Recitation: 123 – Favorite TA    101 - Richard Tillquist
//
// Assignment 2

#include <iostream>

using namespace std;

/**
 * one year have 365*60*60seconds, and population plus birth and immigrant minutes death is the current population
 *
 */
int howMany(int population) {
	population=population +365*60*60*24/8-365*60*60*24/12+365*60*60*24/33;
    return population;
}

/**
 * at first find the days, int days make sure days are integer, use seconds minutes days to calculate how many seconds left, and hours minutes are same.
 *
 */
void howLong(int seconds) {
	if(seconds<0){
		seconds=0;}
	else{
		seconds=seconds;}
	int days=0;
	int hours=0;
	int minutes=0;
	days=seconds/86400;
	seconds =seconds-days*86400;
	hours=seconds/3600;
	seconds=seconds-hours*3600;
	minutes=seconds/60;
	seconds=seconds-60*minutes;

	cout<<"Time is "<<days<<" days, "<<hours<<" hours, "<<minutes<<" minutes, and "<<seconds<<" seconds.";
    return;
}

/**
 * F=C*1.8+32
 *
 */
int howHot(int temperature) {
	temperature=temperature*1.8+32;
    return temperature;
}


int main() {
    // Problem 1 test
    // Change value of 'pop' to change value you want to test
    int pop = 1000000;
    cout << "Given the initial population of " << pop;
    cout << " your estimation finds a population of ";
    cout << howMany(pop) << endl << endl;

    // Problem 2 test
    // Change value 'sec' to change value you want to test
    int sec = 120;
    cout << "Given the seconds value of " << sec;
    cout << " your output is: " << endl;
    howLong(sec);
    cout << endl;

    // Problem 3 test
    // Change value 'temp' to change value you want to test
    int temp = 32;
    cout << "Given temperature " << temp;
    cout << " degrees Celsius you calculate ";
    cout << howHot(temp) << " degrees Fahrenheit" << endl;
    return 0;
}
