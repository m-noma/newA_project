-- 追加課題1
SELECT 
    `class1_tb`.`ordinal_num`
		AS "第〇回",
	`class_info`.`class_name`
		AS "所属クラス",
	`class1_tb`.`emoloyee_name` 
		AS "氏名", 
	MAX(`class1_tb`.`percentage_answers`) 
		AS "最高得点率",
	`class_info`.`class_mastor_name`
		AS "担当講師"
FROM 
	`class1_tb`
	INNER JOIN
		`class_info`
ON SUBSTRING(`class1_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
GROUP BY 
	`ordinal_num`
UNION 
SELECT  
	`class2_tb`.`ordinal_num`
		AS "第〇回",
	`class_info`.`class_name`
		AS "所属クラス",
	`class2_tb`.`emoloyee_name` 
		AS "氏名",
	MAX(`class2_tb`.`percentage_answers`) 
		AS "最高得点率",
	`class_info`.`class_mastor_name`
		AS "担当講師"
FROM 
	`class2_tb`
	INNER JOIN
		`class_info`
ON SUBSTRING(`class2_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
GROUP BY 
	`ordinal_num`
UNION
SELECT 
	`class3_tb`.`ordinal_num`
		AS "第〇回",
	`class_info`.`class_name`
		AS "所属クラス",
	`class3_tb`.`emoloyee_name` 
		AS "氏名", 
	MAX(`class3_tb`.`percentage_answers`) 
		AS "最高得点率",
	`class_info`.`class_mastor_name`
		AS "担当講師"
FROM 
	`class3_tb`
	INNER JOIN
		`class_info`
ON SUBSTRING(`class3_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
GROUP BY 
	`ordinal_num`
UNION
SELECT 
	`class4_tb`.`ordinal_num`
		AS "第〇回",
	`class_info`.`class_name`
		AS "所属クラス",
	`class4_tb`.`emoloyee_name` 
		AS "氏名", 
	MAX(`class4_tb`.`percentage_answers`) 
		AS "最高得点率",
	`class_info`.`class_mastor_name`
		AS "担当講師"
FROM 
	`class4_tb`
	INNER JOIN
		`class_info`
ON SUBSTRING(`class4_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
GROUP BY 
	`ordinal_num`
ORDER BY `第〇回`, `所属クラス`;






-- 追加課題2
SELECT 
	`class1_tb`.`ordinal_num`
		AS "第〇回",
	`class_info`.`class_name`
		AS "所属クラス",
	ROUND(AVG(`class1_tb`.`percentage_answers`),3) 
		AS "平均得点率",
	`class_info`.`class_mastor_name`
		AS "担当講師"
FROM 
	`class1_tb`
	INNER JOIN
		`class_info`
ON SUBSTRING(`class1_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
GROUP BY 
	`ordinal_num`
UNION 
SELECT 
	`class2_tb`.`ordinal_num`
		AS "第〇回",
	`class_info`.`class_name`
		AS "所属クラス",
	ROUND(AVG(`class2_tb`.`percentage_answers`),3)
		AS "最高得点率",
	`class_info`.`class_mastor_name`
		AS "担当講師"
FROM 
	`class2_tb`
	INNER JOIN
		`class_info`
ON SUBSTRING(`class2_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
GROUP BY 
	`ordinal_num`
UNION
SELECT 
	`class3_tb`.`ordinal_num`
		AS "第〇回",
	`class_info`.`class_name`
		AS "所属クラス",
	ROUND(AVG(`class3_tb`.`percentage_answers`),4)
		AS "最高得点率",
	`class_info`.`class_mastor_name`
		AS "担当講師"
FROM 
	`class3_tb`
	INNER JOIN
		`class_info`
ON SUBSTRING(`class3_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
GROUP BY 
	`ordinal_num`
UNION
SELECT 
	`class4_tb`.`ordinal_num`
		AS "第〇回",
	`class_info`.`class_name`
		AS "所属クラス",
	ROUND(AVG(`class4_tb`.`percentage_answers`),3) 
		AS "最高得点率",
	`class_info`.`class_mastor_name`
		AS "担当講師"
FROM 
	`class4_tb`
	INNER JOIN
		`class_info`
ON SUBSTRING(`class4_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
GROUP BY 
	`ordinal_num`
ORDER BY `第〇回`, `所属クラス`;








-- 追加課題3
(SELECT 
    `class1_tb`.`ordinal_num`
		AS "第〇回",
    `class_info`.`class_name`
		AS "所属クラス",
	`class1_tb`.`emoloyee_name` 
        AS "氏名",
    `class_info`.`class_mastor_name`
		AS "担当講師",
    `class1_tb`.`percentage_answers`
        AS "得点率"
FROM
    `class1_tb`
    INNER JOIN
		`class_info`
        ON 
            SUBSTRING(`class1_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
UNION
SELECT 
    `class2_tb`.`ordinal_num`
		AS "第〇回",
    `class_info`.`class_name`
		AS "所属クラス",
	`class2_tb`.`emoloyee_name` 
        AS "氏名",
    `class_info`.`class_mastor_name`
		AS "担当講師",
    `class2_tb`.`percentage_answers`
        AS "得点率"
FROM
    `class2_tb`
    INNER JOIN
		`class_info`
        ON 
            SUBSTRING(`class2_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
UNION
SELECT 
    `class3_tb`.`ordinal_num`
		AS "第〇回",
    `class_info`.`class_name`
		AS "所属クラス",
	`class3_tb`.`emoloyee_name` 
        AS "氏名",
    `class_info`.`class_mastor_name`
		AS "担当講師",
    `class3_tb`.`percentage_answers`
        AS "得点率"
FROM
    `class3_tb`
    INNER JOIN
		`class_info`
        ON 
            SUBSTRING(`class3_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
UNION
SELECT 
    `class4_tb`.`ordinal_num`
		AS "第〇回",
    `class_info`.`class_name`
		AS "所属クラス",
	`class4_tb`.`emoloyee_name` 
        AS "氏名",
    `class_info`.`class_mastor_name`
		AS "担当講師",
    `class4_tb`.`percentage_answers`
        AS "得点率"
FROM
    `class4_tb`
    INNER JOIN
		`class_info`
        ON 
            SUBSTRING(`class4_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
ORDER BY `第〇回`, `得点率` DESC
LIMIT 10)
UNION ALL
(SELECT 
    `class1_tb`.`ordinal_num`
		AS "第〇回",
    `class_info`.`class_name`
		AS "所属クラス",
	`class1_tb`.`emoloyee_name` 
        AS "氏名",
    `class_info`.`class_mastor_name`
		AS "担当講師",
    `class1_tb`.`percentage_answers`
        AS "得点率"
FROM
    `class1_tb`
    INNER JOIN
		`class_info`
        ON 
            SUBSTRING(`class1_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
UNION
SELECT 
    `class2_tb`.`ordinal_num`
		AS "第〇回",
    `class_info`.`class_name`
		AS "所属クラス",
	`class2_tb`.`emoloyee_name` 
        AS "氏名",
    `class_info`.`class_mastor_name`
		AS "担当講師",
    `class2_tb`.`percentage_answers`
        AS "得点率"
FROM
    `class2_tb`
    INNER JOIN
		`class_info`
        ON 
            SUBSTRING(`class2_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
UNION
SELECT 
    `class3_tb`.`ordinal_num`
		AS "第〇回",
    `class_info`.`class_name`
		AS "所属クラス",
	`class3_tb`.`emoloyee_name` 
        AS "氏名",
    `class_info`.`class_mastor_name`
		AS "担当講師",
    `class3_tb`.`percentage_answers`
        AS "得点率"
FROM
    `class3_tb`
    INNER JOIN
		`class_info`
        ON 
            SUBSTRING(`class3_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
UNION
SELECT 
    `class4_tb`.`ordinal_num`
		AS "第〇回",
    `class_info`.`class_name`
		AS "所属クラス",
	`class4_tb`.`emoloyee_name` 
        AS "氏名",
    `class_info`.`class_mastor_name`
		AS "担当講師",
    `class4_tb`.`percentage_answers`
        AS "得点率"
FROM
    `class4_tb`
    INNER JOIN
		`class_info`
        ON 
            SUBSTRING(`class4_tb`.`record_number`, 1, 3) = `class_info`.`class_name`
ORDER BY `第〇回` DESC, `得点率` DESC
LIMIT 10);