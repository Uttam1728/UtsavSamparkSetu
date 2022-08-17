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
-- Name: FolloWUp_followup; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."FolloWUp_followup" (
    id bigint NOT NULL,
    "FollowUp_Time" timestamp with time zone NOT NULL,
    "LastFollowUp_Time" timestamp with time zone NOT NULL,
    "How" integer NOT NULL,
    "Remark" character varying(1000),
    "Karyakram_id" bigint NOT NULL,
    "KaryKarVrund_id" bigint NOT NULL,
    "Yuvak_id" bigint NOT NULL,
    "Status" integer NOT NULL,
    "Coming" integer,
    "Present" boolean
);


ALTER TABLE public."FolloWUp_followup" OWNER TO postgres;

--
-- Name: FolloWUp_followup_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."FolloWUp_followup_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."FolloWUp_followup_id_seq" OWNER TO postgres;

--
-- Name: FolloWUp_followup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."FolloWUp_followup_id_seq" OWNED BY public."FolloWUp_followup".id;


--
-- Name: Mandal_karyakram; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Mandal_karyakram" (
    id bigint NOT NULL,
    "Title" character varying(1000) NOT NULL,
    "Start_Attandance" boolean NOT NULL,
    "Start_date" timestamp with time zone,
    "End_date" timestamp with time zone,
    "Start_Folloup" boolean NOT NULL,
    "Mandal_id" bigint,
    "Karyakram_date" timestamp with time zone,
    "IsDone" boolean NOT NULL
);


ALTER TABLE public."Mandal_karyakram" OWNER TO postgres;

--
-- Name: Mandal_karyakram_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Mandal_karyakram_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Mandal_karyakram_id_seq" OWNER TO postgres;

--
-- Name: Mandal_karyakram_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Mandal_karyakram_id_seq" OWNED BY public."Mandal_karyakram".id;


--
-- Name: Mandal_mandalprofile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Mandal_mandalprofile" (
    id bigint NOT NULL,
    "Name" character varying(100) NOT NULL,
    "Area" character varying(100) NOT NULL,
    "Nirikshak_id" bigint,
    "Sanchalak_id" bigint
);


ALTER TABLE public."Mandal_mandalprofile" OWNER TO postgres;

--
-- Name: Mandal_mandalprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Mandal_mandalprofile_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Mandal_mandalprofile_id_seq" OWNER TO postgres;

--
-- Name: Mandal_mandalprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Mandal_mandalprofile_id_seq" OWNED BY public."Mandal_mandalprofile".id;


--
-- Name: SamparkKarykar_karyakarprofile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."SamparkKarykar_karyakarprofile" (
    id bigint NOT NULL,
    karykar1profile_id bigint NOT NULL,
    mandal_id bigint NOT NULL,
    karykar2profile_id bigint
);


ALTER TABLE public."SamparkKarykar_karyakarprofile" OWNER TO postgres;

--
-- Name: SamparkKarykar_karyakarprofile_Yuvaks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."SamparkKarykar_karyakarprofile_Yuvaks" (
    id bigint NOT NULL,
    karyakarprofile_id bigint NOT NULL,
    yuvakprofile_id bigint NOT NULL
);


ALTER TABLE public."SamparkKarykar_karyakarprofile_Yuvaks" OWNER TO postgres;

--
-- Name: SamparkKarykar_karyakarprofile_Yuvaks_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."SamparkKarykar_karyakarprofile_Yuvaks_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."SamparkKarykar_karyakarprofile_Yuvaks_id_seq" OWNER TO postgres;

--
-- Name: SamparkKarykar_karyakarprofile_Yuvaks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."SamparkKarykar_karyakarprofile_Yuvaks_id_seq" OWNED BY public."SamparkKarykar_karyakarprofile_Yuvaks".id;


--
-- Name: SamparkKarykar_karyakarprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."SamparkKarykar_karyakarprofile_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."SamparkKarykar_karyakarprofile_id_seq" OWNER TO postgres;

--
-- Name: SamparkKarykar_karyakarprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."SamparkKarykar_karyakarprofile_id_seq" OWNED BY public."SamparkKarykar_karyakarprofile".id;


--
-- Name: Yuvak_satsangprofile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Yuvak_satsangprofile" (
    id bigint NOT NULL,
    "NityaPuja" boolean,
    "NityaPujaYear" integer,
    "TilakChandlo" boolean,
    "TilakChandloYear" integer,
    "Satsangi" boolean,
    "SatsangiYear" integer,
    "AthvadikSabha" boolean,
    "AthvadikSabhaYear" integer,
    "Ravisabha" boolean,
    "RavisabhaYear" integer,
    "GharSatsang" boolean,
    "GharSatsangYear" integer,
    "SSP" boolean,
    "SSPStage" integer NOT NULL,
    "Ekadashi" boolean,
    "EkadashiYear" integer,
    "Niymit_Vanchan" boolean,
    "Niymit_VanchanYear" integer,
    "yuvakProfile_id" bigint NOT NULL
);


ALTER TABLE public."Yuvak_satsangprofile" OWNER TO postgres;

--
-- Name: Yuvak_satsangprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Yuvak_satsangprofile_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Yuvak_satsangprofile_id_seq" OWNER TO postgres;

--
-- Name: Yuvak_satsangprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Yuvak_satsangprofile_id_seq" OWNED BY public."Yuvak_satsangprofile".id;


--
-- Name: Yuvak_yuvakprofile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Yuvak_yuvakprofile" (
    id bigint NOT NULL,
    "FirstName" character varying(50) NOT NULL,
    "MiddleName" character varying(50) NOT NULL,
    "SurName" character varying(50) NOT NULL,
    "WhatsappNo" character varying(10) NOT NULL,
    "HomePhoneNo" character varying(10),
    "PinCode" character varying(6),
    user_id integer,
    mandal_id bigint NOT NULL,
    "Area" character varying(50),
    "HouseNo" integer,
    "LandMark" character varying(100),
    "Soc_Name" character varying(50),
    "DateOfBirth" date,
    "Education" character varying(100),
    "Married" boolean
);


ALTER TABLE public."Yuvak_yuvakprofile" OWNER TO postgres;

--
-- Name: Yuvak_yuvakprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Yuvak_yuvakprofile_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Yuvak_yuvakprofile_id_seq" OWNER TO postgres;

--
-- Name: Yuvak_yuvakprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Yuvak_yuvakprofile_id_seq" OWNED BY public."Yuvak_yuvakprofile".id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: FolloWUp_followup id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FolloWUp_followup" ALTER COLUMN id SET DEFAULT nextval('public."FolloWUp_followup_id_seq"'::regclass);


--
-- Name: Mandal_karyakram id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Mandal_karyakram" ALTER COLUMN id SET DEFAULT nextval('public."Mandal_karyakram_id_seq"'::regclass);


--
-- Name: Mandal_mandalprofile id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Mandal_mandalprofile" ALTER COLUMN id SET DEFAULT nextval('public."Mandal_mandalprofile_id_seq"'::regclass);


--
-- Name: SamparkKarykar_karyakarprofile id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile" ALTER COLUMN id SET DEFAULT nextval('public."SamparkKarykar_karyakarprofile_id_seq"'::regclass);


--
-- Name: SamparkKarykar_karyakarprofile_Yuvaks id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile_Yuvaks" ALTER COLUMN id SET DEFAULT nextval('public."SamparkKarykar_karyakarprofile_Yuvaks_id_seq"'::regclass);


--
-- Name: Yuvak_satsangprofile id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Yuvak_satsangprofile" ALTER COLUMN id SET DEFAULT nextval('public."Yuvak_satsangprofile_id_seq"'::regclass);


