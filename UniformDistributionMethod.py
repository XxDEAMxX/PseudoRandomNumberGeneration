from LinearCongruentialMethod import LinearCongruentialMethod

class UniformDistributionMethod:
    """
        Esta clase implementa el método de distribución uniforme para generar números pseudoaleatorios.
    """

    def __init__(self, min_val, max_val, num_amount, lcm_x0, lcm_k, lcm_c, lcm_g):
        """
        Este es el método constructor de la clase UniformDistributionMethod.
        Inicializa la clase con los parámetros dados.
        """
        self.min = min_val  # Valor mínimo para el rango de números aleatorios a crear
        self.max = max_val  # Valor máximo para el rango de números aleatorios a crear
        self.num_amount = num_amount  # Cantidad de números a generar
        self.ri_values = []  # Lista para almacenar los valores de Ri
        self.ni_values = []  # Lista para almacenar los valores de Ni

        # Instancia de la clase LinearCongruentialMethod
        self.lcm = LinearCongruentialMethod(lcm_x0, lcm_k, lcm_c, lcm_g, min_val, max_val, num_amount)

    def fillRiValues(self):
        """
        Este método genera y almacena valores de Ri utilizando el método de congruencia lineal.
        """
        self.lcm.fillFirstXiValue()
        self.lcm.fillXiValues()
        self.lcm.fillRiAndNiValues()
        self.ri_values = self.lcm.get_ri_values_array()

    def obtainMinValue(self):
        """
            Este método devuelve el valor mínimo para el rango de los numeros Ni.
        """
        return self.min

    def obtainMaxValue(self):
        """
            Este método devuelve el valor máximo para el rango de los numeros Ni.
        """
        return self.max

    def fillNiValues(self):
        """
            Este método calcula y almacena los valores de Ni en función de los valores de Ri.
        """
        min_value = self.obtainMinValue()
        max_value = self.obtainMaxValue()

        for i in range(len(self.ri_values)):
            value = min_value + (max_value - min_value) * self.ri_values[i]
            self.ni_values.append(round(value, 6))

    def get_ri_values_array(self):
        """
            Este método devuelve el arreglo de valores Ri.
        """
        return self.ri_values

    def get_ni_values_array(self):
        """
            Este método devuelve el arreglo de valores Ni.
        """
        return self.ni_values

if __name__ == "__main__":
    # Parámetros del método de congruencia lineal
    seed = 1  # Valor inicial de la semilla
    a = 1103515245  # Multiplicador
    c = 12345  # Incremento
    m = 31  # Módulo

    # Parámetros del rango y cantidad
    min_val = 0  # Valor mínimo del rango
    max_val = 10  # Valor máximo del rango
    num_amount = 100  # Cantidad de números a generar

    # Crear una instancia de UniformDistributionMethod con el método de congruencia lineal
    udm = UniformDistributionMethod(min_val, max_val, num_amount, seed, a, c, m)

    # Generar los valores Ri y Ni
    udm.fillRiValues()
    udm.fillNiValues()

    # Imprimir los resultados
    print("Valores Ri:", udm.get_ri_values_array())
    print("Valores Ni (distribuidos uniformemente en el rango [0, 10]):", udm.get_ni_values_array())
