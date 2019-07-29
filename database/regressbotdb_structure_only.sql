--
-- PostgreSQL database dump
--

-- Dumped from database version 11.4
-- Dumped by pg_dump version 11.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: rgbotsm; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA rgbotsm;


ALTER SCHEMA rgbotsm OWNER TO postgres;

--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: hcs_connect_info; Type: TABLE; Schema: rgbotsm; Owner: postgres
--

CREATE TABLE rgbotsm.hcs_connect_info (
    id integer NOT NULL,
    subsystem_id integer NOT NULL,
    server_id integer NOT NULL
);


ALTER TABLE rgbotsm.hcs_connect_info OWNER TO postgres;

--
-- Name: hcs_connect_info_id_seq; Type: SEQUENCE; Schema: rgbotsm; Owner: postgres
--

CREATE SEQUENCE rgbotsm.hcs_connect_info_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rgbotsm.hcs_connect_info_id_seq OWNER TO postgres;

--
-- Name: hcs_connect_info_id_seq; Type: SEQUENCE OWNED BY; Schema: rgbotsm; Owner: postgres
--

ALTER SEQUENCE rgbotsm.hcs_connect_info_id_seq OWNED BY rgbotsm.hcs_connect_info.id;


--
-- Name: hcs_members; Type: TABLE; Schema: rgbotsm; Owner: postgres
--

CREATE TABLE rgbotsm.hcs_members (
    id integer NOT NULL,
    login character varying(256) NOT NULL,
    user_name character varying(256) NOT NULL
);


ALTER TABLE rgbotsm.hcs_members OWNER TO postgres;

--
-- Name: hcs_members_id_seq; Type: SEQUENCE; Schema: rgbotsm; Owner: postgres
--

CREATE SEQUENCE rgbotsm.hcs_members_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rgbotsm.hcs_members_id_seq OWNER TO postgres;

--
-- Name: hcs_members_id_seq; Type: SEQUENCE OWNED BY; Schema: rgbotsm; Owner: postgres
--

ALTER SEQUENCE rgbotsm.hcs_members_id_seq OWNED BY rgbotsm.hcs_members.id;


--
-- Name: hcs_servers; Type: TABLE; Schema: rgbotsm; Owner: postgres
--

CREATE TABLE rgbotsm.hcs_servers (
    id integer NOT NULL,
    stand_id integer NOT NULL,
    server_name character varying(256) NOT NULL,
    host character varying(256) NOT NULL,
    port integer NOT NULL
);


ALTER TABLE rgbotsm.hcs_servers OWNER TO postgres;

--
-- Name: hcs_servers_id_seq; Type: SEQUENCE; Schema: rgbotsm; Owner: postgres
--

CREATE SEQUENCE rgbotsm.hcs_servers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rgbotsm.hcs_servers_id_seq OWNER TO postgres;

--
-- Name: hcs_servers_id_seq; Type: SEQUENCE OWNED BY; Schema: rgbotsm; Owner: postgres
--

ALTER SEQUENCE rgbotsm.hcs_servers_id_seq OWNED BY rgbotsm.hcs_servers.id;


--
-- Name: hcs_stands; Type: TABLE; Schema: rgbotsm; Owner: postgres
--

CREATE TABLE rgbotsm.hcs_stands (
    id integer NOT NULL,
    stand_name character varying(256) NOT NULL
);


ALTER TABLE rgbotsm.hcs_stands OWNER TO postgres;

--
-- Name: hcs_stands_id_seq; Type: SEQUENCE; Schema: rgbotsm; Owner: postgres
--

CREATE SEQUENCE rgbotsm.hcs_stands_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rgbotsm.hcs_stands_id_seq OWNER TO postgres;

--
-- Name: hcs_stands_id_seq; Type: SEQUENCE OWNED BY; Schema: rgbotsm; Owner: postgres
--

ALTER SEQUENCE rgbotsm.hcs_stands_id_seq OWNED BY rgbotsm.hcs_stands.id;


--
-- Name: hcs_subsystems; Type: TABLE; Schema: rgbotsm; Owner: postgres
--

