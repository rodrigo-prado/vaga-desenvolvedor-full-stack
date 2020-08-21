#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
CREATE TABLE link (
  id      integer DEFAULT nextval(('link_id_seq'::text)::regclass)  NOT NULL,
  url     character varying(2048)                                   NOT NULL,
  tracked integer
);
EOSQL
