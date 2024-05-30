CREATE DATABASE vending_machine_db;
USE vending_machine_db;



CREATE TABLE `vending_machine_db`.`product_tb` ( 
	product_id INT NOT NULL PRIMARY KEY, 
	product_name VARCHAR(15) NOT NULL DEFAULT "よくある謎の奴",
	product_price INT NOT NULL DEFAULT 0, 
	product_count INT NOT NULL DEFAULT 0);



CREATE TABLE `vending_machine_db`.`cache_tb`(
	cache_price INT NOT NULL DEFAULT 0 PRIMARY KEY,
   	cache_num INT NOT NULL DEFAULT 0);



CREATE TABLE `vending_machine_db`.`order_tb`(
	order_id INT NOT NULL DEFAULT 0,
	product_id INT NOT NULL DEFAULT 0,
	date_stamp DATETIME NOT NULL,
	FOREIGN KEY(`product_id`)
	REFERENCES `product_tb`(`product_id`));



INSERT INTO `vending_machine_db`.`product_tb`(`product_id`, `product_name`, `product_price`, `product_count`) VALUE (1, '水', 110, 10);
INSERT INTO `vending_machine_db`.`product_tb`(`product_id`, `product_name`, `product_price`, `product_count`) VALUE (2, 'お茶', 120, 10);
INSERT INTO `vending_machine_db`.`product_tb`(`product_id`, `product_name`, `product_price`, `product_count`) VALUE (3, '炭酸水', 130, 10);
INSERT INTO `vending_machine_db`.`product_tb`(`product_id`, `product_name`, `product_price`, `product_count`) VALUE (4, 'ソーダ', 160, 10);
INSERT INTO `vending_machine_db`.`product_tb`(`product_id`, `product_name`, `product_price`, `product_count`) VALUE (5, 'コーラ', 160, 10);



INSERT INTO `vending_machine_db`.`cache_tb`(`cache_price`, `cache_num`) VALUE ('10yen', 10);
INSERT INTO `vending_machine_db`.`cache_tb`(`cache_price`, `cache_num`) VALUE ('50yen', 10);
INSERT INTO `vending_machine_db`.`cache_tb`(`cache_price`, `cache_num`) VALUE ('100yen', 10);
INSERT INTO `vending_machine_db`.`cache_tb`(`cache_price`, `cache_num`) VALUE ('500yen', 10);
INSERT INTO `vending_machine_db`.`cache_tb`(`cache_price`, `cache_num`) VALUE ('1000yen', 10);



-- INSERT INTO `vending_machine_db`.`order_tb`(`order_id`, `product_id`, `date_stmp`) VALUE ('購入物id', 'datastamp');