--
-- Name: Yuvak_yuvakprofile id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Yuvak_yuvakprofile" ALTER COLUMN id SET DEFAULT nextval('public."Yuvak_yuvakprofile_id_seq"'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: FolloWUp_followup; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."FolloWUp_followup" (id, "FollowUp_Time", "LastFollowUp_Time", "How", "Remark", "Karyakram_id", "KaryKarVrund_id", "Yuvak_id", "Status", "Coming", "Present") FROM stdin;
118	2022-02-15 18:38:28.55842+05:30	2022-02-15 18:39:00.873346+05:30	6	\N	8	9	19	2	2	f
101	2022-02-15 18:38:28.43045+05:30	2022-02-15 18:38:28.43045+05:30	6	\N	8	6	1	3	\N	f
102	2022-02-15 18:38:28.44642+05:30	2022-02-15 18:38:28.44642+05:30	6	\N	8	6	29	3	\N	f
103	2022-02-15 18:38:28.454455+05:30	2022-02-15 18:38:28.454455+05:30	6	\N	8	6	33	3	\N	f
104	2022-02-15 18:38:28.462422+05:30	2022-02-15 18:38:28.462422+05:30	6	\N	8	8	27	3	\N	f
105	2022-02-15 18:38:28.470421+05:30	2022-02-15 18:38:28.470421+05:30	6	\N	8	8	35	3	\N	f
106	2022-02-15 18:38:28.49442+05:30	2022-02-15 18:38:28.49442+05:30	6	\N	8	9	20	3	\N	f
107	2022-02-15 18:38:28.49442+05:30	2022-02-15 18:38:28.49442+05:30	6	\N	8	9	25	3	\N	f
108	2022-02-15 18:38:28.502421+05:30	2022-02-15 18:38:28.502421+05:30	6	\N	8	9	26	3	\N	f
109	2022-02-15 18:38:28.51042+05:30	2022-02-15 18:38:28.51042+05:30	6	\N	8	9	39	3	\N	f
110	2022-02-15 18:38:28.51042+05:30	2022-02-15 18:38:28.51042+05:30	6	\N	8	9	31	3	\N	f
137	2022-02-15 18:38:28.670417+05:30	2022-02-15 18:38:28.670417+05:30	6	\N	8	9	3	3	\N	f
136	2022-02-15 18:38:28.662419+05:30	2022-02-15 18:38:28.662419+05:30	6	\N	8	9	43	3	\N	t
111	2022-02-15 18:38:28.518421+05:30	2022-02-15 18:38:28.518421+05:30	6	\N	8	9	34	3	\N	f
112	2022-02-15 18:38:28.52642+05:30	2022-02-15 18:38:28.52642+05:30	6	\N	8	9	2	3	\N	f
113	2022-02-15 18:38:28.534421+05:30	2022-02-15 18:38:28.534421+05:30	6	\N	8	9	47	3	\N	f
114	2022-02-15 18:38:28.534421+05:30	2022-02-15 18:38:28.534421+05:30	6	\N	8	9	46	3	\N	f
115	2022-02-15 18:38:28.54242+05:30	2022-02-15 18:38:28.54242+05:30	6	\N	8	9	40	3	\N	f
116	2022-02-15 18:38:28.550423+05:30	2022-02-15 18:38:28.550423+05:30	6	\N	8	9	21	3	\N	f
117	2022-02-15 18:38:28.550423+05:30	2022-02-15 18:38:28.550423+05:30	6	\N	8	9	5	3	\N	f
119	2022-02-15 18:38:28.56642+05:30	2022-02-15 18:38:28.56642+05:30	6	\N	8	9	37	3	\N	f
120	2022-02-15 18:38:28.56642+05:30	2022-02-15 18:38:28.56642+05:30	6	\N	8	9	32	3	\N	f
121	2022-02-15 18:38:28.574421+05:30	2022-02-15 18:38:28.574421+05:30	6	\N	8	9	24	3	\N	f
122	2022-02-15 18:38:28.58242+05:30	2022-02-15 18:38:28.58242+05:30	6	\N	8	9	38	3	\N	f
123	2022-02-15 18:38:28.590421+05:30	2022-02-15 18:38:28.590421+05:30	6	\N	8	9	48	3	\N	f
124	2022-02-15 18:38:28.590421+05:30	2022-02-15 18:38:28.590421+05:30	6	\N	8	9	28	3	\N	f
125	2022-02-15 18:38:28.59842+05:30	2022-02-15 18:38:28.59842+05:30	6	\N	8	9	30	3	\N	f
126	2022-02-15 18:38:28.60642+05:30	2022-02-15 18:38:28.60642+05:30	6	\N	8	9	42	3	\N	f
127	2022-02-15 18:38:28.614428+05:30	2022-02-15 18:38:28.614428+05:30	6	\N	8	9	6	3	\N	f
128	2022-02-15 18:38:28.614428+05:30	2022-02-15 18:38:28.614428+05:30	6	\N	8	9	41	3	\N	f
129	2022-02-15 18:38:28.622475+05:30	2022-02-15 18:38:28.622475+05:30	6	\N	8	9	36	3	\N	f
130	2022-02-15 18:38:28.63042+05:30	2022-02-15 18:38:28.63042+05:30	6	\N	8	9	4	3	\N	f
131	2022-02-15 18:38:28.638421+05:30	2022-02-15 18:38:28.638421+05:30	6	\N	8	9	23	3	\N	f
132	2022-02-15 18:38:28.638421+05:30	2022-02-15 18:38:28.638421+05:30	6	\N	8	9	44	3	\N	f
133	2022-02-15 18:38:28.646421+05:30	2022-02-15 18:38:28.646421+05:30	6	\N	8	9	49	3	\N	f
134	2022-02-15 18:38:28.65445+05:30	2022-02-15 18:38:28.65445+05:30	6	\N	8	9	22	3	\N	f
135	2022-02-15 18:38:28.662419+05:30	2022-02-15 18:38:28.662419+05:30	6	\N	8	9	45	3	\N	f
\.


--
-- Data for Name: Mandal_karyakram; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Mandal_karyakram" (id, "Title", "Start_Attandance", "Start_date", "End_date", "Start_Folloup", "Mandal_id", "Karyakram_date", "IsDone") FROM stdin;
8	17 ફેબ્રુવારી યુવક સભા	t	2022-02-15 18:38:12+05:30	2022-02-17 18:00:00+05:30	t	1	2022-02-17 18:00:00+05:30	t
\.


--
-- Data for Name: Mandal_mandalprofile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Mandal_mandalprofile" (id, "Name", "Area", "Nirikshak_id", "Sanchalak_id") FROM stdin;
1	Utsav	Yogichowk	3	1
\.


--
-- Data for Name: SamparkKarykar_karyakarprofile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."SamparkKarykar_karyakarprofile" (id, karykar1profile_id, mandal_id, karykar2profile_id) FROM stdin;
6	20	1	19
8	47	1	\N
9	49	1	\N
\.


--
-- Data for Name: SamparkKarykar_karyakarprofile_Yuvaks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."SamparkKarykar_karyakarprofile_Yuvaks" (id, karyakarprofile_id, yuvakprofile_id) FROM stdin;
10	6	1
11	6	29
12	6	33
13	8	35
14	8	27
\.


--
-- Data for Name: Yuvak_satsangprofile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Yuvak_satsangprofile" (id, "NityaPuja", "NityaPujaYear", "TilakChandlo", "TilakChandloYear", "Satsangi", "SatsangiYear", "AthvadikSabha", "AthvadikSabhaYear", "Ravisabha", "RavisabhaYear", "GharSatsang", "GharSatsangYear", "SSP", "SSPStage", "Ekadashi", "EkadashiYear", "Niymit_Vanchan", "Niymit_VanchanYear", "yuvakProfile_id") FROM stdin;
8	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	6
9	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	5
10	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	4
11	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	3
12	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	2
13	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	1
26	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	19
27	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	20
28	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	21
29	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	22
30	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	23
31	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	24
32	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	25
33	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	26
34	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	27
35	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	28
36	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	29
37	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	30
38	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	31
39	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	32
40	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	33
41	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	34
42	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	35
43	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	36
44	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	37
45	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	38
46	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	39
47	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	40
48	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	41
49	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	42
50	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	43
51	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	44
52	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	45
53	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	46
54	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	47
55	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	48
56	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	49
\.


