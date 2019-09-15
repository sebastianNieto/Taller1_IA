#********************************************************************
# Calculadora de matrices: realiza operaciones básicas entre matrices
# y guarda los resultados en un archivo de texto
#
# Desarrollado por:
# John Sebastian Nieto Gil
# Ricardo Andres Villalobos Marulanda
#**********************************************************************

from random import randint
import os

class Calculadora:
    # Limpia la terminal dependiendo del sistema
    def limparPantalla(self):
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")

    # Muestra las opciones del menu inicial
    def showMenu(self):
        self.limparPantalla()
        print ("    ***** MENU *****")
        print ("")
        print ("[1] Suma de Matrices")
        print ("[2] Resta de Matrices")
        print ("[3] Multiplicacion de Matrices")
        print ("[4] Determinante de Matriz")
        print ("[5] Transpuesta de una Matriz")
        print ("[6] Multiplicacion por escalar")
        print ("[7] Generar matriz aleatoria")
        print ("[0] Salir")
        print ("")

    # Crea un matriz de m * n. El inidicativo es un nombre que se le puede dar a la matriz
    def ingresarMatriz(self, indicativo = ''):
        filas = input("Ingrese la cantidad de filas para la matriz {}: ".format(indicativo))
        columnas = input("Ingrese la cantidad de columnas para la matriz {}: ".format(indicativo))
        fila = []
        matriz = []
        for f in list(range(int(filas))):
            for c in list(range(int(columnas))):
                fila.append(int(input("Elemento [{}, {}]: ".format(f,c))))
            matriz.append(fila.copy())
            fila.clear()
        return matriz

    # Guarda el resultado de una matriz en un archivo de text
    def saveFile(self, result, operacion = ''):
        f = open('resultados.txt','a')
        f.write('----------------------------------------- \n')
        f.write('Operacion: ' + operacion + '\n')
        f.write('[ \n')
        for i in range(len(result)):
            for j in range(len(result[i])):
                f.write('%s, ' % str(result[i][j]))
            f.write('\n')
        f.write('] \n')
        f.write('----------------------------------------- \n \n')
        f.close()
    
    # Muestra el resultado de la operación realizada en pantalla
    def showResult(self, result, operacion = ''):
        self.limparPantalla()
        print('')
        print('--------------------')
        print('Matriz resultante de la operacion: ' + operacion + ': ')
        print('')
        print('[')
        for i in range(len(result)):
            for j in range(len(result[i])):
                print ('{:>3s}'.format(str(result[i][j])), end=', '),
            print('')
        print (']')
        print('')
        print('--------------------')
        print('')
        guardar = input('¿ Desea guardar el resultado N/Y ? ')
        if guardar.upper() != 'N':
            self.saveFile(result, operacion)

    # Valida si dos matrices son iguales en sus dimensiones
    def validarMatricesIguales(self, matrizA, matrizB):
        return all(len(lst) == len(matrizA) for lst in [matrizB])

    # Valida si la cantidad de filas de la primer matriz es igual a la cantidad de columnas de la segunda y viceversa
    def validarMatricesMultiplicacion(self, matrizA, matrizB):
        return len(matrizA[0]) == len(matrizB)
 
    # Valida si las dimensiones de una matriz son iguales
    def validarMatrizCuadrada(self, matriz):
        return len(matriz) == len(matriz[0])

    # Reserva las dimensiones para una matriz
    def reservarMatriz(self, filas, columnas):
        result = []
        for i in range (filas):
            result.append([0] * columnas)
        return result

    # Suma o Resta dos matrices según la operación indicada
    def sumaRestaMatriz(self, operacion, matrizA, matrizB):
        filas = len(matrizA)
        columnas = len(matrizA[0])
        result = self.reservarMatriz(filas, columnas)

        for a in range(filas):
            for b in range(columnas):
                if operacion == '+':
                    result[a][b] += matrizA[a][b] + matrizB[a][b]
                else:
                    result[a][b] += matrizA[a][b] + matrizB[a][b]
        return result

    # Multiplica dos matrices y retorna la matriz resultante
    def multiplicarMatriz(self, matrizA, matrizB):
        filas1 = len(matrizA)
        filas2 = len(matrizB)
        columnas1 = len(matrizA[0])
        columnas2 = len(matrizB[0])
        result = self.reservarMatriz(filas1, columnas2)

        for a in range(filas1):
            for b in range(columnas2):
                for c in range(filas2):
                    result[a][b] += matrizA[a][c] * matrizB[c][b]
        return result

    # Retorna el determinante de una matriz cuadrada
    def determinanteMatriz(self, matriz):
        filas = len(matriz)
        resultante = []
        resultante.append([0] * 1)
        if (filas > 2):
            i = 1
            j = 0
            result = 0
            while j <= filas - 1:
                d = {}
                t1 = 1
                while t1 <= filas - 1:
                    m = 0
                    d[t1] = []
                    while m <= filas - 1:
                        if (m == j):
                            u = 0
                        else:
                            d[t1].append(matriz[t1][m])
                        m += 1
                    t1 += 1
                l1 = [d[x] for x in d]
                result = result + i*(matriz[0][j])*(det(l1))
                i = i*(-1)
                j += 1
            resultante[0][0] = (result)
        else:
            resultante[0][0] = (matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0])
        return resultante

    # Retorna la transpuesta de una matriz
    def transponerMatriz(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        result = self.reservarMatriz(columnas, filas)

        for i in range(filas):
            for j in range(columnas):
                result[j][i] = matriz[i][j]
        return result
    
    # Retorna una matriz resultante de multiplicar una matriz por un escalar
    def multiplicarEscalarMatriz(self, matriz, escalar):
        filas = len(matriz)
        columnas = len(matriz[0])
        result = self.reservarMatriz(filas, columnas)

        for i in range (filas):
            for j in range (columnas):
                result[i][j] = matriz[i][j] * escalar
        return result

    # Retorna una matriz n * m con valores aleatoros 
    def generarMatrizAleatoria(self):
        filas = int(input("Ingrese el numero de filas: "))
        columnas = int(input("Ingrese el numero de columnas: "))
        result = self.reservarMatriz(filas, columnas)

        for i in range (filas):
            for j in range (columnas):
                result[i][j] = randint(-100,100)
        return result            

    # Funcion principal del programa que ejecuta el menu y las diferentes operaciones realizadas
    def main(self):
        opcion = 1
        msgerror = "ERROR: Las matrices deben poseer las mismas dimensiones, es decir  la misma cantidad tanto de columnas como de filas."
        while opcion != 0:
            self.showMenu()
            opcion = int(input("Ingrese Opcion: "))
            self.limparPantalla()
            if opcion == 1:
                matrizA = self.ingresarMatriz('A')
                matrizB = self.ingresarMatriz('B')
                if self.validarMatricesIguales(matrizA, matrizB):
                    result = self.sumaRestaMatriz('+', matrizA, matrizB)
                    self.showResult(result, 'Suma')
                else:
                    print(msgerror)
            elif opcion == 2:
                matrizA = self.ingresarMatriz('A')
                matrizB = self.ingresarMatriz('B')
                if self.validarMatricesIguales(matrizA, matrizB):
                    result = self.sumaRestaMatriz('-', matrizA, matrizB)
                    self.showResult(result, 'Resta')
                else:
                    print(msgerror)
            elif opcion == 3:
                matrizA = self.ingresarMatriz('A')
                matrizB = self.ingresarMatriz('B')
                if self.validarMatricesMultiplicacion(matrizA, matrizB):
                    result = self.multiplicarMatriz(matrizA, matrizB)
                    self.showResult(result, 'Multiplicacion')
                else:
                    print("El numero de columnas de la matriz A debe ser igual al numero de filas de la matriz B")
            elif opcion == 4:
                matriz = self.ingresarMatriz('')
                if self.validarMatrizCuadrada(matriz):
                    result = self.determinanteMatriz(matriz)
                    self.showResult(result, 'Determinante')
                else:
                    print("La matriz no es cuadrada")
            elif opcion == 5:
                matrizA = self.ingresarMatriz('')
                result = self.transponerMatriz(matrizA)
                self.showResult(result, 'Transpuesta')
            elif opcion == 6:
                matrizA = self.ingresarMatriz('')
                escalar =  int(input("Ingrese el escalar: "))
                result = self.multiplicarEscalarMatriz(matrizA, escalar)
                self.showResult(result, 'Escalar')
            elif opcion == 7:
                result = self.generarMatrizAleatoria()
                self.showResult(result, 'Aleatoria')
            elif opcion == 0:
                print("Vuelve pronto...")
            input("Presione una tecla para continuar ")

if __name__ == "__main__":
    c = Calculadora()
    c.main()
