# Password Manager

---

### Requirements 
- Python 3.9.6
- postgresql@14 (Database)

Install required modules via
```bash
pip3 install -r requirements.txt
```

---

### Run
```bash
python main.py -h
```

---
### Postgres Commands 
1. Start server (from the root repo)
```bash
pg_ctl -D database -l logfile.log start
```
2. Login to Postgres Database
```bash
psql storage -U python_app
```
3. List tables in database
```bash
\dt
```
4. List users
```bash
\du
```
5. Check table information
```bash 
\d users
```
6. Basic
```bash
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
```bash
DELETE FROM users
WHERE username='test';
```
8. Add column to table
```bash
ALTER TABLE your_table_name
ADD COLUMN key_byte BYTEA; 
```
9. Exit server
```bash
exit;
```
10. Delete table
```bash
DROP TABLE table_name;
```
