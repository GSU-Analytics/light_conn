from light_conn.oracle_connect import LightOracleConnection
from light_conn.config import oracle_user, lib_dir, oracle_dsn

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

df = oracle_conn.execute_query(query)

df.to_csv('example.csv', index=False)

