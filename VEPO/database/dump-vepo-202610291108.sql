--
-- PostgreSQL database dump
--

\restrict kK55nWewIsZkL1GcL83ZzbJSVdcMHlxpNjAcG1TkOiLtNC2agpIc6MijDvO48JJ

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

-- Started on 2026-10-29 11:08:01

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 6 (class 2615 OID 16531)
-- Name: agua_inmaculada; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA agua_inmaculada;


ALTER SCHEMA agua_inmaculada OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 234 (class 1259 OID 16744)
-- Name: closings_cash; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.closings_cash (
    id_closing_cash integer NOT NULL,
    id_employee integer NOT NULL,
    date date NOT NULL,
    date_start date NOT NULL,
    date_finish date NOT NULL,
    amount numeric NOT NULL
);


ALTER TABLE agua_inmaculada.closings_cash OWNER TO postgres;

--
-- TOC entry 5123 (class 0 OID 0)
-- Dependencies: 234
-- Name: TABLE closings_cash; Type: COMMENT; Schema: agua_inmaculada; Owner: postgres
--

COMMENT ON TABLE agua_inmaculada.closings_cash IS 'regiatros de corte de caja';


--
-- TOC entry 220 (class 1259 OID 16532)
-- Name: employee; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.employee (
    id_employee integer NOT NULL,
    id_status integer NOT NULL,
    name character varying NOT NULL,
    name2 character varying,
    lastname character varying NOT NULL,
    lastname2 character varying,
    birthdate date NOT NULL
);


ALTER TABLE agua_inmaculada.employee OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16547)
-- Name: employee-sampling_log; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada."employee-sampling_log" (
    id_sampling_log integer,
    id_employee integer NOT NULL
);


ALTER TABLE agua_inmaculada."employee-sampling_log" OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16551)
-- Name: employee_address; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.employee_address (
    id_employee integer NOT NULL,
    street character varying NOT NULL,
    zip character varying NOT NULL,
    int_number character varying,
    ext_number character varying
);


ALTER TABLE agua_inmaculada.employee_address OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16559)
-- Name: employee_contact; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.employee_contact (
    id_employee integer,
    cellphone integer,
    telephone integer,
    email character varying
);


ALTER TABLE agua_inmaculada.employee_contact OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16542)
-- Name: employee_rol; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.employee_rol (
    id_employee integer CONSTRAINT "employee-rol_id_employee_not_null" NOT NULL,
    id_rol integer CONSTRAINT "employee-rol_id_rol_not_null" NOT NULL
);


ALTER TABLE agua_inmaculada.employee_rol OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 16727)
-- Name: expenditures; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.expenditures (
    id_expenditures integer NOT NULL,
    id_employee integer NOT NULL,
    date date NOT NULL,
    amount numeric NOT NULL,
    reason text NOT NULL
);


ALTER TABLE agua_inmaculada.expenditures OWNER TO postgres;

--
-- TOC entry 5124 (class 0 OID 0)
-- Dependencies: 233
-- Name: TABLE expenditures; Type: COMMENT; Schema: agua_inmaculada; Owner: postgres
--

COMMENT ON TABLE agua_inmaculada.expenditures IS 'registro de egresos';


--
-- TOC entry 225 (class 1259 OID 16564)
-- Name: log; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.log (
    id_login integer NOT NULL,
    username character varying NOT NULL,
    id_status integer NOT NULL,
    id_rol integer NOT NULL,
    date_modification date NOT NULL,
    id_log integer NOT NULL
);


ALTER TABLE agua_inmaculada.log OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 24628)
-- Name: log_id_log_seq; Type: SEQUENCE; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE agua_inmaculada.log ALTER COLUMN id_log ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME agua_inmaculada.log_id_log_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 226 (class 1259 OID 16574)
-- Name: logeo; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.logeo (
    id_login integer NOT NULL,
    id_status integer NOT NULL,
    id_employee integer,
    username character varying NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE agua_inmaculada.logeo OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16583)
-- Name: parameter_measurement; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.parameter_measurement (
    id_measurement integer NOT NULL,
    id_sampling_log integer NOT NULL,
    chlorine real NOT NULL,
    ph real NOT NULL,
    hardness real NOT NULL,
    sst real NOT NULL,
    temperature real NOT NULL
);


ALTER TABLE agua_inmaculada.parameter_measurement OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16593)
-- Name: rol; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.rol (
    id_rol integer NOT NULL,
    employee boolean NOT NULL,
    admin boolean NOT NULL
);


