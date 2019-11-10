--
-- PostgreSQL database cluster dump
--

-- Started on 2019-11-04 22:38:30 UTC

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'md553f48b7c4b76a86ce72276c5755f217d';
CREATE ROLE projadmin;
ALTER ROLE projadmin WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'md5c1fc744f2f1845cf91433778035e9346';
CREATE ROLE projuser;
ALTER ROLE projuser WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'md54d769f546793f188f6f501c20f7097ab';






-- Completed on 2019-11-04 22:38:31 UTC

--
-- PostgreSQL database cluster dump complete
--

