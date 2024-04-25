
# LightOracleConnection

## Description
A lightweight Oracle database connection handler for managing secure database interactions.

## Installation

### Using Conda

To install and use the LightOracleConnection package in a Conda environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/GSU-Analytics/light_conn.git
   cd light_conn
   ```

2. Create a Conda environment:
   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment:
   ```bash
   conda activate light_conn
   ```

4. Install the package:
   ```bash
   pip install .
   ```

## Usage

To establish a connection to an Oracle database using the `LightOracleConnection` class, configure your connection parameters in the `config_dummy.py` file. Here's a guide on how to do that and then utilize the configuration to connect to your Oracle database.

### Configuring Connection Parameters

The `config_example.py` file contains essential attributes for setting up your Oracle database connection. Before you begin using the `LightOracleConnection`, make sure you have correctly configured the following attributes:

- `oracle_user`: Your Oracle database username.
- `lib_dir`: The directory path to the Oracle Client libraries on your machine. This is necessary if your Oracle Client libraries are not included in your system's PATH environment variable.
- `oracle_dsn`: The Data Source Name for the Oracle database connection, which typically includes the hostname, port, and database name.

Here's an example of how to set up `config_dummy.py`:

```python
# config.py

# Oracle Connection details
oracle_user = "your_username_here"
lib_dir = "C:/path/to/your/oracle/client/libraries"  # Only set this if necessary
oracle_dsn = "your_dsn_here"
```

After configuring the `config_example.py` file, rename the file to `config.py` and you can use these parameters to establish a connection to your Oracle database.

### Connecting to the Database

With your `config.py` file set up, you can use the `LightOracleConnection` class to connect to your Oracle database. Below is a step-by-step example of importing your configuration and creating a database connection:

```python
# Usage example in your Python script

from light_conn.oracle_connect import LightOracleConnection
from light_conn.config import oracle_user, lib_dir, oracle_dsn

# Create a connection instance with the configured parameters
oracle_conn = LightOracleConnection(oracle_user, oracle_dsn, lib_dir)

# Connect to the Oracle database
oracle_conn.connect()

# Now you can use `oracle_conn` to perform database operations
```

Please replace `"your_username_here"` and `"your_dsn_here"` with your actual Oracle username and DSN. If you are not setting a `lib_dir` because the Oracle Client libraries are already in your PATH, you can leave it as an empty string.

### Important Notes

- Always ensure that the `oracle_user`, `lib_dir`, and `oracle_dsn` attributes in `config.py` are updated with the correct information corresponding to your Oracle database setup.
- Never commit sensitive information, such as your actual Oracle username or DSN, to a public repository. It's recommended to use environment variables or a secure credential management system for handling sensitive data.
- If you encounter any issues with connecting to the Oracle database, verify that the Oracle Instant Client is correctly installed and configured on your system. You can find more information and a detailed installation guide on the [Oracle Instant Client website](https://www.oracle.com/database/technologies/instant-client.html).

For more information, refer to the examples provided in `light_conn/oracle_connect.py` for details on how to use this package.

## 4. Handling Windows-Specific Dependencies

If there are any Windows-specific dependencies or configurations, make sure to include those in the `environment.yml` or as part of the installation instructions. If `oracledb` requires specific client libraries or binaries that are not handled by Conda, provide detailed instructions on how to install and configure these components on Windows.