CREATE TABLE rgbotsm.hcs_subsystems (
    id integer NOT NULL,
    database_name character varying(256) NOT NULL,
    subsystem_name character varying(256) NOT NULL
);


ALTER TABLE rgbotsm.hcs_subsystems OWNER TO postgres;

--
-- Name: hcs_subsystems_id_seq; Type: SEQUENCE; Schema: rgbotsm; Owner: postgres
--

CREATE SEQUENCE rgbotsm.hcs_subsystems_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rgbotsm.hcs_subsystems_id_seq OWNER TO postgres;

--
-- Name: hcs_subsystems_id_seq; Type: SEQUENCE OWNED BY; Schema: rgbotsm; Owner: postgres
--

ALTER SEQUENCE rgbotsm.hcs_subsystems_id_seq OWNED BY rgbotsm.hcs_subsystems.id;


--
-- Name: hcs_team_lineups; Type: TABLE; Schema: rgbotsm; Owner: postgres
--

CREATE TABLE rgbotsm.hcs_team_lineups (
    id integer NOT NULL,
    team_id integer NOT NULL,
    tpm_id integer NOT NULL,
    teamlead_id integer NOT NULL,
    analyst_id integer NOT NULL,
    qa_id integer NOT NULL,
    dba_id integer NOT NULL
);


ALTER TABLE rgbotsm.hcs_team_lineups OWNER TO postgres;

--
-- Name: hcs_team_lineups_id_seq; Type: SEQUENCE; Schema: rgbotsm; Owner: postgres
--

CREATE SEQUENCE rgbotsm.hcs_team_lineups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rgbotsm.hcs_team_lineups_id_seq OWNER TO postgres;

--
-- Name: hcs_team_lineups_id_seq; Type: SEQUENCE OWNED BY; Schema: rgbotsm; Owner: postgres
--

ALTER SEQUENCE rgbotsm.hcs_team_lineups_id_seq OWNED BY rgbotsm.hcs_team_lineups.id;


--
-- Name: hcs_teams; Type: TABLE; Schema: rgbotsm; Owner: postgres
--

CREATE TABLE rgbotsm.hcs_teams (
    id integer NOT NULL,
    team_number integer NOT NULL,
    subsystem_id integer NOT NULL
);


ALTER TABLE rgbotsm.hcs_teams OWNER TO postgres;

--
-- Name: hcs_teams_id_seq; Type: SEQUENCE; Schema: rgbotsm; Owner: postgres
--

CREATE SEQUENCE rgbotsm.hcs_teams_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rgbotsm.hcs_teams_id_seq OWNER TO postgres;

--
-- Name: hcs_teams_id_seq; Type: SEQUENCE OWNED BY; Schema: rgbotsm; Owner: postgres
--

ALTER SEQUENCE rgbotsm.hcs_teams_id_seq OWNED BY rgbotsm.hcs_teams.id;


--
-- Name: jira_tasks; Type: TABLE; Schema: rgbotsm; Owner: postgres
--

CREATE TABLE rgbotsm.jira_tasks (
    id integer NOT NULL,
    stand_id integer NOT NULL,
    subsystem_id integer NOT NULL,
    statement_hash character varying(256) NOT NULL,
    statement_text character varying(256) NOT NULL,
    issue_number character varying(256) NOT NULL,
    creation_date timestamp without time zone DEFAULT now()
);


ALTER TABLE rgbotsm.jira_tasks OWNER TO postgres;

--
-- Name: jira_tasks_id_seq; Type: SEQUENCE; Schema: rgbotsm; Owner: postgres
--

CREATE SEQUENCE rgbotsm.jira_tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rgbotsm.jira_tasks_id_seq OWNER TO postgres;

--
-- Name: jira_tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: rgbotsm; Owner: postgres
--

ALTER SEQUENCE rgbotsm.jira_tasks_id_seq OWNED BY rgbotsm.jira_tasks.id;


--
-- Name: user_filters; Type: TABLE; Schema: rgbotsm; Owner: postgres
--

CREATE TABLE rgbotsm.user_filters (
    id integer NOT NULL,
    user_id integer NOT NULL,
    filter_name character varying DEFAULT 'noname_filter'::character varying,
    stand_id integer[],
    subsystem_id integer[],
    table_names character varying[],
    key_words character varying[],
    duration integer
);


