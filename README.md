# Light Oracle Connection

## Description
A lightweight Oracle database connection handler for managing secure database interactions.

## Installation Instructions

### Local Installation

For local installation, particularly useful if you plan to contribute to the package or need a development setup:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/GSU-Analytics/lightoracle.git
   cd lightoracle
   ```

2. **Create and Activate the Conda Environment**:
   Use the `local_install.yaml` located in the conda_env folder to set up an environment with all necessary dependencies 
   installed via Conda. Navigate to the directory containing `local_install.yaml`, or specify the full path to the file.

   ```bash
   conda env create -f local_install.yaml
   conda activate lightoracle
   ```

3. **Install the Package Locally**:
   This step installs the current local version of the package into the Conda environment.
   ```bash
   pip install .
   ```

### Remote Installation

This approach does not require cloning the repository as it installs the package directly from the remote repository. This is useful 
for users who only need to use the package without contributing to its development.

1. **Create and Activate the Conda Environment**:
   Copy the `remote_install.yaml` located in the conda_env folder to your local machine. 

   ```yaml
   # remote_install.yaml

   name: lightoracle
   channels:
   - defaults
   dependencies:
   - python>=3.10
   - pip:
      - git+https://github.com/GSU-Analytics/light_conn.git
   ```

   Install the package by following these steps: 
   1. Check that conda is installed by typing `conda -v` in the command line.
   2. Create a new conda environment using the `remote_install.yaml` file with the following command:
      ```cmd
      conda env create -f remote_install.yaml
      conda activate lightoracle
      ```

## Usage

To establish a connection to an Oracle database using the `LightOracleConnection` class, configure your connection parameters in the `config_example.py` file. After configuring the `config_example.py` file, rename the file to `config.py` and you can use these parameters to establish a connection to your Oracle database.Here's a guide on how to do that and then utilize the configuration to connect to your Oracle database.

### Configuring Connection Parameters

The `config_example.py` file contains essential attributes for setting up your Oracle database connection. Before you begin using the `LightOracleConnection`, make sure you have correctly configured the following attributes:

- `oracle_user`: Your Oracle database username.
- `lib_dir`: The directory path to the Oracle Client libraries on your machine. This is necessary if your Oracle Client libraries are not included in your system's PATH environment variable.
- `oracle_dsn`: The Data Source Name for the Oracle database connection, which typically includes the hostname, port, and database name.

Here's an example of how to set up `config_example.py`:

```python
# config.py

# Oracle Connection details
oracle_user = "your_username_here"
lib_dir = "C:/path/to/your/oracle/client/libraries"  # Only set this if necessary
oracle_dsn = "your_dsn_here"
```

### Connecting to the Database

With your `config.py` file set up, you can use the `LightOracleConnection` class to connect to your Oracle database. Below is a step-by-step example of importing your configuration and creating a database connection:

```python

# main.py
from lightoracle import LightOracleConnection
from config import oracle_user, lib_dir, oracle_dsn

# Create a connection instance with the configured parameters
oracle_conn = LightOracleConnection(oracle_user, oracle_dsn, lib_dir)

# Connect to the Oracle database
oracle_conn.connect()

# Now you can use `oracle_conn` to perform database operations
```

### Important Notes

- Always ensure that the `oracle_user`, `lib_dir`, and `oracle_dsn` attributes in `config.py` are updated with the correct information corresponding to your Oracle database setup.
- Never commit sensitive information, such as your actual Oracle username or DSN, to a public repository. It's recommended to use environment variables or a secure credential management system for handling sensitive data.
- If you encounter any issues with connecting to the Oracle database, verify that the Oracle Instant Client is correctly installed and configured on your system. You can find more information and a detailed installation guide on the [Oracle Instant Client website](https://www.oracle.com/database/technologies/instant-client.html).

## Examples

See the `example.py` file for a simple example of how to use the `LightOracleConnection` class to connect to an Oracle database and execute a query. This will fetch the first 20 rows of student data from the `edwprd.sdstumain` table and save the results to a CSV file.

```python
# example.py

from lightoracle import LightOracleConnection
from config import oracle_user, lib_dir, oracle_dsn

query = """
SELECT
    s.term,
    s.college, 
    s.department,
    s.degree,
    s.major,
    s.gpa
FROM edwprd.sdstumain s
WHERE s.term = '202401'
AND s.major = 'PHY'
FETCH FIRST 20 ROWS ONLY
"""

oracle_conn = LightOracleConnection(oracle_user, oracle_dsn, lib_dir)
print("Connecting to Oracle database...")
df = oracle_conn.execute_query(query)
print("Query executed successfully.")
print("Saving query results to CSV file...")
df.to_csv('example.csv', index=False)
print("Results saved to example.csv.")
```

For more information, refer to the examples provided in `lightoracle/oracle_connect.py` for details on how to use this package.