ALTER TABLE agua_inmaculada.rol OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 16599)
-- Name: sampling_log; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.sampling_log (
    id_sampling_log integer NOT NULL,
    id_employee integer NOT NULL
);


ALTER TABLE agua_inmaculada.sampling_log OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 16604)
-- Name: sampling_point; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.sampling_point (
    id_sampling_point integer NOT NULL,
    id_measurement integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE agua_inmaculada.sampling_point OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 16710)
-- Name: sells; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.sells (
    id_sell integer NOT NULL,
    id_employee integer NOT NULL,
    date date NOT NULL,
    type character varying NOT NULL,
    amount numeric NOT NULL
);


ALTER TABLE agua_inmaculada.sells OWNER TO postgres;

--
-- TOC entry 5125 (class 0 OID 0)
-- Dependencies: 232
-- Name: TABLE sells; Type: COMMENT; Schema: agua_inmaculada; Owner: postgres
--

COMMENT ON TABLE agua_inmaculada.sells IS 'registro de ingresos/ventas';


--
-- TOC entry 231 (class 1259 OID 16612)
-- Name: status; Type: TABLE; Schema: agua_inmaculada; Owner: postgres
--

CREATE TABLE agua_inmaculada.status (
    id_status integer NOT NULL,
    active boolean NOT NULL,
    inactive boolean NOT NULL
);


ALTER TABLE agua_inmaculada.status OWNER TO postgres;

--
-- TOC entry 5116 (class 0 OID 16744)
-- Dependencies: 234
-- Data for Name: closings_cash; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.closings_cash (id_closing_cash, id_employee, date, date_start, date_finish, amount) FROM stdin;
\.


--
-- TOC entry 5102 (class 0 OID 16532)
-- Dependencies: 220
-- Data for Name: employee; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.employee (id_employee, id_status, name, name2, lastname, lastname2, birthdate) FROM stdin;
0	0	Sebastián	Gilberto	Rios	Rivera	2007-11-27
\.


--
-- TOC entry 5104 (class 0 OID 16547)
-- Dependencies: 222
-- Data for Name: employee-sampling_log; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada."employee-sampling_log" (id_sampling_log, id_employee) FROM stdin;
\.


--
-- TOC entry 5105 (class 0 OID 16551)
-- Dependencies: 223
-- Data for Name: employee_address; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.employee_address (id_employee, street, zip, int_number, ext_number) FROM stdin;
\.


--
-- TOC entry 5106 (class 0 OID 16559)
-- Dependencies: 224
-- Data for Name: employee_contact; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.employee_contact (id_employee, cellphone, telephone, email) FROM stdin;
\.


--
-- TOC entry 5103 (class 0 OID 16542)
-- Dependencies: 221
-- Data for Name: employee_rol; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.employee_rol (id_employee, id_rol) FROM stdin;
0	0
\.


--
-- TOC entry 5115 (class 0 OID 16727)
-- Dependencies: 233
-- Data for Name: expenditures; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.expenditures (id_expenditures, id_employee, date, amount, reason) FROM stdin;
\.


--
-- TOC entry 5107 (class 0 OID 16564)
-- Dependencies: 225
-- Data for Name: log; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.log (id_login, username, id_status, id_rol, date_modification, id_log) FROM stdin;
0	sebastian	0	0	2026-10-16	1
0	admin	0	0	2026-10-27	3
0	admin	0	0	2026-10-27	5
0	admin	0	0	2026-10-27	6
\.


--
-- TOC entry 5108 (class 0 OID 16574)
-- Dependencies: 226
-- Data for Name: logeo; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.logeo (id_login, id_status, id_employee, username, password) FROM stdin;
0	0	0	admin	admin123
\.


--
-- TOC entry 5109 (class 0 OID 16583)
-- Dependencies: 227
-- Data for Name: parameter_measurement; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.parameter_measurement (id_measurement, id_sampling_log, chlorine, ph, hardness, sst, temperature) FROM stdin;
\.


--
-- TOC entry 5110 (class 0 OID 16593)
-- Dependencies: 228
-- Data for Name: rol; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.rol (id_rol, employee, admin) FROM stdin;
0	f	t
\.


--
-- TOC entry 5111 (class 0 OID 16599)
-- Dependencies: 229
-- Data for Name: sampling_log; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.sampling_log (id_sampling_log, id_employee) FROM stdin;
\.


