--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: annieh
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.categories OWNER TO annieh;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: annieh
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO annieh;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: annieh
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: deckmarks; Type: TABLE; Schema: public; Owner: annieh
--

CREATE TABLE public.deckmarks (
    id integer NOT NULL,
    link character varying(20) NOT NULL,
    description character varying(1000),
    thumbnail character varying(1000)
);


ALTER TABLE public.deckmarks OWNER TO annieh;

--
-- Name: deckmarks_id_seq; Type: SEQUENCE; Schema: public; Owner: annieh
--

CREATE SEQUENCE public.deckmarks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.deckmarks_id_seq OWNER TO annieh;

--
-- Name: deckmarks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: annieh
--

ALTER SEQUENCE public.deckmarks_id_seq OWNED BY public.deckmarks.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: annieh
--

CREATE TABLE public.users (
    id integer NOT NULL,
    fname character varying(100) NOT NULL,
    lname character varying(100) NOT NULL,
    email character varying(1000) NOT NULL,
    password character varying(100) NOT NULL
);


ALTER TABLE public.users OWNER TO annieh;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: annieh
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO annieh;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: annieh
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: deckmarks id; Type: DEFAULT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.deckmarks ALTER COLUMN id SET DEFAULT nextval('public.deckmarks_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: annieh
--

COPY public.categories (id, name) FROM stdin;
\.


--
-- Data for Name: deckmarks; Type: TABLE DATA; Schema: public; Owner: annieh
--

COPY public.deckmarks (id, link, description, thumbnail) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: annieh
--

COPY public.users (id, fname, lname, email, password) FROM stdin;
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: annieh
--

SELECT pg_catalog.setval('public.categories_id_seq', 1, false);


--
-- Name: deckmarks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: annieh
--

SELECT pg_catalog.setval('public.deckmarks_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: annieh
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: deckmarks deckmarks_pkey; Type: CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.deckmarks
    ADD CONSTRAINT deckmarks_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