--
-- Data for Name: Yuvak_yuvakprofile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Yuvak_yuvakprofile" (id, "FirstName", "MiddleName", "SurName", "WhatsappNo", "HomePhoneNo", "PinCode", user_id, mandal_id, "Area", "HouseNo", "LandMark", "Soc_Name", "DateOfBirth", "Education", "Married") FROM stdin;
19	Ketanbhai	Jivrajbhai	Vaghani	9925819694	\N	\N	35	1	\N	\N	\N	\N	\N	\N	\N
49	Admin	Utsav	Mandal	999999999	\N	\N	65	1	\N	\N	\N	\N	\N	\N	\N
41	Kaushik	Kishorbhai	Vaddoriya	982519683	\N	\N	57	1	\N	\N	\N	\N	\N	\N	\N
42	Tirth	Rakeshbhai	Isamaliya	9512719511	\N	\N	58	1	\N	\N	\N	\N	\N	\N	\N
6	Chirag	Rameshbhai	Katrodiya	9727386952	\N	395010	22	1	Yogichowk	61	yogichowk	sanman soc	\N	\N	\N
5	HariKrushn	rameshbhai	kakadiya	9727386952	\N	395010	20	1	Yogichowk	61	yogichowk	sanman soc	1989-02-01	B.Tech	f
4	Kaushik	Rameshbhai	Vadadoriya	9727386952	\N	395010	16	1	a	1	a	a	\N	\N	f
3	ManishBhai	Rameshbhai	BHuva	9727386952	\N	395010	17	1	a	1	a	a	\N	\N	f
2	Jenish	Rameshbhai	Savaliya	9727386952	\N	395010	18	1	a	1	a	a	\N	\N	f
20	Ashokbhai	Dhanjibhai	Paladiya	8866251138	\N	\N	36	1	\N	\N	\N	\N	\N	\N	\N
1	Ushank	Rajeshbhai	Radadiya	9727386952	9727386952	395010	19	1	a	1	a	a	2000-01-04	B.Tech	f
21	Harikrushna	Rameshbhai	Kakadiya	7359663446	\N	\N	37	1	\N	\N	\N	\N	\N	\N	\N
22	Manish	Dilipbhai	Bhuva	8140156780	\N	\N	38	1	\N	\N	\N	\N	\N	\N	\N
23	Yogeshbhai	Rameshbhai	Kakadiya	9574515515	\N	\N	39	1	\N	\N	\N	\N	\N	\N	\N
24	Dhaval	Naranbhai	Dholakiya	9898528152	\N	\N	40	1	\N	\N	\N	\N	\N	\N	\N
25	Rakesh	Dhanjibhai	Paladiya	9998597533	\N	\N	41	1	\N	\N	\N	\N	\N	\N	\N
26	Yogesh	Devchandbhai	Buha	7043323343	\N	\N	42	1	\N	\N	\N	\N	\N	\N	\N
27	Ronil	Rasikbhai	Kakadiya	9925297081	\N	\N	43	1	\N	\N	\N	\N	\N	\N	\N
28	Ketanbhai	Vajibhai	Nasit	9722547310	\N	\N	44	1	\N	\N	\N	\N	\N	\N	\N
29	Dharmesh	Vinubhai	Gabani	8980824039	\N	\N	45	1	\N	\N	\N	\N	\N	\N	\N
30	Sharad	Nagjibhai	Rangoliya	826455151	\N	\N	46	1	\N	\N	\N	\N	\N	\N	\N
31	Tilak	Kishorbhai	Chalodiya	9725880095	\N	\N	47	1	\N	\N	\N	\N	\N	\N	\N
32	Hitesh	Nagjibhai	Rangoliya	743597512	\N	\N	48	1	\N	\N	\N	\N	\N	\N	\N
33	Arvind	Veljibhai	Khanpara	9327372590	\N	\N	49	1	\N	\N	\N	\N	\N	\N	\N
34	Mahesh	Sanjaybhai	Patel	9662620832	\N	\N	50	1	\N	\N	\N	\N	\N	\N	\N
35	Pankaj	Ukabhai	Lathiya	9173729814	\N	\N	51	1	\N	\N	\N	\N	\N	\N	\N
36	Mayur	Ukabhai	Lathiya	9737091870	\N	\N	52	1	\N	\N	\N	\N	\N	\N	\N
37	Ravi	Kanubhai	Dhamecha	9913719559	\N	\N	53	1	\N	\N	\N	\N	\N	\N	\N
38	Rohit	Kanjibhai	Virani	9925865353	\N	\N	54	1	\N	\N	\N	\N	\N	\N	\N
39	Vivek	Narshibhai	Vaghasiya	9825355088	\N	\N	55	1	\N	\N	\N	\N	\N	\N	\N
40	Darshan	Prbhubhai	Isamaliya	9925236542	\N	\N	56	1	\N	\N	\N	\N	\N	\N	\N
43	Maulik	Rajeshbhai	Viradiya	9638699288	\N	\N	59	1	\N	\N	\N	\N	\N	\N	\N
44	Jenish	Rajeshbhai	Savaliya	9033015515	\N	\N	60	1	\N	\N	\N	\N	\N	\N	\N
45	Hit	Rajeshbhai	Dholakiya	9512088899	\N	\N	61	1	\N	\N	\N	\N	\N	\N	\N
46	Vikash	Rajeshbhai	Ramani	9054353408	\N	\N	62	1	\N	\N	\N	\N	\N	\N	\N
47	Priyam	Rajeshbhai	Baldha	8160263052	\N	\N	63	1	\N	\N	\N	\N	\N	\N	\N
48	Tirthan	Rajeshbhai	Jasholiya	8160263052	\N	\N	64	1	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
2	Sampark Karykar
1	Yuvak
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	26
2	1	28
3	2	13
4	2	14
5	2	15
6	2	16
7	2	25
8	2	26
10	2	28
11	2	32
13	2	30
15	2	40
16	2	42
17	2	44
18	2	36
19	1	16
20	1	40
21	1	32
22	1	14
23	1	36
24	2	48
25	2	46
26	1	48
27	1	46
31	1	44
32	2	52
33	1	52
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add yuvak profile	7	add_yuvakprofile
26	Can change yuvak profile	7	change_yuvakprofile
27	Can delete yuvak profile	7	delete_yuvakprofile
28	Can view yuvak profile	7	view_yuvakprofile
29	Can add karyakar profile	8	add_karyakarprofile
30	Can change karyakar profile	8	change_karyakarprofile
31	Can delete karyakar profile	8	delete_karyakarprofile
32	Can view karyakar profile	8	view_karyakarprofile
33	Can add mandal profile	9	add_mandalprofile
34	Can change mandal profile	9	change_mandalprofile
35	Can delete mandal profile	9	delete_mandalprofile
36	Can view mandal profile	9	view_mandalprofile
37	Can add karyakram	10	add_karyakram
38	Can change karyakram	10	change_karyakram
39	Can delete karyakram	10	delete_karyakram
40	Can view karyakram	10	view_karyakram
41	Can add follow up	11	add_followup
42	Can change follow up	11	change_followup
43	Can delete follow up	11	delete_followup
44	Can view follow up	11	view_followup
45	Can add satsang profile	12	add_satsangprofile
46	Can change satsang profile	12	change_satsangprofile
47	Can delete satsang profile	12	delete_satsangprofile
48	Can view satsang profile	12	view_satsangprofile
49	Can add Attandance	13	add_attandance
50	Can change Attandance	13	change_attandance
51	Can delete Attandance	13	delete_attandance
52	Can view Attandance	13	view_attandance
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
13	pbkdf2_sha256$320000$BjaRK5VOYSdUjyDDw7TYMW$ojfSlHvL+IjIARI2lhqdHBaqcs1ClkEaPiSanQNYfHU=	\N	f	Kaushik004			Kaushik004@kaushik004.com	t	t	2022-02-06 22:18:01.897441+05:30
16	pbkdf2_sha256$320000$t5qhgWkmOzdIOgIbHpMrFs$4/7z0pMc4ULws9EOR7IKryz+sD0xJnzTWP4ZFn6WL4I=	\N	f	kaushik004			kaushik004@kaushik004.com	t	t	2022-02-06 22:18:53.680731+05:30
18	pbkdf2_sha256$320000$m9FpDJmG6wXkW3WjHY31qF$9CXn7VAJdB61suDb8shGTggLQyk44YI1bu2v1yQi1U4=	\N	f	jenish002			jenish002@jenish002.com	t	t	2022-02-06 22:19:19.595831+05:30
20	pbkdf2_sha256$320000$5hLh5tF2NexvyfbxYIEul6$Dfe8zRRO/cjdHN4Fdu3e+WX2piQYoWeOseZsPiD75RA=	\N	f	harikrushn005			harikrushn005@harikrushn005.com	t	t	2022-02-06 22:25:51.661416+05:30
30	pbkdf2_sha256$320000$RW98iGe3aEicIkGNFvkiuq$hyVDL2yk69PfR9Ivxwvp1xJBxiiQRcBWejS5TGVVDmU=	\N	f	jenish014			jenish014@jenish014.com	t	t	2022-02-10 14:21:43.151294+05:30
31	pbkdf2_sha256$320000$KG4Xfs2FrXxz6vwdNT7Uza$iJNy3ziU7/q494qtOVIaZ82g3cwSac4bK1WcnDX7cQI=	\N	f	jenish015			jenish015@jenish015.com	t	t	2022-02-10 14:21:43.384293+05:30
33	pbkdf2_sha256$320000$LbrOsRArQu1tuboksNJZ43$4N2Bt//os3tToYGAA+WM0Ofg2f0tVZQZlxee2NYB+lA=	\N	f	jenish017			jenish017@jenish017.com	t	t	2022-02-10 14:27:58.858156+05:30
34	pbkdf2_sha256$320000$uokjNNhVMjb7IawZE4Bs6z$2o3lAhI69qGNl05o5y1x3P3uNBOc4ykAh/xc5DNeUjI=	\N	f	jenish018			jenish018@jenish018.com	t	t	2022-02-10 14:27:59.035118+05:30
32	pbkdf2_sha256$320000$u9CCpIPT9JKlif4VpbTgTg$2YoUu5utZ/sA67Xu0oa0oqd06UUPs/CvCNglzrruIQ0=	\N	f	jenish016			jenish016@jenish016.com	t	t	2022-02-10 14:27:58+05:30
36	pbkdf2_sha256$320000$Lc9mFvw1oc8KWSBoQokfPu$JHgYgKlzv+OeUq1HlFmPje0OZ2qMXLGU4Z17vgOI0cc=	\N	f	ashokbhai020			ashokbhai020@ashokbhai020.com	t	t	2022-02-10 15:12:01.490298+05:30
37	pbkdf2_sha256$320000$TMvkHqbe6l8zx59ejji9dh$w0yeenfbs5f2CPEpjML4JFRZLFzRAD3PbLmelL8W7uI=	\N	f	harikrushna021			harikrushna021@harikrushna021.com	t	t	2022-02-10 15:12:01.959299+05:30
22	pbkdf2_sha256$320000$NoKjcaGdMZWlJkAZjcXJBH$TR3TeN3yovZhz07HWs3HaSDycbeqbaMJPNrBS8Byomk=	\N	f	chirag006			chirag006@chirag006.com	t	t	2022-02-08 17:08:12.875221+05:30
35	pbkdf2_sha256$320000$RlLq6R4v2lV0SwGWByFE8A$DL1mf8m4gi+00KzzYa7fDQSV33Iz5cy4kW4AD5v+PtA=	2022-02-15 18:38:47.918113+05:30	f	ketanbhai019			ketanbhai019@ketanbhai019.com	t	t	2022-02-10 15:12:00+05:30
38	pbkdf2_sha256$320000$ERCdzZgYjEGDYBxTMaWfNk$Yg6bDyuHfpHo5B7Z9PApkhYhqIZuUlWBwNa3wpyWw1w=	\N	f	manish022			manish022@manish022.com	t	t	2022-02-10 15:12:02.315296+05:30
39	pbkdf2_sha256$320000$0OcIT9Ba0mcJsBZoaFCRhv$Xvekd1RspcmJXj0adqGvL3kbVGiPQ5PpJxbup9lEJtk=	\N	f	yogeshbhai023			yogeshbhai023@yogeshbhai023.com	t	t	2022-02-10 15:12:02.6633+05:30
40	pbkdf2_sha256$320000$FZUrmKKkAGlcgmnSGU2KKO$J/xSKOYb3vxkIH+IKDLYxmXX2fvCnk8NVBGszn86y2g=	\N	f	dhaval024			dhaval024@dhaval024.com	t	t	2022-02-10 15:12:03.343299+05:30
41	pbkdf2_sha256$320000$Fbm5F5WiP99WowJNXWR6C7$Tdvx8yrceLsYTsV5j97pvZ3LkzFhEHYdhRh8+vamn6s=	\N	f	rakesh025			rakesh025@rakesh025.com	t	t	2022-02-10 15:12:03.911298+05:30
17	pbkdf2_sha256$320000$e8oLeYvEOlzRMcQ6eAUnU1$ofBZN8V1SI6SR+JgJo2HsdCEyZ38MES1cvSO7HH3Bps=	2022-02-11 19:34:10+05:30	f	manishbhai003			manishbhai003@manishbhai003.com	t	t	2022-02-06 22:19:09+05:30
42	pbkdf2_sha256$320000$SsGYxAJ6vJxoQLlSB83pFq$JQYPOB07qLO6/tvidkRv2RVB+2cwDmjl44AH8iijSQg=	\N	f	yogesh026			yogesh026@yogesh026.com	t	t	2022-02-10 15:12:04.359299+05:30
43	pbkdf2_sha256$320000$f56IUSSKLxkhs2HNq9Onmi$hE3NBtGOxPGQDXo1rY2GZTiPMmgBL/lwC5fXuUmBh2E=	\N	f	ronil027			ronil027@ronil027.com	t	t	2022-02-10 15:12:04.783298+05:30
44	pbkdf2_sha256$320000$jnOzOEgWh5TOoceyHrWgOy$V/7NTNLONrE8nG5NWoqAtMYpkg/1DLR2IITYgOzczX8=	\N	f	ketanbhai028			ketanbhai028@ketanbhai028.com	t	t	2022-02-10 15:12:05.137301+05:30
45	pbkdf2_sha256$320000$3L3AT3ATfzVIQZh1h9Qvx2$IvQhWQ28TWu1IsiTXbPwNkbLvq083bBWc0cmUfZ/Ntk=	\N	f	dharmesh029			dharmesh029@dharmesh029.com	t	t	2022-02-10 15:12:05.476298+05:30
46	pbkdf2_sha256$320000$5D7cEvGYDp7g8FLkHOQ65z$vqaQh3FVKFeK0JYXUoqTdv32c6q+y8U8p+NAM8bW6O0=	\N	f	sharad030			sharad030@sharad030.com	t	t	2022-02-10 15:12:05.846605+05:30
47	pbkdf2_sha256$320000$QHggzIQVNKFVtvwx4h088x$NtGUQKnRY7v6jHonL3s/Cg6cSdNL+zhMs4i8Vk3ChP4=	\N	f	tilak031			tilak031@tilak031.com	t	t	2022-02-10 15:12:06.287607+05:30
48	pbkdf2_sha256$320000$caWmW7Ev9WMdKO6w8lUgLf$laTc+xAZ278jLuNooeIC+J4OVrwPgeVQVHqlxXfrxfo=	\N	f	hitesh032			hitesh032@hitesh032.com	t	t	2022-02-10 15:12:06.863984+05:30
50	pbkdf2_sha256$320000$PHOXe5gUdNzj43RZSVaz0i$htbvLyeO3/Pui8XSkT5dBpgH+YDQc8N3HRWNYXdzX3k=	\N	f	mahesh034			mahesh034@mahesh034.com	t	t	2022-02-10 15:12:07.7392+05:30
51	pbkdf2_sha256$320000$4dBwtvnSsPXhcofAT10QmA$Fufi/ALAg1LyqdX5f2ckK7WIwER1oZ/MhcFrYF0vIWQ=	\N	f	pankaj035			pankaj035@pankaj035.com	t	t	2022-02-10 15:12:08.124201+05:30
53	pbkdf2_sha256$320000$tFYgrE8i25Tcwkti91mRAK$RUPK7SOvD9wZ2xTDGPSHN1hgTxrN6NxWLBcZXZMyu7w=	\N	f	ravi037			ravi037@ravi037.com	t	t	2022-02-10 15:12:08.945485+05:30
54	pbkdf2_sha256$320000$mMaku9rExKjc7bsAkvHXPL$dY4dl7RNeVkeBuy3nZoqsEodVI5s3g/C3YfkEo+TMeM=	\N	f	rohit038			rohit038@rohit038.com	t	t	2022-02-10 15:12:09.289146+05:30
55	pbkdf2_sha256$320000$Qqpn8tkTgXSsfvhKgrxcUz$AZPDuY4UjFhFI+kdUT3pe0fYsj9aWfdz6rhtUTUjdaA=	\N	f	vivek039			vivek039@vivek039.com	t	t	2022-02-10 15:12:09.666494+05:30
56	pbkdf2_sha256$320000$fqCqP95JojP2DrjILNAgzA$4nEnB2SVkl3Ij+b1rrJyOkRjOFunE1TBboE3IaaKIEA=	\N	f	darshan040			darshan040@darshan040.com	t	t	2022-02-10 15:12:10.103498+05:30
58	pbkdf2_sha256$320000$9rVvtKCnVVpkB782GrpS0p$f1qpQyKDr/Z1u4w2ojMPcQxpBsf+Nm1s2rn/9sx2KE0=	\N	f	tirth042			tirth042@tirth042.com	t	t	2022-02-10 15:12:10.850528+05:30
49	pbkdf2_sha256$320000$FhAiLox76QWp0ECT7jzfEv$zUhrtJ709iZ1scM8t+H2ZdpKZ0iC8/vEi/QQN9CR6Xw=	2022-02-15 18:00:03.627664+05:30	f	arvind033			arvind033@arvind033.com	t	t	2022-02-10 15:12:07.310236+05:30
57	pbkdf2_sha256$320000$EBUf49w7q2ED8ENUbYjJ2V$hlRS0jtickMWIOfdeJwjRJfRNDBInDU+lISphT9rROk=	2022-02-11 23:05:37+05:30	f	kaushik041			kaushik041@kaushik041.com	t	t	2022-02-10 15:12:10+05:30
19	pbkdf2_sha256$320000$fOAODRjiZPsBMlxnEKbLsd$5Yf0lkJFgAUXdDJp/QrISA5WTDST5v1dtZIgjofuhk4=	2022-02-12 13:03:52.098136+05:30	f	ushank001			ushank001@ushank001.com	t	t	2022-02-06 22:19:25.013798+05:30
52	pbkdf2_sha256$320000$Znmtfc0ThTVwuXkCLlqjgo$HjzdO2liVTRCymx4xZgQaU62Ck1xMDxg+uOEtE5hI8U=	\N	f	mayur036			mayur036@mayur036.com	t	t	2022-02-10 15:12:08+05:30
59	pbkdf2_sha256$320000$nfkK0dcb006YTZo7YKazBQ$YstC3ZKYJRJ5e8rdMGLX7Qfh0bbAf7IFNJtWrxnNlYE=	\N	f	maulik043			maulik043@maulik043.com	t	t	2022-02-10 15:12:11.239531+05:30
60	pbkdf2_sha256$320000$HeheNtpRiv9zpF93xKODM0$PMEfMCSw7LCj55DDm3bMXjCfl3c4XcP7TIPSWNavPoI=	\N	f	jenish044			jenish044@jenish044.com	t	t	2022-02-10 15:12:11.620315+05:30
61	pbkdf2_sha256$320000$FLeCv9jMiEqQs0MBv14tA1$RZmpJCI1qpUyAFvNviaJIbtcLN73nG8qwZBQN6b4TNg=	\N	f	hit045			hit045@hit045.com	t	t	2022-02-10 15:12:11.967982+05:30
62	pbkdf2_sha256$320000$eARAGjeprbc82oyu9IgJyq$gXOhLg4089+fEMUOPF+11qCSmDkWQZDCDtpNYCbXCuM=	\N	f	vikash046			vikash046@vikash046.com	t	t	2022-02-10 15:12:12.242906+05:30
63	pbkdf2_sha256$320000$F2YLoFJMUBgtBQMxZ45XJd$yTJcmofi9fotS8KDkBTsISjbkrk1TRnDRNm7a1HHgdw=	\N	f	priyam047			priyam047@priyam047.com	t	t	2022-02-10 15:12:12.560877+05:30
64	pbkdf2_sha256$320000$gWa14aElHrp28H5vGMZmI0$Yme+KPOTv+cwYUtJMc6r/30z3juxLbIyq9Jk/PM+Gxs=	\N	f	tirthan048			tirthan048@tirthan048.com	t	t	2022-02-10 15:12:12.899245+05:30
65	pbkdf2_sha256$320000$gOoLtBp8mq2x2rRRhGIyfk$a8vVAv7tMHG51YA18nOBRxOmebuRO+hMqfyhLkUoJqU=	2022-02-15 17:04:38.483842+05:30	t	admin049			admin049@admin049.com	t	t	2022-02-15 16:24:55+05:30
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
7	13	1
8	16	1
9	17	1
10	18	1
11	19	1
12	20	1
14	22	1
22	30	1
23	31	1
24	32	1
25	33	1
26	34	1
27	35	1
28	36	1
29	37	1
30	38	1
31	39	1
32	40	1
33	41	1
34	42	1
35	43	1
36	44	1
37	45	1
38	46	1
39	47	1
40	48	1
41	49	1
42	50	1
43	51	1
44	52	1
45	53	1
46	54	1
47	55	1
48	56	1
49	57	1
50	58	1
51	59	1
52	60	1
53	61	1
54	62	1
55	63	1
56	64	1
58	36	2
59	35	2
60	63	2
62	65	1
63	65	2
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
169	2022-02-15 17:07:17.71705+05:30	6	Feb 17 YS	3		10	65
170	2022-02-15 17:07:17.74449+05:30	4	Yuvak sabha  12 Feb	3		10	65
172	2022-02-15 17:11:57.701609+05:30	7	૧૭ ફેબૃઅરી યુવક સભા	2	[]	10	65
174	2022-02-15 18:09:42.953574+05:30	7	૧૭ ફેબૃઅરી યુવક સભા	2	[]	10	65
176	2022-02-15 18:38:23.497564+05:30	8	17 ફેબ્રુવારી યુવક સભા	1	[{"added": {}}]	10	65
178	2022-02-15 18:39:00.881376+05:30	118	17 ફેબ્રુવારી યુવક સભા	2	[{"changed": {"fields": ["Status", "Coming"]}}]	11	35
180	2022-02-15 18:40:16.352873+05:30	8	17 ફેબ્રુવારી યુવક સભા	2	[]	10	65
171	2022-02-15 17:10:31.163462+05:30	7	૧૭ ફેબૃઅરી યુવક સભા	1	[{"added": {}}]	10	65
173	2022-02-15 18:08:56.556733+05:30	100	૧૭ ફેબૃઅરી યુવક સભા	2	[{"changed": {"fields": ["Status", "Coming", "How"]}}]	11	65
175	2022-02-15 18:37:46.489811+05:30	7	૧૭ ફેબૃઅરી યુવક સભા	3		10	65
177	2022-02-15 18:38:28.678429+05:30	8	17 ફેબ્રુવારી યુવક સભા	2	[]	10	65
179	2022-02-15 18:39:07.564732+05:30	8	17 ફેબ્રુવારી યુવક સભા	2	[]	10	65
138	2022-02-12 19:50:40.634378+05:30	14	Yuvak sabha  12 Feb	2	[{"changed": {"fields": ["Status", "Present"]}}]	11	35
168	2022-02-15 17:05:02.276725+05:30	23	admin	3		4	65
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	Yuvak	yuvakprofile
8	SamparkKarykar	karyakarprofile
9	Mandal	mandalprofile
10	Mandal	karyakram
11	FolloWUp	followup
12	Yuvak	satsangprofile
13	FolloWUp	attandance
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-01-26 20:22:50.633025+05:30
2	auth	0001_initial	2022-01-26 20:22:50.809026+05:30
3	admin	0001_initial	2022-01-26 20:22:50.843024+05:30
4	admin	0002_logentry_remove_auto_add	2022-01-26 20:22:50.852023+05:30
5	admin	0003_logentry_add_action_flag_choices	2022-01-26 20:22:50.859025+05:30
6	contenttypes	0002_remove_content_type_name	2022-01-26 20:22:50.881022+05:30
7	auth	0002_alter_permission_name_max_length	2022-01-26 20:22:50.894025+05:30
8	auth	0003_alter_user_email_max_length	2022-01-26 20:22:50.904026+05:30
9	auth	0004_alter_user_username_opts	2022-01-26 20:22:50.911023+05:30
10	auth	0005_alter_user_last_login_null	2022-01-26 20:22:50.920022+05:30
11	auth	0006_require_contenttypes_0002	2022-01-26 20:22:50.922023+05:30
12	auth	0007_alter_validators_add_error_messages	2022-01-26 20:22:50.930024+05:30
13	auth	0008_alter_user_username_max_length	2022-01-26 20:22:50.947025+05:30
14	auth	0009_alter_user_last_name_max_length	2022-01-26 20:22:50.957023+05:30
15	auth	0010_alter_group_name_max_length	2022-01-26 20:22:50.969024+05:30
16	auth	0011_update_proxy_permissions	2022-01-26 20:22:50.977024+05:30
17	auth	0012_alter_user_first_name_max_length	2022-01-26 20:22:50.987027+05:30
18	sessions	0001_initial	2022-01-26 20:22:51.005026+05:30
19	Yuvak	0001_initial	2022-02-01 10:19:43.392643+05:30
20	Yuvak	0002_alter_yuvakprofile_addressline1_and_more	2022-02-01 10:28:21.813059+05:30
21	Yuvak	0003_rename_firstname_yuvakprofile_firstname	2022-02-01 10:30:14.574777+05:30
22	SamparkKarykar	0001_initial	2022-02-02 22:56:41.776864+05:30
23	SamparkKarykar	0002_alter_karyakarprofile_yuvaks	2022-02-02 23:03:41.809753+05:30
24	Mandal	0001_initial	2022-02-03 23:04:03.722293+05:30
25	Yuvak	0002_yuvakprofile_mandal	2022-02-03 23:04:03.760397+05:30
26	SamparkKarykar	0002_karyakarprofile_mandal_alter_karyakarprofile_yuvaks	2022-02-03 23:04:03.788548+05:30
27	Mandal	0002_karyakram	2022-02-03 23:04:03.825494+05:30
28	FolloWUp	0001_initial	2022-02-03 23:04:03.885855+05:30
29	Mandal	0003_karyakram_karyakram_date	2022-02-04 22:57:54.593674+05:30
30	SamparkKarykar	0003_alter_karyakarprofile_user	2022-02-04 23:20:31.721785+05:30
31	Mandal	0004_alter_karyakram_mandal	2022-02-05 16:35:06.786774+05:30
32	FolloWUp	0002_followup_status	2022-02-05 21:52:03.463729+05:30
33	Mandal	0005_mandalprofile_nirikshak_mandalprofile_sanchalak	2022-02-06 20:01:29.049506+05:30
34	Yuvak	0003_remove_yuvakprofile_addressline1_and_more	2022-02-06 20:22:58.00112+05:30
35	Yuvak	0004_alter_yuvakprofile_area_alter_yuvakprofile_houseno_and_more	2022-02-06 20:23:30.41713+05:30
36	Yuvak	0005_yuvakprofile_dateofbirth_yuvakprofile_education_and_more	2022-02-06 21:14:28.063616+05:30
37	Yuvak	0006_satsangprofile	2022-02-06 21:28:10.561107+05:30
38	Yuvak	0007_alter_yuvakprofile_user	2022-02-06 21:41:58.045444+05:30
39	SamparkKarykar	0004_remove_karyakarprofile_user	2022-02-06 22:36:15.502526+05:30
40	Yuvak	0008_alter_satsangprofile_athvadiksabha_and_more	2022-02-08 17:06:14.749146+05:30
41	Yuvak	0009_alter_yuvakprofile_area_alter_yuvakprofile_houseno_and_more	2022-02-10 14:05:22.55702+05:30
42	Yuvak	0010_csvtest	2022-02-10 14:12:33.688823+05:30
43	Yuvak	0011_csvtest	2022-02-10 14:14:24.628166+05:30
44	Yuvak	0012_csvtest	2022-02-10 14:18:49.455222+05:30
45	Yuvak	0013_csvtest	2022-02-10 14:21:43.598293+05:30
46	Yuvak	0014_csvtest	2022-02-10 14:27:59.226123+05:30
47	Yuvak	0015_csvtest	2022-02-10 15:12:13.252515+05:30
48	FolloWUp	0003_followup_present	2022-02-11 16:51:18.338118+05:30
49	SamparkKarykar	0005_rename_profile_karyakarprofile_karykar1profile	2022-02-11 16:51:18.491252+05:30
50	SamparkKarykar	0006_karyakarprofile_karykar2profile_and_more	2022-02-11 16:51:18.566821+05:30
51	Yuvak	0015_alter_yuvakprofile_mandal	2022-02-11 16:51:18.590326+05:30
52	FolloWUp	0004_rename_samparkkarykar_followup_karykarvrund	2022-02-11 18:17:42.072643+05:30
53	SamparkKarykar	0007_alter_karyakarprofile_options	2022-02-11 18:17:42.100643+05:30
54	FolloWUp	0005_alter_followup_present	2022-02-12 18:31:28.107348+05:30
55	FolloWUp	0006_alter_followup_present	2022-02-12 18:32:44.37746+05:30
56	FolloWUp	0007_rename_present_followup_coming	2022-02-13 22:12:39.265354+05:30
57	FolloWUp	0008_followup_present	2022-02-13 22:29:02.27529+05:30
58	FolloWUp	0009_attandance	2022-02-14 13:21:27.334349+05:30
59	Mandal	0006_rename_for_all_karyakram_start_folloup	2022-02-14 13:21:27.394348+05:30
60	Mandal	0007_rename_is_active_karyakram_start_attandance	2022-02-14 13:28:52.628002+05:30
61	Mandal	0008_karyakram_isdone_alter_karyakram_end_date_and_more	2022-02-15 18:02:57.433547+05:30
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
b1xydk7c1g3hamwntr48i7pgigpu6sg0	.eJxVjEEOgjAQRe_StWmY2g7WpXvOQKYzg6CmTSisjHcXEha6_e-9_zY9rcvYr1XnfhJzNWBOv1sifmregTwo34vlkpd5SnZX7EGr7Yro63a4fwcj1XGrfTNI4LaBEB2ABuQWkqIMF2pd5CCoZwHnMW2owYjiUSIweSXvIJnPF9NcN50:1nCjgL:o1u6xLbKGVUe6GG1PeQtYkMC2eLYbdkNrG6laZjphm4	2022-02-09 20:23:57.216044+05:30
5hwhx3lavcoqivrb9tuh9huv6w5t2lrh	.eJxVjEEOgjAQRe_StWmY2g7WpXvOQKYzg6CmTSisjHcXEha6_e-9_zY9rcvYr1XnfhJzNWBOv1sifmregTwo34vlkpd5SnZX7EGr7Yro63a4fwcj1XGrfTNI4LaBEB2ABuQWkqIMF2pd5CCoZwHnMW2owYjiUSIweSXvIJnPF9NcN50:1nEkzr:I_f82zHb71T_sWcNgm6-wq9JtwrsOXli1POawTi98RY	2022-02-15 10:12:27.610404+05:30
ss0yp6polbczt7alh34vvkj4e1k840re	.eJxVjEEOwiAQRe_C2pCOAwIu3XsGMjCDVA1NSrsy3l2bdKHb_977LxVpXWpcu8xxZHVW4NThd0yUH9I2wndqt0nnqS3zmPSm6J12fZ1Ynpfd_Tuo1Ou3TiYksJY95-L4mMUAMpUgYNglgjJkSESICIgSCrFzkh3SqfjBglfvDzTROO0:1nGlPz:6TRrKWG7SC9iEB2AqHl1ekMvsUWs-hRHxZYGaGSpdgg	2022-02-20 23:03:43.138494+05:30
z19f4eqxbrkuj15p0zywvkv1481pb8ht	.eJxVjEEOwiAQRe_C2pCOAwIu3XsGMjCDVA1NSrsy3l2bdKHb_977LxVpXWpcu8xxZHVW4NThd0yUH9I2wndqt0nnqS3zmPSm6J12fZ1Ynpfd_Tuo1Ou3TiYksJY95-L4mMUAMpUgYNglgjJkSESICIgSCrFzkh3SqfjBglfvDzTROO0:1nGlRw:wIm8myCoMRf1xki3JKLXWQGf8jKzr4TvZvaGIw198e0	2022-02-20 23:05:44.054473+05:30
le5bnbhzdzaecaltma1lmzh64cj2p4kc	.eJxVjEEOgjAQRe_StWmY2g7WpXvOQKYzg6CmTSisjHcXEha6_e-9_zY9rcvYr1XnfhJzNWBOv1sifmregTwo34vlkpd5SnZX7EGr7Yro63a4fwcj1XGrfTNI4LaBEB2ABuQWkqIMF2pd5CCoZwHnMW2owYjiUSIweSXvIJnPF9NcN50:1nGlbZ:8azuH9kkxseH8kp8gtqHUCy57V2RAPumA8BggYyafe8	2022-02-20 23:15:41.12247+05:30
zuk1d2l7j6abq9u5yrpsef5q5fqt9g0c	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nHPbB:0a4HrXdyIIQ9eHl2pALf2PKg8G3xod_h_4v5PiXDtbM	2022-02-22 17:57:57.533993+05:30
5b16hrefru5hifyv1h02too6esbsjzxj	.eJxVjEEOgjAQRe_StWmY2g7WpXvOQKYzg6CmTSisjHcXEha6_e-9_zY9rcvYr1XnfhJzNWBOv1sifmregTwo34vlkpd5SnZX7EGr7Yro63a4fwcj1XGrfTNI4LaBEB2ABuQWkqIMF2pd5CCoZwHnMW2owYjiUSIweSXvIJnPF9NcN50:1nFF72:4GbbafeuLNEKnerVoS_vqQ-jVI7d7UIloeNfLOFHlqk	2022-02-16 18:21:52.142504+05:30
s1abhayijwi0bpf5cy3gjngwv7k1p8xf	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nI4qQ:k1VDMQdFiXEbBEsjunrr6mYmAGW17LESVlNJy-7cpRk	2022-02-24 14:00:26.43881+05:30
4k5i08blvr57kl595cpsbvaalua47u81	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nIUgJ:dGtPndMHa44zyhZDOvXN7zjOMknlDAhX0RHKS_f51qw	2022-02-25 17:35:43.30487+05:30
knpmm8grv89ydf49yv4jle6min58lhl1	.eJxVjEEOgjAQRe_StWmY2g7WpXvOQKYzg6CmTSisjHcXEha6_e-9_zY9rcvYr1XnfhJzNWBOv1sifmregTwo34vlkpd5SnZX7EGr7Yro63a4fwcj1XGrfTNI4LaBEB2ABuQWkqIMF2pd5CCoZwHnMW2owYjiUSIweSXvIJnPF9NcN50:1nFJRG:BQOgvECEiZr5yoSvLpS5MVhLZ-glA4b0DB20AGWJaRA	2022-02-16 22:59:02.299005+05:30
3nmtr0327o66ywjeh9zjwdmf04vhyhdh	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nIUoh:1gnsb408nMFsbVXIapMjzE7oxC_5BcnOGNu4Llb5_H0	2022-02-25 17:44:23.968646+05:30
jcm7ywqhrcuoqmjj4pu5n3vhzu34sinj	.eJxVjEEOgjAQRe_StWmY2g7WpXvOQKYzg6CmTSisjHcXEha6_e-9_zY9rcvYr1XnfhJzNWBOv1sifmregTwo34vlkpd5SnZX7EGr7Yro63a4fwcj1XGrfTNI4LaBEB2ABuQWkqIMF2pd5CCoZwHnMW2owYjiUSIweSXvIJnPF9NcN50:1nFg0I:5aVx0hr7-HJK2xqZ3aI-9KXIEqcSuF1G5b1HVrQApaU	2022-02-17 23:04:42.836687+05:30
tcyf8nk5p5mwhi62rpbkh87z324z9hjo	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nIV20:6p2G5VGxjdhdlcsPUGOJb4VNqlAAhhTj3vynPSig7Lg	2022-02-25 17:58:08.246667+05:30
ywmtu33l1xv87caa7sm0uqbjwb3uls67	.eJxVjEEOgjAQRe_StWmY2g7WpXvOQKYzg6CmTSisjHcXEha6_e-9_zY9rcvYr1XnfhJzNWBOv1sifmregTwo34vlkpd5SnZX7EGr7Yro63a4fwcj1XGrfTNI4LaBEB2ABuQWkqIMF2pd5CCoZwHnMW2owYjiUSIweSXvIJnPF9NcN50:1nFuMI:OUV_xCOlzT47P0gx_egmSL8OEhSnllEtq8QGcsZ2JEI	2022-02-18 14:24:22.66646+05:30
l58bmsjadxujl4logz5o79bawxtz2agr	.eJxVjDsOwjAQBe_iGln-YSeU9DmDtWvv4gCypTipEHeHSCmgfTPzXiLCtpa4dVrinMVFOHH63RDSg-oO8h3qrcnU6rrMKHdFHrTLqWV6Xg_376BAL99ajT54No5tUKwsDWmwPrhstQYV2DIZRdoZO4YUABEMAyZvyOMZlfPi_QHGDDeX:1nFuN4:AXsZ4-xPuDTJj3Irtz2b9G7fKbc2qTnC68YrcIcWSes	2022-02-18 14:25:10.446097+05:30
bk15c126ge004lllbm9dlmvx793sm0ou	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nIVC1:mTDN1jeBNQ3VMpSua5713LVXeEU6uvpoOBY4C61OvDI	2022-02-25 18:08:29.379249+05:30
g4ghwtaxki3yj4l0qpza4m8wh7cwbqeq	.eJxVjDsOwjAQRO_iGln-xpiSnjNY6901DiBHipMKcXcSKQUU08x7M2-RYF1qWjvPaSRxEUacfrsM-OS2A3pAu08Sp7bMY5a7Ig_a5W0ifl0P9--gQq_bOlIoGE2JAdCDR8PR2JK1AlBBR6LzoKxCAixbjCvsNLvgabBkUTnx-QIGdzi3:1nFvBl:BlvEoBL_njGx8JeGFZWtMKwAptXLKbWuYdb8HZkw6k4	2022-02-18 15:17:33.31214+05:30
9vipl623nfvu4cdzkn3x7btkt60bmtpx	.eJxVjEEOgjAQRe_StWmY2g7WpXvOQKYzg6CmTSisjHcXEha6_e-9_zY9rcvYr1XnfhJzNWBOv1sifmregTwo34vlkpd5SnZX7EGr7Yro63a4fwcj1XGrfTNI4LaBEB2ABuQWkqIMF2pd5CCoZwHnMW2owYjiUSIweSXvIJnPF9NcN50:1nG2ab:B9sJPlMY73Drfwg2GK-rvvqeDpGC9mLGo-XsT7elInM	2022-02-18 23:11:41.678386+05:30
l1uuyyu93tm1azpg25wgaoju9fu7si60	.eJxVjEEOgjAQRe_StWmY2g7WpXvOQKYzg6CmTSisjHcXEha6_e-9_zY9rcvYr1XnfhJzNWBOv1sifmregTwo34vlkpd5SnZX7EGr7Yro63a4fwcj1XGrfTNI4LaBEB2ABuQWkqIMF2pd5CCoZwHnMW2owYjiUSIweSXvIJnPF9NcN50:1nGfAS:Dl93I-_pMd26F30gE9xSBpFVtBx4XPLX3O8VebeE1o4	2022-02-20 16:23:16.659893+05:30
8s8vf491havgezc57pvakgrnvkpro1yj	.eJxVjDsOwjAQRO_iGln-xpiSnjNY6901DiBHipMKcXcSKQUU08x7M2-RYF1qWjvPaSRxEUacfrsM-OS2A3pAu08Sp7bMY5a7Ig_a5W0ifl0P9--gQq_bOlIoGE2JAdCDR8PR2JK1AlBBR6LzoKxCAixbjCvsNLvgabBkUTnx-QIGdzi3:1nGfB3:5rq6QfyTZ1KNS8EjaFmsxJORcMnUC5amiP_0XXTG9So	2022-02-20 16:23:53.682299+05:30
aycv9nrfgehy0jy7yganpqrojahu1c7b	.eJxVjMsOwiAQRf-FtSEMhJdL934DmWFAqoYmpV0Z_12bdKHbe865L5FwW1vaRlnSxOIsIIrT70iYH6XvhO_Yb7PMc1-XieSuyIMOeZ25PC-H-3fQcLRvXUwANpbBUwjOakXWxpwDk6vgXSSTMxYDxljvsXpWVXsGABU0QrDi_QH9bjd5:1nImum:YKA3_y19dNz9QBMNI3jqWZlDQmN2mDyKj3sX8N1UIZA	2022-02-26 13:03:52.105229+05:30
owghb2kqrw0fcgniuhaxm3y7j00qm37n	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nIs7i:GtQMp6aSNecO8h8cTidSAw5BOgw_O4h6ccRoL-2E3AM	2022-02-26 18:37:34.781152+05:30
j1cbp2o3jn4792ya4wdwhd1dhgj4ig5i	.eJxVjDsOwjAQBe_iGln4v6GkzxmstdeLA8iW8qkQd4dIKaB9M_NeIuK21rgtZY4TiYuwgzj9jgnzo7Sd0B3brcvc2zpPSe6KPOgix07leT3cv4OKS_3WHi0NxqLLxg1MQaWzSuyN8kFbTmAJfCEANACgHHvNOjjNORFrYi_eHwNVOCg:1nItKM:IiKYrvy6v7I2iLjlpi6lJdu91FDwaL8WQfDO-nwTx30	2022-02-26 19:54:42.243745+05:30
nrn3mhdrgwujnnfrskngyia005ix8s6k	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nJ8C2:vQzndICjSaVJnfFA5twbx81AdpJyfQ9hD1m3gnM3c9U	2022-02-27 11:47:06.551356+05:30
etsrbg9fkgexybdazilhyt3rxm9bvqmq	.eJxVjMsOwiAQRf-FtSE8OkVcuvcbyDADUjWQlHZl_HdD0oVu7znnvkXAfSth72kNC4uLsCBOv2NEeqY6CD-w3pukVrd1iXIo8qBd3hqn1_Vw_w4K9jJq623SNvEMEZynnAHOmmJykwOlsteKojM0gSfWxmhCNTsHjF5xBBSfLwfaOAU:1nJHuc:iOaiSrshrbeQ06c1K-xc2wl-XnKqODatTHQVmTJrfzY	2022-02-27 22:09:46.083406+05:30
f3jcquqv6k2hj7jl243rhqaj3zb52myk	.eJxVjDsOwjAQBe_iGln4v6GkzxmstdeLA8iW8qkQd4dIKaB9M_NeIuK21rgtZY4TiYuwgzj9jgnzo7Sd0B3brcvc2zpPSe6KPOgix07leT3cv4OKS_3WHi0NxqLLxg1MQaWzSuyN8kFbTmAJfCEANACgHHvNOjjNORFrYi_eHwNVOCg:1nJ9zH:E2h2JUBaVioXvN32FzL_e5MxJH1FhggInq4CGY_5OfA	2022-02-27 13:42:03.117436+05:30
nrjvblv7t7fyde67tevhbqbfza6ywaew	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nJeqg:4s0m90jAEOgelIFHn0UJ9eYRKGj66_kNAOWMN-yl99Y	2022-02-28 22:39:14.38022+05:30
0d051cn7fu1ynlaqsb4qnk0oga4p4q2y	.eJxVjDsOwjAQBe_iGln4v6GkzxmstdeLA8iW8qkQd4dIKaB9M_NeIuK21rgtZY4TiYuwgzj9jgnzo7Sd0B3brcvc2zpPSe6KPOgix07leT3cv4OKS_3WHi0NxqLLxg1MQaWzSuyN8kFbTmAJfCEANACgHHvNOjjNORFrYi_eHwNVOCg:1nJsLf:RVwP0F26d1muoHSsdtb0XGhDSxynLB2FBbkC3W2PlRc	2022-03-01 13:04:07.817848+05:30
6boferg40a1y3mccwtz9invncu2tgiw8	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nJWHQ:DE5Ib7aSFBbf5zB4EGq0eMFmYo18OjgSRBNenXpSrBM	2022-02-28 13:30:16.966025+05:30
0es39br46cbwmmt8rjn2y7s7riyq8ibk	.eJxVjDsOwjAQBe_iGln4v6GkzxmstdeLA8iW8qkQd4dIKaB9M_NeIuK21rgtZY4TiYuwgzj9jgnzo7Sd0B3brcvc2zpPSe6KPOgix07leT3cv4OKS_3WHi0NxqLLxg1MQaWzSuyN8kFbTmAJfCEANACgHHvNOjjNORFrYi_eHwNVOCg:1nJerP:9_hgBwmrYCjvkcDR41wc6re5DGgR9QY0Zl8VtynhON0	2022-02-28 22:39:59.969618+05:30
gekc0l89506jdbr96wew7h2ua5vdeqfw	.eJxVjEEOwiAQRe_C2hAoDB1cuvcMZIYhUjU0Ke3KeHdt0oVu_3vvv1Siba1p62VJk6izCqBOvyNTfpS2E7lTu806z21dJta7og_a9XWW8rwc7t9BpV6_NZGNwTAD8kgReUAo1nlvvBliCdFlcF7AiBOMvoALlAPYjCMRYjTq_QHvZDcl:1nJw6Q:qjj7eXjpEh6_aTgXSSeopGpMG55xZgm8iSg77VIanew	2022-03-01 17:04:38.485873+05:30
2kqk0bvbtiztx8ull3g1glscndwok7nx	.eJxVjMsOwiAQRf-FtSE8OkVcuvcbyDADUjWQlHZl_HdD0oVu7znnvkXAfSth72kNC4uLsCBOv2NEeqY6CD-w3pukVrd1iXIo8qBd3hqn1_Vw_w4K9jJq623SNvEMEZynnAHOmmJykwOlsteKojM0gSfWxmhCNTsHjF5xBBSfLwfaOAU:1nJxZX:but_IUQHAlEOOOKmsgTkwZ5KoTJyftjkmJEZbGOeL6U	2022-03-01 18:38:47.926078+05:30
gemodqw7p6qmx6h7lh2x9rddizc4d2j4	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nJWM7:kyvMMBNeNSRGAZfpRSZtcQLRMfrmvq8trH9pC_x-AM8	2022-02-28 13:35:07.961628+05:30
df4g4k75672euhbms61ukgtlhxa6fjcf	.eJxVjEEOwiAQRe_C2hBmoLS4dO8ZyMAMUjVtUtqV8e7apAvd_vfef6lI21rj1mSJI6uzQqtOv2Oi_JBpJ3yn6TbrPE_rMia9K_qgTV9nluflcP8OKrX6rS0zEfboEICEpffBYPaSEjrwpZNBrE_sgoXSDQhsAKwpBAGBsinq_QELJTfh:1nJsLJ:MfBB_hV3LFTKaRX2gdVFlRDbKV2TdggG6vJxbWDUF_o	2022-03-01 13:03:45.884723+05:30
\.


