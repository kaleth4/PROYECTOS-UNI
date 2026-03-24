Algoritmo calculadora
	Definir res Como Caracter;
	
	Escribir "las opciones del 1 al 3 de acuerdo al operacion"
	leer NUMERO;
	segun NUMERO Hacer
		1:
			Escribir "digite primer numero a sumar";
			leer s1;
			Escribir "digite segundo numero a sumar";
			leer s2;
			res=s1+s2;
			escribir"el resultado de la suma es",res;
			
			
		2:
			Escribir "digite primer numero a restar";
			leer s1;
			Escribir "digite segundo numero a restar";
			leer s2;
			res=s1-s2;
			escribir"el resultado de la resta es",res;
		3:
			Escribir "digite primer numero a multiplicar";
			leer s1;
			Escribir "digite segundo numero a multiplicar";
			leer s2;
			res=s1*s2;
			escribir"el resultado de la multiplicacion es",res;
			
		De Otro Modo:
			Escribir "Favor escribir la opcion que desea";
			
	FinSegun
FinAlgoritmo
