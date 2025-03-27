import matplotlib
matplotlib.use('Agg')

from flask import Flask, render_template, request, redirect, url_for, flash
from LinearCongruentialMethod import LinearCongruentialMethod
from MiddleSquareMethod import MiddleSquareMethod
from MultiplicativeCongruentialMethod import MultiplicativeCongruentialMethod
from NormalInvDistributionMethod import NormalInvDistributionMethod
from UniformDistributionMethod import UniformDistributionMethod
from IntervalFrequencyCalculator import IntervalFrequencyCalculator
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.secret_key = 'some_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        method = request.form['selected_method']

        if not request.form['iterations'].isdigit():
            flash('El número de iteraciones debe ser un entero válido.')
            return redirect(url_for('index'))    

        iterations = int(request.form['iterations'])

        if iterations < 1 or iterations > 1000000:
            flash('El número de iteraciones debe estar entre 1 y 1,000,000.')
            return redirect(url_for('index'))

        result = {}
        plot_url = None

        if method in ['LinearCongruential', 'MiddleSquare', 'MultiplicativeCongruential']:
            xo = int(request.form['xo'])
            min_val = float(request.form.get('min'))
            max_val = float(request.form.get('max'))

            if method == 'LinearCongruential':
                k = int(request.form['k'])
                c = int(request.form['c'])
                g = int(request.form['g'])

                lcm = LinearCongruentialMethod(xo, k, c, g, min_val, max_val, iterations)
                lcm.fillFirstXiValue()
                lcm.fillXiValues()
                lcm.fillRiAndNiValues()

                result['xi'] = lcm.get_xi_values_array()
                result['ri'] = lcm.get_ri_values_array()
                result['ni'] = lcm.get_ni_values_array()

            elif method == 'MiddleSquare':
                msm = MiddleSquareMethod(xo, min_val, max_val, iterations)
                msm.generateRandoms()

                result['xi'] = msm.get_xi_values_array()
                result['ri'] = msm.get_ri_values_array()
                result['ni'] = msm.get_ni_values_array()

            elif method == 'MultiplicativeCongruential':
                k = int(request.form['k2'])
                g = int(request.form['g2'])

                mcm = MultiplicativeCongruentialMethod(xo, k, g, min_val, max_val, iterations)
                mcm.fillFirstXiValue()
                mcm.fillXiValues()
                mcm.fillRiAndNiValues()

                result['xi'] = mcm.get_xi_values_array()
                result['ri'] = mcm.get_ri_values_array()
                result['ni'] = mcm.get_ni_values_array()

            img = io.BytesIO()
            plt.plot(result['ri'], label='Valores Ri')
            plt.title(f'Gráfico de los Valores Ri - {method}')
            plt.legend()
            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()

        elif method in ['NormalInvDistribution', 'UniformDistribution']:
            xo = int(request.form['xo'])
            k = int(request.form['k'])
            c = int(request.form['c'])
            g = int(request.form['g'])

            if method == 'NormalInvDistribution':
                mean = float(request.form['mean'])
                std_dev = float(request.form['std_dev'])

                nidm = NormalInvDistributionMethod(iterations, mean, std_dev, xo, k, c, g)
                nidm.fillRiValues()
                nidm.fillNiValues()

                result['ri'] = nidm.get_ri_values_array()
                result['ni'] = nidm.get_ni_values_array()

            elif method == 'UniformDistribution':
                min_val = float(request.form.get('min2'))
                max_val = float(request.form.get('max2'))

                udm = UniformDistributionMethod(min_val, max_val, iterations, xo, k, c, g)
                udm.fillRiValues()
                udm.fillNiValues()

                result['ri'] = udm.get_ri_values_array()
                result['ni'] = udm.get_ni_values_array()

            interval_calculator = IntervalFrequencyCalculator(result['ni'])
            interval_calculator.calculate_intervals()
            interval_data = interval_calculator.get_interval_data()

            img = io.BytesIO()
            plt.figure(figsize=(10, 6))
            intervals = [f"{i['lower_bound']} - {i['upper_bound']}" for i in interval_data]
            frequencies = [i['frequency'] for i in interval_data]
            plt.bar(intervals, frequencies, color='blue')
            plt.title(f'Histograma de la Distribución - {method}')
            plt.xlabel('Intervalos')
            plt.ylabel('Frecuencia')
            plt.xticks(rotation=45)
            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()

        return render_template('results.html', result=result, plot_url=plot_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
