USE lab_3;

DROP PROCEDURE IF EXISTS insert_into_menu_description;
DELIMITER //
CREATE PROCEDURE insert_into_menu_description(
  IN description VARCHAR(45)
)
BEGIN
  INSERT INTO menu (description) VALUES (description);
END //
DELIMITER ;

CALL insert_into_menu_description("some description");