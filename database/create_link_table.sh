#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL

CREATE SEQUENCE link_id_seq
  START WITH 1
  INCREMENT BY 1
  NO MINVALUE
  NO MAXVALUE
  CACHE 1;

CREATE TABLE link (
  id      integer DEFAULT nextval(('link_id_seq'::text)::regclass)  NOT NULL,
  url     character varying(2048)                                   NOT NULL,
  tracked integer
);
EOSQL