--
-- Name: FolloWUp_followup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."FolloWUp_followup_id_seq"', 137, true);


--
-- Name: Mandal_karyakram_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Mandal_karyakram_id_seq"', 8, true);


--
-- Name: Mandal_mandalprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Mandal_mandalprofile_id_seq"', 1, true);


--
-- Name: SamparkKarykar_karyakarprofile_Yuvaks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."SamparkKarykar_karyakarprofile_Yuvaks_id_seq"', 14, true);


--
-- Name: SamparkKarykar_karyakarprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."SamparkKarykar_karyakarprofile_id_seq"', 9, true);


--
-- Name: Yuvak_satsangprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Yuvak_satsangprofile_id_seq"', 56, true);


--
-- Name: Yuvak_yuvakprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Yuvak_yuvakprofile_id_seq"', 49, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 33, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 63, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 65, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 180, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 61, true);


--
-- Name: FolloWUp_followup FolloWUp_followup_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FolloWUp_followup"
    ADD CONSTRAINT "FolloWUp_followup_pkey" PRIMARY KEY (id);


--
-- Name: Mandal_karyakram Mandal_karyakram_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Mandal_karyakram"
    ADD CONSTRAINT "Mandal_karyakram_pkey" PRIMARY KEY (id);


--
-- Name: Mandal_mandalprofile Mandal_mandalprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Mandal_mandalprofile"
    ADD CONSTRAINT "Mandal_mandalprofile_pkey" PRIMARY KEY (id);


