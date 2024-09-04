CREATE DATABASE hotel_db;
USE hotel_db;

CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    guest_name VARCHAR(255),
    room_type VARCHAR(50),
    stay_duration INT
);
SELECT * FROM reservations;
DELETE FROM reservations WHERE id = 2;