ALTER TABLE rgbotsm.user_filters OWNER TO postgres;

--
-- Name: user_filters_id_seq; Type: SEQUENCE; Schema: rgbotsm; Owner: postgres
--

CREATE SEQUENCE rgbotsm.user_filters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rgbotsm.user_filters_id_seq OWNER TO postgres;

--
-- Name: user_filters_id_seq; Type: SEQUENCE OWNED BY; Schema: rgbotsm; Owner: postgres
--

ALTER SEQUENCE rgbotsm.user_filters_id_seq OWNED BY rgbotsm.user_filters.id;


--
-- Name: user_login_info; Type: TABLE; Schema: rgbotsm; Owner: postgres
--

CREATE TABLE rgbotsm.user_login_info (
    id integer NOT NULL,
    login character varying(256) NOT NULL,
    pass_hash character varying(256)
);


ALTER TABLE rgbotsm.user_login_info OWNER TO postgres;

--
-- Name: user_login_info_id_seq; Type: SEQUENCE; Schema: rgbotsm; Owner: postgres
--

CREATE SEQUENCE rgbotsm.user_login_info_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rgbotsm.user_login_info_id_seq OWNER TO postgres;

--
-- Name: user_login_info_id_seq; Type: SEQUENCE OWNED BY; Schema: rgbotsm; Owner: postgres
--

ALTER SEQUENCE rgbotsm.user_login_info_id_seq OWNED BY rgbotsm.user_login_info.id;


--
-- Name: hcs_connect_info id; Type: DEFAULT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_connect_info ALTER COLUMN id SET DEFAULT nextval('rgbotsm.hcs_connect_info_id_seq'::regclass);


--
-- Name: hcs_members id; Type: DEFAULT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_members ALTER COLUMN id SET DEFAULT nextval('rgbotsm.hcs_members_id_seq'::regclass);


--
-- Name: hcs_servers id; Type: DEFAULT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_servers ALTER COLUMN id SET DEFAULT nextval('rgbotsm.hcs_servers_id_seq'::regclass);


--
-- Name: hcs_stands id; Type: DEFAULT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_stands ALTER COLUMN id SET DEFAULT nextval('rgbotsm.hcs_stands_id_seq'::regclass);


--
-- Name: hcs_subsystems id; Type: DEFAULT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_subsystems ALTER COLUMN id SET DEFAULT nextval('rgbotsm.hcs_subsystems_id_seq'::regclass);


--
-- Name: hcs_team_lineups id; Type: DEFAULT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_team_lineups ALTER COLUMN id SET DEFAULT nextval('rgbotsm.hcs_team_lineups_id_seq'::regclass);


--
-- Name: hcs_teams id; Type: DEFAULT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_teams ALTER COLUMN id SET DEFAULT nextval('rgbotsm.hcs_teams_id_seq'::regclass);


--
-- Name: jira_tasks id; Type: DEFAULT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.jira_tasks ALTER COLUMN id SET DEFAULT nextval('rgbotsm.jira_tasks_id_seq'::regclass);


--
-- Name: user_filters id; Type: DEFAULT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.user_filters ALTER COLUMN id SET DEFAULT nextval('rgbotsm.user_filters_id_seq'::regclass);


--
-- Name: user_login_info id; Type: DEFAULT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.user_login_info ALTER COLUMN id SET DEFAULT nextval('rgbotsm.user_login_info_id_seq'::regclass);


--
-- Name: hcs_connect_info_id_seq; Type: SEQUENCE SET; Schema: rgbotsm; Owner: postgres
--

SELECT pg_catalog.setval('rgbotsm.hcs_connect_info_id_seq', 20, true);


--
-- Name: hcs_members_id_seq; Type: SEQUENCE SET; Schema: rgbotsm; Owner: postgres
--

SELECT pg_catalog.setval('rgbotsm.hcs_members_id_seq', 23, true);


--
-- Name: hcs_servers_id_seq; Type: SEQUENCE SET; Schema: rgbotsm; Owner: postgres
--

SELECT pg_catalog.setval('rgbotsm.hcs_servers_id_seq', 22, true);


