SELECT rolname FROM pg_roles;

CREATE ROLE rohan WITH LOGIN PASSWORD '2272';

GRANT CONNECT ON DATABASE primarydb TO rohan;

-- Restart System
-- sudo systemctl reload postgresql
-- sudo service postgresql reload
--  or
-- sudo brew services restart postgresql
--  List fo roles 
-- \du
ALTER ROLE rohan WITH LOGIN;