--
-- TOC entry 5112 (class 0 OID 16604)
-- Dependencies: 230
-- Data for Name: sampling_point; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.sampling_point (id_sampling_point, id_measurement, name) FROM stdin;
\.


--
-- TOC entry 5114 (class 0 OID 16710)
-- Dependencies: 232
-- Data for Name: sells; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.sells (id_sell, id_employee, date, type, amount) FROM stdin;
\.


--
-- TOC entry 5113 (class 0 OID 16612)
-- Dependencies: 231
-- Data for Name: status; Type: TABLE DATA; Schema: agua_inmaculada; Owner: postgres
--

COPY agua_inmaculada.status (id_status, active, inactive) FROM stdin;
0	t	f
\.


--
-- TOC entry 5126 (class 0 OID 0)
-- Dependencies: 235
-- Name: log_id_log_seq; Type: SEQUENCE SET; Schema: agua_inmaculada; Owner: postgres
--

SELECT pg_catalog.setval('agua_inmaculada.log_id_log_seq', 6, true);


--
-- TOC entry 4938 (class 2606 OID 16756)
-- Name: closings_cash closings_cash_pk; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.closings_cash
    ADD CONSTRAINT closings_cash_pk PRIMARY KEY (id_closing_cash);


--
-- TOC entry 4918 (class 2606 OID 16619)
-- Name: employee_contact employee_contact_unique; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.employee_contact
    ADD CONSTRAINT employee_contact_unique UNIQUE (email);


--
-- TOC entry 4914 (class 2606 OID 16621)
-- Name: employee employee_pk; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.employee
    ADD CONSTRAINT employee_pk PRIMARY KEY (id_employee);


--
-- TOC entry 4916 (class 2606 OID 16623)
-- Name: employee-sampling_log employee_sampling_log_pk; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada."employee-sampling_log"
    ADD CONSTRAINT employee_sampling_log_pk PRIMARY KEY (id_employee);


--
-- TOC entry 4936 (class 2606 OID 16738)
-- Name: expenditures expenditures_pk; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.expenditures
    ADD CONSTRAINT expenditures_pk PRIMARY KEY (id_expenditures);


--
-- TOC entry 4920 (class 2606 OID 24631)
-- Name: log log_pkey; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.log
    ADD CONSTRAINT log_pkey PRIMARY KEY (id_log);


--
-- TOC entry 4922 (class 2606 OID 16629)
-- Name: logeo logeo_unique; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.logeo
    ADD CONSTRAINT logeo_unique UNIQUE (username);


--
-- TOC entry 4924 (class 2606 OID 16631)
-- Name: parameter_measurement parameter_measurement_pk; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.parameter_measurement
    ADD CONSTRAINT parameter_measurement_pk PRIMARY KEY (id_measurement);


--
-- TOC entry 4926 (class 2606 OID 16633)
-- Name: rol rol_pk; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.rol
    ADD CONSTRAINT rol_pk PRIMARY KEY (id_rol);


--
-- TOC entry 4928 (class 2606 OID 16635)
-- Name: sampling_log sampling_log_pk; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.sampling_log
    ADD CONSTRAINT sampling_log_pk PRIMARY KEY (id_sampling_log);


--
-- TOC entry 4930 (class 2606 OID 16637)
-- Name: sampling_point sampling_point_pk; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.sampling_point
    ADD CONSTRAINT sampling_point_pk PRIMARY KEY (id_sampling_point);


--
-- TOC entry 4934 (class 2606 OID 16721)
-- Name: sells sells_pk; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.sells
    ADD CONSTRAINT sells_pk PRIMARY KEY (id_sell);


--
-- TOC entry 4932 (class 2606 OID 16639)
-- Name: status status_pk; Type: CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.status
    ADD CONSTRAINT status_pk PRIMARY KEY (id_status);


--
-- TOC entry 4954 (class 2606 OID 16757)
-- Name: closings_cash closings_cash_employee_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.closings_cash
    ADD CONSTRAINT closings_cash_employee_fk FOREIGN KEY (id_employee) REFERENCES agua_inmaculada.employee(id_employee);


--
-- TOC entry 4943 (class 2606 OID 16640)
-- Name: employee_address employee_address_employee_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.employee_address
    ADD CONSTRAINT employee_address_employee_fk FOREIGN KEY (id_employee) REFERENCES agua_inmaculada.employee(id_employee);


