USE lab_3;

DROP PROCEDURE IF EXISTS create_tables_from_column;
DROP VIEW IF EXISTS user_view;

DELIMITER //

CREATE PROCEDURE create_tables_from_column(
    IN custom_column_name VARCHAR(45),
    IN custom_table_name VARCHAR(45)
)
BEGIN
    DECLARE a INT DEFAULT 0;
    DECLARE b INT DEFAULT 0;
    DECLARE table_name VARCHAR(45);
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE num_columns INT;
    DECLARE column_list VARCHAR(255);
    DECLARE column_name VARCHAR(45);

    DECLARE zxcursor CURSOR FOR SELECT price FROM user_view;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET @query = CONCAT('CREATE OR REPLACE VIEW user_view AS SELECT ', custom_column_name, ' AS price FROM ', custom_table_name);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    OPEN zxcursor;
    my_loop: LOOP
        FETCH zxcursor INTO table_name;
        IF done THEN
            LEAVE my_loop;
        END IF;

        SET num_columns = FLOOR(1 + RAND() * 9);
    SELECT num_columns;
    SET column_list = '';
    WHILE b < num_columns DO
      SET column_name = CONCAT('column_', b + 1);
      SET column_list = CONCAT(column_list, column_name, ' INT ');
      IF b < num_columns - 1 THEN
        SET column_list = CONCAT(column_list, ', ');
      END IF;
      SET b = b + 1;
    END WHILE;
    SET b = 0;

        SET column_list = SUBSTRING(column_list, 1, LENGTH(column_list) - 1);

    SET @sql_query = CONCAT('CREATE TABLE IF NOT EXISTS ', table_name, '_', UNIX_TIMESTAMP(), ' (', column_list, ')');
    PREPARE stmt FROM @sql_query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

        DROP VIEW IF EXISTS user_view;
        SET a = a + 1;
    END LOOP my_loop;

    CLOSE zxcursor;
END //

DELIMITER ;

CALL create_tables_from_column('rate', 'object');
