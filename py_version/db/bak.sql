create table file_finger
(
    file_path   TEXT PRIMARY KEY NOT NULL,
    driver_name TEXT             NOT NULL,
    finger      TEXT             NOT NULL,
    created_at  TEXT             NOT NULL,
    updated_at  TEXT             NOT NULL
);

create index idx_finger on file_finger (finger);

.tables

.schema file_finger
