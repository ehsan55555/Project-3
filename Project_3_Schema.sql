-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/XRggwS
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- DROP TABLE IF EXISTS persons_table CASCADE;
-- DROP TABLE IF EXISTS crashes_table CASCADE;

SELECT * FROM crashes_table;
SELECT * FROM persons_table;

CREATE TABLE "crashes_table" (
    "collision_id" INT   NOT NULL,
    "crash_date" DATE   NOT NULL,
    "crash_time" VARCHAR(25)   NOT NULL,
    "borough" VARCHAR(45)   NOT NULL,
    "latitude" VARCHAR(25)   NOT NULL,
    "longitude" VARCHAR(25)   NOT NULL,
    CONSTRAINT "pk_crashes_table" PRIMARY KEY (
        "collision_id"
     )
);

CREATE TABLE "persons_table" (
    "collision_id" INT   NOT NULL,
    "persons_injured" INT   NOT NULL,
    "persons_killed" INT   NOT NULL,
    "pedestrians_injured" INT   NOT NULL,
    "pedestrians_killed" INT   NOT NULL,
    "cyclists_injured" INT   NOT NULL,
    "cyclists_killed" INT   NOT NULL,
    "motorists_injured" INT   NOT NULL,
    "motorists_killed" INT   NOT NULL,
    CONSTRAINT "pk_persons_table" PRIMARY KEY (
        "collision_id"
     )
);

ALTER TABLE "persons_table" ADD CONSTRAINT "fk_persons_table_collision_id" FOREIGN KEY("collision_id")
REFERENCES "crashes_table" ("collision_id");

