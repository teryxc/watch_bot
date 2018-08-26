USER = 'postgres'
PASSWORD = 'furry621'
PORT = 5432
DB_NAME = 'watch_bot'
DEFAULT_DB_NAME = 'postgres'
CONNECTION_STRING = 'postgresql://{}:{}@localhost:{}/{}'

JOURNALS_SQL = '''CREATE TABLE public.journals
(
    "user" character varying(255) COLLATE pg_catalog."default",
    "date" character varying(255) COLLATE pg_catalog."default",
    "id" bigint NOT NULL,
    "title" character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT journals_pkey PRIMARY KEY ("id")
)'''