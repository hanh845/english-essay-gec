DROP TABLE IF EXISTS authors CASCADE;
DROP TABLE IF EXISTS documents CASCADE;
DROP TABLE IF EXISTS document_authors CASCADE;
DROP TABLE IF EXISTS lang_8 CASCADE;
DROP TABLE IF EXISTS document_versions CASCADE;
DROP TABLE IF EXISTS models CASCADE;
DROP TABLE IF EXISTS sentences CASCADE;
DROP TABLE IF EXISTS predictions CASCADE;


-- 1. Create table authors
CREATE TABLE IF NOT EXISTS authors (
    author_id UUID PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) UNIQUE,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
			

-- 2. Create table documents
CREATE TABLE IF NOT EXISTS documents (
    document_id UUID PRIMARY KEY,
	title TEXT,
	file_type VARCHAR(50),
	file_path TEXT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Create table document_authors
CREATE TABLE IF NOT EXISTS document_authors (
    document_id UUID REFERENCES documents(document_id),
	author_id UUID REFERENCES authors(author_id),
	PRIMARY KEY (document_id, author_id)
);					

-- 4. Create table Lang-8
CREATE TABLE IF NOT EXISTS lang_8 (
    id SERIAL PRIMARY KEY,
    source TEXT,
    target TEXT
);			
	
-- 5. Create table document_versions
CREATE TABLE IF NOT EXISTS document_versions (
    version_id UUID PRIMARY KEY,
	document_id UUID REFERENCES documents(document_id),
	extracted_text TEXT,
	extraction_method VARCHAR(100),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);		
			
--6. models	
CREATE TABLE IF NOT EXISTS models (
    model_id UUID PRIMARY KEY,
	model_name VARCHAR(255),
	version VARCHAR(50),
	accuracy FLOAT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 7. sentences
CREATE TABLE IF NOT EXISTS sentences (
    sentence_id UUID PRIMARY KEY,
	document_id UUID REFERENCES documents(document_id),
	version_id UUID REFERENCES document_versions(version_id),
	content TEXT,
	position INTEGER,
	is_clean BOOLEAN DEFAULT TRUE,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 8. predictions
CREATE TABLE IF NOT EXISTS predictions (
    prediction_id UUID PRIMARY KEY,
	sentence_id UUID REFERENCES sentences(sentence_id),
	model_id UUID REFERENCES models(model_id),
	label INTEGER,
	confidence FLOAT,
	original_text TEXT,
	corrected_text TEXT,
	error_type VARCHAR(100),
	predicted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- dump data
INSERT INTO authors (author_id, name, email, created_at)
VALUES ('11111111-1111-1111-1111-111111111111', 'Nguyen Van A', 'nguyenvana@gmail.com', CURRENT_TIMESTAMP),
	('22222222-2222-2222-2222-222222222222', 'Tran Thi B', 'tranthib@gmail.com', CURRENT_TIMESTAMP),
	('33333333-3333-3333-3333-333333333333', 'Le Van C', 'levanc@gmail.com', CURRENT_TIMESTAMP),
	('44444444-4444-4444-4444-444444444444', 'Pham Thi D', 'phamthid@gmail.com', CURRENT_TIMESTAMP),
	('55555555-5555-5555-5555-555555555555', 'Hoang Van E', 'hoangvane@gmail.com', CURRENT_TIMESTAMP);
