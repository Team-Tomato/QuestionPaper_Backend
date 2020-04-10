CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS questionpaper (
	qpId uuid DEFAULT uuid_generate_v4(),
	subjectName TEXT,
	shortForm TEXT,
	staff TEXT,
	year INT,
	url TEXT
);