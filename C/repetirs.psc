Algoritmo repetirs
	Definir res Como Caracter;
	Definir nota Como Real;
	Definir ca , cr Como Entero;
	Dimension nombre[25];
	Definir nombre Como Caracter;
	ca=0;
	cr=0;
	//se inicia la estructura Repetir
	//  mayor igual >=
	// menor igual   <=
	Repetir
		Escribir "ingrese el nombre del estudiante ";
		leer nombre[25];
		Escribir "ingrese la nota del estudiante ";
		Leer nota;
		si nota >= 60 Entonces
			ca=ca+1;
		SiNo
			cr=cr+1;
		FinSi
		Escribir "Desea continuar S/N";
		Leer res;
		
		
	Hasta Que res ="n" o res="N";
	
	Escribir "APROBADOS", ca;
	Escribir "REPROBADOS", cr;
	
	
	Leer res;
	
	
	
	
	
	
	
	
	
	
	
	
FinAlgoritmo
