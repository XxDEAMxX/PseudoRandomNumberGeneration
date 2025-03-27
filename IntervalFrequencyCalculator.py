import math

class IntervalFrequencyCalculator:
    """
    Esta clase se encarga de calcular los intervalos, amplitud y frecuencias de los números generados.
    """
    def __init__(self, values):
        self.values = values  # Los números generados
        self.num_intervals = self.calculate_intervals_sturges()  # Calcular número de intervalos con la Regla de Sturges
        self.interval_data = []  # Lista para almacenar los intervalos y frecuencias

    def calculate_intervals_sturges(self):
        """
        Calcula el número de intervalos utilizando la Regla de Sturges.
        """
        n = len(self.values)
        k = 1 + 3.322 * math.log10(n)  # Regla de Sturges
        return math.ceil(k)  # Redondear hacia arriba el número de intervalos

    def calculate_intervals(self):
        """
        Este método calcula los intervalos, amplitud y frecuencias de los valores.
        """
        min_value = min(self.values)
        max_value = max(self.values)
        amplitude = (max_value - min_value) / self.num_intervals

        for i in range(self.num_intervals):
            lower_bound = min_value + i * amplitude
            upper_bound = lower_bound + amplitude
            frequency = sum(lower_bound <= x < upper_bound for x in self.values)
            self.interval_data.append({
                'lower_bound': round(lower_bound, 2),
                'upper_bound': round(upper_bound, 2),
                'frequency': frequency
            })

    def get_interval_data(self):
        """
        Retorna los datos de los intervalos y las frecuencias.
        """
        return self.interval_data