--
-- Name: hcs_stands_id_seq; Type: SEQUENCE SET; Schema: rgbotsm; Owner: postgres
--

SELECT pg_catalog.setval('rgbotsm.hcs_stands_id_seq', 2, true);


--
-- Name: hcs_subsystems_id_seq; Type: SEQUENCE SET; Schema: rgbotsm; Owner: postgres
--

SELECT pg_catalog.setval('rgbotsm.hcs_subsystems_id_seq', 10, true);


--
-- Name: hcs_team_lineups_id_seq; Type: SEQUENCE SET; Schema: rgbotsm; Owner: postgres
--

SELECT pg_catalog.setval('rgbotsm.hcs_team_lineups_id_seq', 21, true);


--
-- Name: hcs_teams_id_seq; Type: SEQUENCE SET; Schema: rgbotsm; Owner: postgres
--

SELECT pg_catalog.setval('rgbotsm.hcs_teams_id_seq', 12, true);


--
-- Name: jira_tasks_id_seq; Type: SEQUENCE SET; Schema: rgbotsm; Owner: postgres
--

SELECT pg_catalog.setval('rgbotsm.jira_tasks_id_seq', 1, false);


--
-- Name: user_filters_id_seq; Type: SEQUENCE SET; Schema: rgbotsm; Owner: postgres
--

SELECT pg_catalog.setval('rgbotsm.user_filters_id_seq', 1, false);


--
-- Name: user_login_info_id_seq; Type: SEQUENCE SET; Schema: rgbotsm; Owner: postgres
--

SELECT pg_catalog.setval('rgbotsm.user_login_info_id_seq', 2, true);


--
-- Name: hcs_connect_info hcs_connect_info_pkey; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_connect_info
    ADD CONSTRAINT hcs_connect_info_pkey PRIMARY KEY (id);


--
-- Name: hcs_members hcs_members_login_key; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_members
    ADD CONSTRAINT hcs_members_login_key UNIQUE (login);


--
-- Name: hcs_members hcs_members_pkey; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_members
    ADD CONSTRAINT hcs_members_pkey PRIMARY KEY (id);


--
-- Name: hcs_servers hcs_servers_host_key; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_servers
    ADD CONSTRAINT hcs_servers_host_key UNIQUE (host);


--
-- Name: hcs_servers hcs_servers_pkey; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_servers
    ADD CONSTRAINT hcs_servers_pkey PRIMARY KEY (id);


--
-- Name: hcs_servers hcs_servers_server_name_key; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_servers
    ADD CONSTRAINT hcs_servers_server_name_key UNIQUE (server_name);


--
-- Name: hcs_stands hcs_stands_pkey; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_stands
    ADD CONSTRAINT hcs_stands_pkey PRIMARY KEY (id);


--
-- Name: hcs_stands hcs_stands_stand_name_key; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_stands
    ADD CONSTRAINT hcs_stands_stand_name_key UNIQUE (stand_name);


--
-- Name: hcs_subsystems hcs_subsystems_pkey; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_subsystems
    ADD CONSTRAINT hcs_subsystems_pkey PRIMARY KEY (id);


--
-- Name: hcs_subsystems hcs_subsystems_subsystem_name_key; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_subsystems
    ADD CONSTRAINT hcs_subsystems_subsystem_name_key UNIQUE (subsystem_name);


--
-- Name: hcs_team_lineups hcs_team_lineups_pkey; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_team_lineups
    ADD CONSTRAINT hcs_team_lineups_pkey PRIMARY KEY (id);


--
-- Name: hcs_teams hcs_teams_pkey; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_teams
    ADD CONSTRAINT hcs_teams_pkey PRIMARY KEY (id);


--
-- Name: jira_tasks jira_tasks_issue_number_key; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.jira_tasks
    ADD CONSTRAINT jira_tasks_issue_number_key UNIQUE (issue_number);


--
-- Name: jira_tasks jira_tasks_pkey; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.jira_tasks
    ADD CONSTRAINT jira_tasks_pkey PRIMARY KEY (id);


--
-- Name: jira_tasks jira_tasks_statement_hash_key; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.jira_tasks
    ADD CONSTRAINT jira_tasks_statement_hash_key UNIQUE (statement_hash);


