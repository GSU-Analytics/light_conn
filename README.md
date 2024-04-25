
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

Refer to the examples provided in `light_oracle_connection/oracle_connect.py` for details on how to use this package.

### 4. Handling Windows-Specific Dependencies

If there are any Windows-specific dependencies or configurations, make sure to include those in the `environment.yml` or as part of the installation instructions. If `oracledb` requires specific client libraries or binaries that are not handled by Conda, provide detailed instructions on how to install and configure these components on Windows.
