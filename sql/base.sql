CREATE DATABASE sistemadistribuido;

\c sistemadistribuido;
--
-- PostgreSQL database cluster dump
--

-- Started on 2019-11-04 22:38:30 UTC

--SET default_transaction_read_only = off;

--SET client_encoding = 'UTF8';
--SET standard_conforming_strings = on;

--
-- Roles
--

--CREATE ROLE postgres;
--ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'md553f48b7c4b76a86ce72276c5755f217d';
CREATE ROLE projadmin;
ALTER ROLE projadmin WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'md5c1fc744f2f1845cf91433778035e9346';
CREATE ROLE projuser;
ALTER ROLE projuser WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'md54d769f546793f188f6f501c20f7097ab';






-- Completed on 2019-11-04 22:38:31 UTC

--
-- PostgreSQL database cluster dump complete
--


--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Debian 11.5-1.pgdg90+1)
-- Dumped by pg_dump version 11.5 (Debian 11.5-1.pgdg90+1)

--SET statement_timeout = 0;
--SET lock_timeout = 0;
--SET idle_in_transaction_session_timeout = 0;
--SET client_encoding = 'UTF8';
--SET standard_conforming_strings = on;
--SELECT pg_catalog.set_config('search_path', '', false);
--SET check_function_bodies = false;
--SET xmloption = content;
--SET client_min_messages = warning;
--SET row_security = off;

--
-- Name: admisionucv; Type: SCHEMA; Schema: -; Owner: projadmin
--

CREATE SCHEMA admisionucv;


ALTER SCHEMA admisionucv OWNER TO projadmin;

--
-- Name: id_aspirante; Type: SEQUENCE; Schema: admisionucv; Owner: postgres
--

CREATE SEQUENCE admisionucv.id_aspirante
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 99999999
    CACHE 1;


ALTER TABLE admisionucv.id_aspirante OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: aspirante; Type: TABLE; Schema: admisionucv; Owner: projadmin
--

CREATE TABLE admisionucv.aspirante (
    id_aspirante integer DEFAULT nextval('admisionucv.id_aspirante'::regclass) NOT NULL,
    nombre1 character varying(100) NOT NULL,
    nombre2 character varying(100) DEFAULT NULL::character varying,
    apellido1 character varying(100) NOT NULL,
    apellido2 character varying(100) DEFAULT NULL::character varying,
    codido_documento character varying(1) NOT NULL,
    documento character varying(20) NOT NULL,
    fecha_nacimiento date NOT NULL,
    pais_nacimiento character varying(100) NOT NULL,
    sexo character varying(1) NOT NULL,
    fecha_bachiller date NOT NULL,
    calificacion numeric(4,2) DEFAULT NULL::numeric
);


ALTER TABLE admisionucv.aspirante OWNER TO projadmin;

--
-- Name: seq_pregunta; Type: SEQUENCE; Schema: admisionucv; Owner: projadmin
--

CREATE SEQUENCE admisionucv.seq_pregunta
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 99999999
    CACHE 1;


ALTER TABLE admisionucv.seq_pregunta OWNER TO projadmin;

--
-- Name: pregunta; Type: TABLE; Schema: admisionucv; Owner: projadmin
--

CREATE TABLE admisionucv.pregunta (
    id_pregunta integer DEFAULT nextval('admisionucv.seq_pregunta'::regclass) NOT NULL,
    pregunta character varying(100) NOT NULL
);


ALTER TABLE admisionucv.pregunta OWNER TO projadmin;

--
-- Name: seq_repuesta; Type: SEQUENCE; Schema: admisionucv; Owner: projadmin
--

CREATE SEQUENCE admisionucv.seq_repuesta
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 99999999
    CACHE 1;


ALTER TABLE admisionucv.seq_repuesta OWNER TO projadmin;

--
-- Name: respuesta; Type: TABLE; Schema: admisionucv; Owner: projadmin
--

CREATE TABLE admisionucv.respuesta (
    id_respuesta integer DEFAULT nextval('admisionucv.seq_repuesta'::regclass) NOT NULL,
    respuesta character varying(100) NOT NULL,
    id_pregunta integer,
    respuesta_correcta character varying(1)
);


ALTER TABLE admisionucv.respuesta OWNER TO projadmin;

--
-- Name: sexo; Type: TABLE; Schema: admisionucv; Owner: projadmin
--

CREATE TABLE admisionucv.sexo (
    codigo character varying(1) NOT NULL,
    descripcion character varying(50) NOT NULL
);


ALTER TABLE admisionucv.sexo OWNER TO projadmin;

--
-- Data for Name: aspirante; Type: TABLE DATA; Schema: admisionucv; Owner: projadmin
--

