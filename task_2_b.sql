USE lab_3;

DROP PROCEDURE IF EXISTS insert_rows_in_menu_description;
DELIMITER //

CREATE PROCEDURE insert_rows_in_menu_description()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 10 DO
       INSERT INTO menu (description) VALUES (CONCAT('description', i));
       SET i = i + 1;
    END WHILE;
END //

DELIMITER ;

CALL insert_rows_in_menu_description();