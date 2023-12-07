USE lab_3; 

DROP PROCEDURE IF EXISTS insert_into_menu_dish;
DELIMITER //

CREATE PROCEDURE insert_into_menu_dish (
    IN menu_description VARCHAR(45),
    IN dish_name VARCHAR(45)
)
BEGIN
    DECLARE menu_id INT;
    DECLARE dish_id INT;

    SELECT id INTO menu_id FROM menu WHERE description = menu_description;

    SELECT id INTO dish_id FROM dish WHERE name = dish_name;

    INSERT INTO menu_dish (menu_id, dish_id) VALUES (menu_id, dish_id);
END //

DELIMITER ;

CALL insert_into_menu_dish("some description","Spaghetti Bolognese");