COPY admisionucv.aspirante (id_aspirante, nombre1, nombre2, apellido1, apellido2, codido_documento, documento, fecha_nacimiento, pais_nacimiento, sexo, fecha_bachiller, calificacion) FROM stdin;
99	khloe	Agustina+	Rodriguez+	San+martin	P	12765432	2019-11-09	venezuela	F	2019-11-09	\N
100	nombre1	nombre2	rodriguez1	rodriguez2	V	12121212121	2019-11-16	venezuela	M	2019-11-15	\N
101	HOLA	HOLA	HOLA	HOLA	E	HOLA	2019-11-08	HOLA	F	2019-11-08	\N
102	BACHI	BACHI	BACHI	BACHI	V	13847136	2019-11-17	BACHI	F	2019-11-14	\N
103	nombre	nombre	nombre	nombre	P	nombre	2019-11-24	nombre	F	2019-11-07	\N
104	primer	primer	primer	primer	V	primer	2019-11-24	primer	F	2019-11-09	\N
105	1	1	1	1	E	1	2019-11-10	1	F	2019-11-06	\N
106	h	h	h	h	V	h	2019-11-02	h	M	2019-11-05	\N
107	container	container	container	container	E	container	2019-11-16	container	F	2019-11-14	\N
108	gggg	gggg	gggg	gggg	P	gggg	2019-11-17	gggg	F	2019-11-06	0.00
109	Erikson	Agustin	Rodriguez	Morillo	V	13847136	2019-11-02	venezuela	F	2019-11-08	\N
110	4	4	4	4	E	4	2019-11-02	4	M	2019-11-12	\N
111	hola	hola	hola	hola	E	hola	2019-11-10	hola	F	2019-10-31	0.00
112	danixxx	danixxx	holadanixxx	holadanixxx	E	holadanixxx	2019-11-10	holadanixxx	F	2019-10-31	0.00
113	ssss	ssss	ssss	ssss	P	sss	2019-11-06	ssss	F	2019-11-13	0.00
114	ttttt	ttttt	ttttt	ttttt	V	ttttt	2019-11-09	ttttt	F	2019-11-01	0.00
115	aaaaaaaaaa	aaaaaaaaa	aaaaaaaaaaaa	aaaaaaaaaaaa	E	aaaaaaa	2019-11-09	aaaaaaaaaaa	F	2019-11-01	\N
116	andres	andres	andres	andres	E	andres	2019-11-02	andres	F	2019-11-07	\N
117	wwww	anwwwwdres	wwww	www	E	andres	2019-11-02	www	F	2019-11-07	\N
118	sssss	sssss	sssss	sssss	P	sssss	2019-11-10	www	M	2019-11-07	\N
119	sssss	sssss	sssss	sssss	P	sssss	2019-11-10	www	M	2019-11-07	\N
120	bbbbbb	bbbbb	bbbbb	bbbbbb	E	bbbbbb	2019-11-02	bbbbb	F	2019-11-07	\N
121	ffffffff	ff	f	f	V	f	2019-11-10	f	F	2019-11-05	4.00
122	erete	ertetr	ertetr	erterte	V	ertete	2019-11-06	ertetr	F	2019-11-07	\N
123	Erikson	werwrw	werwerw	werwre	E	werwer	2019-11-16	werwer	M	2019-11-19	\N
124	Erikson	werwrw	werwerw	werwre	E	werwer	2019-11-16	werwer	M	2019-11-19	\N
125	Erikson	werwrw	werwerw	werwre	E	werwer	2019-11-16	werwer	M	2019-11-19	\N
126	Erikson	werwrw	werwerw	werwre	E	werwer	2019-11-16	werwer	M	2019-11-19	\N
127	Erikson	werwrw	werwerw	werwre	E	werwer	2019-11-16	werwer	M	2019-11-19	\N
128	Erikson	werwrw	werwerw	werwre	E	werwer	2019-11-16	werwer	M	2019-11-19	\N
\.


--
-- Data for Name: pregunta; Type: TABLE DATA; Schema: admisionucv; Owner: projadmin
--

COPY admisionucv.pregunta (id_pregunta, pregunta) FROM stdin;
1	Cual es la capital de Venezuela?
2	Cual es el resultado de la suma de 2 + 2?
3	A que facultad pertenece la escuela de computación en la UCV?
4	Quien fue el creador del sistema operativo Linux?
5	Cual es el nombre de la empresa que su logo es una manzana?
6	Como es llamado tambien al sistema diádico?
7	Cual es el nombre del profesor del curso Sistemas Distribuidos?
8	Cual es el objetivo de esta prueba?
9	Que es un socket?
10	Cuales son la siglas en ingles de lenguaje de modelado universal?
\.


--
-- Data for Name: respuesta; Type: TABLE DATA; Schema: admisionucv; Owner: projadmin
--

