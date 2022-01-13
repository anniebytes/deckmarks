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
    name character varying(1000) NOT NULL
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
    link character varying(1000) NOT NULL,
    description text,
    thumbnail character varying(1000),
    user_id integer
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
-- Name: decktags; Type: TABLE; Schema: public; Owner: annieh
--

CREATE TABLE public.decktags (
    id integer NOT NULL,
    deckmark_id integer,
    tag_id integer
);


ALTER TABLE public.decktags OWNER TO annieh;

--
-- Name: decktags_id_seq; Type: SEQUENCE; Schema: public; Owner: annieh
--

CREATE SEQUENCE public.decktags_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.decktags_id_seq OWNER TO annieh;

--
-- Name: decktags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: annieh
--

ALTER SEQUENCE public.decktags_id_seq OWNED BY public.decktags.id;


--
-- Name: group_items; Type: TABLE; Schema: public; Owner: annieh
--

CREATE TABLE public.group_items (
    id integer NOT NULL,
    group_id integer,
    deckmark_id integer
);


ALTER TABLE public.group_items OWNER TO annieh;

--
-- Name: group_items_id_seq; Type: SEQUENCE; Schema: public; Owner: annieh
--

CREATE SEQUENCE public.group_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.group_items_id_seq OWNER TO annieh;

--
-- Name: group_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: annieh
--

ALTER SEQUENCE public.group_items_id_seq OWNED BY public.group_items.id;


--
-- Name: groups; Type: TABLE; Schema: public; Owner: annieh
--

CREATE TABLE public.groups (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description text,
    private boolean,
    user_id integer
);


ALTER TABLE public.groups OWNER TO annieh;

--
-- Name: groups_id_seq; Type: SEQUENCE; Schema: public; Owner: annieh
--

CREATE SEQUENCE public.groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.groups_id_seq OWNER TO annieh;

--
-- Name: groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: annieh
--

ALTER SEQUENCE public.groups_id_seq OWNED BY public.groups.id;


--
-- Name: tags; Type: TABLE; Schema: public; Owner: annieh
--

CREATE TABLE public.tags (
    id integer NOT NULL,
    name character varying(1000) NOT NULL
);


ALTER TABLE public.tags OWNER TO annieh;

--
-- Name: tags_id_seq; Type: SEQUENCE; Schema: public; Owner: annieh
--

CREATE SEQUENCE public.tags_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tags_id_seq OWNER TO annieh;

--
-- Name: tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: annieh
--

ALTER SEQUENCE public.tags_id_seq OWNED BY public.tags.id;


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
-- Name: decktags id; Type: DEFAULT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.decktags ALTER COLUMN id SET DEFAULT nextval('public.decktags_id_seq'::regclass);


--
-- Name: group_items id; Type: DEFAULT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.group_items ALTER COLUMN id SET DEFAULT nextval('public.group_items_id_seq'::regclass);


--
-- Name: groups id; Type: DEFAULT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.groups ALTER COLUMN id SET DEFAULT nextval('public.groups_id_seq'::regclass);


