-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS extracurricular_activities_db;
USE extracurricular_activities_db;

-- Table for students
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    interests TEXT,
    talents TEXT,
    age INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for Activity Types
CREATE TABLE IF NOT EXISTS ActivityTypes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table for Clubs
CREATE TABLE IF NOT EXISTS Clubs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    activity_type_id INT,
    location VARCHAR(255),
    FOREIGN KEY (activity_type_id) REFERENCES ActivityTypes(id)
);

-- Inserting sample activity types if not already present
INSERT IGNORE INTO ActivityTypes (name) VALUES
    ('Sports'),
    ('Arts'),
    ('Music'),
    ('Dance');

-- Inserting sample clubs if not already present
INSERT IGNORE INTO Clubs (name, activity_type_id, location) VALUES
    ('Sports Academy', 1, 'Berlin'),
    ('Art Studio', 2, 'Berlin'),
    ('Music School', 3, 'Berlin');