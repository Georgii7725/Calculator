# Calculator
Project consist of 3 python files. 
In calculate-beta you will find calculator, that can calculates sum, difference, product and quotient of two non-negative numbers in any notation, that less than 10.
In second one (calculate-alfa) there is code, that can do same things, but for two whole numbers
In third file I absolutely change architecture. Before numbers were inteder and they parse number position, now number present as array. Due to this fact notation may be no more than 36 
The suumator and the additor were implemented via bitwise computation
The differator, that calculate difference between two numbers, and divider were implemented as finding a results, that satisfies summator or additor.
I mean a - b is c, that satisfies expression c + b = a. Also it was implemented in divider: find c = a / b is find c, that satisfies expression c * b = a
