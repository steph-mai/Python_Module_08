# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 15:30:32 by stmaire         #+#    #+#               #
#  Updated: 2026/03/10 15:30:37 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import importlib


def check_dependencies() -> None:
    dependencies = {
        "pandas": "Data manipulation",
        "requests": "Network access",
        "matplotlib": "Visualization"
    }

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for lib, desc in dependencies.items():
        try:
            module = importlib.import_module(lib)
            version = getattr(module, '__version__', "unknown")
            print(f"[OK] {lib} ({version}) - {desc} ready")
        except (ImportError, ValueError) as e:
            print(f"[ERROR] {lib} is missing or incompatible: {e}")


def run_analysis() -> None:
    try:
        import pandas
        import numpy
        import matplotlib.pyplot as plt

        print("Analyzing Matrix data...")
        data = numpy.random.randn(1000).cumsum()
        serie = pandas.Series(data)
        plt.plot(serie)
        plt.savefig("matrix_analysis.png")

    except ImportError:
        print("\nERROR: Analysis aborted. Missing required libraries.")


if __name__ == "__main__":
    check_dependencies()
    run_analysis()