--
-- Name: tags id; Type: DEFAULT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.tags ALTER COLUMN id SET DEFAULT nextval('public.tags_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: annieh
--

COPY public.categories (id, name) FROM stdin;
1	Technology
2	Business
3	Art
\.


--
-- Data for Name: deckmarks; Type: TABLE DATA; Schema: public; Owner: annieh
--

COPY public.deckmarks (id, link, description, thumbnail, user_id) FROM stdin;
1	https://www.slideshare.net/e2m/flask-sqlalchemy	Python CodeLabs - Intro to Flask SQLAlchemy \n                         http://eueung.github.io/python/flask-sqlalchemy	www.somesite.com/someimg.jpg	1
2	https://docs.google.com/presentation/d/1WqsKSL88CDxdzHFR6J66vcU_85EbcNcQ4dbi5LCIWvk/edit#slide=id.g7ce099e2c8_1_0	sphinx-autoapi Generating API documentation with static analysis		1
3	https://docs.google.com/presentation/d/1yG8Cr1GcVcWUroPcIGHr4eqZblk5qQWIR1j0iGCuY6k/edit#slide=id.g7d7b1e67a3_0_218	Katie McLaughlin: Django Translations for the next generation	someimg.png	1
4	https://tldr-a11y.yuraima.com/			2
5	https://speakerdeck.com/jensimmons/how-new-css-is-changing-everything-about-graphic-design-on-the-web			2
6	https://speakerdeck.com/brad_frost/for-a-future-friendly-web	This talk introduces the need to start thinking and acting in a more future-friendly (http://futurefriend.ly) way when approaching web design. The diversity of web-enabled devices is increasing at an alarming rate. We have to rethink our content and the contexts in which our content is viewed.		2
7	https://speakerdeck.com/reverentgeek/javascript-past-present-and-future-ndc-porto-2020	This talk will be a parade of face-palm JavaScript fails, stupid JavaScript tricks, and bad jokes sure to get an eye-roll from everyone! Along the way, we may even learn a few mistakes to avoid and tips to make our own JavaScript less terrible!		2
8	https://slides.com/michaelingmarstaib/building-real-time-applications-with-graphql-and-blazor-be3f33	 Hot Chocolate: An Introduction to GraphQL on ASP.NET Core		2
\.


--
-- Data for Name: decktags; Type: TABLE DATA; Schema: public; Owner: annieh
--

COPY public.decktags (id, deckmark_id, tag_id) FROM stdin;
\.


--
-- Data for Name: group_items; Type: TABLE DATA; Schema: public; Owner: annieh
--

COPY public.group_items (id, group_id, deckmark_id) FROM stdin;
1	4	5
2	5	6
3	6	7
4	6	8
\.


--
-- Data for Name: groups; Type: TABLE DATA; Schema: public; Owner: annieh
--

COPY public.groups (id, name, description, private, user_id) FROM stdin;
1	Hogwarts 2022	Hogwarts School of Magic Winter 2022	f	1
2	PyCascades 2020	a regional Python conference in the Pacific Northwest hosted in Portland, Oregon, USA	\N	1
3	HB	hb slides	\N	2
4	W3C Publishing Summit 2017	Presented at the first W3C Publishing Summit, in San Francisco	\N	2
5	Web Design Day		\N	2
6	NDC Porto 2020	NDC Porto 2022 is a 5-Day Event for Software Developers, 25-29 April at the Alfandega Conference Centre in Porto.	\N	2
\.


--
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: annieh
--

COPY public.tags (id, name) FROM stdin;
1	tech
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: annieh
--

COPY public.users (id, fname, lname, email, password) FROM stdin;
1	Harry	Potter	harrypotter@hogwarts.edu	ilovegryffindor
2	kat	instructor	kat@hb.com	katiscool
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: annieh
--

SELECT pg_catalog.setval('public.categories_id_seq', 3, true);


--
-- Name: deckmarks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: annieh
--

SELECT pg_catalog.setval('public.deckmarks_id_seq', 8, true);


--
-- Name: decktags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: annieh
--

SELECT pg_catalog.setval('public.decktags_id_seq', 1, false);


--
-- Name: group_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: annieh
--

SELECT pg_catalog.setval('public.group_items_id_seq', 4, true);


--
-- Name: groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: annieh
--

SELECT pg_catalog.setval('public.groups_id_seq', 6, true);


--
-- Name: tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: annieh
--

SELECT pg_catalog.setval('public.tags_id_seq', 1, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: annieh
--

SELECT pg_catalog.setval('public.users_id_seq', 2, true);


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
-- Name: decktags decktags_pkey; Type: CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.decktags
    ADD CONSTRAINT decktags_pkey PRIMARY KEY (id);


--
-- Name: group_items group_items_pkey; Type: CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.group_items
    ADD CONSTRAINT group_items_pkey PRIMARY KEY (id);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (id);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: deckmarks deckmarks_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.deckmarks
    ADD CONSTRAINT deckmarks_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: decktags decktags_deckmark_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.decktags
    ADD CONSTRAINT decktags_deckmark_id_fkey FOREIGN KEY (deckmark_id) REFERENCES public.deckmarks(id);


--
-- Name: decktags decktags_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.decktags
    ADD CONSTRAINT decktags_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES public.tags(id);


--
-- Name: group_items group_items_deckmark_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.group_items
    ADD CONSTRAINT group_items_deckmark_id_fkey FOREIGN KEY (deckmark_id) REFERENCES public.deckmarks(id);


--
-- Name: group_items group_items_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.group_items
    ADD CONSTRAINT group_items_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: groups groups_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: annieh
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

