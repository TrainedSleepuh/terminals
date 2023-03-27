// LEARNING:
        //  Encapsulation
        //  Abstraction
        //  Inheritance
        //  Polymorphism

#include <iostream>
using std::string;

class AbstractEmployee {
    virtual void AskForPromotion() = 0;
};

class Employee:AbstractEmployee {
private:
    string Company;
    int Age;
protected:
    string Name;
public:
    void setName(string name) {
        Name = name;
    } 
    string getName() {
        return Name;
    }
    void setCompany(string company) {
        Company = company;
    }
    string getCompany() {
        return Company;
    }
    void setAge(int age) {
        if(age>=18)
        Age = age;
    }
    int getAge() {
        return Age;
    }

    void IntroduceYourself() {
        std::cout << "Name - " << Name << std::endl;
        std::cout << "Company - " << Company << std::endl;
        std::cout << "Age - " << Age << std::endl;
    }
    Employee(string name, string company, int age) {
        Name = name;
        Company = company;
        Age = age;
    }
    void AskForPromotion() {
        if(Age>30)
            std::cout << Name << " got promoted!" << std::endl;
        else
            std::cout << Name << ", sorry NO promotion for you!" << std::endl;
    }
};

class Developer:Employee {
public:
    string FavProgrammingLanguage;
    Developer(string name, string company, int age, string favprogramminglanguage)
        :Employee(name, company, age)
    {
        FavProgrammingLanguage = favprogramminglanguage;
    }
    void FixBug() {
        std::cout << Name << " fixed bug using " << FavProgrammingLanguage << std::endl;
    }
};
int main()
{
    // Employee employee1 = Employee("Wolfgang", "Wolfgang Corp", 37);
    // Employee employee2 = Employee("Mike", "Wolfgang Corp", 25);

    // std::cout << employee1.getName() << " is " << employee1.getAge() << " years old" << std::endl << std::endl;
    // std::cout << employee2.getName() << " is " << employee2.getAge() << " years old" << std::endl << std::endl;

    // employee1.AskForPromotion();
    // employee2.AskForPromotion();

    Developer d = Developer("Billy", "Wolfgang Corp", 19, "C++");
    d.FixBug();
}

// 1:07:33