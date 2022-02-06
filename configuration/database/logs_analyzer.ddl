-- RDS: PostgreSQL.

-- Table: public.log

-- DROP TABLE IF EXISTS public.log;

CREATE TABLE IF NOT EXISTS public.log
(
    id serial,
    remote_addr inet,
    remote_user text COLLATE pg_catalog."default",
    time_local timestamp with time zone,
    request text COLLATE pg_catalog."default",
    status smallint,
    body_bytes_sent integer,
    http_referer text COLLATE pg_catalog."default",
    http_user_agent text COLLATE pg_catalog."default",
    CONSTRAINT log_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;