COPY admisionucv.respuesta (id_respuesta, respuesta, id_pregunta, respuesta_correcta) FROM stdin;
1	Distrito Capital	1	X
2	Bogota	1	\N
3	Valencia	1	\N
4	Miami	1	\N
5	4	2	X
6	22	2	\N
7	2	2	\N
8	0	2	\N
9	Ciencias	3	X
10	Ingenieria	3	\N
11	Farmacia	3	\N
12	Medicina	3	\N
13	Linus Torvalds	4	X
14	Andres Sanoja	4	\N
15	Steve Jobs	4	\N
16	Erikson Rodriguez	4	\N
17	Apple	5	X
18	Kraft	5	\N
19	Marlboro	5	\N
20	Asics	5	\N
21	Binario	6	X
22	Electoral	6	\N
23	Matematico	6	\N
24	Nervioso	6	\N
29	Andres	7	X
30	Ruben	7	\N
31	Omar	7	\N
32	Jesus	7	\N
25	Ser admitido como estudiante.	8	X
26	Aprender a jugar futbol	8	\N
27	Hacer deporte	8	\N
28	Estudiar leyes	8	\N
33	Son componentes de sistemas compuestos por una aplicacion cliente y otra cumple el rol de servidor	9	X
34	Es un medio de transporte	9	\N
35	Un producto farmaceutico	9	\N
36	Una religión de america	9	\N
37	UML	10	X
38	UNI	10	\N
39	MUL	10	\N
40	LMU	10	\N
\.


--
-- Data for Name: sexo; Type: TABLE DATA; Schema: admisionucv; Owner: projadmin
--

COPY admisionucv.sexo (codigo, descripcion) FROM stdin;
F	FEMENINO
M	MASCULINO
\.


--
-- Name: id_aspirante; Type: SEQUENCE SET; Schema: admisionucv; Owner: postgres
--

SELECT pg_catalog.setval('admisionucv.id_aspirante', 128, true);


--
-- Name: seq_pregunta; Type: SEQUENCE SET; Schema: admisionucv; Owner: projadmin
--

SELECT pg_catalog.setval('admisionucv.seq_pregunta', 10, true);


--
-- Name: seq_repuesta; Type: SEQUENCE SET; Schema: admisionucv; Owner: projadmin
--

SELECT pg_catalog.setval('admisionucv.seq_repuesta', 40, true);


--
-- Name: sexo codigo_sexo_pk; Type: CONSTRAINT; Schema: admisionucv; Owner: projadmin
--

ALTER TABLE ONLY admisionucv.sexo
    ADD CONSTRAINT codigo_sexo_pk PRIMARY KEY (codigo);


--
-- Name: aspirante id_aspirante_pk; Type: CONSTRAINT; Schema: admisionucv; Owner: projadmin
--

ALTER TABLE ONLY admisionucv.aspirante
    ADD CONSTRAINT id_aspirante_pk PRIMARY KEY (id_aspirante);


--
-- Name: pregunta pk_pregunta; Type: CONSTRAINT; Schema: admisionucv; Owner: projadmin
--

ALTER TABLE ONLY admisionucv.pregunta
    ADD CONSTRAINT pk_pregunta PRIMARY KEY (id_pregunta);


--
-- Name: respuesta pk_respuesta; Type: CONSTRAINT; Schema: admisionucv; Owner: projadmin
--

ALTER TABLE ONLY admisionucv.respuesta
    ADD CONSTRAINT pk_respuesta PRIMARY KEY (id_respuesta);


--
-- Name: index_aspirante_01; Type: INDEX; Schema: admisionucv; Owner: projadmin
--

CREATE UNIQUE INDEX index_aspirante_01 ON admisionucv.aspirante USING btree (codido_documento, documento, calificacion);


--
-- Name: respuesta fk_respuesta_pregunta; Type: FK CONSTRAINT; Schema: admisionucv; Owner: projadmin
--

ALTER TABLE ONLY admisionucv.respuesta
    ADD CONSTRAINT fk_respuesta_pregunta FOREIGN KEY (id_pregunta) REFERENCES admisionucv.pregunta(id_pregunta);


--
-- Name: SCHEMA admisionucv; Type: ACL; Schema: -; Owner: projadmin
--

GRANT USAGE ON SCHEMA admisionucv TO projuser;


--
-- Name: SEQUENCE id_aspirante; Type: ACL; Schema: admisionucv; Owner: postgres
--

GRANT SELECT,USAGE ON SEQUENCE admisionucv.id_aspirante TO projadmin;
GRANT SELECT,USAGE ON SEQUENCE admisionucv.id_aspirante TO projuser;


--
-- Name: TABLE aspirante; Type: ACL; Schema: admisionucv; Owner: projadmin
--

GRANT SELECT,INSERT,UPDATE ON TABLE admisionucv.aspirante TO projuser;


--
-- Name: TABLE pregunta; Type: ACL; Schema: admisionucv; Owner: projadmin
--

GRANT SELECT ON TABLE admisionucv.pregunta TO projuser;


--
-- Name: TABLE respuesta; Type: ACL; Schema: admisionucv; Owner: projadmin
--

GRANT SELECT ON TABLE admisionucv.respuesta TO projuser;


--
-- Name: TABLE sexo; Type: ACL; Schema: admisionucv; Owner: projadmin
--

GRANT SELECT ON TABLE admisionucv.sexo TO projuser;


--
-- PostgreSQL database dump complete
--


