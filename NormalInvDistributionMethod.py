from LinearCongruentialMethod import LinearCongruentialMethod
from scipy.stats import norm

class NormalInvDistributionMethod:
    """
        Esta clase implementa el método de distribución inversa normal para generar números pseudoaleatorios.
    """

    def __init__(self, iterations, mean, std_dev, lcm_x0, lcm_k, lcm_c, lcm_g):
        """
        Este es el método constructor de la clase NormalInvDistributionMethod.
        Inicializa la clase con los parámetros dados.
        """
        self.iterations = iterations  # Número de iteraciones
        self.mean = mean  # Media de la distribución normal
        self.std_dev = std_dev  # Desviación estándar de la distribución normal
        self.ri_values = []  # Lista para almacenar los valores de Ri
        self.ni_values = []  # Lista para almacenar los valores de Ni

        # Instancia de la clase LinearCongruentialMethod
        self.lcm = LinearCongruentialMethod(lcm_x0, lcm_k, lcm_c, lcm_g, 0, 1, iterations)

    def fillRiValues(self):
        """
        Este método genera y almacena valores de Ri utilizando el método de congruencia lineal.
        """
        self.lcm.fillFirstXiValue()
        self.lcm.fillXiValues()
        self.lcm.fillRiAndNiValues()
        self.ri_values = [ri for ri in self.lcm.get_ri_values_array() if 0 < ri < 1]  # Excluye 0 y 1

    def fillNiValues(self):
        """
            Este método calcula y almacena los valores de Ni basándose en los valores de Ri utilizando la distribución inversa de la normal.
        """
        average = self.mean
        standard_deviation = self.std_dev

        for i in range(len(self.ri_values)):
            ni_value = float(norm.ppf(self.ri_values[i], loc=average, scale=standard_deviation))
            self.ni_values.append(round(ni_value, 5))

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
    seed = 345  # Valor inicial de la semilla (x0)
    a = 67  # Multiplicador (a)
    c = 57  # Incremento (c)
    m = 16  # Módulo (m)

    # Parámetros de la distribución normal
    mean = 0  # Media de la distribución normal
    std_dev = 1  # Desviación estándar de la distribución normal
    iterations = 100  # Número de iteraciones/números a generar

    nidm = NormalInvDistributionMethod(iterations, mean, std_dev, seed, a, c, m)

    nidm.fillRiValues()
    nidm.fillNiValues()

    print("Valores Ri:", nidm.get_ri_values_array())
    print("Valores Ni (distribuidos normalmente):", nidm.get_ni_values_array())
