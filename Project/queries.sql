CREATE TABLE `department` (
  `dep_id` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`dep_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `enroll` (
  `order_id` bigint NOT NULL,
  `quiz_id` bigint NOT NULL,
  `stu_id` bigint NOT NULL,
  PRIMARY KEY (`order_id`),
  UNIQUE KEY `enroll_quiz_id_stu_id_8155ceaf_uniq` (`quiz_id`,`stu_id`),
  KEY `enroll_stu_id_4e75869c_fk_students_stu_id` (`stu_id`),
  CONSTRAINT `enroll_quiz_id_1f1b9e9e_fk_quizzes_id` FOREIGN KEY (`quiz_id`) REFERENCES `quizzes` (`id`),
  CONSTRAINT `enroll_stu_id_4e75869c_fk_students_stu_id` FOREIGN KEY (`stu_id`) REFERENCES `students` (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
CREATE TABLE `flashcard` (
  `id` bigint NOT NULL,
  `question` longtext NOT NULL,
  `answer` longtext NOT NULL,
  `is_question_md` tinyint(1) DEFAULT NULL,
  `is_answer_md` tinyint(1) DEFAULT NULL,
  `hint` longtext,
  `categoryID` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `flashcard_categoryID_39453989_fk_flashcard_category_id` (`categoryID`),
  CONSTRAINT `flashcard_categoryID_39453989_fk_flashcard_category_id` FOREIGN KEY (`categoryID`) REFERENCES `flashcard_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `flashcard_category` (
  `id` bigint NOT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `participated` (
  `stu_id` bigint NOT NULL,
  `mark` double DEFAULT NULL,
  `quiz_id` bigint NOT NULL,
  PRIMARY KEY (`stu_id`),
  UNIQUE KEY `participated_stu_id_quiz_id_d600c2dc_uniq` (`stu_id`,`quiz_id`),
  KEY `participated_quiz_id_09ac659b_fk_quizzes_id` (`quiz_id`),
  CONSTRAINT `participated_quiz_id_09ac659b_fk_quizzes_id` FOREIGN KEY (`quiz_id`) REFERENCES `quizzes` (`id`),
  CONSTRAINT `participated_stu_id_98810429_fk_students_stu_id` FOREIGN KEY (`stu_id`) REFERENCES `students` (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `professors` (
  `prof_id` bigint NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `department` bigint DEFAULT NULL,
  PRIMARY KEY (`prof_id`),
  KEY `professors_department_211116bf_fk_department_dep_id` (`department`),
  CONSTRAINT `professors_department_211116bf_fk_department_dep_id` FOREIGN KEY (`department`) REFERENCES `department` (`dep_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `questions` (
  `id` bigint NOT NULL,
  `question` varchar(256) NOT NULL,
  `wrong_answers_1` varchar(256) DEFAULT NULL,
  `correct_answer` varchar(256) DEFAULT NULL,
  `wrong_answers_2` varchar(256) DEFAULT NULL,
  `wrong_answers_3` varchar(256) DEFAULT NULL,
  `quiz_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questions_quiz_id_5c84443f_fk_quizzes_id` (`quiz_id`),
  CONSTRAINT `questions_quiz_id_5c84443f_fk_quizzes_id` FOREIGN KEY (`quiz_id`) REFERENCES `quizzes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `quizzes` (
  `id` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  `price` double DEFAULT NULL,
  `began_at` date DEFAULT NULL,
  `end_at` date DEFAULT NULL,
  `prof_id` bigint NOT NULL,
  `quiz_subject_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `quizzes_prof_id_ebfc79f0_fk_professors_prof_id` (`prof_id`),
  KEY `quizzes_quiz_subject_id_dc18a9c0_fk_quizzes_subject_id` (`quiz_subject_id`),
  CONSTRAINT `quizzes_prof_id_ebfc79f0_fk_professors_prof_id` FOREIGN KEY (`prof_id`) REFERENCES `professors` (`prof_id`),
  CONSTRAINT `quizzes_quiz_subject_id_dc18a9c0_fk_quizzes_subject_id` FOREIGN KEY (`quiz_subject_id`) REFERENCES `quizzes_subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `quizzes_subject` (
  `id` bigint NOT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `student_category` (
  `stu_id` bigint NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`stu_id`),
  UNIQUE KEY `student_category_category_id_stu_id_be6ae872_uniq` (`category_id`,`stu_id`),
  UNIQUE KEY `student_category_stu_id_category_id_2ae82516_uniq` (`stu_id`,`category_id`),
  CONSTRAINT `student_category_category_id_a408eb4f_fk_flashcard_category_id` FOREIGN KEY (`category_id`) REFERENCES `flashcard_category` (`id`),
  CONSTRAINT `student_category_stu_id_97948242_fk_students_stu_id` FOREIGN KEY (`stu_id`) REFERENCES `students` (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `students` (
  `stu_id` bigint NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(128) DEFAULT NULL,
  `balance` double NOT NULL,
  PRIMARY KEY (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci