# Password Manager

---

### Requirements 
- Python 3.9.6
- cryptography==42.0.5
- deepface==0.0.90
- opencv_python==4.9.0.80
- psycopg2_binary==2.9.9
- python_bcrypt==0.3.2
- secret==0.8
- postgresql@14

---

### Postgres Commands 
1. Start server (from the root repo)
```commandline
pg_ctl -D database -l logfile.log start
```
2. Login to Postgres Database
```commandline
psql storage -U python_app
```
3. List tables in database
```commandline
\dt
```
4. List users
```commandline
\du
```
5. Check table information
```commandline 
\d users
```
6. Basic
```commandline
ALTER TABLE users
ALTER COLUMN password_hash TYPE character(128);

SELECT rolname FROM pg_roles;
CREATE ROLE rohan WITH LOGIN PASSWORD '2272';

GRANT CONNECT ON DATABASE primarydb TO rohan;

-- Restart System
-- sudo systemctl reload postgresql
-- sudo service postgresql reload
--  or
-- sudo brew services restart postgresql

```
7. Delete a row from table
```commandline
DELETE FROM users
WHERE username='test';
```
8. Add column to table
```commandline
ALTER TABLE your_table_name
ADD COLUMN key_byte BYTEA; 
```
9. Exit server
```commandline
exit;
```
10. Delete table
```commandline
DROP TABLE table_name;
```