--
-- Name: user_filters user_filters_pkey; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.user_filters
    ADD CONSTRAINT user_filters_pkey PRIMARY KEY (id);


--
-- Name: user_login_info user_login_info_login_key; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.user_login_info
    ADD CONSTRAINT user_login_info_login_key UNIQUE (login);


--
-- Name: user_login_info user_login_info_pkey; Type: CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.user_login_info
    ADD CONSTRAINT user_login_info_pkey PRIMARY KEY (id);


--
-- Name: hcs_connect_info hcs_connect_info_server_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_connect_info
    ADD CONSTRAINT hcs_connect_info_server_id_fkey FOREIGN KEY (server_id) REFERENCES rgbotsm.hcs_servers(id);


--
-- Name: hcs_connect_info hcs_connect_info_subsystem_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_connect_info
    ADD CONSTRAINT hcs_connect_info_subsystem_id_fkey FOREIGN KEY (subsystem_id) REFERENCES rgbotsm.hcs_subsystems(id);


--
-- Name: hcs_servers hcs_servers_stand_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_servers
    ADD CONSTRAINT hcs_servers_stand_id_fkey FOREIGN KEY (stand_id) REFERENCES rgbotsm.hcs_stands(id);


--
-- Name: hcs_team_lineups hcs_team_lineups_analyst_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_team_lineups
    ADD CONSTRAINT hcs_team_lineups_analyst_id_fkey FOREIGN KEY (analyst_id) REFERENCES rgbotsm.hcs_members(id);


--
-- Name: hcs_team_lineups hcs_team_lineups_dba_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_team_lineups
    ADD CONSTRAINT hcs_team_lineups_dba_id_fkey FOREIGN KEY (dba_id) REFERENCES rgbotsm.hcs_members(id);


--
-- Name: hcs_team_lineups hcs_team_lineups_qa_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_team_lineups
    ADD CONSTRAINT hcs_team_lineups_qa_id_fkey FOREIGN KEY (qa_id) REFERENCES rgbotsm.hcs_members(id);


--
-- Name: hcs_team_lineups hcs_team_lineups_team_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_team_lineups
    ADD CONSTRAINT hcs_team_lineups_team_id_fkey FOREIGN KEY (team_id) REFERENCES rgbotsm.hcs_teams(id);


--
-- Name: hcs_team_lineups hcs_team_lineups_teamlead_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_team_lineups
    ADD CONSTRAINT hcs_team_lineups_teamlead_id_fkey FOREIGN KEY (teamlead_id) REFERENCES rgbotsm.hcs_members(id);


--
-- Name: hcs_team_lineups hcs_team_lineups_tpm_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_team_lineups
    ADD CONSTRAINT hcs_team_lineups_tpm_id_fkey FOREIGN KEY (tpm_id) REFERENCES rgbotsm.hcs_members(id);


--
-- Name: hcs_teams hcs_teams_subsystem_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.hcs_teams
    ADD CONSTRAINT hcs_teams_subsystem_id_fkey FOREIGN KEY (subsystem_id) REFERENCES rgbotsm.hcs_subsystems(id);


--
-- Name: jira_tasks jira_tasks_stand_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.jira_tasks
    ADD CONSTRAINT jira_tasks_stand_id_fkey FOREIGN KEY (stand_id) REFERENCES rgbotsm.hcs_stands(id);


--
-- Name: jira_tasks jira_tasks_subsystem_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.jira_tasks
    ADD CONSTRAINT jira_tasks_subsystem_id_fkey FOREIGN KEY (subsystem_id) REFERENCES rgbotsm.hcs_subsystems(id);


--
-- Name: user_filters user_filters_user_id_fkey; Type: FK CONSTRAINT; Schema: rgbotsm; Owner: postgres
--

ALTER TABLE ONLY rgbotsm.user_filters
    ADD CONSTRAINT user_filters_user_id_fkey FOREIGN KEY (user_id) REFERENCES rgbotsm.user_login_info(id);


--
-- Name: SCHEMA rgbotsm; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA rgbotsm TO regressbot_rw;


--
-- PostgreSQL database dump complete
--

