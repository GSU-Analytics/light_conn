# config.py

"""

****************************************************************************************************
*       ADD YOUR OWN CREDENTIALS AND CONNECTION DETAILS. THEN RENAME THIS FILE TO config.py        *
****************************************************************************************************

Configuration settings for database connections, including credentials and connection details.
This module contains configuration details used by the `oracle_connect.py` for connecting to Oracle databases. 
It specifies usernames, database names, hostnames, port numbers, and driver information required for establishing 
database connections.

The `oracle_user`, `lib_dir`, and `oracle_dsn` are used for Oracle database connections, specifying the Oracle user, 
library directory (for Oracle Client libraries), and the Data Source Name (DSN) for the Oracle database.

Attributes:

    oracle_user (str): The username for the Oracle database connection.
    lib_dir (str): The directory path where the Oracle Client libraries are located.
    oracle_dsn (str): The Data Source Name for the Oracle database connection.

Example usage with `oracle_connect.py`:
    from oracle_connect import LightOracleConnection
    import setup
    
    oracle_conn = LightOracleConnection(user=setup.oracle_user,
                                        dsn=setup.oracle_dsn,
                                        lib_dir=setup.lib_dir)
    oracle_conn.connect()

Note:
    Ensure that the driver specified in `driver` is installed and matches the version of your SQL Server.
    If the path to the Oracle Client libraries is not specified in your Windows PATH, set the `lib_dir` to 
    the location of the Oracle Client libraries on your machine otherwise leave the string empty. If the 
    Oracle Client libraries are not installed, See the Oracle Instant Client installation guide for more 
    information: https://www.oracle.com/database/technologies/instant-client.html
"""

# Oracle Connection details
oracle_user = "dummy_name"  # The Oracle user
lib_dir = ""
oracle_dsn = ""  # The Data Source Name for the Oracle database