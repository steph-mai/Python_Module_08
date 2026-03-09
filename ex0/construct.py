# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 16:18:00 by stmaire         #+#    #+#               #
#  Updated: 2026/03/09 17:48:53 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import os
import site


def get_environment_infos() -> None:
    if os.environ.get("VIRTUAL_ENV") is None:
        print("\nMATRIX STATUS: You're still plugged in\n")

        py_version = sys.version_info
        minor = f"{py_version.minor}"
        print(f"Current Python: {sys.executable}.{minor}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")

        print("\nThen run this program again.")

    else:
        print("MATRIX STATUS: Welcome to the construct\n")

        venv_infos: str | None = os.environ.get('VIRTUAL_ENV')
        if venv_infos is not None:
            venv_name = os.path.basename(venv_infos)
        current_py = f"{sys.executable.replace('3', '')}"

        print(f"Current Python: {current_py}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_infos}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages "
              "without affecting the global system.\n")

        print("Package installation path:")
        path = site.getsitepackages()[0]
        print(f"{path}")


if __name__ == "__main__":
    get_environment_infos()
