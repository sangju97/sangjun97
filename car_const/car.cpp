#include "car.h""

class Car {
public:
	Car() : name(), cc(0), hp(0) {}
	Car(string name, double cc, double hp) : name(name), cc(cc), hp(hp) {}

	string Getname() {
		return name;
	}
	void Setname(string name_) {
		name = name_;
	}

	double Getkm() {
		return cc;
	}

	void Setkm(double cc_) {
		cc = cc_;
	}

	double Gethp() {
		return hp;
	}

	void Sethp(double hp_) {
		hp = hp_;
	}

private:
	string name;
	double cc;
	double hp;
};