--
-- TOC entry 4944 (class 2606 OID 16645)
-- Name: employee_contact employee_contact_employee_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.employee_contact
    ADD CONSTRAINT employee_contact_employee_fk FOREIGN KEY (id_employee) REFERENCES agua_inmaculada.employee(id_employee);


--
-- TOC entry 4940 (class 2606 OID 16650)
-- Name: employee_rol employee_rol_employee_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.employee_rol
    ADD CONSTRAINT employee_rol_employee_fk FOREIGN KEY (id_employee) REFERENCES agua_inmaculada.employee(id_employee);


--
-- TOC entry 4941 (class 2606 OID 16655)
-- Name: employee_rol employee_rol_rol_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.employee_rol
    ADD CONSTRAINT employee_rol_rol_fk FOREIGN KEY (id_rol) REFERENCES agua_inmaculada.rol(id_rol);


--
-- TOC entry 4942 (class 2606 OID 16660)
-- Name: employee-sampling_log employee_sampling_log_sampling_log_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada."employee-sampling_log"
    ADD CONSTRAINT employee_sampling_log_sampling_log_fk FOREIGN KEY (id_sampling_log) REFERENCES agua_inmaculada.sampling_log(id_sampling_log);


--
-- TOC entry 4939 (class 2606 OID 16665)
-- Name: employee employee_status_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.employee
    ADD CONSTRAINT employee_status_fk FOREIGN KEY (id_status) REFERENCES agua_inmaculada.status(id_status);


--
-- TOC entry 4953 (class 2606 OID 16739)
-- Name: expenditures expenditures_employee_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.expenditures
    ADD CONSTRAINT expenditures_employee_fk FOREIGN KEY (id_employee) REFERENCES agua_inmaculada.employee(id_employee);


--
-- TOC entry 4945 (class 2606 OID 16670)
-- Name: log log_rol_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.log
    ADD CONSTRAINT log_rol_fk FOREIGN KEY (id_rol) REFERENCES agua_inmaculada.rol(id_rol);


--
-- TOC entry 4946 (class 2606 OID 16675)
-- Name: log log_status_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.log
    ADD CONSTRAINT log_status_fk FOREIGN KEY (id_status) REFERENCES agua_inmaculada.status(id_status);


--
-- TOC entry 4947 (class 2606 OID 16680)
-- Name: logeo logeo_employee_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.logeo
    ADD CONSTRAINT logeo_employee_fk FOREIGN KEY (id_employee) REFERENCES agua_inmaculada.employee(id_employee);


--
-- TOC entry 4948 (class 2606 OID 16690)
-- Name: logeo logeo_status_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.logeo
    ADD CONSTRAINT logeo_status_fk FOREIGN KEY (id_status) REFERENCES agua_inmaculada.status(id_status);


--
-- TOC entry 4949 (class 2606 OID 16695)
-- Name: parameter_measurement parameter_measurement_sampling_log_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.parameter_measurement
    ADD CONSTRAINT parameter_measurement_sampling_log_fk FOREIGN KEY (id_sampling_log) REFERENCES agua_inmaculada.sampling_log(id_sampling_log);


--
-- TOC entry 4950 (class 2606 OID 16700)
-- Name: sampling_log sampling_log_employee_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.sampling_log
    ADD CONSTRAINT sampling_log_employee_fk FOREIGN KEY (id_employee) REFERENCES agua_inmaculada.employee(id_employee);


--
-- TOC entry 4951 (class 2606 OID 16705)
-- Name: sampling_point sampling_point_parameter_measurement_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.sampling_point
    ADD CONSTRAINT sampling_point_parameter_measurement_fk FOREIGN KEY (id_measurement) REFERENCES agua_inmaculada.parameter_measurement(id_measurement);


--
-- TOC entry 4952 (class 2606 OID 16722)
-- Name: sells sells_employee_fk; Type: FK CONSTRAINT; Schema: agua_inmaculada; Owner: postgres
--

ALTER TABLE ONLY agua_inmaculada.sells
    ADD CONSTRAINT sells_employee_fk FOREIGN KEY (id_employee) REFERENCES agua_inmaculada.employee(id_employee);


-- Completed on 2026-10-29 11:08:05

--
-- PostgreSQL database dump complete
--

\unrestrict kK55nWewIsZkL1GcL83ZzbJSVdcMHlxpNjAcG1TkOiLtNC2agpIc6MijDvO48JJ

