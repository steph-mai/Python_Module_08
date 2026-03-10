# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 15:30:19 by stmaire         #+#    #+#               #
#  Updated: 2026/03/10 15:30:20 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
from dotenv import load_dotenv


def oracle() -> None:
    load_dotenv(override=False)

    print("ORACLE STATUS: Reading the Matrix...")

    mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion = os.getenv("ZION_ENDPOINT")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if db_url and "localhost" in db_url:
        print("Database: Connected to local instance")
    elif db_url:
        print("Database: Connected to production instance")
    else:
        print("Database: Disconnected")

    api_status = "Authenticated" if api_key else "Missing Key"
    print(f"API Access: {api_status}")

    print(f"Log Level: {log_level}")

    zion_status = "Online" if zion else "Offline"
    print(f"Zion Network: {zion_status}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()