--
-- Name: SamparkKarykar_karyakarprofile_Yuvaks SamparkKarykar_karyakarp_karyakarprofile_id_yuvak_da8f586a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile_Yuvaks"
    ADD CONSTRAINT "SamparkKarykar_karyakarp_karyakarprofile_id_yuvak_da8f586a_uniq" UNIQUE (karyakarprofile_id, yuvakprofile_id);


--
-- Name: SamparkKarykar_karyakarprofile_Yuvaks SamparkKarykar_karyakarprofile_Yuvaks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile_Yuvaks"
    ADD CONSTRAINT "SamparkKarykar_karyakarprofile_Yuvaks_pkey" PRIMARY KEY (id);


--
-- Name: SamparkKarykar_karyakarprofile SamparkKarykar_karyakarprofile_karykar2profile_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile"
    ADD CONSTRAINT "SamparkKarykar_karyakarprofile_karykar2profile_id_key" UNIQUE (karykar2profile_id);


--
-- Name: SamparkKarykar_karyakarprofile SamparkKarykar_karyakarprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile"
    ADD CONSTRAINT "SamparkKarykar_karyakarprofile_pkey" PRIMARY KEY (id);


--
-- Name: SamparkKarykar_karyakarprofile SamparkKarykar_karyakarprofile_profile_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile"
    ADD CONSTRAINT "SamparkKarykar_karyakarprofile_profile_id_key" UNIQUE (karykar1profile_id);


