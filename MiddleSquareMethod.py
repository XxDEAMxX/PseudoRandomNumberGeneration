class MiddleSquareMethod:
    """
        Esta clase implementa el método del cuadrado medio para generar números pseudoaleatorios.
    """

    def __init__(self, seed, min, max, numAmount):
        """
            Este es el método constructor de la clase MiddleSquareMethod.
            Inicializa la clase con los parámetros dados.
        """
        self.seed = seed  # Valor inicial de la semilla
        self.niValues = []  # Lista para almacenar los valores de Ni
        self.riValues = []  # Lista para almacenar los valores de Ri
        self.xiValues = []  # Lista para almacenar los valores de Xi
        self.centers = []  # Lista para almacenar los valores centrales
        self.min = min  # Valor Ni minimo
        self.max = max  # Valor Ni maximo
        self.numAmount = numAmount  # Numero de numeros pseudoaleatorios a generar

    def generateRandoms(self):
        """
            Este método genera números pseudoaleatorios utilizando el método del cuadrado medio.
        """
        seed = self.seed
        len_seed = len(str(self.seed))
        for i in range(self.numAmount):
            self.xiValues.append(seed)
            xi2 = seed * seed
            center = self.getCenter(str(xi2))
            self.centers.append(center)
            ri = center / self.getDivNum(len_seed)
            ri = self.truncate(ri, 5) 
            self.riValues.append(ri)
            ni = self.genNiNumber(ri)
            ni = self.truncate(ni, 5)
            self.niValues.append(ni)
            seed = center

    def genNiNumber(self, ri):
        """
            Este método genera un valor de Ni a partir de un valor de Ri determinado usando una distribucion uniforme.
        """
        return self.min + ((self.max - self.min) * ri)

    def getCenter(self, num):
        """
            Este método extrae los dígitos centrales de un número determinado.
        """
        len_seed = len(str(self.seed))
        len_num = len(str(num))
        padded = ""

        if len_num == (len_seed * 2):
            padded = num
        elif len(num) < len_seed * 2:
            while len(padded) < len_seed * 2 - len_num:
                padded = "0" + padded
            padded += num

        startIndex = int(len_seed / 2)
        endIndex = startIndex + len_seed
        center = padded[startIndex:endIndex]

        return int(center)

    def getDivNum(self, length):
        """
            Este método genera un número divisor basado en la longitud de la semilla.
            Se utiliza para calcular los valores de Ri.
        """
        num = ""
        for i in range(length):
            num += "0"
        num = "1" + num
        return float(num)

    def truncate(self, number, decimals):
        """
            Este método trunca un número a una cantidad especificada de decimales.
        """
        factor = 10 ** decimals
        return int(number * factor) / factor

    def get_xi_values_array(self):
        """
            Este método devuelve el arreglo de valores Xi.
        """
        return self.xiValues

    def get_ri_values_array(self):
        """
            Este método devuelve el arreglo de valores Ri.
        """
        return self.riValues

    def get_ni_values_array(self):
        """
            Este método devuelve el arreglo de valores Ni.
        """
        return self.niValues


if __name__ == "__main__":
    var = MiddleSquareMethod(12345, 10, 100, 20)
    var.generateRandoms()
    print("Valores Xi:", var.get_xi_values_array())
    print("Valores Ri:", var.get_ri_values_array())
    print("Valores Ni:", var.get_ni_values_array())