--
-- Name: Yuvak_satsangprofile Yuvak_satsangprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Yuvak_satsangprofile"
    ADD CONSTRAINT "Yuvak_satsangprofile_pkey" PRIMARY KEY (id);


--
-- Name: Yuvak_satsangprofile Yuvak_satsangprofile_yuvakProfile_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Yuvak_satsangprofile"
    ADD CONSTRAINT "Yuvak_satsangprofile_yuvakProfile_id_key" UNIQUE ("yuvakProfile_id");


--
-- Name: Yuvak_yuvakprofile Yuvak_yuvakprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Yuvak_yuvakprofile"
    ADD CONSTRAINT "Yuvak_yuvakprofile_pkey" PRIMARY KEY (id);


--
-- Name: Yuvak_yuvakprofile Yuvak_yuvakprofile_user_id_229f4079_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Yuvak_yuvakprofile"
    ADD CONSTRAINT "Yuvak_yuvakprofile_user_id_229f4079_uniq" UNIQUE (user_id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: FolloWUp_followup_Karyakram_id_6e6023a5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "FolloWUp_followup_Karyakram_id_6e6023a5" ON public."FolloWUp_followup" USING btree ("Karyakram_id");


--
-- Name: FolloWUp_followup_SamparkKarykar_id_5c499db3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "FolloWUp_followup_SamparkKarykar_id_5c499db3" ON public."FolloWUp_followup" USING btree ("KaryKarVrund_id");


--
-- Name: FolloWUp_followup_Yuvak_id_f99991a5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "FolloWUp_followup_Yuvak_id_f99991a5" ON public."FolloWUp_followup" USING btree ("Yuvak_id");


--
-- Name: Mandal_karyakram_Mandal_id_370ad199; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Mandal_karyakram_Mandal_id_370ad199" ON public."Mandal_karyakram" USING btree ("Mandal_id");


--
-- Name: Mandal_mandalprofile_Nirikshak_id_19759718; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Mandal_mandalprofile_Nirikshak_id_19759718" ON public."Mandal_mandalprofile" USING btree ("Nirikshak_id");


--
-- Name: Mandal_mandalprofile_Sanchalak_id_408fe89e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Mandal_mandalprofile_Sanchalak_id_408fe89e" ON public."Mandal_mandalprofile" USING btree ("Sanchalak_id");


--
-- Name: SamparkKarykar_karyakarpro_karyakarprofile_id_e3ff760e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "SamparkKarykar_karyakarpro_karyakarprofile_id_e3ff760e" ON public."SamparkKarykar_karyakarprofile_Yuvaks" USING btree (karyakarprofile_id);


--
-- Name: SamparkKarykar_karyakarprofile_Yuvaks_yuvakprofile_id_f2c45bff; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "SamparkKarykar_karyakarprofile_Yuvaks_yuvakprofile_id_f2c45bff" ON public."SamparkKarykar_karyakarprofile_Yuvaks" USING btree (yuvakprofile_id);


--
-- Name: SamparkKarykar_karyakarprofile_mandal_id_45b77139; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "SamparkKarykar_karyakarprofile_mandal_id_45b77139" ON public."SamparkKarykar_karyakarprofile" USING btree (mandal_id);


--
-- Name: Yuvak_yuvakprofile_WhatsappNo_8fcab33c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Yuvak_yuvakprofile_WhatsappNo_8fcab33c" ON public."Yuvak_yuvakprofile" USING btree ("WhatsappNo");


--
-- Name: Yuvak_yuvakprofile_WhatsappNo_8fcab33c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Yuvak_yuvakprofile_WhatsappNo_8fcab33c_like" ON public."Yuvak_yuvakprofile" USING btree ("WhatsappNo" varchar_pattern_ops);


--
-- Name: Yuvak_yuvakprofile_mandal_id_cd689d21; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Yuvak_yuvakprofile_mandal_id_cd689d21" ON public."Yuvak_yuvakprofile" USING btree (mandal_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: FolloWUp_followup FolloWUp_followup_KaryKarVrund_id_785b4b14_fk_SamparkKa; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FolloWUp_followup"
    ADD CONSTRAINT "FolloWUp_followup_KaryKarVrund_id_785b4b14_fk_SamparkKa" FOREIGN KEY ("KaryKarVrund_id") REFERENCES public."SamparkKarykar_karyakarprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: FolloWUp_followup FolloWUp_followup_Karyakram_id_6e6023a5_fk_Mandal_karyakram_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FolloWUp_followup"
    ADD CONSTRAINT "FolloWUp_followup_Karyakram_id_6e6023a5_fk_Mandal_karyakram_id" FOREIGN KEY ("Karyakram_id") REFERENCES public."Mandal_karyakram"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: FolloWUp_followup FolloWUp_followup_Yuvak_id_f99991a5_fk_Yuvak_yuvakprofile_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."FolloWUp_followup"
    ADD CONSTRAINT "FolloWUp_followup_Yuvak_id_f99991a5_fk_Yuvak_yuvakprofile_id" FOREIGN KEY ("Yuvak_id") REFERENCES public."Yuvak_yuvakprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Mandal_karyakram Mandal_karyakram_Mandal_id_370ad199_fk_Mandal_mandalprofile_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Mandal_karyakram"
    ADD CONSTRAINT "Mandal_karyakram_Mandal_id_370ad199_fk_Mandal_mandalprofile_id" FOREIGN KEY ("Mandal_id") REFERENCES public."Mandal_mandalprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Mandal_mandalprofile Mandal_mandalprofile_Nirikshak_id_19759718_fk_Yuvak_yuv; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Mandal_mandalprofile"
    ADD CONSTRAINT "Mandal_mandalprofile_Nirikshak_id_19759718_fk_Yuvak_yuv" FOREIGN KEY ("Nirikshak_id") REFERENCES public."Yuvak_yuvakprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Mandal_mandalprofile Mandal_mandalprofile_Sanchalak_id_408fe89e_fk_Yuvak_yuv; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Mandal_mandalprofile"
    ADD CONSTRAINT "Mandal_mandalprofile_Sanchalak_id_408fe89e_fk_Yuvak_yuv" FOREIGN KEY ("Sanchalak_id") REFERENCES public."Yuvak_yuvakprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SamparkKarykar_karyakarprofile_Yuvaks SamparkKarykar_karya_karyakarprofile_id_e3ff760e_fk_SamparkKa; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile_Yuvaks"
    ADD CONSTRAINT "SamparkKarykar_karya_karyakarprofile_id_e3ff760e_fk_SamparkKa" FOREIGN KEY (karyakarprofile_id) REFERENCES public."SamparkKarykar_karyakarprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SamparkKarykar_karyakarprofile SamparkKarykar_karya_karykar1profile_id_87c145ee_fk_Yuvak_yuv; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile"
    ADD CONSTRAINT "SamparkKarykar_karya_karykar1profile_id_87c145ee_fk_Yuvak_yuv" FOREIGN KEY (karykar1profile_id) REFERENCES public."Yuvak_yuvakprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SamparkKarykar_karyakarprofile SamparkKarykar_karya_karykar2profile_id_b2fcd367_fk_Yuvak_yuv; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile"
    ADD CONSTRAINT "SamparkKarykar_karya_karykar2profile_id_b2fcd367_fk_Yuvak_yuv" FOREIGN KEY (karykar2profile_id) REFERENCES public."Yuvak_yuvakprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SamparkKarykar_karyakarprofile SamparkKarykar_karya_mandal_id_45b77139_fk_Mandal_ma; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile"
    ADD CONSTRAINT "SamparkKarykar_karya_mandal_id_45b77139_fk_Mandal_ma" FOREIGN KEY (mandal_id) REFERENCES public."Mandal_mandalprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SamparkKarykar_karyakarprofile_Yuvaks SamparkKarykar_karya_yuvakprofile_id_f2c45bff_fk_Yuvak_yuv; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SamparkKarykar_karyakarprofile_Yuvaks"
    ADD CONSTRAINT "SamparkKarykar_karya_yuvakprofile_id_f2c45bff_fk_Yuvak_yuv" FOREIGN KEY (yuvakprofile_id) REFERENCES public."Yuvak_yuvakprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Yuvak_satsangprofile Yuvak_satsangprofile_yuvakProfile_id_afd46976_fk_Yuvak_yuv; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Yuvak_satsangprofile"
    ADD CONSTRAINT "Yuvak_satsangprofile_yuvakProfile_id_afd46976_fk_Yuvak_yuv" FOREIGN KEY ("yuvakProfile_id") REFERENCES public."Yuvak_yuvakprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Yuvak_yuvakprofile Yuvak_yuvakprofile_mandal_id_cd689d21_fk_Mandal_ma; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Yuvak_yuvakprofile"
    ADD CONSTRAINT "Yuvak_yuvakprofile_mandal_id_cd689d21_fk_Mandal_ma" FOREIGN KEY (mandal_id) REFERENCES public."Mandal_mandalprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Yuvak_yuvakprofile Yuvak_yuvakprofile_user_id_229f4079_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Yuvak_yuvakprofile"
    ADD CONSTRAINT "Yuvak_yuvakprofile_user_id_229f4079_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

