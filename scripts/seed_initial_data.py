import psycopg2
from psycopg2.extras import RealDictCursor


DB_CONFIG = {
    "dbname": "virtual_dean",
    "user": "postgres",
    "password": "admin123",
    "host": "localhost",
    "port": "5432"
}


def get_db_connection():
    return psycopg2.connect(
        **DB_CONFIG,
        cursor_factory=RealDictCursor
    )

library_questions = [
    {
        "category": "library",
        "translations": {
            "ru": {
                "question": "Как получить читательский билет?",
                "answer": "Для получения и оформления читательского билета необходимо предоставить паспорт и две фотографии 3×4 см в библиотеку. Для перерегистрации необходимо предоставить студенческий билет с отметкой об обучении на текущем курсе учебного года."
            },
            "en": {
                "question": "How can I get a library card?",
                "answer": "To obtain a library card, you need to provide your passport and two 3×4 cm photos to the library. For re-registration, you need to provide your student ID with confirmation of enrollment for the current academic year."
            },
            "zh": {
                "question": "如何办理借书证？",
                "answer": "办理借书证需要向图书馆提交护照和两张3×4厘米照片。重新注册时，需要提供带有当前学年在读证明的学生证。"
            }
        }
    },
    {
        "category": "library",
        "translations": {
            "ru": {
                "question": "Как найти нужную литературу по программе?",
                "answer": "Для поиска необходимой литературы по программе можно обратиться в библиотеку лично, воспользоваться электронной библиотекой МТУСИ или сайтом elibrary.ru."
            },
            "en": {
                "question": "How can I find the required literature for my study program?",
                "answer": "To find the required literature for your study program, you can contact the library in person, use the MTUCI electronic library, or use the elibrary.ru website."
            },
            "zh": {
                "question": "如何查找课程所需的文献？",
                "answer": "如需查找课程所需的文献，可以亲自前往图书馆咨询，也可以使用莫斯科通信与信息技术大学电子图书馆或 elibrary.ru 网站。"
            }
        }
    },
    {
        "category": "library",
        "translations": {
            "ru": {
                "question": "Есть ли у студентов и преподавателей доступ к электронным библиотекам?",
                "answer": "Да, доступ к электронным библиотекам предоставляется. При обращении в библиотеку по электронной почте или через форму обратной связи, а также при регистрации в электронно-библиотечных системах необходимо указывать адрес корпоративной почты МТУСИ."
            },
            "en": {
                "question": "Do students and teachers have access to electronic libraries?",
                "answer": "Yes, access to electronic libraries is available. When contacting the library by email or through the feedback form, as well as when registering in electronic library systems, you should use your MTUCI corporate email address."
            },
            "zh": {
                "question": "学生和教师可以使用电子图书馆吗？",
                "answer": "可以。通过电子邮件或反馈表联系图书馆，以及在电子图书馆系统中注册时，需要使用莫斯科通信与信息技术大学的企业邮箱地址。"
            }
        }
    },
    {
        "category": "library",
        "translations": {
            "ru": {
                "question": "Можно ли продлить срок сдачи книг?",
                "answer": "Да, срок сдачи книг можно продлить. Для этого необходимо обратиться в библиотеку."
            },
            "en": {
                "question": "Can I extend the return period for library books?",
                "answer": "Yes, the return period for library books can be extended. To do this, you need to contact the library."
            },
            "zh": {
                "question": "可以延长还书期限吗？",
                "answer": "可以，图书的归还期限可以延长。为此，需要联系图书馆。"
            }
        }
    }
]

military_questions = [
    {
        "category": "military",
        "translations": {
            "ru": {
                "question": "Кто обязан встать на воинский учет?",
                "answer": "На воинский учет во втором отделе МТУСИ обязаны встать юноши, являющиеся гражданами Российской Федерации и зачисленные на 1 курс очной формы обучения."
            },
            "en": {
                "question": "Who is required to register for military service?",
                "answer": "Male students who are citizens of the Russian Federation and are enrolled in the first year of full-time studies are required to register for military service at the Second Department of MTUCI."
            },
            "zh": {
                "question": "谁需要进行兵役登记？",
                "answer": "俄罗斯联邦公民中的男性学生，如果被录取为全日制一年级学生，需要在莫斯科通信与信息技术大学第二部门进行兵役登记。"
            }
        }
    },
    {
        "category": "military",
        "translations": {
            "ru": {
                "question": "Когда проходит постановка на воинский учет?",
                "answer": "Постановка студентов 1 курса на воинский учет проводится на общих собраниях факультетов университета в период с 25 по 30 августа. Точную дату необходимо уточнить в деканате или на сайте МТУСИ в разделе для абитуриентов."
            },
            "en": {
                "question": "When does military registration take place?",
                "answer": "Military registration for first-year students takes place at general faculty meetings from August 25 to August 30. The exact date should be clarified at the dean's office or on the MTUCI website in the applicants section."
            },
            "zh": {
                "question": "兵役登记什么时候进行？",
                "answer": "一年级学生的兵役登记通常在8月25日至8月30日期间于各学院的统一会议上进行。具体日期需要向院系办公室咨询，或在莫斯科通信与信息技术大学网站的招生相关栏目中查看。"
            }
        }
    },
    {
        "category": "military",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для воинского учета?",
                "answer": "Для постановки на воинский учет необходимы паспорт гражданина Российской Федерации, военный билет или приписное удостоверение, водительское удостоверение при наличии, а также авторучка с синими или черными чернилами."
            },
            "en": {
                "question": "What documents are required for military registration?",
                "answer": "For military registration, you need a passport of a citizen of the Russian Federation, a military ID or a certificate of a citizen subject to conscription, a driver's license if available, and a pen with blue or black ink."
            },
            "zh": {
                "question": "兵役登记需要哪些文件？",
                "answer": "兵役登记需要俄罗斯联邦公民护照、军人证或应征公民登记证，如有驾驶证也需提供，同时需要携带蓝色或黑色墨水笔。"
            }
        }
    },
    {
        "category": "military",
        "translations": {
            "ru": {
                "question": "Что делать, если студент не был на организационном собрании факультета?",
                "answer": "Если студент не присутствовал на организационном собрании факультета и не заполнял Форму № 10, необходимо прибыть во второй отдел в период с 15 по 30 сентября и получить форму для самостоятельного заполнения."
            },
            "en": {
                "question": "What should a student do if they missed the faculty orientation meeting?",
                "answer": "If a student did not attend the faculty orientation meeting and did not complete Form No. 10, they must come to the Second Department between September 15 and September 30 to receive the form for independent completion."
            },
            "zh": {
                "question": "如果学生没有参加学院组织会议该怎么办？",
                "answer": "如果学生没有参加学院组织会议，也没有填写第10号表格，则需要在9月15日至9月30日期间前往第二部门领取表格并自行填写。"
            }
        }
    },
    {
        "category": "military",
        "translations": {
            "ru": {
                "question": "Кому предоставляется отсрочка от призыва?",
                "answer": "Отсрочка от призыва предоставляется юношам, обучающимся по очной форме, которые поступили в университет сразу после окончания школы."
            },
            "en": {
                "question": "Who is eligible for deferment from military service?",
                "answer": "Deferment from military service is granted to male full-time students who entered the university immediately after graduating from school."
            },
            "zh": {
                "question": "哪些人可以获得兵役延期？",
                "answer": "兵役延期适用于高中毕业后直接进入大学全日制学习的男性学生。"
            }
        }
    }
]

graduation_questions = [
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Может ли студент выбрать тему ВКР самостоятельно?",
                "answer": "Да, студент имеет право предложить собственную тему выпускной квалификационной работы с обоснованием её выбора. Предлагаемая тема должна быть согласована с заведующим выпускающей кафедрой."
            },
            "en": {
                "question": "Can a student choose the final thesis topic independently?",
                "answer": "Yes, a student has the right to propose their own final thesis topic with a justification for the choice. The proposed topic must be approved by the head of the graduating department."
            },
            "zh": {
                "question": "学生可以自己选择毕业论文题目吗？",
                "answer": "可以。学生有权提出自己的毕业论文题目，并说明选择该题目的理由。所提出的题目必须经过毕业教研室主任批准。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Когда должно быть оформлено заявление студента на ВКР?",
                "answer": "Заявление студента на выпускную квалификационную работу должно быть оформлено до 1 января текущего года."
            },
            "en": {
                "question": "When must the application for the final thesis be submitted?",
                "answer": "The student’s application for the final thesis must be submitted by January 1 of the current year."
            },
            "zh": {
                "question": "毕业论文申请应在什么时候提交？",
                "answer": "学生的毕业论文申请应在当年1月1日前提交。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Когда выходит приказ об утверждении тем ВКР?",
                "answer": "Декан факультета, на котором обучается студент, подготавливает приказ об утверждении тем ВКР не позднее 25 января текущего учебного года."
            },
            "en": {
                "question": "When is the order approving final thesis topics issued?",
                "answer": "The dean of the faculty prepares the order approving students’ final thesis topics no later than January 25 of the current academic year."
            },
            "zh": {
                "question": "毕业论文题目批准命令什么时候发布？",
                "answer": "学生所在学院的院长应不迟于本学年1月25日准备批准毕业论文题目的命令。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Можно ли изменить тему ВКР?",
                "answer": "Изменение или уточнение темы ВКР возможно не позднее чем за два месяца до предполагаемой даты защиты. Для этого необходимо личное заявление студента на имя ректора, согласованное с руководителем, заведующим кафедрой и деканом. Изменение или уточнение темы оформляется приказом по университету."
            },
            "en": {
                "question": "Is it possible to change the final thesis topic?",
                "answer": "Changing or clarifying the final thesis topic is possible no later than two months before the expected defense date. This requires a personal application addressed to the rector and approved by the supervisor, the head of the department, and the dean. The change is formalized by a university order."
            },
            "zh": {
                "question": "可以更改毕业论文题目吗？",
                "answer": "可以，但必须不晚于预计答辩日期前两个月提出。学生需要向校长提交个人申请，并经指导教师、教研室主任和学院院长同意。毕业论文题目的更改或调整应通过学校正式命令确认。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Когда должна быть готова ВКР?",
                "answer": "Полностью готовая выпускная квалификационная работа должна быть представлена студентом руководителю за две недели до начала работы государственной экзаменационной комиссии по защите ВКР."
            },
            "en": {
                "question": "When must the final thesis be ready?",
                "answer": "The completed final thesis must be submitted by the student to the supervisor two weeks before the start of the State Examination Commission’s work on thesis defenses."
            },
            "zh": {
                "question": "毕业论文应在什么时候完成？",
                "answer": "完整的毕业论文应在国家考试委员会开始毕业论文答辩工作前两周提交给指导教师。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Кто принимает решение о допуске ВКР к защите?",
                "answer": "Заведующий кафедрой или его заместитель на основании представленных документов оценивает готовность ВКР и принимает решение о допуске к защите. Если заведующий кафедрой не считает возможным допустить работу к защите, вопрос рассматривается на заседании кафедры с участием руководителя и автора работы."
            },
            "en": {
                "question": "Who decides whether the final thesis is admitted to defense?",
                "answer": "The head of the department or their deputy evaluates the readiness of the final thesis based on the submitted documents and decides whether it can be admitted to defense. If the head of the department does not consider it possible to admit the work, the issue is considered at a department meeting with the participation of the supervisor and the author."
            },
            "zh": {
                "question": "谁决定毕业论文是否允许答辩？",
                "answer": "教研室主任或其副主任会根据提交的材料评估毕业论文的完成情况，并决定是否允许学生参加答辩。如果教研室主任认为论文不能参加答辩，该问题将在教研室会议上讨论，指导教师和论文作者也会参加。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Как пройти антиплагиат на ВКР?",
                "answer": "До защиты ВКР направляется на кафедру для проверки на антиплагиат. Если показатель оригинальности составляет более 65%, работа допускается к защите. Если показатель ниже 65%, студенту предоставляется возможность доработки и повторной проверки."
            },
            "en": {
                "question": "How does the plagiarism check for the final thesis work?",
                "answer": "Before the defense, the final thesis is submitted to the department for a plagiarism check. If the originality score is above 65%, the work is admitted to defense. If it is below 65%, the student is given an opportunity to revise the work and pass the check again."
            },
            "zh": {
                "question": "毕业论文如何进行查重？",
                "answer": "答辩前，毕业论文需要提交到教研室进行查重。如果原创率高于65%，论文可以参加答辩。如果低于65%，学生可以修改论文并再次进行查重。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Когда и куда сдается готовая ВКР?",
                "answer": "За 2 дня до защиты студент сдаёт в деканат ВКР в переплетённом виде, подписанную заведующим кафедрой, с отзывом руководителя и рецензией. Рецензия требуется только для магистров. Также необходимо предоставить электронную копию ВКР."
            },
            "en": {
                "question": "When and where should the completed final thesis be submitted?",
                "answer": "Two days before the defense, the student submits the bound final thesis to the dean’s office. The thesis must be signed by the head of the department and include the supervisor’s review and a reviewer's report. The reviewer’s report is required only for master’s students. An electronic copy of the thesis must also be submitted."
            },
            "zh": {
                "question": "完成的毕业论文应在什么时候交到哪里？",
                "answer": "答辩前2天，学生应将装订好的毕业论文提交到院系办公室。论文应由教研室主任签字，并附上指导教师评语和评审意见。评审意见只对硕士生要求。同时还需要提交毕业论文电子版。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Когда проводится защита ВКР?",
                "answer": "Защита ВКР проводится в сроки, установленные графиком учебного процесса. Расписание работы государственной экзаменационной комиссии утверждается деканом не позднее чем за месяц до начала защиты и доводится до сведения студентов."
            },
            "en": {
                "question": "When does the final thesis defense take place?",
                "answer": "The final thesis defense takes place according to the academic schedule. The schedule of the State Examination Commission is approved by the dean no later than one month before the start of the defenses and is communicated to students."
            },
            "zh": {
                "question": "毕业论文答辩什么时候进行？",
                "answer": "毕业论文答辩按照教学进程安排进行。国家考试委员会的工作日程由院长在答辩开始前不晚于一个月批准，并通知所有学生。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Что необходимо сделать студенту после защиты ВКР?",
                "answer": "После защиты ВКР студенту необходимо получить обходной лист в Едином деканате, подписать его и сдать в отдел кадров студентов на Авиамоторной."
            },
            "en": {
                "question": "What should a student do after the final thesis defense?",
                "answer": "After the final thesis defense, the student must receive a clearance form at the Unified Dean’s Office, have it signed, and submit it to the student HR department at Aviamotornaya."
            },
            "zh": {
                "question": "毕业论文答辩后学生需要做什么？",
                "answer": "毕业论文答辩后，学生需要在统一院系办公室领取离校手续单，完成签字后交到位于 Aviamotornaya 校区的学生人事部门。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Как получить диплом и забрать документы?",
                "answer": "Институт или факультет организует официальное вручение дипломов на торжественных собраниях. Даты собраний размещаются на сайте МТУСИ. Если студент отсутствовал на вручении, он может забрать диплом и документы в отделе кадров студентов."
            },
            "en": {
                "question": "How can I receive my diploma and collect my documents?",
                "answer": "The institute or faculty organizes official diploma award ceremonies. The dates are published on the MTUCI website. If a student does not attend the ceremony, they can collect the diploma and documents from the student HR department."
            },
            "zh": {
                "question": "如何领取毕业证书和其他文件？",
                "answer": "学院会组织正式的毕业证书颁发仪式。具体日期会发布在莫斯科通信与信息技术大学网站上。如果学生未参加颁发仪式，可以到学生人事部门领取毕业证书和相关文件。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Какие документы выдаются при выпуске?",
                "answer": "При выпуске студенту выдаётся документ об образовании: диплом бакалавра, специалиста или магистра, а также аттестат при наличии его в личном деле."
            },
            "en": {
                "question": "What documents are issued upon graduation?",
                "answer": "Upon graduation, the student receives an education document: a bachelor’s, specialist’s, or master’s diploma, as well as the school certificate if it is stored in the student’s personal file."
            },
            "zh": {
                "question": "毕业时会发放哪些文件？",
                "answer": "毕业时，学生会获得相应的学历证书，例如学士、专家或硕士毕业证书。如果中学毕业证保存在个人档案中，也会一并发放。"
            }
        }
    },
    {
        "category": "graduation",
        "translations": {
            "ru": {
                "question": "Как получить характеристику с места учёбы?",
                "answer": "Для получения характеристики с места учёбы необходимо подать заявление по форме, размещённой на сайте МТУСИ. Также можно обратиться к преподавателям выпускающей кафедры."
            },
            "en": {
                "question": "How can I get a reference letter from the university?",
                "answer": "To obtain a reference letter from the university, you need to submit an application using the form available on the MTUCI website. You may also contact teachers of the graduating department."
            },
            "zh": {
                "question": "如何获得学校出具的学生评价或证明？",
                "answer": "如需获得学校出具的学生评价或证明，需要按照莫斯科通信与信息技术大学网站上的表格提交申请。也可以联系毕业教研室的教师。"
            }
        }
    }
]

activities_questions = [
    {
        "category": "activities",
        "translations": {
            "ru": {
                "question": "Как вступить в студенческий совет?",
                "answer": "Для вступления в студенческий совет необходимо заполнить анкету на стажировку в группе VK «Студенческое самоуправление | МТУСИ»."
            },
            "en": {
                "question": "How can I join the student council?",
                "answer": "To join the student council, you need to fill out an internship application form in the VK group “Student Self-Government | MTUCI”."
            },
            "zh": {
                "question": "如何加入学生会？",
                "answer": "如需加入学生会，需要在 VK 群组“学生自治 | 莫斯科通信与信息技术大学”中填写实习申请表。"
            }
        }
    },
    {
        "category": "activities",
        "translations": {
            "ru": {
                "question": "Где узнать про мероприятия и конкурсы?",
                "answer": "Информация о мероприятиях и конкурсах публикуется в Telegram-канале «Активист МТУСИ» и на сайте МТУСИ."
            },
            "en": {
                "question": "Where can I find information about events and competitions?",
                "answer": "Information about events and competitions is published in the Telegram channel “MTUCI Activist” and on the MTUCI website."
            },
            "zh": {
                "question": "在哪里可以了解活动和竞赛信息？",
                "answer": "有关活动和竞赛的信息发布在 Telegram 频道“MTUCI Activist”以及莫斯科通信与信息技术大学网站上。"
            }
        }
    },
    {
        "category": "activities",
        "translations": {
            "ru": {
                "question": "Как подать заявку на волонтерство от вуза?",
                "answer": "Для подачи заявки на волонтёрство от университета необходимо заполнить анкету на стажировку в группе VK «Студенческое самоуправление | МТУСИ»."
            },
            "en": {
                "question": "How can I apply for university volunteering?",
                "answer": "To apply for university volunteering, you need to fill out an internship application form in the VK group “Student Self-Government | MTUCI”."
            },
            "zh": {
                "question": "如何申请参加大学志愿者活动？",
                "answer": "如需申请参加大学志愿者活动，需要在 VK 群组“学生自治 | 莫斯科通信与信息技术大学”中填写实习申请表。"
            }
        }
    },
    {
        "category": "activities",
        "translations": {
            "ru": {
                "question": "Как поощряется студент за активное участие?",
                "answer": "По результатам активного участия студенту могут быть выданы грамоты. Вид поощрения зависит от мероприятия, в котором студент принимал участие."
            },
            "en": {
                "question": "How is a student rewarded for active participation?",
                "answer": "Based on active participation, a student may receive certificates of appreciation. The type of reward depends on the event in which the student participated."
            },
            "zh": {
                "question": "学生积极参加活动会得到什么奖励？",
                "answer": "根据学生的积极参与情况，学校可能会颁发荣誉证书。奖励形式取决于学生参加的具体活动。"
            }
        }
    }
]

study_questions = [
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Обязан ли преподаватель проводить консультации перед экзаменами?",
                "answer": "Консультации перед экзаменами проводятся согласно расписанию. Для преподавателя явка на консультацию является обязательной, для студента — необязательной."
            },
            "en": {
                "question": "Is a teacher required to hold consultations before exams?",
                "answer": "Pre-exam consultations are held according to the schedule. Attendance is mandatory for the teacher, but optional for the student."
            },
            "zh": {
                "question": "教师必须在考试前进行答疑咨询吗？",
                "answer": "考试前的答疑咨询按照时间表进行。教师必须参加，学生可以自愿参加。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Как записаться на консультацию перед экзаменом?",
                "answer": "Запись на консультацию перед экзаменом не требуется. Консультации проводятся согласно расписанию."
            },
            "en": {
                "question": "How can I register for a consultation before an exam?",
                "answer": "Registration for a pre-exam consultation is not required. Consultations are held according to the schedule."
            },
            "zh": {
                "question": "如何报名参加考试前答疑咨询？",
                "answer": "考试前答疑咨询不需要提前报名，按照时间表进行。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Что делать, если в личном кабинете отображаются неверные данные по дисциплине?",
                "answer": "Если в личном кабинете отображаются неверные данные по дисциплине, необходимо обратиться к преподавателю, ведущему данную дисциплину."
            },
            "en": {
                "question": "What should I do if incorrect course information is displayed in my personal account?",
                "answer": "If incorrect course information is displayed in your personal account, you should contact the teacher responsible for that course."
            },
            "zh": {
                "question": "如果个人账户中显示的课程信息不正确，该怎么办？",
                "answer": "如果个人账户中显示的课程信息不正确，需要联系负责该课程的教师。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Как найти научного руководителя?",
                "answer": "Научного руководителя необходимо согласовать с преподавателем выпускающей кафедры. Студент может выбрать преподавателя, который работает в соответствующей предметной области."
            },
            "en": {
                "question": "How can I find a research supervisor?",
                "answer": "A research supervisor should be agreed upon with a teacher from the graduating department. A student may choose any teacher working in the relevant subject area."
            },
            "zh": {
                "question": "如何寻找科研导师？",
                "answer": "科研导师需要与毕业教研室的教师协商确定。学生可以选择在相关专业领域工作的教师。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Что нужно для участия в НИР?",
                "answer": "Для участия в научно-исследовательской работе необходим научный руководитель и совместная работа с ним над выбранной темой."
            },
            "en": {
                "question": "What is required to participate in research work?",
                "answer": "To participate in research work, a student needs a research supervisor and joint work with them on the selected topic."
            },
            "zh": {
                "question": "参加科研工作需要什么？",
                "answer": "参加科研工作需要有科研导师，并与导师一起围绕选定的课题开展工作。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Где искать информацию о научных конференциях?",
                "answer": "Информацию о научных конференциях можно найти на сайте МТУСИ в разделе «Научно-исследовательские работы студентов». Также сведения о предстоящих конференциях публикуются в Telegram-канале МТУСИ."
            },
            "en": {
                "question": "Where can I find information about scientific conferences?",
                "answer": "Information about scientific conferences can be found on the MTUCI website in the section “Student Research Work”. Information about upcoming conferences is also published in the MTUCI Telegram channel."
            },
            "zh": {
                "question": "在哪里可以找到科研会议的信息？",
                "answer": "科研会议的信息可以在莫斯科通信与信息技术大学网站“学生科研工作”栏目中找到。即将举行的会议信息也会发布在学校的 Telegram 频道中。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Как оформить пропуск по болезни?",
                "answer": "Для оформления пропуска по болезни необходимо предоставить справку из медицинского учреждения."
            },
            "en": {
                "question": "How can I document an absence due to illness?",
                "answer": "To document an absence due to illness, you need to provide a medical certificate from a healthcare institution."
            },
            "zh": {
                "question": "因病缺课应如何办理证明？",
                "answer": "因病缺课需要提供医疗机构出具的证明。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Нужно ли приносить справку в деканат после болезни?",
                "answer": "Да, справку необходимо предоставить в деканат не позднее трёх дней после её закрытия."
            },
            "en": {
                "question": "Do I need to submit a medical certificate to the dean’s office after illness?",
                "answer": "Yes, the medical certificate must be submitted to the dean’s office no later than three days after it is closed."
            },
            "zh": {
                "question": "病假后需要把医疗证明交到院系办公室吗？",
                "answer": "需要。医疗证明应在证明结束后三天内提交到院系办公室。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Что делать, если студент пропустил зачёт или экзамен по уважительной причине?",
                "answer": "Если студент пропустил зачёт или экзамен по уважительной причине, необходимо предоставить справку из медицинского учреждения или иной документ, подтверждающий причину пропуска."
            },
            "en": {
                "question": "What should I do if I missed a pass/fail test or exam for a valid reason?",
                "answer": "If a student missed a pass/fail test or exam for a valid reason, they must provide a medical certificate or another document confirming the reason for the absence."
            },
            "zh": {
                "question": "如果因正当理由错过考查或考试，该怎么办？",
                "answer": "如果学生因正当理由错过考查或考试，需要提供医疗机构证明或其他能够证明缺席原因的文件。"
            }
        }
    }
]

documents_questions = [
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "Где заказать справку об обучении?",
                "answer": "Справку об обучении можно получить в Едином деканате или оформить через личный кабинет в разделе «Электронные услуги»."
            },
            "en": {
                "question": "Where can I request a certificate of enrollment?",
                "answer": "A certificate of enrollment can be obtained at the Unified Dean’s Office or requested through the personal account in the “Electronic services” section."
            },
            "zh": {
                "question": "在哪里可以申请在读证明？",
                "answer": "在读证明可以在统一院系办公室领取，也可以通过个人账户中的“电子服务”栏目申请。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "Сколько дней делается справка об обучении?",
                "answer": "В Едином деканате справка выдаётся сразу при предъявлении паспорта или студенческого билета."
            },
            "en": {
                "question": "How long does it take to issue a certificate of enrollment?",
                "answer": "At the Unified Dean’s Office, the certificate is issued immediately upon presentation of a passport or student ID."
            },
            "zh": {
                "question": "办理在读证明需要多长时间？",
                "answer": "在统一院系办公室，出示护照或学生证后可立即领取证明。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "Можно ли получить справку в электронном виде?",
                "answer": "Да, справку можно оформить в электронном виде через личный кабинет в разделе «Электронные услуги». В этом случае студент получает скан справки."
            },
            "en": {
                "question": "Can I receive a certificate electronically?",
                "answer": "Yes, a certificate can be requested electronically through the personal account in the “Electronic services” section. In this case, the student receives a scanned copy of the certificate."
            },
            "zh": {
                "question": "可以电子版形式获得证明吗？",
                "answer": "可以。学生可以通过个人账户中的“电子服务”栏目在线申请证明。在这种情况下，学生会收到证明的扫描件。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "Когда можно получить диплом?",
                "answer": "Красные дипломы вручает ректор на торжественном мероприятии, организованном институтом. Синие дипломы вручает декан факультета на торжественном мероприятии, организованном факультетом. Если студент не присутствовал на мероприятии, он может получить диплом в отделе кадров студентов."
            },
            "en": {
                "question": "When can I receive my diploma?",
                "answer": "Honors diplomas are presented by the rector at a ceremony organized by the institute. Standard diplomas are presented by the faculty dean at a ceremony organized by the faculty. If a student did not attend the ceremony, they can collect the diploma from the student HR department."
            },
            "zh": {
                "question": "什么时候可以领取毕业证书？",
                "answer": "优秀毕业证书由校长在学院组织的正式活动上颁发。普通毕业证书由院长在学院组织的正式活动上颁发。如果学生未参加活动，可以到学生人事部门领取毕业证书。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "Что делать, если диплом потерян?",
                "answer": "Если диплом потерян, необходимо написать заявление в отдел кадров студентов на Авиамоторной."
            },
            "en": {
                "question": "What should I do if my diploma is lost?",
                "answer": "If a diploma is lost, the student must submit an application to the student HR department at Aviamotornaya."
            },
            "zh": {
                "question": "如果毕业证书丢失了怎么办？",
                "answer": "如果毕业证书丢失，需要向位于 Aviamotornaya 校区的学生人事部门提交申请。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "Как получить дубликат диплома?",
                "answer": "Для получения дубликата диплома необходимо написать заявление в отдел кадров студентов на Авиамоторной."
            },
            "en": {
                "question": "How can I obtain a duplicate diploma?",
                "answer": "To obtain a duplicate diploma, the student must submit an application to the student HR department at Aviamotornaya."
            },
            "zh": {
                "question": "如何获得毕业证书副本？",
                "answer": "如需获得毕业证书副本，学生必须向位于 Aviamotornaya 校区的学生人事部门提交申请。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "Как забрать школьный аттестат?",
                "answer": "Для получения школьного аттестата необходимо обратиться в отдел кадров студентов на Авиамоторной."
            },
            "en": {
                "question": "How can I collect my school certificate?",
                "answer": "To collect the school certificate, the student should contact the student HR department at Aviamotornaya."
            },
            "zh": {
                "question": "如何取回中学毕业证书？",
                "answer": "如需取回中学毕业证书，学生应联系位于 Aviamotornaya 校区的学生人事部门。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "В каком случае могут не выдать диплом?",
                "answer": "Диплом могут не выдать, если не подписан обходной лист, если он не сдан в отдел кадров студентов или если не защищена выпускная работа."
            },
            "en": {
                "question": "In what cases may a diploma not be issued?",
                "answer": "A diploma may not be issued if the clearance form has not been signed, if it has not been submitted to the student HR department, or if the final thesis has not been defended."
            },
            "zh": {
                "question": "在什么情况下可能不发放毕业证书？",
                "answer": "如果离校手续单未签字、未提交到学生人事部门，或毕业论文未通过答辩，可能不会发放毕业证书。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "У меня ошибка в ФИО в зачетной книжке — как исправить?",
                "answer": "Для исправления ошибки в ФИО в зачётной книжке необходимо написать заявление в Едином деканате."
            },
            "en": {
                "question": "There is a mistake in my full name in the gradebook. How can I correct it?",
                "answer": "To correct a mistake in the full name in the gradebook, the student must submit an application at the Unified Dean’s Office."
            },
            "zh": {
                "question": "成绩册中的姓名有错误，如何更正？",
                "answer": "如需更正成绩册中的姓名错误，学生必须在统一院系办公室提交申请。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "В дипломе неверно указана дата — что делать?",
                "answer": "Если в дипломе неверно указана дата, необходимо обратиться в отдел кадров студентов."
            },
            "en": {
                "question": "The date in my diploma is incorrect. What should I do?",
                "answer": "If the date in the diploma is incorrect, the student should contact the student HR department."
            },
            "zh": {
                "question": "毕业证书上的日期有误，该怎么办？",
                "answer": "如果毕业证书上的日期有误，学生应联系学生人事部门。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "В дипломе неверно указана оценка — что делать?",
                "answer": "Если в дипломе неверно указана оценка, необходимо обратиться в Единый деканат."
            },
            "en": {
                "question": "The grade in my diploma is incorrect. What should I do?",
                "answer": "If the grade in the diploma is incorrect, the student should contact the Unified Dean’s Office."
            },
            "zh": {
                "question": "毕业证书上的成绩有误，该怎么办？",
                "answer": "如果毕业证书上的成绩有误，学生应联系统一院系办公室。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "Нужно ли заявление писать от руки или можно напечатать?",
                "answer": "Заявление можно заполнить от руки или напечатать."
            },
            "en": {
                "question": "Should an application be handwritten or can it be typed?",
                "answer": "An application can be either handwritten or typed."
            },
            "zh": {
                "question": "申请书必须手写吗，还是可以打印？",
                "answer": "申请书可以手写，也可以打印。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "Какой срок рассмотрения заявления?",
                "answer": "Срок рассмотрения заявления устанавливает Единый деканат."
            },
            "en": {
                "question": "What is the processing time for an application?",
                "answer": "The processing time for an application is determined by the Unified Dean’s Office."
            },
            "zh": {
                "question": "申请的处理期限是多久？",
                "answer": "申请的处理期限由统一院系办公室确定。"
            }
        }
    },
    {
        "category": "documents",
        "translations": {
            "ru": {
                "question": "Где узнать результат обращения?",
                "answer": "Результат обращения можно узнать в Едином деканате."
            },
            "en": {
                "question": "Where can I find out the result of my application?",
                "answer": "The result of an application can be obtained at the Unified Dean’s Office."
            },
            "zh": {
                "question": "在哪里可以查询申请结果？",
                "answer": "申请结果可以在统一院系办公室查询。"
            }
        }
    }
]

it_support_questions = [
    {
        "category": "it_support",
        "translations": {
            "ru": {
                "question": "Для чего нужен личный кабинет студента?",
                "answer": "Личный кабинет студента используется для оперативного получения информации о результатах успеваемости, прохождения учебной программы при дистанционном обучении, доступа к информационно-образовательной среде и электронным ресурсам библиотечной системы, связи с преподавателями, а также получения информации об учебном плане, образовательной программе, рабочих программах дисциплин и практик."
            },
            "en": {
                "question": "What is the student personal account used for?",
                "answer": "The student personal account is used to quickly access academic performance results, complete the study program during distance learning, access the information and educational environment and electronic library resources, communicate with teachers, and obtain information about the curriculum, educational program, course syllabi, and internship programs."
            },
            "zh": {
                "question": "学生个人账户有什么用途？",
                "answer": "学生个人账户用于快速查看学习成绩、在远程学习期间完成课程、访问信息教育环境和电子图书馆资源、与任课教师联系，以及查看教学计划、教育项目、课程和实习的工作大纲。"
            }
        }
    },
    {
        "category": "it_support",
        "translations": {
            "ru": {
                "question": "Будет ли у студента адрес корпоративной электронной почты?",
                "answer": "Да, у студента будет адрес корпоративной электронной почты. Его выдаёт деканат факультета."
            },
            "en": {
                "question": "Will a student have a corporate email address?",
                "answer": "Yes, the student will have a corporate email address. It is issued by the faculty dean’s office."
            },
            "zh": {
                "question": "学生会有学校企业邮箱吗？",
                "answer": "会的，学生会获得学校企业邮箱地址。该邮箱由学院教务办公室发放。"
            }
        }
    },
    {
        "category": "it_support",
        "translations": {
            "ru": {
                "question": "Как получить доступ в личный кабинет студента?",
                "answer": "Данные для входа в личный кабинет направляются на адрес корпоративной почты студента. Если письмо с данными отсутствует, необходимо обратиться в службу поддержки личного кабинета по адресу lk_support@mtuci.ru."
            },
            "en": {
                "question": "How can I get access to the student personal account?",
                "answer": "Login details for the student personal account are sent to the student’s corporate email address. If the email with login details is missing, contact personal account support at lk_support@mtuci.ru."
            },
            "zh": {
                "question": "如何获得学生个人账户的访问权限？",
                "answer": "学生个人账户的登录信息会发送到学生的学校企业邮箱。如果没有收到包含登录信息的邮件，请联系个人账户支持服务：lk_support@mtuci.ru。"
            }
        }
    },
    {
        "category": "it_support",
        "translations": {
            "ru": {
                "question": "Что делать, если забыл пароль от портала?",
                "answer": "Для восстановления пароля необходимо перейти на страницу авторизации и нажать кнопку «Забыли пароль?»."
            },
            "en": {
                "question": "What should I do if I forgot my portal password?",
                "answer": "To reset your password, go to the authorization page and click the “Forgot password?” button."
            },
            "zh": {
                "question": "忘记密码怎么办",
                "answer": "如需恢复密码，请进入登录页面并点击“忘记密码？”按钮。"
            }
        }
    },
    {
        "category": "it_support",
        "translations": {
            "ru": {
                "question": "Что делать, если не отображаются оценки в личном кабинете?",
                "answer": "Если в личном кабинете не отображаются оценки, необходимо связаться со службой поддержки личного кабинета по адресу lk_support@mtuci.ru и предоставить всю необходимую информацию о проблеме."
            },
            "en": {
                "question": "What should I do if grades are not displayed in my personal account?",
                "answer": "If grades are not displayed in the personal account, contact personal account support at lk_support@mtuci.ru and provide all necessary information about the problem."
            },
            "zh": {
                "question": "如果个人账户中不显示成绩该怎么办？",
                "answer": "如果个人账户中不显示成绩，请联系个人账户支持服务：lk_support@mtuci.ru，并提供有关问题的所有必要信息。"
            }
        }
    },
    {
        "category": "it_support",
        "translations": {
            "ru": {
                "question": "Кому писать при проблемах с корпоративной почтой?",
                "answer": "При проблемах с корпоративной почтой необходимо связаться со службой поддержки личного кабинета по адресу lk_support@mtuci.ru и предоставить всю необходимую информацию о проблеме."
            },
            "en": {
                "question": "Who should I contact if I have problems with corporate email?",
                "answer": "If there are problems with corporate email, contact personal account support at lk_support@mtuci.ru and provide all necessary information about the problem."
            },
            "zh": {
                "question": "学校企业邮箱出现问题应该联系谁？",
                "answer": "如果学校企业邮箱出现问题，请联系个人账户支持服务：lk_support@mtuci.ru，并提供有关问题的所有必要信息。"
            }
        }
    }
]
international_questions = [
    {
        "category": "international",
        "translations": {
            "ru": {
                "question": "Кто курирует иностранных студентов?",
                "answer": "Иностранных студентов курирует иностранный деканат, расположенный на Авиамоторной."
            },
            "en": {
                "question": "Who supervises international students?",
                "answer": "International students are supervised by the international dean’s office located at Aviamotornaya."
            },
            "zh": {
                "question": "谁负责管理国际学生？",
                "answer": "国际学生由位于 Aviamotornaya 校区的国际学生教务办公室负责管理。"
            }
        }
    },
    {
        "category": "international",
        "translations": {
            "ru": {
                "question": "Какие документы нужно продлевать иностранному студенту?",
                "answer": "Иностранному студенту необходимо следить за актуальностью документов, связанных с пребыванием в Российской Федерации. Для продления обычно требуются оригинал и две копии заполненных страниц паспорта, оригинал и две копии миграционной карты, оригинал и две копии регистрации, фотография 3×4, копия карты дактилоскопии, а также копия действующих сертификатов медицинского освидетельствования."
            },
            "en": {
                "question": "What documents does an international student need to renew?",
                "answer": "An international student must keep documents related to their stay in the Russian Federation up to date. Renewal usually requires the original and two copies of the completed passport pages, the original and two copies of the migration card, the original and two copies of registration, a 3×4 photo, a copy of the fingerprint registration card, and copies of valid medical examination certificates."
            },
            "zh": {
                "question": "国际学生需要续办哪些文件？",
                "answer": "国际学生需要确保与在俄罗斯联邦居留有关的文件保持有效。通常需要提交护照已填写页面的原件和两份复印件、移民卡原件和两份复印件、登记证明原件和两份复印件、3×4照片、指纹登记卡复印件，以及有效体检证明的复印件。"
            }
        }
    },
    {
        "category": "international",
        "translations": {
            "ru": {
                "question": "Что делать, если заканчивается виза?",
                "answer": "Если у иностранного студента заканчивается виза, необходимо своевременно обратиться в иностранный деканат и продлить визу в установленном порядке."
            },
            "en": {
                "question": "What should I do if my visa is expiring?",
                "answer": "If an international student’s visa is expiring, they must contact the international dean’s office in advance and renew the visa according to the established procedure."
            },
            "zh": {
                "question": "如果签证快到期了该怎么办？",
                "answer": "如果国际学生的签证即将到期，需要提前联系国际学生教务办公室，并按照规定程序办理签证延期。"
            }
        }
    },
    {
        "category": "international",
        "translations": {
            "ru": {
                "question": "Как оформить справку для миграционной службы?",
                "answer": "Если требуется справка для миграционной службы, возможно, имеется в виду справка о месте регистрации. Получить её можно в подразделении по вопросам миграции МВД по месту пребывания, то есть в паспортном столе."
            },
            "en": {
                "question": "How can I obtain a certificate for the migration service?",
                "answer": "If a certificate for the migration service is required, it may refer to a certificate of place of registration. It can be obtained from the migration department of the Ministry of Internal Affairs at the place of stay, that is, at the passport office."
            },
            "zh": {
                "question": "如何办理移民部门所需的证明？",
                "answer": "如果需要提交给移民部门的证明，通常可能指居住登记地点证明。该证明可在居住地的俄罗斯内务部移民事务部门办理，也就是护照办公室。"
            }
        }
    },
    {
        "category": "international",
        "translations": {
            "ru": {
                "question": "Можно ли иностранному студенту работать во время учёбы?",
                "answer": "Иностранные обучающиеся имеют право осуществлять трудовую деятельность в свободное от учёбы время без разрешения на работу в образовательной организации высшего образования, где они обучаются, а также выполнять работу в других организациях во время каникул. При этом работодатель должен корректно оформить трудоустройство и подать в территориальный орган МВД уведомление о заключении трудового договора с иностранным обучающимся."
            },
            "en": {
                "question": "Can an international student work while studying?",
                "answer": "International students may work in their free time without a work permit at the higher education institution where they study, and may also work in other organizations during vacations. The employer must properly formalize the employment and submit a notification of the employment contract with the international student to the territorial body of the Ministry of Internal Affairs."
            },
            "zh": {
                "question": "国际学生在学习期间可以工作吗？",
                "answer": "国际学生可以在课余时间在其就读的高等教育机构工作，无需办理工作许可；也可以在假期期间在其他组织工作。但雇主必须依法办理劳动关系，并向当地内务部机构提交与国际学生签订劳动合同的通知。"
            }
        }
    },
    {
        "category": "international",
        "translations": {
            "ru": {
                "question": "Могут ли иностранные студенты проходить практику в российских организациях?",
                "answer": "Иностранные обучающиеся могут проходить практику в российских организациях, согласных их принять, если для этого не требуется оформление формы допуска. Также практика может проходить на кафедрах, в лабораториях и других подразделениях университета. Кроме того, иностранные обучающиеся могут быть направлены для прохождения практики в организации зарубежных стран при выполнении всех необходимых согласующих процедур."
            },
            "en": {
                "question": "Can international students do internships in Russian organizations?",
                "answer": "International students may do internships in Russian organizations that agree to accept them, provided that no special access clearance is required. Internships may also take place at departments, laboratories, and other university units. In addition, international students may be sent for internships to organizations in other countries if all required approval procedures are completed."
            },
            "zh": {
                "question": "国际学生可以在俄罗斯机构实习吗？",
                "answer": "国际学生可以在同意接收他们的俄罗斯机构实习，前提是不需要办理特殊准入许可。实习也可以在大学的教研室、实验室和其他部门进行。此外，在完成所有必要审批程序后，国际学生也可以被派往国外机构实习。"
            }
        }
    },
    {
        "category": "international",
        "translations": {
            "ru": {
                "question": "Нужно ли иностранному студенту подтверждать знание русского языка?",
                "answer": "Да. При поступлении в МТУСИ иностранные граждане, не владеющие русским языком, проходят предварительное обучение по дополнительной образовательной программе на подготовительном отделении с последующей сдачей вступительных испытаний на русском языке."
            },
            "en": {
                "question": "Does an international student need to confirm knowledge of the Russian language?",
                "answer": "Yes. When applying to MTUCI, foreign citizens who do not know Russian complete preliminary training under an additional educational program at the preparatory department and then take entrance examinations in Russian."
            },
            "zh": {
                "question": "国际学生需要证明俄语水平吗？",
                "answer": "需要。申请进入莫斯科通信与信息技术大学时，不掌握俄语的外国公民需要先在预科部门完成补充教育课程，然后用俄语参加入学考试。"
            }
        }
    }
]

medical_questions = [
    {
        "category": "medical",
        "translations": {
            "ru": {
                "question": "Где взять справку в случае болезни?",
                "answer": "Справку в случае болезни предоставляет медицинское учреждение. Справку необходимо сдать в деканат или Единый деканат в течение 3 дней после получения. На справке должно быть 3 печати."
            },
            "en": {
                "question": "Where can I get a medical certificate in case of illness?",
                "answer": "A medical certificate in case of illness is issued by a medical institution. The certificate must be submitted to the dean’s office or the Unified Dean’s Office within 3 days after receiving it. The certificate must have 3 stamps."
            },
            "zh": {
                "question": "生病时在哪里可以获得医疗证明？",
                "answer": "生病时的医疗证明由医疗机构出具。收到证明后，必须在3天内将其提交到院系办公室或统一院系办公室。证明上必须有3个印章。"
            }
        }
    },
    {
        "category": "medical",
        "translations": {
            "ru": {
                "question": "Кто подписывает справки по форме 095/у?",
                "answer": "Справку по форме 095/у подписывает врач в медицинском учреждении. На справке должно быть 3 печати."
            },
            "en": {
                "question": "Who signs medical certificates in form 095/u?",
                "answer": "A medical certificate in form 095/u is signed by a doctor at a medical institution. The certificate must have 3 stamps."
            },
            "zh": {
                "question": "095/u格式的医疗证明由谁签署？",
                "answer": "095/u格式的医疗证明由医疗机构的医生签署。证明上必须有3个印章。"
            }
        }
    },
    {
        "category": "medical",
        "translations": {
            "ru": {
                "question": "Как получить справку для санатория?",
                "answer": "Справку для санатория необходимо оформить в медицинском учреждении."
            },
            "en": {
                "question": "How can I get a certificate for a sanatorium?",
                "answer": "A certificate for a sanatorium must be issued by a medical institution."
            },
            "zh": {
                "question": "如何获得疗养院所需的证明？",
                "answer": "疗养院所需的证明必须在医疗机构办理。"
            }
        }
    }
]
housing_questions = [
    {
        "category": "housing",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для заселения в общежитие?",
                "answer": "Для заселения в общежитие необходимы ксерокопия паспорта, включая первую страницу и страницу с пропиской; справка из отдела кадров о том, что обучающийся является студентом МТУСИ; медицинская справка по форме 086/у с отметкой о прохождении флюорографии или рентгенографии органов грудной клетки давностью не более 1 года; анализ крови на RW; заключение врача-дерматолога об отсутствии кожных заболеваний; справка из наркодиспансера о том, что студент не состоит на учёте; заявление о заселении в общежитие. При наличии льготной категории она должна быть подтверждена соответствующими документами."
            },
            "en": {
                "question": "What documents are required for dormitory accommodation?",
                "answer": "For dormitory accommodation, the following documents are required: a copy of the passport, including the first page and the page with registration; a certificate from the HR department confirming that the person is an MTUCI student; a medical certificate in form 086/u with a note on fluorography or chest X-ray completed no more than 1 year ago; an RW blood test; a dermatologist’s conclusion confirming the absence of skin diseases; a certificate from a narcological dispensary confirming that the student is not registered there; and an application for dormitory accommodation. If the student belongs to a preferential category, this must be confirmed by relevant documents."
            },
            "zh": {
                "question": "入住宿舍需要哪些文件？",
                "answer": "入住宿舍需要以下文件：护照复印件，包括第一页和登记页；学生人事部门出具的莫斯科通信与信息技术大学学生证明；086/u格式医疗证明，其中应包含一年内完成的胸部透视或X光检查记录；RW血液检测结果；皮肤科医生出具的无皮肤病证明；麻醉药物依赖诊所出具的未登记证明；宿舍入住申请。如学生属于优惠类别，还需提供相应证明文件。"
            }
        }
    },
    {
        "category": "housing",
        "translations": {
            "ru": {
                "question": "Кому предоставляется общежитие?",
                "answer": "Общежитие предоставляется студентам бюджетной или договорной формы обучения по конкурсу, если они проживают или зарегистрированы на расстоянии более 60 км от МКАД."
            },
            "en": {
                "question": "Who is eligible for dormitory accommodation?",
                "answer": "Dormitory accommodation is provided on a competitive basis to students studying on a state-funded or tuition-paying basis, if they live or are registered more than 60 km from the Moscow Ring Road."
            },
            "zh": {
                "question": "哪些学生可以申请宿舍？",
                "answer": "宿舍按照竞争性分配原则提供给预算制或合同制学生，条件是学生居住地或登记地距离莫斯科环城公路超过60公里。"
            }
        }
    },
    {
        "category": "housing",
        "translations": {
            "ru": {
                "question": "Как заселиться в общежитие?",
                "answer": "Заселение в общежитие происходит в конце августа после заключения договора и оплаты проживания. Конкретные даты заранее публикуются на сайте приёмной комиссии. Перед переездом необходимо убедиться, что студент есть в списках на заселение, которые публикуются на сайте."
            },
            "en": {
                "question": "How can I move into the dormitory?",
                "answer": "Dormitory check-in takes place at the end of August after the contract is signed and accommodation is paid for. Specific dates are published in advance on the admissions committee website. Before moving in, the student must make sure that their name is included in the check-in lists published on the website."
            },
            "zh": {
                "question": "如何入住宿舍？",
                "answer": "宿舍入住通常在8月底进行，需先签订合同并支付住宿费。具体日期会提前公布在招生委员会网站上。搬入前，学生必须确认自己已列入网站公布的入住名单。"
            }
        }
    },
    {
        "category": "housing",
        "translations": {
            "ru": {
                "question": "Что делать, если студенту нет 18 лет при заселении в общежитие?",
                "answer": "Студенты, не достигшие 18 лет, в том числе дети-сироты, должны оформлять документы для заселения в общежитие в присутствии родителей или опекуна с предъявлением документов, подтверждающих личность. Также возможно оформление документов на основании доверенности или согласия родителей либо опекуна."
            },
            "en": {
                "question": "What should I do if I am under 18 when moving into the dormitory?",
                "answer": "Students under the age of 18, including orphans, must complete the dormitory accommodation documents in the presence of their parents or guardian, with identity documents presented. It is also possible to complete the documents based on a power of attorney or consent from the parents or guardian."
            },
            "zh": {
                "question": "如果入住宿舍时未满18岁该怎么办？",
                "answer": "未满18岁的学生，包括孤儿，在办理宿舍入住文件时必须由父母或监护人在场，并出示身份证明文件。也可以根据父母或监护人的授权书或同意书办理入住文件。"
            }
        }
    },
    {
        "category": "housing",
        "translations": {
            "ru": {
                "question": "Кто признается не нуждающимся в общежитии?",
                "answer": "Обучающийся признаётся не нуждающимся в общежитии и теряет право на проживание, если без уважительной причины не заключил договор до 10 сентября текущего года, либо если заключил договор на проживание, получил ордер на заселение, но не заселился в течение 5 дней после получения ордера."
            },
            "en": {
                "question": "Who is considered not to need dormitory accommodation?",
                "answer": "A student is considered not to need dormitory accommodation and loses the right to live in the dormitory if they fail to sign the contract without a valid reason by September 10 of the current year, or if they signed the accommodation contract, received a check-in order, but did not move in within 5 days after receiving it."
            },
            "zh": {
                "question": "哪些学生会被认定为不需要宿舍？",
                "answer": "如果学生无正当理由未在当年9月10日前签订合同，或已签订住宿合同并获得入住通知但在收到通知后5天内未入住，将被认定为不需要宿舍，并失去住宿权利。"
            }
        }
    },
    {
        "category": "housing",
        "translations": {
            "ru": {
                "question": "Где находятся общежития МТУСИ?",
                "answer": "Общежития МТУСИ расположены по адресам: ул. Маршала Тухачевского, 18; ул. Авиамоторная, 8А, стр. 7; 2-й Кабельный проезд, 4."
            },
            "en": {
                "question": "Where are the MTUCI dormitories located?",
                "answer": "MTUCI dormitories are located at the following addresses: 18 Marshal Tukhachevsky Street; 8A Aviamotornaya Street, building 7; 4 2nd Kabelny Passage."
            },
            "zh": {
                "question": "莫斯科通信与信息技术大学宿舍在哪里？",
                "answer": "莫斯科通信与信息技术大学宿舍地址如下：Marshal Tukhachevsky 街18号；Aviamotornaya 街8A号7栋；2nd Kabelny Passage 4号。"
            }
        }
    }
]
organizational_questions = [
    {
        "category": "general",
        "translations": {
            "ru": {
                "question": "Как получить или восстановить студенческий пропуск?",
                "answer": "Для получения или восстановления студенческого пропуска необходимо лично обратиться либо в банк, если пропуск привязан к банковской карте, либо в отдел выдачи пропусков на Авиамоторной, кабинет 121."
            },
            "en": {
                "question": "How can I get or restore a student pass?",
                "answer": "To get or restore a student pass, you need to personally contact either the bank, if the pass is linked to a bank card, or the pass issuance office at Aviamotornaya, room 121."
            },
            "zh": {
                "question": "如何办理或恢复学生通行证？",
                "answer": "如需办理或恢复学生通行证，需要本人前往相关银行办理（如果通行证与银行卡绑定），或前往 Aviamotornaya 校区121室的通行证发放部门。"
            }
        }
    },
    {
        "category": "general",
        "translations": {
            "ru": {
                "question": "Можно ли пройти в корпус без пропуска?",
                "answer": "Первокурсники могут проходить в корпус по спискам от деканата факультета, если им ещё не выдали студенческий пропуск."
            },
            "en": {
                "question": "Can I enter the building without a student pass?",
                "answer": "First-year students may enter the building according to lists provided by the faculty dean’s office if they have not yet received a student pass."
            },
            "zh": {
                "question": "没有学生通行证可以进入教学楼吗？",
                "answer": "如果一年级学生尚未收到学生通行证，可以根据学院教务办公室提供的名单进入教学楼。"
            }
        }
    },
    {
        "category": "general",
        "translations": {
            "ru": {
                "question": "Как связаться с руководством факультета?",
                "answer": "Для связи с руководством факультета необходимо обратиться в деканат факультета. Контакты деканата размещены на сайте МТУСИ."
            },
            "en": {
                "question": "How can I contact the faculty administration?",
                "answer": "To contact the faculty administration, you should contact the faculty dean’s office. The dean’s office contact details are available on the MTUCI website."
            },
            "zh": {
                "question": "如何联系学院领导？",
                "answer": "如需联系学院领导，应联系学院教务办公室。教务办公室联系方式可在莫斯科通信与信息技术大学网站上查看。"
            }
        }
    },
    {
        "category": "general",
        "translations": {
            "ru": {
                "question": "Куда обращаться по любым вопросам?",
                "answer": "По общим вопросам можно обратиться в Единый деканат, в деканат факультета или на горячую линию университета по телефону +7 (495) 957-77-31."
            },
            "en": {
                "question": "Where should I go for general questions?",
                "answer": "For general questions, you can contact the Unified Dean’s Office, your faculty dean’s office, or the university hotline at +7 (495) 957-77-31."
            },
            "zh": {
                "question": "有任何问题应该联系哪里？",
                "answer": "如有一般问题，可以联系统一教务办公室、学院教务办公室，或拨打大学热线电话 +7 (495) 957-77-31。"
            }
        }
    },
    {
        "category": "general",
        "translations": {
            "ru": {
                "question": "Куда обращаться по вопросам безопасности?",
                "answer": "По вопросам безопасности можно обратиться в деканат факультета или на горячую линию университета по телефону +7 (495) 957-77-31. Также можно обратиться в Федеральную службу безопасности Российской Федерации по телефону +7 (495) 224-22-22 или по адресу: 107031, г. Москва, ул. Большая Лубянка, д. 1/3. По вопросам чрезвычайных ситуаций можно обратиться в МЧС России по единому телефону доверия +7 (499) 449-99-99 или по адресу: 109012, г. Москва, Театральный пр., д. 3."
            },
            "en": {
                "question": "Where should I report security-related issues?",
                "answer": "For security-related issues, you can contact your faculty dean’s office or the university hotline at +7 (495) 957-77-31. You may also contact the Federal Security Service of the Russian Federation by phone at +7 (495) 224-22-22 or at 1/3 Bolshaya Lubyanka Street, Moscow, 107031. For emergency-related issues, you may contact EMERCOM of Russia through the trust line +7 (499) 449-99-99 or at 3 Teatralny Proezd, Moscow, 109012."
            },
            "zh": {
                "question": "安全相关问题应联系哪里？",
                "answer": "如有安全相关问题，可以联系学院教务办公室或拨打大学热线 +7 (495) 957-77-31。也可以联系俄罗斯联邦安全局，电话：+7 (495) 224-22-22，地址：107031，莫斯科，Bolshaya Lubyanka 街1/3号。紧急情况相关问题可联系俄罗斯紧急情况部，信任热线：+7 (499) 449-99-99，地址：109012，莫斯科，Teatralny Proezd 3号。"
            }
        }
    },
    {
        "category": "general",
        "translations": {
            "ru": {
                "question": "Есть ли горячая линия университета?",
                "answer": "Да, горячая линия университета доступна по номеру телефона +7 (495) 957-77-31."
            },
            "en": {
                "question": "Does the university have a hotline?",
                "answer": "Yes, the university hotline is available at +7 (495) 957-77-31."
            },
            "zh": {
                "question": "大学有热线电话吗？",
                "answer": "有，大学热线电话是 +7 (495) 957-77-31。"
            }
        }
    }
]

transfer_questions = [
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Когда можно перевестись или восстановиться в МТУСИ?",
                "answer": "Процедура восстановления и перевода в МТУСИ осуществляется дважды в год на соответствующий семестр."
            },
            "en": {
                "question": "When can I transfer or be reinstated at MTUCI?",
                "answer": "The transfer and reinstatement procedure at MTUCI is carried out twice a year for the corresponding semester."
            },
            "zh": {
                "question": "什么时候可以转入或恢复莫斯科通信与信息技术大学的学籍？",
                "answer": "莫斯科通信与信息技术大学的转学和恢复学籍程序每年进行两次，分别对应相应学期。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Как осуществляется перевод или восстановление?",
                "answer": "Восстановление и перевод обучающихся осуществляется на основании личного заявления заявителя."
            },
            "en": {
                "question": "How is transfer or reinstatement carried out?",
                "answer": "Student transfer and reinstatement are carried out based on the applicant’s personal application."
            },
            "zh": {
                "question": "转学或恢复学籍如何办理？",
                "answer": "学生转学或恢复学籍根据申请人的个人申请办理。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Кто принимает решение о переводе или восстановлении?",
                "answer": "Решение о восстановлении или переводе на бюджетные места принимается Комиссией на основании рекомендации Аттестационной комиссии и оформляется протоколом и приказом ректора. Решение о восстановлении или переводе на платные места принимается на основании решения Аттестационной комиссии и также оформляется протоколом и приказом ректора университета."
            },
            "en": {
                "question": "Who makes the decision on transfer or reinstatement?",
                "answer": "The decision on reinstatement or transfer to state-funded places is made by the Commission based on the recommendation of the Attestation Commission and is formalized by a protocol and an order of the rector. The decision on reinstatement or transfer to tuition-paying places is made based on the decision of the Attestation Commission and is also formalized by a protocol and an order of the rector."
            },
            "zh": {
                "question": "谁决定转学或恢复学籍？",
                "answer": "恢复学籍或转入预算名额的决定由委员会根据认证委员会的建议作出，并通过会议记录和校长命令正式确认。恢复学籍或转入付费名额的决定根据认证委员会的决定作出，也通过会议记录和校长命令正式确认。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Сколько раз принимаются документы на восстановление или перевод?",
                "answer": "Приём документов для восстановления лиц, ранее обучавшихся в МТУСИ, перевода из других образовательных организаций в МТУСИ и перевода внутри университета проводится дважды в год на соответствующий семестр."
            },
            "en": {
                "question": "How often are documents accepted for reinstatement or transfer?",
                "answer": "Documents for reinstatement of former MTUCI students, transfer from other educational organizations to MTUCI, and internal transfer within the university are accepted twice a year for the corresponding semester."
            },
            "zh": {
                "question": "恢复学籍或转学文件一年接收几次？",
                "answer": "曾在莫斯科通信与信息技术大学学习人员的恢复学籍、从其他教育机构转入莫斯科通信与信息技术大学以及校内转专业的文件每年接收两次，对应相应学期。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Когда осуществляется приём документов на перевод или восстановление?",
                "answer": "Приём документов по восстановлению и переводу в МТУСИ осуществляется до начала семестра. Информация о сроках приёма документов размещается на официальном сайте МТУСИ в разделе «Студенту»."
            },
            "en": {
                "question": "When are documents accepted for transfer or reinstatement?",
                "answer": "Documents for reinstatement and transfer to MTUCI are accepted before the beginning of the semester. Information about document submission deadlines is published on the official MTUCI website in the “Student” section."
            },
            "zh": {
                "question": "转学或恢复学籍的文件什么时候提交？",
                "answer": "恢复学籍和转入莫斯科通信与信息技术大学的文件在学期开始前提交。文件接收期限的信息发布在莫斯科通信与信息技术大学官网“学生”栏目。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Сколько заявлений можно подать на один конкурс?",
                "answer": "Заявитель может подать не более 5 заявлений в совокупности на один конкурс."
            },
            "en": {
                "question": "How many applications can be submitted for one competition?",
                "answer": "An applicant may submit no more than 5 applications in total for one competition."
            },
            "zh": {
                "question": "一次选拔可以提交多少份申请？",
                "answer": "申请人在一次选拔中总共最多可以提交5份申请。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Куда нужно направить заявление на восстановление или перевод?",
                "answer": "При восстановлении и переводе из другой образовательной организации, переводе с одной формы обучения на другую или с одной образовательной программы на другую заявитель из числа граждан РФ направляет заявление и необходимый пакет документов в ЦРО-ЕД — Центр по работе с обучающимися, Единый деканат."
            },
            "en": {
                "question": "Where should I send an application for reinstatement or transfer?",
                "answer": "For reinstatement, transfer from another educational organization, transfer from one form of study to another, or transfer from one educational program to another, an applicant who is a citizen of the Russian Federation submits the application and required documents to the Unified Dean’s Office, the Center for Student Services."
            },
            "zh": {
                "question": "恢复学籍或转学申请应提交到哪里？",
                "answer": "恢复学籍、从其他教育机构转入、从一种学习形式转到另一种学习形式，或从一个教育项目转到另一个教育项目时，俄罗斯联邦公民申请人需将申请和所需文件提交至学生服务中心—统一教务办公室。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Как можно предоставить заявление и пакет документов на перевод или восстановление?",
                "answer": "Документы можно предоставить лично в МТУСИ заявителем или законным представителем, направить в электронной форме на адрес ed@mtuci.ru или через личный кабинет при наличии доступа. Для иностранных граждан документы направляются на электронную почту отдела по работе с иностранными учащимися indec@mtuci.ru. Также документы можно направить почтой по адресу: 111024, г. Москва, ул. Авиамоторная, д. 8а, МТУСИ, Центр по работе с обучающимися, Единый деканат."
            },
            "en": {
                "question": "How can I submit an application and documents for transfer or reinstatement?",
                "answer": "Documents may be submitted in person to MTUCI by the applicant or legal representative, sent electronically to ed@mtuci.ru, or submitted through the personal account if access is available. International students submit documents to the department for international students at indec@mtuci.ru. Documents may also be sent by post to: 8a Aviamotornaya Street, Moscow, 111024, MTUCI, Center for Student Services, Unified Dean’s Office."
            },
            "zh": {
                "question": "如何提交转学或恢复学籍申请及文件？",
                "answer": "文件可由申请人或法定代表人亲自提交至莫斯科通信与信息技术大学，也可发送电子版至 ed@mtuci.ru，或在有访问权限时通过个人账户提交。国际学生需将文件发送至国际学生事务部门邮箱 indec@mtuci.ru。也可邮寄至：111024，莫斯科，Aviamotornaya 街8A号，莫斯科通信与信息技术大学，学生服务中心，统一教务办公室。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "В каком случае можно перевестись в МТУСИ из другой образовательной организации?",
                "answer": "Право перевода в МТУСИ имеют обучающиеся государственных и негосударственных образовательных организаций, имеющих государственную аккредитацию. Перевод возможен при наличии образования, требуемого для освоения соответствующей образовательной программы высшего образования, в том числе при получении образования за рубежом."
            },
            "en": {
                "question": "When can I transfer to MTUCI from another educational organization?",
                "answer": "Students of state and non-state educational organizations with state accreditation have the right to transfer to MTUCI. Transfer is possible if the student has the education required to study the corresponding higher education program, including education received abroad."
            },
            "zh": {
                "question": "什么情况下可以从其他教育机构转入莫斯科通信与信息技术大学？",
                "answer": "具有国家认证的公立和非公立教育机构的学生有权转入莫斯科通信与信息技术大学。转学需具备学习相应高等教育课程所要求的教育基础，包括在国外获得的教育。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "На какие формы обучения можно перевестись в МТУСИ?",
                "answer": "Обучающиеся могут быть переведены в МТУСИ из других образовательных организаций как на бюджетные места, так и на места по договорам об оказании платных образовательных услуг при наличии вакантных мест на соответствующем курсе."
            },
            "en": {
                "question": "What forms of study can I transfer to at MTUCI?",
                "answer": "Students may transfer to MTUCI from other educational organizations either to state-funded places or to tuition-paying places, provided that there are vacant places in the corresponding year of study."
            },
            "zh": {
                "question": "可以转入莫斯科通信与信息技术大学的哪些学习形式？",
                "answer": "学生可以从其他教育机构转入莫斯科通信与信息技术大学的预算名额或付费名额，前提是在相应年级有空余名额。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Можно ли перевестись с одной образовательной программы на другую?",
                "answer": "Да. Перевод обучающихся из других образовательных организаций в МТУСИ может сопровождаться переходом с одной образовательной программы на другую, а также сменой формы обучения."
            },
            "en": {
                "question": "Can I transfer from one educational program to another?",
                "answer": "Yes. Transfer from other educational organizations to MTUCI may involve changing from one educational program to another, as well as changing the form of study."
            },
            "zh": {
                "question": "可以从一个教育项目转到另一个教育项目吗？",
                "answer": "可以。从其他教育机构转入莫斯科通信与信息技术大学时，可以同时从一个教育项目转到另一个教育项目，也可以改变学习形式。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для перевода в МТУСИ из другой образовательной организации?",
                "answer": "Для перевода предоставляются: личное заявление о переводе, копия документа, удостоверяющего личность и гражданство, справка о периоде обучения по соответствующей образовательной программе, документ о предшествующем образовании, документы, подтверждающие индивидуальные достижения при наличии, копия СНИЛС и ИНН кроме иностранных граждан, фото 3×4 в количестве 6 штук на матовой фотобумаге, а также иные документы по усмотрению обучающегося."
            },
            "en": {
                "question": "What documents are required to transfer to MTUCI from another educational organization?",
                "answer": "The following documents are required: a personal transfer application, a copy of an identity and citizenship document, a certificate of the period of study for the relevant educational program, a previous education document, documents confirming individual achievements if available, copies of SNILS and TIN except for foreign citizens, six 3×4 photos on matte photo paper, and other documents at the student’s discretion."
            },
            "zh": {
                "question": "从其他教育机构转入莫斯科通信与信息技术大学需要哪些文件？",
                "answer": "需要提交：个人转学申请、身份证明和国籍证明文件复印件、相应教育项目学习期间证明、先前教育证明文件、个人成就证明文件如有、SNILS和INN复印件但外国公民除外、6张3×4磨砂照片，以及学生认为需要提交的其他文件。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "В течение какого срока можно восстановиться в МТУСИ после отчисления?",
                "answer": "Лица, отчисленные из МТУСИ по собственному желанию или по другой уважительной причине, имеют право на восстановление в течение 5 лет с даты отчисления при наличии вакантных мест и с сохранением основы обучения. Лица, отчисленные по инициативе университета, также могут восстановиться в течение 5 лет после отчисления при наличии вакантных мест и с сохранением прежних условий обучения, но не ранее завершения учебного года или семестра, в котором они были отчислены."
            },
            "en": {
                "question": "How long after expulsion can I be reinstated at MTUCI?",
                "answer": "Persons expelled from MTUCI at their own request or for another valid reason have the right to reinstatement within 5 years from the date of expulsion, if there are vacant places and with the same funding basis. Persons expelled at the initiative of the university may also be reinstated within 5 years if vacant places are available and the previous study conditions are preserved, but not earlier than the end of the academic year or semester in which they were expelled."
            },
            "zh": {
                "question": "退学后多长时间内可以恢复莫斯科通信与信息技术大学学籍？",
                "answer": "因本人意愿或其他正当原因被莫斯科通信与信息技术大学退学的人员，自退学之日起5年内，在有空余名额并保留原学习基础的情况下有权恢复学籍。因大学方面原因被退学的人员，在有空余名额并保留原学习条件的情况下，也可在退学后5年内恢复学籍，但不得早于其被退学所在学年或学期结束。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "На какой семестр осуществляется восстановление?",
                "answer": "Восстановление возможно на семестр, следующий за последним семестром, в котором был полностью выполнен учебный план."
            },
            "en": {
                "question": "For which semester is reinstatement possible?",
                "answer": "Reinstatement is possible for the semester following the last semester in which the curriculum was fully completed."
            },
            "zh": {
                "question": "可以恢复到哪个学期？",
                "answer": "可以恢复到最后一个已完全完成教学计划的学期之后的下一学期。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Что делать, если прежняя образовательная программа больше не реализуется?",
                "answer": "Если образовательная программа высшего образования, по которой обучался восстанавливающийся, в настоящее время не реализуется, заявитель имеет право по заявлению восстановиться на образовательную программу, которая реализуется в настоящее время."
            },
            "en": {
                "question": "What should I do if my previous educational program is no longer offered?",
                "answer": "If the higher education program in which the applicant previously studied is no longer offered, the applicant has the right to apply for reinstatement to a currently available higher education program."
            },
            "zh": {
                "question": "如果原来的教育项目现在不再开设，该怎么办？",
                "answer": "如果申请人原来学习的高等教育项目目前不再开设，申请人有权通过申请恢复到目前正在实施的高等教育项目。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Кто не имеет права на восстановление?",
                "answer": "Не имеет права на восстановление лицо, ранее обучавшееся в МТУСИ и отчисленное за нарушение порядка приёма в образовательную организацию, повлекшее по его вине незаконное зачисление. Также не допускается восстановление лиц, отчисленных с 1 курса и не прошедших в полном объёме первую промежуточную аттестацию."
            },
            "en": {
                "question": "Who is not eligible for reinstatement?",
                "answer": "A person previously studying at MTUCI who was expelled for violating the admission procedure resulting in unlawful enrollment through their fault is not eligible for reinstatement. Reinstatement is also not allowed for persons expelled from the first year who did not fully pass the first interim assessment."
            },
            "zh": {
                "question": "哪些人没有恢复学籍的权利？",
                "answer": "曾在莫斯科通信与信息技术大学学习并因违反招生程序、因本人原因导致非法录取而被退学的人员无权恢复学籍。第一年级被退学且未完整通过第一次中期考核的人员也不得恢复学籍。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "В каком случае можно восстановиться на курс выше?",
                "answer": "Лицо, ранее обучавшееся в МТУСИ на очной форме обучения, при восстановлении на заочную форму обучения может быть восстановлено на курс выше, если срок обучения по учебному плану заочной формы обучения не менее чем на 6 месяцев превышает срок обучения по учебному плану очной формы обучения."
            },
            "en": {
                "question": "When can a student be reinstated to a higher year of study?",
                "answer": "A person who previously studied full-time at MTUCI may be reinstated to part-time study one year higher if the duration of the part-time curriculum is at least 6 months longer than the duration of the full-time curriculum."
            },
            "zh": {
                "question": "什么情况下可以恢复到更高年级？",
                "answer": "曾在莫斯科通信与信息技术大学全日制学习的人员，在恢复到函授或非全日制学习时，如果该学习形式的教学计划期限比全日制教学计划至少长6个月，可以恢复到更高年级。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для восстановления в МТУСИ?",
                "answer": "Для восстановления в МТУСИ заявитель предоставляет в ЦРО-ЕД личное заявление о восстановлении, справку о периоде обучения по соответствующей образовательной программе, копию документа, удостоверяющего личность, документы, подтверждающие индивидуальные достижения при наличии, копию СНИЛС и ИНН кроме иностранных граждан, фото 3×4 в количестве 6 штук на матовой фотобумаге, а также иные документы по усмотрению обучающегося."
            },
            "en": {
                "question": "What documents are required for reinstatement at MTUCI?",
                "answer": "For reinstatement at MTUCI, the applicant submits to the Unified Dean’s Office a personal application for reinstatement, a certificate of the period of study for the relevant educational program, a copy of an identity document, documents confirming individual achievements if available, copies of SNILS and TIN except for foreign citizens, six 3×4 photos on matte photo paper, and other documents at the applicant’s discretion."
            },
            "zh": {
                "question": "恢复莫斯科通信与信息技术大学学籍需要哪些文件？",
                "answer": "恢复学籍时，申请人需向统一教务办公室提交恢复学籍个人申请、相应教育项目学习期间证明、身份证明文件复印件、个人成就证明文件如有、SNILS和INN复印件但外国公民除外、6张3×4磨砂照片，以及申请人认为需要提交的其他文件。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Кто может перевестись из МТУСИ в другую образовательную организацию?",
                "answer": "Обучающийся МТУСИ вправе перевестись в другую образовательную организацию при согласии этой образовательной организации. Для этого обучающийся подаёт в ЦРО-ЕД заявление о выдаче справки о периоде обучения по соответствующей образовательной программе в связи с намерением быть переведённым в другую образовательную организацию."
            },
            "en": {
                "question": "Who can transfer from MTUCI to another educational organization?",
                "answer": "An MTUCI student has the right to transfer to another educational organization with the consent of that organization. To do this, the student submits an application to the Unified Dean’s Office for a certificate of the period of study for the relevant educational program due to the intention to transfer to another educational organization."
            },
            "zh": {
                "question": "谁可以从莫斯科通信与信息技术大学转到其他教育机构？",
                "answer": "莫斯科通信与信息技术大学学生在获得其他教育机构同意的情况下，有权转到该机构。为此，学生需向统一教务办公室提交申请，要求出具相应教育项目学习期间证明，以便转入其他教育机构。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Когда выдаётся копия приказа об отчислении при переводе в другую образовательную организацию?",
                "answer": "Лицу, отчисленному в связи с переводом в другую образовательную организацию, в течение 3 рабочих дней со дня издания приказа об отчислении выдаётся заверенная копия приказа или выписка из приказа, справка об обучении и оригинал документа об образовании или об образовании и квалификации при наличии."
            },
            "en": {
                "question": "When is a copy of the expulsion order issued when transferring to another educational organization?",
                "answer": "A person expelled due to transfer to another educational organization receives, within 3 working days from the date of the expulsion order, a certified copy of the order or an extract from it, a certificate of study, and the original education or qualification document if available."
            },
            "zh": {
                "question": "转到其他教育机构时，退学命令副本什么时候发放？",
                "answer": "因转入其他教育机构而被退学的人员，自退学命令发布之日起3个工作日内，会收到经认证的命令副本或摘录、学习证明，以及教育或学历资格文件原件如有。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Кем осуществляется перевод внутри МТУСИ?",
                "answer": "Перевод обучающихся внутри МТУСИ с одной образовательной программы на другую, в том числе с изменением формы обучения, направления подготовки, научной специальности или условий освоения образовательной программы, осуществляется приказом ректора университета на основании личного заявления обучающегося, учебной карточки и протокола Аттестационной комиссии или Комиссии."
            },
            "en": {
                "question": "Who carries out internal transfer within MTUCI?",
                "answer": "Internal transfer within MTUCI from one educational program to another, including changes in form of study, field of study, scientific specialty, or study conditions, is carried out by an order of the rector based on the student’s personal application, academic record card, and the protocol of the Attestation Commission or Commission."
            },
            "zh": {
                "question": "莫斯科通信与信息技术大学内部转专业由谁办理？",
                "answer": "莫斯科通信与信息技术大学内部从一个教育项目转到另一个教育项目，包括改变学习形式、培养方向、科研专业或学习条件，根据学生个人申请、学习卡和认证委员会或委员会会议记录，由校长命令办理。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Как готовится приказ о переводе внутри МТУСИ?",
                "answer": "ЦРО-ЕД готовит приказ в течение 5 рабочих дней со дня, когда заявитель, в отношении которого принято положительное решение Комиссией или Аттестационной комиссией, заверил личной подписью поданное заявление с условиями перевода и предоставил копию чека об оплате при переводе на платные места."
            },
            "en": {
                "question": "How is an internal transfer order prepared at MTUCI?",
                "answer": "The Unified Dean’s Office prepares the order within 5 working days from the day when the applicant, for whom a positive decision was made by the Commission or Attestation Commission, signs the submitted application with the transfer conditions and provides a copy of the payment receipt if transferring to tuition-paying places."
            },
            "zh": {
                "question": "莫斯科通信与信息技术大学内部转学命令如何准备？",
                "answer": "在委员会或认证委员会作出积极决定后，申请人在转学条件申请上签字，并在转入付费名额时提供付款收据复印件，自此之日起5个工作日内，统一教务办公室准备相关命令。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "В каком случае можно перейти с платного обучения на бюджет?",
                "answer": "Переход с платного обучения на обучение за счёт бюджетных ассигнований возможен при наличии свободных бюджетных мест по соответствующей образовательной программе, специальности, направлению подготовки, форме обучения и курсу либо за счёт собственных средств МТУСИ."
            },
            "en": {
                "question": "When can I transfer from tuition-paying study to state-funded study?",
                "answer": "Transfer from tuition-paying study to state-funded study is possible if there are vacant state-funded places in the corresponding educational program, specialty, field of study, form of study, and year, or at the expense of MTUCI’s own funds."
            },
            "zh": {
                "question": "什么情况下可以从付费学习转为预算名额？",
                "answer": "如果相应教育项目、专业、培养方向、学习形式和年级有空余预算名额，或由莫斯科通信与信息技术大学自有资金支持，则可以从付费学习转为预算名额。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Когда можно подать заявление о переходе с платного обучения на бюджет?",
                "answer": "Заявления о переходе подаются с момента размещения информации о заседании Комиссии на официальном сайте МТУСИ в течение 6 календарных дней. Заседание Комиссии назначается не позднее даты начала очередного семестра."
            },
            "en": {
                "question": "When can I apply to transfer from tuition-paying study to state-funded study?",
                "answer": "Applications for transfer are submitted within 6 calendar days from the publication of information about the Commission meeting on the official MTUCI website. The Commission meeting is scheduled no later than the start date of the next semester."
            },
            "zh": {
                "question": "什么时候可以提交从付费学习转为预算名额的申请？",
                "answer": "自莫斯科通信与信息技术大学官网发布委员会会议信息之日起6个自然日内可以提交转学申请。委员会会议安排不得晚于下一学期开始日期。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Кто имеет право на переход с платного обучения на бюджет?",
                "answer": "Право на переход имеют обучающиеся, прошедшие промежуточную аттестацию за последний семестр перед подачей заявления на оценки «отлично», «отлично» и «хорошо» или «хорошо», а также отдельные категории граждан: дети-сироты, дети, оставшиеся без попечения родителей, граждане до 20 лет с одним родителем-инвалидом I группы при низком среднедушевом доходе семьи, женщины, родившие ребёнка в период обучения, дети участников специальной военной операции, а также обучающиеся, утратившие одного или обоих родителей либо единственного родителя в период обучения."
            },
            "en": {
                "question": "Who has the right to transfer from tuition-paying study to state-funded study?",
                "answer": "The right to transfer is available to students who passed the interim assessment in the last semester before applying with grades of excellent, excellent and good, or good, as well as certain categories of citizens: orphans, children without parental care, citizens under 20 with one parent who is a group I disabled person and low family income, women who gave birth during study, children of participants in the special military operation, and students who lost one or both parents or their only parent during study."
            },
            "zh": {
                "question": "谁有权从付费学习转为预算名额？",
                "answer": "有权申请的学生包括：在提交申请前最后一个学期的中期考核成绩为“优秀”、“优秀和良好”或“良好”的学生，以及特定类别公民，如孤儿、失去父母照顾的儿童、20岁以下且唯一父母为I级残疾人并家庭人均收入低的公民、学习期间生育的女性、特别军事行动参与者子女，以及学习期间失去一方或双方父母或唯一父母的学生。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для перехода с платного обучения на бюджет?",
                "answer": "ЦРО-ЕД и отдел по работе с иностранными гражданами в течение 2 календарных дней после окончания срока приёма заявлений визируют заявление и передают в Комиссию заявление с прилагаемыми документами, мнение представительных органов обучающихся и родителей, а также информацию структурного подразделения МТУСИ о результатах промежуточной аттестации за последний семестр и об отсутствии дисциплинарных взысканий."
            },
            "en": {
                "question": "What documents are required to transfer from tuition-paying study to state-funded study?",
                "answer": "Within 2 calendar days after the application period ends, the Unified Dean’s Office and the department for international students endorse the application and submit to the Commission the application with attached documents, the opinion of student and parent representative bodies, and information from the MTUCI structural unit about the student’s interim assessment results for the last semester and absence of disciplinary penalties."
            },
            "zh": {
                "question": "从付费学习转为预算名额需要哪些文件？",
                "answer": "申请接收期限结束后2个自然日内，统一教务办公室和外国公民事务部门审核申请，并向委员会提交附带文件的申请、学生和家长代表机构意见，以及莫斯科通信与信息技术大学结构部门关于学生上一学期中期考核结果和无纪律处分的信息。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Что является итогом рассмотрения заявления о переходе на бюджет?",
                "answer": "По итогам рассмотрения заявления и документов Комиссия в срок не более 10 календарных дней принимает одно из решений: о переходе обучающегося с платного обучения на вакантное бюджетное место, о переходе на обучение за счёт собственных средств образовательной организации или об отказе в переходе."
            },
            "en": {
                "question": "What is the result of considering an application to transfer to state-funded study?",
                "answer": "After reviewing the application and documents, the Commission makes one of the following decisions within no more than 10 calendar days: transfer from tuition-paying study to a vacant state-funded place, transfer to study at the expense of the educational organization’s own funds, or refusal of the transfer."
            },
            "zh": {
                "question": "转为预算名额申请的审查结果是什么？",
                "answer": "委员会在审查申请和文件后，在不超过10个自然日内作出以下决定之一：从付费学习转入空余预算名额；转为由教育机构自有资金资助学习；或拒绝转入。"
            }
        }
    },
    {
        "category": "transfer",
        "translations": {
            "ru": {
                "question": "Положена ли стипендия после перехода на бюджет?",
                "answer": "Обучающимся по очной форме обучения, перешедшим на обучение за счёт бюджетных ассигнований, назначаются стипендии в установленном порядке."
            },
            "en": {
                "question": "Is a scholarship provided after transferring to state-funded study?",
                "answer": "Full-time students who transfer to study funded by budget allocations are assigned scholarships in the established procedure."
            },
            "zh": {
                "question": "转为预算名额后有奖学金吗？",
                "answer": "转为预算资金学习的全日制学生将按照规定程序获得奖学金。"
            }
        }
    }
]

discipline_questions = [
    {
        "category": "discipline",
        "translations": {
            "ru": {
                "question": "Что считается нарушением учебной дисциплины?",
                "answer": "Нарушением учебной дисциплины считаются пропуски занятий, курение в неразрешённом месте, распитие алкогольных напитков на территории университета, употребление запрещённых веществ на территории университета, а также драки."
            },
            "en": {
                "question": "What is considered a violation of academic discipline?",
                "answer": "Violations of academic discipline include missing classes, smoking in unauthorized places, drinking alcoholic beverages on university premises, using prohibited substances on university premises, and fights."
            },
            "zh": {
                "question": "哪些行为被视为违反学习纪律？",
                "answer": "违反学习纪律的行为包括缺课、在禁止吸烟区域吸烟、在大学校园内饮酒、在大学校园内使用违禁物质以及打架。"
            }
        }
    },
    {
        "category": "discipline",
        "translations": {
            "ru": {
                "question": "Кто выносит замечания и выговоры?",
                "answer": "Замечания и выговоры студентам выносит деканат."
            },
            "en": {
                "question": "Who issues reprimands and warnings?",
                "answer": "Warnings and reprimands for students are issued by the dean’s office."
            },
            "zh": {
                "question": "谁会对学生作出警告或处分？",
                "answer": "学生的警告和处分由院系办公室作出。"
            }
        }
    },
    {
        "category": "discipline",
        "translations": {
            "ru": {
                "question": "Что делать, если возник конфликт с преподавателем?",
                "answer": "Если возник конфликт с преподавателем, необходимо обратиться к заведующему кафедрой или в деканат."
            },
            "en": {
                "question": "What should I do if I have a conflict with a teacher?",
                "answer": "If you have a conflict with a teacher, you should contact the head of the department or the dean’s office."
            },
            "zh": {
                "question": "如果与教师发生冲突该怎么办？",
                "answer": "如果与教师发生冲突，应联系教研室主任或院系办公室。"
            }
        }
    },
    {
        "category": "discipline",
        "translations": {
            "ru": {
                "question": "Что делать, если возник конфликт с другим студентом?",
                "answer": "Если возник конфликт с другим студентом, необходимо обратиться к заведующему кафедрой или в деканат."
            },
            "en": {
                "question": "What should I do if I have a conflict with another student?",
                "answer": "If you have a conflict with another student, you should contact the head of the department or the dean’s office."
            },
            "zh": {
                "question": "如果与其他学生发生冲突该怎么办？",
                "answer": "如果与其他学生发生冲突，应联系教研室主任或院系办公室。"
            }
        }
    },
    {
        "category": "discipline",
        "translations": {
            "ru": {
                "question": "Как избежать отчисления за прогулы?",
                "answer": "Чтобы избежать отчисления за прогулы, необходимо посещать занятия. В случае пропуска нужно предоставить документ, подтверждающий уважительную причину отсутствия."
            },
            "en": {
                "question": "How can I avoid expulsion for absenteeism?",
                "answer": "To avoid expulsion for absenteeism, you must attend classes. If you miss a class, you need to provide a document confirming a valid reason for the absence."
            },
            "zh": {
                "question": "如何避免因旷课被退学？",
                "answer": "为了避免因旷课被退学，必须按时上课。如有缺课，需要提供证明缺席有正当理由的文件。"
            }
        }
    }
]

practice_questions = [
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Можно ли не проходить практику?",
                "answer": "Нет, освобождение обучающихся от прохождения практической подготовки не допускается."
            },
            "en": {
                "question": "Is it possible not to complete an internship?",
                "answer": "No, students cannot be exempted from completing practical training."
            },
            "zh": {
                "question": "可以不参加实习实践吗？",
                "answer": "不可以，学生不得免除实践培训。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Где можно пройти практику?",
                "answer": "Практическая подготовка может быть организована непосредственно в университете, в том числе в его структурном подразделении, предназначенном для проведения практической подготовки, а также в профильной организации на основании договора между университетом и этой организацией."
            },
            "en": {
                "question": "Where can I complete an internship?",
                "answer": "Practical training may be organized directly at the university, including in one of its structural units intended for practical training, or in a relevant organization based on an agreement between the university and that organization."
            },
            "zh": {
                "question": "可以在哪里进行实习实践？",
                "answer": "实践培训可以直接在大学进行，包括在大学用于实践培训的结构部门进行，也可以根据大学与相关专业机构之间的协议在该机构进行。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Где проходят практику студенты целевой формы обучения?",
                "answer": "Обучающиеся, заключившие договоры с будущими работодателями в рамках целевой подготовки, проходят практику в соответствующих организациях при их согласии."
            },
            "en": {
                "question": "Where do targeted-admission students complete their internships?",
                "answer": "Students who have concluded agreements with future employers as part of targeted training complete their internships in the corresponding organizations, provided that those organizations agree."
            },
            "zh": {
                "question": "定向培养学生在哪里进行实习？",
                "answer": "与未来雇主签订定向培养协议的学生，在相关机构同意的情况下，在相应机构进行实习。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Можно ли пройти практику там, где студент уже трудоустроен?",
                "answer": "Да, обучающиеся, совмещающие обучение с трудовой деятельностью, вправе проходить практику по месту работы, если содержание работы соответствует содержанию рабочей программы практики, предусмотренной образовательной программой."
            },
            "en": {
                "question": "Can I complete an internship at my current workplace?",
                "answer": "Yes, students who combine study with employment may complete their internship at their place of work if the content of the work corresponds to the internship program included in the educational program."
            },
            "zh": {
                "question": "可以在自己已经工作的地方进行实习吗？",
                "answer": "可以，学习期间同时工作的学生，如果其工作内容符合教育项目规定的实习工作计划内容，可以在工作地点进行实习。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Нужно ли уведомлять деканат о прохождении практики в МТУСИ?",
                "answer": "Если местом трудовой деятельности являются подразделения университета, руководители этих подразделений уведомляют о возможности прохождения практики обучающимися служебными записками на имя деканов соответствующих факультетов."
            },
            "en": {
                "question": "Do I need to notify the dean’s office about completing an internship at MTUCI?",
                "answer": "If the place of employment is a university unit, the heads of these units notify the relevant faculty deans about the possibility of students completing internships there by official memos."
            },
            "zh": {
                "question": "在莫斯科通信与信息技术大学进行实习需要通知院系办公室吗？",
                "answer": "如果工作地点是大学的部门，则这些部门的负责人会通过提交给相应学院院长的公务函，通知学生可以在其部门进行实习。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Могут ли иностранные студенты проходить практику в российских организациях?",
                "answer": "Да, иностранные обучающиеся могут проходить практику в российских организациях, согласных их принять, если не требуется оформление формы допуска. Также практика может проходить на кафедрах, в лабораториях и других подразделениях университета. Кроме того, иностранные обучающиеся могут быть направлены на практику в организации зарубежных стран при выполнении всех согласующих процедур."
            },
            "en": {
                "question": "Can international students complete internships in Russian organizations?",
                "answer": "Yes, international students may complete internships in Russian organizations that agree to accept them, provided that no special access clearance is required. Internships may also take place at departments, laboratories, and other university units. International students may also be sent for internships to organizations abroad if all approval procedures are completed."
            },
            "zh": {
                "question": "国际学生可以在俄罗斯机构实习吗？",
                "answer": "可以。国际学生可以在同意接收他们的俄罗斯机构实习，前提是不需要办理特殊准入许可。实习也可以在大学的教研室、实验室和其他部门进行。此外，在完成所有审批程序后，国际学生也可以被派往国外机构实习。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Где могут проходить практику студенты очно-заочной и заочной формы обучения?",
                "answer": "Обучающиеся заочной и очно-заочной форм обучения, работающие в организациях по профилю подготовки, могут проходить практику в этих организациях при условии предоставления письма-заявки от организации. Если студент не работает или работает не по профилю подготовки, место практики определяется выпускающей кафедрой."
            },
            "en": {
                "question": "Where can part-time and extramural students complete internships?",
                "answer": "Part-time and extramural students working in organizations related to their field of study may complete internships in these organizations if a request letter is provided by the organization. If the student does not work or works outside the field of study, the internship placement is determined by the graduating department."
            },
            "zh": {
                "question": "非全日制和函授学生可以在哪里实习？",
                "answer": "如果非全日制和函授学生在与专业方向相关的机构工作，并且工作内容符合实习要求，他们可以在该机构实习，但需要提供机构的申请函。如果学生没有工作，或工作内容与专业方向不符，则实习地点由毕业教研室确定。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Где проводится учебная практика?",
                "answer": "Учебная практика проводится в учебных лабораториях кафедр, учебных и научных центрах и других подразделениях университета, обеспечивающих практическую подготовку обучающихся, а также в других организациях на основе договоров на прохождение практики."
            },
            "en": {
                "question": "Where is educational internship conducted?",
                "answer": "Educational internship is conducted in teaching laboratories of departments, educational and research centers, and other university units that provide practical training, as well as in other organizations based on internship agreements."
            },
            "zh": {
                "question": "教学实习在哪里进行？",
                "answer": "教学实习可以在教研室的教学实验室、教学和科研中心以及大学其他能够提供实践培训的部门进行，也可以根据实习协议在其他组织进行。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Какие бывают производственные практики?",
                "answer": "Производственная практика может проводиться стационарно или выездным способом. Стационарная практика проводится в структурных подразделениях университета или в организациях Москвы и Московской области. Выездная практика проводится за пределами указанной территории, а порядок возмещения расходов определяется локальными нормативными актами университета."
            },
            "en": {
                "question": "What types of industrial internships are there?",
                "answer": "Industrial internship may be stationary or off-site. Stationary internship is conducted in university units or in organizations located in Moscow and the Moscow Region. Off-site internship is conducted outside this area, and the procedure for reimbursing expenses is determined by the university’s local regulations."
            },
            "zh": {
                "question": "生产实习有哪些形式？",
                "answer": "生产实习可以是固定地点实习或外出实习。固定地点实习在大学结构部门或莫斯科及莫斯科州的组织中进行。外出实习在上述地区以外进行，费用报销程序由大学地方规范性文件确定。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Что такое преддипломная практика?",
                "answer": "Преддипломная практика является завершающим этапом обучения и проводится после успешного освоения предшествующей программы теоретического и практического обучения. Её содержание определяется темой выпускной квалификационной работы. Задачами преддипломной практики являются закрепление знаний, развитие компетенций и проверка готовности обучающегося к самостоятельной трудовой деятельности."
            },
            "en": {
                "question": "What is pre-graduation internship?",
                "answer": "Pre-graduation internship is the final stage of study and is conducted after successful completion of the previous theoretical and practical training program. Its content is determined by the topic of the final qualification work. Its objectives are to consolidate knowledge, develop competencies, and assess the student’s readiness for independent professional activity."
            },
            "zh": {
                "question": "什么是毕业前实习？",
                "answer": "毕业前实习是学习的最后阶段，在成功完成此前理论和实践学习计划后进行。其内容由毕业论文题目决定。毕业前实习的任务是巩固知识、发展能力，并检验学生独立工作的准备程度。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Какая роль центра карьеры при выборе и прохождении практики?",
                "answer": "Центр карьеры совместно с деканатами факультетов обеспечивает выбор организаций для прохождения практики, заключение договоров на проведение практики, согласование сроков и количества обучающихся, направляемых на производственную практику, а также подготовку исходных данных для формирования приказа об организации практики."
            },
            "en": {
                "question": "What is the role of the Career Center in choosing and completing an internship?",
                "answer": "The Career Center, together with faculty dean’s offices, ensures the selection of organizations for internships, conclusion of internship agreements, coordination of internship dates and the number of students sent for industrial internship, and preparation of initial data for the order on internship organization."
            },
            "zh": {
                "question": "职业中心在选择和完成实习中的作用是什么？",
                "answer": "职业中心与各学院教务办公室共同负责选择实习单位、签订实习协议、协调生产实习的时间和派遣学生人数，并准备实习组织命令所需的基础数据。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Какие отчетные материалы нужно предоставить после прохождения практики?",
                "answer": "После прохождения производственной практики необходимо предоставить дневник по практике, индивидуальное задание, рабочий план или график проведения практики, отзыв руководителя практики и отчет о практике."
            },
            "en": {
                "question": "What reporting materials must be submitted after completing an internship?",
                "answer": "After completing an industrial internship, the student must submit an internship diary, an individual assignment, a work plan or internship schedule, a supervisor’s review, and an internship report."
            },
            "zh": {
                "question": "实习结束后需要提交哪些报告材料？",
                "answer": "生产实习结束后，需要提交实习日记、个人任务书、实习工作计划或时间表、实习指导教师评语以及实习报告。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Что содержит дневник по практике?",
                "answer": "Дневник по практике заполняется обучающимся и содержит сведения о сроках прохождения производственной практики, рабочем месте и кратком содержании выполняемых работ. В дневнике печатями заверяются отметки о сроках пребывания обучающегося в организации."
            },
            "en": {
                "question": "What does the internship diary contain?",
                "answer": "The internship diary is completed by the student and contains information about the internship dates, workplace, and a brief description of the work performed. The diary also contains stamped confirmations of the student’s stay in the organization."
            },
            "zh": {
                "question": "实习日记包含哪些内容？",
                "answer": "实习日记由学生填写，包含生产实习期限、工作地点和所完成工作的简要内容。日记中还需通过印章确认学生在组织中的实习时间。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Что содержит индивидуальное задание по практике?",
                "answer": "Индивидуальное задание выдается руководителем практики с учетом направленности образовательной программы и места прохождения практики. В индивидуальном задании отражаются виды работ. При прохождении практики в организации индивидуальное задание согласовывается с руководителем практики от организации."
            },
            "en": {
                "question": "What does the individual internship assignment contain?",
                "answer": "The individual assignment is issued by the internship supervisor, taking into account the focus of the educational program and the place of internship. It specifies the types of work to be performed. If the internship is completed in an organization, the assignment is agreed with the internship supervisor from that organization."
            },
            "zh": {
                "question": "实习个人任务书包含哪些内容？",
                "answer": "个人任务书由实习指导教师根据教育项目方向和实习地点发放，其中列明工作类型。如果在组织中实习，个人任务书需与该组织的实习指导教师协商确认。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Что должно быть в отзыве руководителя практики?",
                "answer": "В отзыве руководителя практики указывается степень достижения цели практики, выполнение поставленных перед практикантом задач, общая оценка умения выполнять поставленные задачи и вывод о дифференцированной оценке. Отзыв заверяется подписью руководителя и печатью организации."
            },
            "en": {
                "question": "What should be included in the internship supervisor’s review?",
                "answer": "The supervisor’s review indicates the degree to which the internship goal was achieved, completion of the assigned tasks, a general assessment of the student’s ability to complete tasks, and the final differentiated grade. The review is certified by the supervisor’s signature and the organization’s stamp."
            },
            "zh": {
                "question": "实习指导教师评语应包含哪些内容？",
                "answer": "实习指导教师评语应说明实习目标完成程度、实习任务完成情况、对学生完成任务能力的总体评价以及差异化成绩结论。评语需由指导教师签字并加盖组织印章。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Что содержит рабочий план практики?",
                "answer": "Рабочий план или график проведения производственной практики составляется руководителем практики с учетом трудоемкости практики по учебному плану, особенностей базы практики, способа проведения практики и ее содержания."
            },
            "en": {
                "question": "What does the internship work plan contain?",
                "answer": "The work plan or schedule for industrial internship is prepared by the internship supervisor, taking into account the workload according to the curriculum, the features of the internship base, the method of conducting the internship, and its content."
            },
            "zh": {
                "question": "实习工作计划包含哪些内容？",
                "answer": "生产实习工作计划或时间表由实习指导教师制定，并考虑教学计划中的实习工作量、实习基地特点、实习方式和实习内容。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Что должно быть в отчете о производственной практике?",
                "answer": "В отчете о производственной практике отражаются место прохождения и длительность практики, описание выполненной работы в соответствии с программой практики, выполнение индивидуальных заданий, вопросы, возникшие в процессе прохождения практики, личное суждение обучающегося о деятельности организации и выводы по результатам практики. Отчет пишется в произвольной форме и подписывается обучающимся и руководителем практики от кафедры."
            },
            "en": {
                "question": "What should be included in the industrial internship report?",
                "answer": "The industrial internship report includes the place and duration of the internship, a description of the work performed according to the internship program, completion of individual assignments, issues that arose during the internship, the student’s personal opinion about the organization’s activities, and conclusions based on the internship results. The report is written in free form and signed by the student and the internship supervisor from the department."
            },
            "zh": {
                "question": "生产实习报告应包含哪些内容？",
                "answer": "生产实习报告应包括实习地点和实习时间、按照实习计划完成的工作说明、个人任务完成情况、实习过程中出现的问题、学生对实习单位工作的个人评价，以及实习结果总结。报告可以采用自由形式，并由学生和教研室实习指导教师签字。"
            }
        }
    },
    {
        "category": "practice",
        "translations": {
            "ru": {
                "question": "Можно ли пройти практику дистанционно для лиц с ОВЗ?",
                "answer": "Для лиц с ограниченными возможностями здоровья практическая подготовка с использованием электронного обучения и дистанционных образовательных технологий должна предусматривать возможность приема и передачи информации в доступных формах."
            },
            "en": {
                "question": "Can persons with disabilities complete internship remotely?",
                "answer": "For persons with disabilities, practical training using e-learning and distance educational technologies must provide the possibility of receiving and transmitting information in accessible forms."
            },
            "zh": {
                "question": "残障学生可以远程完成实习吗？",
                "answer": "对于残障学生，使用电子学习和远程教育技术进行实践培训时，必须确保可以以无障碍形式接收和传递信息。"
            }
        }
    }
]

attestation_questions = [
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Когда проводится промежуточная аттестация?",
                "answer": "Промежуточная аттестация проводится после выполнения обучающимися всех планируемых в семестре видов работ в соответствии с рабочими программами дисциплин. Она осуществляется в рамках зачётно-экзаменационной сессии по календарному учебному графику, утверждённому ректором МТУСИ."
            },
            "en": {
                "question": "When are exams and assessments held?",
                "answer": "Exams and assessments are held after students complete all planned semester work according to the course syllabi. They take place during the exam session according to the academic calendar approved by the rector of MTUCI."
            },
            "zh": {
                "question": "考试和阶段性考核什么时候进行？",
                "answer": "考试和阶段性考核通常在学生完成本学期课程规定的学习任务后进行。具体时间按照莫斯科通信与信息技术大学校长批准的教学日历，在考试时期内安排。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Есть ли консультации перед зачётами и экзаменами?",
                "answer": "Перед зачётами консультации не проводятся. Перед каждым экзаменом предусматривается консультация."
            },
            "en": {
                "question": "Are there consultations before tests and exams?",
                "answer": "There are no consultations before pass/fail tests. A consultation is provided before each exam."
            },
            "zh": {
                "question": "考查和考试前有答疑咨询吗？",
                "answer": "考查前通常不安排答疑咨询。每门考试前会安排一次考前咨询。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Когда можно узнать расписание сессии?",
                "answer": "Расписание зачётно-экзаменационной сессии должно быть доведено до сведения обучающихся и преподавателей не позднее чем за 10 календарных дней до начала периода промежуточной аттестации."
            },
            "en": {
                "question": "When is the exam session schedule announced?",
                "answer": "The exam session schedule must be announced to students and teachers no later than 10 calendar days before the start of the assessment period."
            },
            "zh": {
                "question": "什么时候可以知道考试时期的时间表？",
                "answer": "考试时期的时间表应在阶段性考核开始前不少于10个自然日通知学生和教师。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Где можно увидеть результаты зачётно-экзаменационной сессии?",
                "answer": "Результаты зачётно-экзаменационной сессии вносятся в электронные зачётные или экзаменационные ведомости через личный кабинет преподавателя. В личном кабинете студента результат отображается в разделе «Успеваемость»."
            },
            "en": {
                "question": "Where can I see my exam session results?",
                "answer": "Exam session results are entered into electronic records through the teacher’s personal account. Students can see their results in the “Academic performance” section of the personal account."
            },
            "zh": {
                "question": "在哪里可以查看考查和考试成绩？",
                "answer": "考查和考试成绩由教师通过个人账户录入电子成绩单。学生可以在个人账户的“学习成绩”栏目中查看结果。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Что происходит в случае опоздания на зачёт или экзамен?",
                "answer": "Обучающийся обязан явиться на испытание промежуточной аттестации в указанное в расписании время. В случае опоздания время, отведённое на зачёт или экзамен, не продлевается."
            },
            "en": {
                "question": "What happens if I am late for a test or exam?",
                "answer": "A student must arrive for the test or exam at the time indicated in the schedule. If the student is late, the time given for the test or exam is not extended."
            },
            "zh": {
                "question": "如果考查或考试迟到了怎么办？",
                "answer": "学生必须按照时间表规定的时间参加考查或考试。如果迟到，考试或考查的时间不会延长。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Что происходит в случае неявки на зачёт или экзамен?",
                "answer": "Неявка на испытание промежуточной аттестации отмечается в электронной ведомости отметкой «неявка». Уважительной причиной неявки считается болезнь, подтверждённая медицинской справкой, которую необходимо предъявить в ЦРО-ЕД или Единый деканат в течение трёх рабочих дней после её закрытия. При предъявлении справки позже указанного срока причина неявки признаётся неуважительной."
            },
            "en": {
                "question": "What happens if I miss a test or exam?",
                "answer": "If a student does not attend a test or exam, the electronic record shows “absent”. Illness confirmed by a medical certificate is considered a valid reason. The certificate must be submitted to the Unified Dean’s Office within three working days after it is closed. If it is submitted later, the absence is considered unjustified."
            },
            "zh": {
                "question": "如果没有参加考查或考试怎么办？",
                "answer": "如果学生没有参加考查或考试，电子成绩单中会显示“缺席”。因病缺席可以被视为正当理由，但必须提供医疗证明，并在证明结束后的三个工作日内提交到统一教务办公室。如果超过期限提交，缺席原因可能会被认定为不正当。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Кто и как принимает зачёт?",
                "answer": "Зачёт принимают преподаватели, проводившие занятия по данной дисциплине. Если преподаватель отсутствует по объективным причинам, зачёт принимает преподаватель, назначенный заведующим кафедрой и ведущий занятия по данной или родственной дисциплине. Форма проведения зачёта устанавливается в рабочей программе дисциплины."
            },
            "en": {
                "question": "Who conducts a pass/fail test?",
                "answer": "A pass/fail test is conducted by the teacher who taught the course. If the teacher is unavailable for objective reasons, the test is conducted by another teacher appointed by the head of the department. The test format is defined in the course syllabus."
            },
            "zh": {
                "question": "考查由谁负责？",
                "answer": "考查通常由讲授该课程的教师负责。如果教师因客观原因无法参加，则由教研室主任指定的、讲授该课程或相关课程的教师负责。考查形式由课程工作大纲规定。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Кто и как принимает экзамен?",
                "answer": "Экзамен принимает преподаватель, являющийся лектором данного потока, в соответствии с утверждённым расписанием. Экзамены могут проводиться в устной или письменной форме по билетам установленной формы, в виде тестов различного типа, в том числе компьютерного тестирования, а также с использованием балльно-рейтинговой системы. Экзаменационные билеты подписываются преподавателем и утверждаются заведующим кафедрой."
            },
            "en": {
                "question": "Who conducts an exam?",
                "answer": "An exam is conducted by the lecturer of the course according to the approved schedule. Exams may be oral or written, based on exam tickets, different types of tests including computer-based testing, and may also use a point-rating system. Exam tickets are signed by the teacher and approved by the head of the department."
            },
            "zh": {
                "question": "考试由谁负责？",
                "answer": "考试通常由该课程的授课教师按照批准的时间表进行。考试可以是口试或笔试，也可以采用试卷、不同类型的测试、计算机测试或积分评分制度。考试题目由教师签字，并由教研室主任批准。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Что является академической задолженностью?",
                "answer": "Академической задолженностью признаются неудовлетворительные результаты промежуточной аттестации по одной или нескольким дисциплинам, модулям, практикам либо непрохождение промежуточной аттестации, включая зачёты и экзамены с отметкой «не явился», при отсутствии уважительных причин."
            },
            "en": {
                "question": "What is considered academic debt?",
                "answer": "Academic debt means failed results in one or more courses, modules, or internships, or failure to pass an assessment, including tests and exams marked as “absent”, if there is no valid reason."
            },
            "zh": {
                "question": "什么情况会被视为需要补考？",
                "answer": "如果学生在一门或多门课程、模块或实习的阶段性考核中未通过，或者在没有正当理由的情况下没有参加考查或考试，这些情况都会被视为需要补考。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Нужно ли закрывать академическую задолженность?",
                "answer": "Да, обучающиеся обязаны ликвидировать академическую задолженность."
            },
            "en": {
                "question": "Do I need to clear academic debt?",
                "answer": "Yes, students are required to clear academic debt."
            },
            "zh": {
                "question": "需要完成补考吗？",
                "answer": "需要。学生必须通过需要补考的课程。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Сколько попыток даётся, чтобы ликвидировать академическую задолженность?",
                "answer": "Обучающиеся, имеющие академическую задолженность, вправе пройти промежуточную аттестацию по соответствующим дисциплинам, модулям или практикам не более двух раз в пределах одного года с момента образования академической задолженности."
            },
            "en": {
                "question": "How many attempts are given to clear academic debt?",
                "answer": "Students who have academic debt may retake the assessment for the relevant courses, modules, or internships no more than two times within one year from the date when the academic debt appeared."
            },
            "zh": {
                "question": "补考有几次机会？",
                "answer": "如果学生有需要补考的课程，可以在形成补考情况之日起一年内参加相关课程、模块或实习的阶段性考核，但最多不超过两次。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Где можно узнать расписание ликвидации академической задолженности?",
                "answer": "Расписание ликвидации академической задолженности доводится до обучающихся через официальный сайт МТУСИ или через личный кабинет в разделе «Расписание»."
            },
            "en": {
                "question": "Where can I find the retake schedule?",
                "answer": "The schedule for clearing academic debt is published on the official MTUCI website or in the “Schedule” section of the personal account."
            },
            "zh": {
                "question": "在哪里可以查看补考时间表？",
                "answer": "补考时间表会通过莫斯科通信与信息技术大学官方网站发布，也可以在个人账户的“时间表”栏目中查看。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Что будет, если не ликвидировать академическую задолженность?",
                "answer": "Если обучающийся не ликвидировал академическую задолженность в установленные сроки, он подлежит отчислению за академическую неуспеваемость. Обучающиеся, имеющие академическую задолженность на конец текущего учебного года, переводятся на следующий курс условно."
            },
            "en": {
                "question": "What happens if I do not clear academic debt?",
                "answer": "If a student does not clear academic debt within the established deadlines, they may be expelled for academic failure. Students who still have academic debt at the end of the academic year are conditionally transferred to the next year of study."
            },
            "zh": {
                "question": "如果没有通过补考会怎样？",
                "answer": "如果学生没有在规定期限内通过需要补考的课程，可能会因学习成绩不合格被退学。如果在本学年结束时仍有未通过的课程，学生会被有条件地升入下一年级。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Можно ли изменить форму сдачи испытания из-за состояния здоровья?",
                "answer": "Да, по желанию обучающихся аттестационные испытания, которые проводятся в письменной форме, могут проводиться в устной форме."
            },
            "en": {
                "question": "Can the assessment format be changed due to health condition?",
                "answer": "Yes, at the student’s request, written assessments may be conducted orally."
            },
            "zh": {
                "question": "可以因为健康原因改变考试形式吗？",
                "answer": "可以。根据学生本人意愿，原本以书面形式进行的考核可以改为口头形式。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Какая продолжительность сдачи зачёта или экзамена для студентов с ограниченными возможностями?",
                "answer": "Продолжительность аттестационного испытания для инвалидов и обучающихся с ограниченными возможностями здоровья может быть увеличена. Письменное испытание может быть продлено не более чем на 30 минут, а подготовка к ответу при устной форме — не более чем на 15 минут. При необходимости аттестационное испытание может проводиться в несколько этапов."
            },
            "en": {
                "question": "How long are tests and exams for students with disabilities?",
                "answer": "The duration of an assessment for students with disabilities may be increased. A written assessment may be extended by no more than 30 minutes, and preparation for an oral answer may be extended by no more than 15 minutes. If necessary, the assessment may be conducted in several stages."
            },
            "zh": {
                "question": "残障学生参加考查或考试时可以延长时间吗？",
                "answer": "可以。残障学生或有健康限制的学生参加考核时，考试时间可以适当延长。书面考核最多可延长30分钟，口头回答的准备时间最多可延长15分钟。如有需要，考核也可以分几个阶段进行。"
            }
        }
    },
    {
        "category": "attestation",
        "translations": {
            "ru": {
                "question": "Есть ли специальные условия сдачи для лиц с ограниченными возможностями здоровья?",
                "answer": "Да. Основанием для создания специальных условий при прохождении текущего контроля и промежуточной аттестации является заявление обучающегося. К заявлению прилагаются документы, подтверждающие индивидуальные особенности, если они отсутствуют в личном деле. Заявление и документы подаются в деканат. В заявлении указываются необходимые условия, например присутствие ассистента, увеличение продолжительности испытания или иные условия. Заявление подаётся не позднее чем за месяц до аттестационного испытания, а при необходимости специальных условий для текущего контроля — в любое время в течение семестра."
            },
            "en": {
                "question": "Are there special assessment conditions for students with disabilities?",
                "answer": "Yes. Special conditions for current control and interim assessment are provided based on the student’s application. Supporting documents must be attached if they are not already in the student’s file. The application is submitted to the dean’s office and must specify the required conditions, such as the presence of an assistant, extended assessment time, or other necessary conditions. The application must be submitted no later than one month before the assessment. For current control, special conditions may be requested at any time during the semester."
            },
            "zh": {
                "question": "残障学生考试时可以申请特殊条件吗？",
                "answer": "可以。学生需要向院系办公室提交申请，并在申请中说明需要哪些特殊条件，例如是否需要助理陪同、是否需要延长考试时间或其他必要条件。如果相关证明文件不在个人档案中，需要随申请一并提交。申请应在考试前至少一个月提交；如果是平时考核需要特殊条件，可以在学期内任何时间提交。"
            }
        }
    }
]
psychological_service_questions = [
    {
        "category": "psychological_service",
        "translations": {
            "ru": {
                "question": "Есть ли в вузе психологическая служба?",
                "answer": "Да, в университете есть психологическая служба."
            },
            "en": {
                "question": "Does the university offer psychological support?",
                "answer": "Yes, the university offers psychological support."
            },
            "zh": {
                "question": "学校有心理疏导吗？",
                "answer": "有，学校提供心理疏导服务。"
            }
        }
    },
    {
        "category": "psychological_service",
        "translations": {
            "ru": {
                "question": "Что делает психологическая служба?",
                "answer": "Психологическая служба оказывает психологическую помощь студентам и преподавателям при обращении."
            },
            "en": {
                "question": "What kind of support does the psychological service provide?",
                "answer": "The psychological service provides psychological support to students and teachers upon request."
            },
            "zh": {
                "question": "心理疏导服务提供哪些帮助？",
                "answer": "心理疏导服务可以为学生和教师提供心理支持和情绪疏导。"
            }
        }
    },
    {
        "category": "psychological_service",
        "translations": {
            "ru": {
                "question": "С кем работает психологическая служба?",
                "answer": "Психологическая служба работает со студентами и преподавателями."
            },
            "en": {
                "question": "Who can use the psychological support service?",
                "answer": "The psychological support service is available to students and teachers."
            },
            "zh": {
                "question": "哪些人可以申请心理疏导？",
                "answer": "心理疏导服务面向学生和教师。"
            }
        }
    },
    {
        "category": "psychological_service",
        "translations": {
            "ru": {
                "question": "Как обратиться в психологическую службу?",
                "answer": "Обратиться в психологическую службу можно по телефону +7 (925) 073-84-58 или по адресу: г. Москва, ул. Авиамоторная, 8А, кабинет 343."
            },
            "en": {
                "question": "How can I contact the psychological support service?",
                "answer": "You can contact the psychological support service by phone at +7 (925) 073-84-58 or visit room 343 at 8A Aviamotornaya Street, Moscow."
            },
            "zh": {
                "question": "如何联系心理疏导服务？",
                "answer": "可以拨打电话 +7 (925) 073-84-58，或前往莫斯科 Авиамоторная 街 8А 号 343 室。"
            }
        }
    }
]
disciplinary_commission_questions = [
    {
        "category": "disciplinary_commission",
        "translations": {
            "ru": {
                "question": "Что такое дисциплинарная комиссия?",
                "answer": "Дисциплинарная комиссия в университете — это коллегиальный орган, который рассматривает вопросы применения к обучающимся мер дисциплинарного взыскания за нарушения Устава, правил внутреннего распорядка и других локальных нормативных актов университета."
            },
            "en": {
                "question": "What is the disciplinary committee?",
                "answer": "The disciplinary committee is a university body that reviews cases involving possible disciplinary measures against students for violations of the university charter, internal rules, and other university regulations."
            },
            "zh": {
                "question": "什么是纪律委员会？",
                "answer": "纪律委员会是学校的集体审议机构，负责审查学生违反大学章程、内部管理规定及其他校内规章制度的情况，并决定是否适用纪律处分。"
            }
        }
    },
    {
        "category": "disciplinary_commission",
        "translations": {
            "ru": {
                "question": "Когда заседает дисциплинарная комиссия?",
                "answer": "Дисциплинарная комиссия заседает после обращения заявителя."
            },
            "en": {
                "question": "When does the disciplinary committee meet?",
                "answer": "The disciplinary committee meets after an application or complaint has been submitted."
            },
            "zh": {
                "question": "纪律委员会什么时候召开会议？",
                "answer": "纪律委员会通常在收到申请或投诉后召开会议。"
            }
        }
    },
    {
        "category": "disciplinary_commission",
        "translations": {
            "ru": {
                "question": "Кто входит в состав дисциплинарной комиссии?",
                "answer": "В состав дисциплинарной комиссии входят председатель комиссии — декан, ответственный секретарь — главный специалист деканата, а также члены комиссии — преподаватели кафедр."
            },
            "en": {
                "question": "Who is on the disciplinary committee?",
                "answer": "The disciplinary committee includes the chairperson, who is the dean; the executive secretary, who is a senior specialist of the dean’s office; and committee members, who are teachers from university departments."
            },
            "zh": {
                "question": "纪律委员会由哪些人组成？",
                "answer": "纪律委员会通常由委员会主席、负责秘书和委员会成员组成。主席为学院院长，负责秘书为院系办公室的主要工作人员，成员为各教研室教师。"
            }
        }
    },
    {
        "category": "disciplinary_commission",
        "translations": {
            "ru": {
                "question": "Можно ли обжаловать дисциплинарное взыскание?",
                "answer": "Да, дисциплинарное взыскание можно обжаловать. Для этого необходимо написать заявление на имя председателя комиссии о повторном рассмотрении нарушения."
            },
            "en": {
                "question": "Can a disciplinary penalty be appealed?",
                "answer": "Yes, a disciplinary penalty can be appealed. To do this, the student must submit an application to the chairperson of the committee requesting a reconsideration of the violation."
            },
            "zh": {
                "question": "可以申诉纪律处分吗？",
                "answer": "可以。如果学生不同意纪律处分，需要向纪律委员会主席提交申请，请求重新审议该违纪情况。"
            }
        }
    }
]

scholarship_questions = [
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому назначается государственная академическая стипендия?",
                "answer": "Государственная академическая стипендия назначается студентам, обучающимся на бюджетной основе, в зависимости от успехов в учебе по результатам промежуточной аттестации. Она назначается с первого числа месяца, следующего за месяцем окончания промежуточной аттестации, не реже двух раз в год."
            },
            "en": {
                "question": "Who can receive the state academic scholarship?",
                "answer": "The state academic scholarship is awarded to students studying on a state-funded basis, depending on their academic results after interim assessment. It is assigned from the first day of the month following the end of the assessment period, at least twice a year."
            },
            "zh": {
                "question": "哪些学生可以获得国家学业奖学金？",
                "answer": "国家学业奖学金发放给预算制学生，具体取决于学生在阶段性考核中的学习成绩。奖学金通常从阶段性考核结束后下一个月的第一天开始发放，每年至少评定两次。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Какие условия получения государственной академической стипендии?",
                "answer": "Для получения государственной академической стипендии у обучающегося не должно быть оценок «удовлетворительно» по итогам промежуточной аттестации и академической задолженности."
            },
            "en": {
                "question": "What are the requirements for receiving the state academic scholarship?",
                "answer": "To receive the state academic scholarship, a student must have no satisfactory grades after interim assessment and no academic debt."
            },
            "zh": {
                "question": "获得国家学业奖学金需要满足哪些条件？",
                "answer": "学生在阶段性考核后不能有“及格”等级的成绩，也不能有需要补考的课程。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Когда назначается государственная академическая стипендия?",
                "answer": "Государственная академическая стипендия назначается с 1-го числа месяца, следующего за месяцем проведения промежуточной аттестации, до последнего дня месяца, в котором проводится следующая промежуточная аттестация."
            },
            "en": {
                "question": "When is the state academic scholarship assigned?",
                "answer": "The state academic scholarship is assigned from the first day of the month following the interim assessment until the last day of the month in which the next interim assessment takes place."
            },
            "zh": {
                "question": "国家学业奖学金什么时候发放？",
                "answer": "国家学业奖学金从阶段性考核结束后下一个月的第一天开始发放，直到下一次阶段性考核所在月份的最后一天。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому предоставляется повышенная государственная стипендия?",
                "answer": "Повышенная государственная стипендия предоставляется обучающимся очной формы обучения за счет бюджетных ассигнований федерального бюджета, в том числе иностранным гражданам и лицам без гражданства, за особые достижения в учебной, научно-исследовательской, общественной, культурно-творческой или спортивной деятельности."
            },
            "en": {
                "question": "Who can receive the increased state scholarship?",
                "answer": "The increased state scholarship may be awarded to full-time students studying on a state-funded basis, including foreign citizens and stateless persons, for special achievements in academic, research, social, cultural, creative, or sports activities."
            },
            "zh": {
                "question": "哪些学生可以获得提高额度的国家奖学金？",
                "answer": "提高额度的国家奖学金可发放给全日制预算制学生，包括外国公民和无国籍学生。学生需要在学习、科研、社会活动、文化创作或体育方面取得突出成绩。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Какие критерии получения повышенной государственной стипендии?",
                "answer": "Повышенная государственная академическая стипендия может назначаться за достижения в учебной деятельности: получение только оценок «отлично» в течение не менее двух последовательных промежуточных аттестаций, получение награды за проектную или опытно-конструкторскую работу, а также победа или призовое место в олимпиаде, конкурсе, соревновании или ином мероприятии."
            },
            "en": {
                "question": "What are the criteria for receiving the increased state scholarship?",
                "answer": "The increased state academic scholarship may be awarded for academic achievements, such as receiving only excellent grades for at least two consecutive interim assessments, receiving an award for project or development work, or becoming a winner or prize-winner of an olympiad, competition, contest, or similar event."
            },
            "zh": {
                "question": "获得提高额度国家奖学金的条件是什么？",
                "answer": "提高额度的国家学业奖学金可因学习方面的突出成绩而发放。例如，学生在至少连续两次阶段性考核中只获得“优秀”成绩，或在项目活动、设计研发工作、奥林匹克竞赛、比赛、竞赛活动等方面获奖。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому назначается государственная социальная стипендия?",
                "answer": "Государственная социальная стипендия назначается детям-сиротам, детям, оставшимся без попечения родителей, лицам, потерявшим в период обучения обоих родителей или единственного родителя, детям-инвалидам, инвалидам I и II групп, инвалидам с детства, студентам, пострадавшим от радиационных катастроф, инвалидам вследствие военной травмы или заболевания, ветеранам боевых действий, а также отдельным категориям граждан, проходивших военную службу по контракту."
            },
            "en": {
                "question": "Who can receive the state social scholarship?",
                "answer": "The state social scholarship is awarded to orphans, children without parental care, students who lost both parents or their only parent during study, disabled children, persons with group I or II disability, persons disabled since childhood, students affected by radiation disasters, persons disabled due to military injury or illness, combat veterans, and certain categories of citizens who served under a military contract."
            },
            "zh": {
                "question": "哪些学生可以获得国家社会奖学金？",
                "answer": "国家社会奖学金可发放给孤儿、失去父母照顾的学生、在学习期间失去父母双方或唯一父母的学生、残障儿童、一级或二级残障人士、儿童时期起残障人士、受辐射灾害影响的学生、因服兵役期间受伤或患病而残障的学生、参战老兵，以及部分曾按合同服兵役的公民。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Что нужно предоставить, чтобы получить государственную социальную стипендию?",
                "answer": "Для получения государственной социальной стипендии необходимо представить в стипендиальную комиссию факультета справку о получении государственной социальной помощи или документ, подтверждающий соответствие одной из категорий граждан, а также личное заявление на имя ректора. В заявлении указываются фамилия, имя, отчество, номер учебной группы и перечень прилагаемых документов. Заявление визируется деканом факультета."
            },
            "en": {
                "question": "What documents are required to receive the state social scholarship?",
                "answer": "To receive the state social scholarship, a student must submit to the faculty scholarship committee a certificate confirming receipt of state social assistance or a document confirming eligibility for one of the categories, as well as a personal application addressed to the rector. The application must include the student’s full name, study group number, and list of attached documents. The application is approved by the faculty dean."
            },
            "zh": {
                "question": "申请国家社会奖学金需要提交哪些材料？",
                "answer": "学生需要向学院奖学金委员会提交获得国家社会援助的证明，或证明其符合相关类别的文件，同时提交写给校长的个人申请。申请中应写明学生姓名、学习小组编号以及附件材料清单。申请需由学院院长确认。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Когда назначается государственная социальная стипендия?",
                "answer": "Государственная социальная стипендия назначается со дня представления в университет документа, подтверждающего назначение государственной социальной помощи, на один год со дня назначения указанной государственной социальной помощи."
            },
            "en": {
                "question": "When is the state social scholarship assigned?",
                "answer": "The state social scholarship is assigned from the day the student submits to the university a document confirming state social assistance, for one year from the date that social assistance was assigned."
            },
            "zh": {
                "question": "国家社会奖学金什么时候开始发放？",
                "answer": "国家社会奖学金从学生向大学提交国家社会援助证明文件之日起发放，有效期为该社会援助被批准之日起一年。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Можно ли одновременно получать государственную социальную и государственную академическую стипендию?",
                "answer": "Да. Обучающиеся, которым назначена государственная социальная стипендия, имеют право на получение государственной академической стипендии в общем порядке."
            },
            "en": {
                "question": "Can I receive both the state social scholarship and the state academic scholarship?",
                "answer": "Yes. Students who receive the state social scholarship may also receive the state academic scholarship under the general procedure."
            },
            "zh": {
                "question": "可以同时获得国家社会奖学金和国家学业奖学金吗？",
                "answer": "可以。获得国家社会奖学金的学生，也可以按照一般规定申请国家学业奖学金。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Когда прекращается выплата государственной социальной стипендии?",
                "answer": "Выплата государственной социальной стипендии прекращается с момента отчисления обучающегося из университета или с первого числа месяца, следующего за месяцем прекращения действия основания, по которому стипендия была назначена."
            },
            "en": {
                "question": "When does payment of the state social scholarship stop?",
                "answer": "Payment of the state social scholarship stops when the student is expelled from the university or from the first day of the month following the month in which the basis for the scholarship ended."
            },
            "zh": {
                "question": "国家社会奖学金什么时候停止发放？",
                "answer": "国家社会奖学金在学生被学校除名时停止发放，或从奖学金发放依据失效后的下一个月第一天起停止发放。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Как назначается государственная стипендия аспирантам?",
                "answer": "Государственная стипендия аспирантам назначается при отсутствии оценки «удовлетворительно» по итогам промежуточной аттестации и академической задолженности. Отдельные правила действуют для аспирантов первого года обучения, переведенных с платной основы на бюджетную, переведенных из другой организации, восстановленных в университете, а также для иностранных граждан и лиц без гражданства, обучающихся в пределах квоты Правительства Российской Федерации."
            },
            "en": {
                "question": "How is the state scholarship for postgraduate students assigned?",
                "answer": "The state scholarship for postgraduate students is assigned if the postgraduate student has no satisfactory grades after interim assessment and no academic debt. Special rules apply to first-year postgraduate students, those transferred from tuition-paying to state-funded study, those transferred from another organization, reinstated students, and foreign citizens or stateless persons studying under the quota of the Government of the Russian Federation."
            },
            "zh": {
                "question": "研究生国家奖学金如何发放？",
                "answer": "研究生国家奖学金通常要求学生在阶段性考核后没有“及格”等级成绩，也没有需要补考的课程。对于一年级研究生、从付费学习转为预算制的研究生、从其他机构转入或恢复学籍的研究生，以及按俄罗斯联邦政府名额学习的外国公民和无国籍人员，适用单独规定。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому назначаются стипендии Президента и Правительства РФ?",
                "answer": "Стипендии Президента Российской Федерации и Правительства Российской Федерации назначаются обучающимся, достигшим выдающихся успехов в учебной и научной деятельности, в соответствии с положениями, утвержденными Президентом Российской Федерации и Правительством Российской Федерации."
            },
            "en": {
                "question": "Who can receive the scholarships of the President and Government of the Russian Federation?",
                "answer": "The scholarships of the President of the Russian Federation and the Government of the Russian Federation are awarded to students who have achieved outstanding success in academic and research activities, according to the regulations approved by the President and the Government of the Russian Federation."
            },
            "zh": {
                "question": "哪些学生可以获得俄罗斯联邦总统和政府奖学金？",
                "answer": "俄罗斯联邦总统奖学金和俄罗斯联邦政府奖学金发放给在学习和科研活动中取得突出成绩的学生，具体按照总统和政府批准的相关规定执行。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Какие критерии назначения стипендии Президента и Правительства РФ?",
                "answer": "Основные критерии: очная бюджетная форма обучения, награды за результаты научно-исследовательской работы, наличие патента или свидетельства на результат интеллектуальной деятельности, публикации в научных изданиях, а также публичное представление результатов научно-исследовательской работы на конференциях, семинарах или иных мероприятиях."
            },
            "en": {
                "question": "What are the criteria for the scholarships of the President and Government of the Russian Federation?",
                "answer": "The main criteria include full-time state-funded study, awards for research results, a patent or certificate for intellectual property results, publications in academic journals, and public presentation of research results at conferences, seminars, or other events."
            },
            "zh": {
                "question": "俄罗斯联邦总统和政府奖学金的评定条件是什么？",
                "answer": "主要条件包括：全日制预算制学习、科研成果获奖、拥有智力成果的专利或证书、在学术刊物上发表论文，以及在会议、研讨会或其他活动中公开展示科研成果。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кто собирает документы на стипендии Президента и Правительства РФ?",
                "answer": "Сбор документов осуществляют деканаты факультетов. Документы передаются экспертной комиссии университета по назначению стипендий. Список кандидатов утверждается решением ученого совета по представлению экспертной комиссии. Назначение стипендий производится Министерством образования и науки Российской Федерации ежегодно с 1 сентября на один учебный год."
            },
            "en": {
                "question": "Who collects documents for the scholarships of the President and Government of the Russian Federation?",
                "answer": "Documents are collected by faculty dean’s offices and submitted to the university expert committee for scholarship assignment. The list of candidates is approved by the Academic Council based on the expert committee’s recommendation. Scholarships are assigned by the Ministry of Education and Science of the Russian Federation annually from September 1 for one academic year."
            },
            "zh": {
                "question": "俄罗斯联邦总统和政府奖学金的材料由谁收集？",
                "answer": "材料由各学院院系办公室收集，并提交给大学奖学金评定专家委员会。候选人名单由学术委员会根据专家委员会的建议批准。奖学金由俄罗斯联邦教育和科学部每年从9月1日起按一个学年发放。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Какие именные стипендии есть в МТУСИ?",
                "answer": "В МТУСИ предусмотрены именные стипендии: стипендия имени А.С. Попова, стипендия имени профессора Н.В. Талызина, стипендия имени В.А. Шамшина, стипендия имени В.А. Котельникова, стипендия ученого совета МТУСИ, стипендия имени К.А. Валиева, стипендия имени К.А. Валиева для аспирантов, стипендия ученого совета для аспирантов МТУСИ, стипендия ученого совета иностранным аспирантам-стажерам — выпускникам университета, а также стипендия ученого совета для аспирантов МТУСИ, обучающихся в целевой аспирантуре по программе «Академическая аспирантура»."
            },
            "en": {
                "question": "What named scholarships are available at MTUCI?",
                "answer": "MTUCI has named scholarships: scholarship named after А.С. Попова, scholarship named after professor Н.В. Талызина, scholarship named after В.А. Шамшина, scholarship named after В.А. Котельникова, MTUCI Academic Council scholarship, scholarship named after К.А. Валиева, scholarship named after К.А. Валиева for postgraduate students, Academic Council scholarship for MTUCI postgraduate students, Academic Council scholarship for foreign postgraduate trainees who graduated from the university, and Academic Council scholarship for MTUCI postgraduate students studying under the Academic Postgraduate Program."
            },
            "zh": {
                "question": "МТУСИ 有哪些个人命名奖学金？",
                "answer": "МТУСИ 设有多种个人命名奖学金，包括：А.С. Попова 奖学金、Н.В. Талызина 教授奖学金、В.А. Шамшина 奖学金、В.А. Котельникова 奖学金、МТУСИ 学术委员会奖学金、К.А. Валиева 奖学金、面向研究生的 К.А. Валиева 奖学金、面向 МТУСИ 研究生的学术委员会奖学金、面向本校毕业的外国研究生进修生的学术委员会奖学金，以及面向参加“Академическая аспирантура”项目的目标培养研究生的学术委员会奖学金。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Влияют ли именные стипендии на другие выплаты?",
                "answer": "Именные стипендии, назначаемые из внебюджетных источников, выплачиваются в соответствии с положениями, установленными учредителями стипендий, не зависят от других стипендий и не влияют на них. Обучающийся на бюджетной форме, получающий именную стипендию, имеет право претендовать на государственную академическую и государственную социальную стипендии на общих основаниях."
            },
            "en": {
                "question": "Do named scholarships affect other payments?",
                "answer": "Named scholarships funded from extra-budgetary sources are paid according to the rules established by the scholarship founders. They do not depend on other scholarships and do not affect them. A state-funded student receiving a named scholarship may still apply for the state academic and state social scholarships under the general procedure."
            },
            "zh": {
                "question": "个人命名奖学金会影响其他奖学金吗？",
                "answer": "由预算外资金设立的个人命名奖学金按照奖学金设立方的规定发放，不依赖其他奖学金，也不影响其他奖学金。预算制学生即使获得个人命名奖学金，也可以按照一般规定申请国家学业奖学金和国家社会奖学金。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Сколько раз в год назначаются именные стипендии?",
                "answer": "Именные стипендии назначаются два раза в год."
            },
            "en": {
                "question": "How many times a year are named scholarships assigned?",
                "answer": "Named scholarships are assigned twice a year."
            },
            "zh": {
                "question": "个人命名奖学金一年评定几次？",
                "answer": "个人命名奖学金每年评定两次。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому назначается стипендия имени А.С. Попова?",
                "answer": "Стипендия имени А.С. Попова назначается обучающимся факультета «Радио и телевидение», начиная с 3-го курса, обучающимся на «отлично» за весь период обучения, показавшим успехи в научно-исследовательской работе и являющимся призерами олимпиад и творческих конкурсов в области связи и информатизации."
            },
            "en": {
                "question": "Who can receive the scholarship named after А.С. Попова?",
                "answer": "The scholarship named after А.С. Попова is awarded to students of the Faculty of Radio and Television starting from the 3rd year, who have excellent grades throughout the entire period of study, have shown success in research, and are prize-winners of olympiads and creative competitions in communications and informatization."
            },
            "zh": {
                "question": "哪些学生可以获得 А.С. Попова 奖学金？",
                "answer": "А.С. Попова 奖学金发放给“广播与电视”学院三年级及以上学生。学生需要在整个学习期间成绩为“优秀”，在科研工作中表现突出，并在通信与信息化领域的奥林匹克竞赛或创意比赛中获奖。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому назначается стипендия имени профессора Н.В. Талызина?",
                "answer": "Стипендия имени профессора Н.В. Талызина назначается обучающимся факультета «Радио и телевидение», начиная с 3-го курса, обучающимся на «отлично» и «хорошо» за весь период обучения, показавшим успехи в научно-исследовательской работе и являющимся призерами олимпиад и творческих конкурсов в области связи и информатизации."
            },
            "en": {
                "question": "Who can receive the scholarship named after professor Н.В. Талызина?",
                "answer": "The scholarship named after professor Н.В. Талызина is awarded to students of the Faculty of Radio and Television starting from the 3rd year, who have excellent and good grades throughout the entire period of study, have shown success in research, and are prize-winners of olympiads and creative competitions in communications and informatization."
            },
            "zh": {
                "question": "哪些学生可以获得 Н.В. Талызина 教授奖学金？",
                "answer": "Н.В. Талызина 教授奖学金发放给“广播与电视”学院三年级及以上学生。学生需要在整个学习期间成绩为“优秀”和“良好”，在科研工作中表现突出，并在通信与信息化领域的奥林匹克竞赛或创意比赛中获奖。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому назначается стипендия имени В.А. Шамшина?",
                "answer": "Стипендия имени В.А. Шамшина назначается обучающимся факультета «Сети и системы связи», начиная с 3-го курса, обучающимся на «отлично» и «хорошо» в течение не менее 4 семестров, принимающим активное участие в научно-исследовательской работе и общественной жизни университета."
            },
            "en": {
                "question": "Who can receive the scholarship named after В.А. Шамшина?",
                "answer": "The scholarship named after В.А. Шамшина is awarded to students of the Faculty of Networks and Communication Systems starting from the 3rd year, who have excellent and good grades for at least 4 semesters and actively participate in research and university social life."
            },
            "zh": {
                "question": "哪些学生可以获得 В.А. Шамшина 奖学金？",
                "answer": "В.А. Шамшина 奖学金发放给“通信网络与系统”学院三年级及以上学生。学生需要至少连续4个学期成绩为“优秀”和“良好”，并积极参加科研工作和大学社会活动。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому назначается стипендия имени В.А. Котельникова?",
                "answer": "Стипендия имени В.А. Котельникова назначается обучающимся и аспирантам МТУСИ по направлениям инфокоммуникационных технологий и систем связи, информатики и вычислительной техники, экономики. Претендентами могут быть обучающиеся начиная с 3-го курса и аспиранты начиная с 1-го года обучения, имеющие оценки «отлично» и «хорошо» за весь период обучения, а также успехи в научных исследованиях в области инфокоммуникаций."
            },
            "en": {
                "question": "Who can receive the scholarship named after В.А. Котельникова?",
                "answer": "The scholarship named after В.А. Котельникова is awarded to MTUCI students and postgraduate students in infocommunication technologies and communication systems, computer science and computer engineering, and economics. Applicants may be students starting from the 3rd year and postgraduate students starting from the 1st year, with excellent and good grades throughout their studies and research achievements in infocommunications."
            },
            "zh": {
                "question": "哪些学生可以获得 В.А. Котельникова 奖学金？",
                "answer": "В.А. Котельникова 奖学金发放给 МТУСИ 在信息通信技术与通信系统、计算机科学与计算机工程、经济学方向学习的学生和研究生。申请人可以是三年级及以上学生或一年级及以上研究生，需要在整个学习期间成绩为“优秀”和“良好”，并在信息通信领域科研方面取得成绩。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому назначается стипендия имени К.А. Валиева?",
                "answer": "Стипендия имени К.А. Валиева назначается обучающимся и аспирантам МТУСИ за значительные достижения в области электронной промышленности при наличии по результатам промежуточной аттестации только оценок «хорошо» и (или) «отлично», полученных в течение года, предшествующего назначению стипендии."
            },
            "en": {
                "question": "Who can receive the scholarship named after К.А. Валиева?",
                "answer": "The scholarship named after К.А. Валиева is awarded to MTUCI students and postgraduate students for significant achievements in the field of the electronics industry, provided that during the year before the scholarship assignment they received only good and/or excellent grades after interim assessment."
            },
            "zh": {
                "question": "哪些学生可以获得 К.А. Валиева 奖学金？",
                "answer": "К.А. Валиева 奖学金发放给在电子工业领域取得显著成绩的 МТУСИ 学生和研究生。申请人需要在奖学金评定前一年内的阶段性考核中只获得“良好”和/或“优秀”成绩。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому назначается стипендия ученого совета МТУСИ?",
                "answer": "Стипендия ученого совета МТУСИ назначается обучающимся университета, начиная с 3-го курса, обучающимся на «отлично» или «отлично» и «хорошо» за весь период обучения и проявившим себя в научно-исследовательской работе."
            },
            "en": {
                "question": "Who can receive the MTUCI Academic Council scholarship?",
                "answer": "The MTUCI Academic Council scholarship is awarded to university students starting from the 3rd year, who have excellent or excellent and good grades throughout the entire period of study and have shown themselves in research work."
            },
            "zh": {
                "question": "哪些学生可以获得 МТУСИ 学术委员会奖学金？",
                "answer": "МТУСИ 学术委员会奖学金发放给三年级及以上学生。学生需要在整个学习期间成绩为“优秀”或“优秀”和“良好”，并在科研工作中表现突出。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для именной стипендии?",
                "answer": "Для большинства именных стипендий требуются выписка из протокола заседания стипендиальной комиссии факультета с указанием достижений кандидата, справка об обучении, а также документы, подтверждающие участие кандидата в научно-исследовательской работе, олимпиадах, творческих конкурсах, общественной жизни университета или иных профильных достижениях."
            },
            "en": {
                "question": "What documents are required for a named scholarship?",
                "answer": "Most named scholarships require an extract from the minutes of the faculty scholarship committee meeting indicating the candidate’s achievements, a certificate of study, and documents confirming participation in research work, olympiads, creative competitions, university social life, or other relevant achievements."
            },
            "zh": {
                "question": "申请个人命名奖学金需要哪些材料？",
                "answer": "大多数个人命名奖学金需要提交学院奖学金委员会会议记录摘录，其中说明候选人的成绩和成就；在读证明；以及确认候选人参加科研工作、奥林匹克竞赛、创意比赛、大学社会活动或其他相关成就的材料。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кому назначается стипендия за высокий балл при поступлении?",
                "answer": "Стипендия за высокий балл при поступлении назначается обучающимся очной формы обучения за счет бюджетных ассигнований по программам бакалавриата и специалитета, поступившим на 1 курс и набравшим по результатам вступительных испытаний 245 и более баллов, а также студентам 1 курса, поступившим без вступительных испытаний, при условии успешного прохождения промежуточной аттестации."
            },
            "en": {
                "question": "Who can receive the scholarship for high admission scores?",
                "answer": "The scholarship for high admission scores is awarded to full-time state-funded bachelor’s and specialist degree students admitted to the 1st year with 245 or more points in entrance examinations, as well as 1st-year students admitted without entrance examinations, provided they successfully pass interim assessment."
            },
            "zh": {
                "question": "哪些学生可以获得高分入学奖学金？",
                "answer": "高分入学奖学金发放给全日制预算制本科和专家学位一年级学生。学生需要在入学考试中获得245分及以上；无入学考试录取的一年级学生，在通过阶段性考核的情况下也可以获得该奖学金。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Кто может получать единовременную материальную помощь?",
                "answer": "Единовременную материальную помощь могут получать обучающиеся из числа детей-сирот и детей, оставшихся без попечения родителей; обучающиеся, признанные инвалидами; пострадавшие от радиационных катастроф; инвалиды вследствие военной травмы или заболевания; ветераны боевых действий; обучающиеся, потерявшие одного из родителей в период обучения; обучающиеся, имеющие родителей-инвалидов I группы или единственного родителя-инвалида I группы; обучающиеся, создавшие семью или имеющие детей; находящиеся в отпуске по беременности и родам; перенесшие тяжелые заболевания и понесшие большие расходы на лечение; ставшие жертвами аварий, катастроф, краж, грабежей или разбойных нападений, а также иные обучающиеся, находящиеся в тяжелом материальном положении."
            },
            "en": {
                "question": "Who can receive one-time financial assistance?",
                "answer": "One-time financial assistance may be provided to orphans and children without parental care, students with disabilities, students affected by radiation disasters, persons disabled due to military injury or illness, combat veterans, students who lost a parent during study, students with a group I disabled parent or an only parent with group I disability, students who created a family or have children, students on maternity leave, students who suffered serious illnesses and had high treatment expenses, victims of accidents, disasters, theft, robbery or assault, and other students in serious financial hardship."
            },
            "zh": {
                "question": "哪些学生可以获得一次性经济资助？",
                "answer": "一次性经济资助可提供给孤儿和失去父母照顾的学生、残障学生、受辐射灾害影响的学生、因服兵役期间受伤或患病而残障的学生、参战老兵、学习期间失去父母一方的学生、有一级残障父母或唯一父母为一级残障人士的学生、学习期间成家或有孩子的学生、处于产假期间的学生、患重病并承担较高治疗费用的学生、遭遇事故、技术灾害、盗窃、抢劫或暴力袭击的学生，以及其他处于严重经济困难并急需帮助的学生。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Сколько раз выплачивается единовременная материальная помощь?",
                "answer": "Обучающиеся могут претендовать на получение материальной помощи не чаще одного раза в семестр."
            },
            "en": {
                "question": "How often can one-time financial assistance be received?",
                "answer": "Students may apply for financial assistance no more than once per semester."
            },
            "zh": {
                "question": "一次性经济资助多久可以申请一次？",
                "answer": "学生每学期最多可以申请一次经济资助。"
            }
        }
    },
    {
        "category": "scholarships",
        "translations": {
            "ru": {
                "question": "Какой размер материальной помощи?",
                "answer": "Размер материальной помощи не может превышать десятикратного размера минимальной государственной академической стипендии, если иное не предусмотрено другими локальными нормативными актами университета."
            },
            "en": {
                "question": "What is the amount of financial assistance?",
                "answer": "The amount of financial assistance cannot exceed ten times the minimum state academic scholarship unless otherwise provided by other local university regulations."
            },
            "zh": {
                "question": "经济资助金额是多少？",
                "answer": "经济资助金额通常不得超过最低国家学业奖学金的十倍，除非大学其他内部规定另有说明。"
            }
        }
    }
]
first_year_questions = [
    {
        "category": "first_year",
        "translations": {
            "ru": {
                "question": "Когда и где проходит общее собрание факультета для первокурсников?",
                "answer": "Собрания факультетов для первокурсников проводятся в конце августа. Объявления о собраниях размещаются в разделе «Абитуриенту» на сайте МТУСИ."
            },
            "en": {
                "question": "When and where is the faculty meeting for first-year students held?",
                "answer": "Faculty meetings for first-year students are held at the end of August. Announcements about the meetings are published in the “Applicants” section on the MTUCI website."
            },
            "zh": {
                "question": "大一学生的学院大会什么时候、在哪里举行？",
                "answer": "大一学生的学院大会通常在8月底举行。相关通知会发布在 МТУСИ 网站的“招生信息”栏目。"
            }
        }
    },
    {
        "category": "first_year",
        "translations": {
            "ru": {
                "question": "Какие вопросы рассматриваются на собрании факультета?",
                "answer": "На собрании факультета первокурсников знакомят с руководством факультета, сотрудниками психологической службы, центром карьеры и представителями военно-учетного стола. Юноши на собрании заполняют Форму №10 — карточку гражданина, подлежащего воинскому учету. Также рассматриваются организационные вопросы: списки групп, выбор старост, расписание, секции и программы дополнительного образования."
            },
            "en": {
                "question": "What topics are discussed at the faculty meeting?",
                "answer": "At the faculty meeting, first-year students meet the faculty administration, psychological support staff, the Career Center, and representatives of the military registration office. Male students fill out Form No. 10 for military registration. The meeting also covers organizational matters such as group lists, selection of group leaders, class schedules, student clubs, and additional education programs."
            },
            "zh": {
                "question": "学院大会会讲哪些内容？",
                "answer": "学院大会上，大一学生会了解学院领导、心理疏导服务、职业中心以及兵役登记部门的相关信息。男生需要填写第10号表格，即兵役登记卡。大会还会说明分组名单、班长选举、课表、学生社团以及补充教育项目等组织事项。"
            }
        }
    },
    {
        "category": "first_year",
        "translations": {
            "ru": {
                "question": "Как определить, в какой я группе?",
                "answer": "Список групп объявляется на собрании факультета. Также списки групп вывешиваются у деканатов."
            },
            "en": {
                "question": "How can I find out which group I am in?",
                "answer": "Group lists are announced at the faculty meeting. They are also posted near the dean’s offices."
            },
            "zh": {
                "question": "怎么知道自己在哪个班级小组？",
                "answer": "分组名单会在学院大会上公布，也会张贴在院系办公室附近。"
            }
        }
    },
    {
        "category": "first_year",
        "translations": {
            "ru": {
                "question": "Когда начинается обучение у студентов первого курса?",
                "answer": "Занятия начинаются 1 сентября, в День знаний."
            },
            "en": {
                "question": "When do classes start for first-year students?",
                "answer": "Classes start on September 1, the Day of Knowledge."
            },
            "zh": {
                "question": "大一学生什么时候开始上课？",
                "answer": "课程从9月1日开始，这一天是俄罗斯的知识日。"
            }
        }
    },
    {
        "category": "first_year",
        "translations": {
            "ru": {
                "question": "Будет ли у студента адрес корпоративной электронной почты?",
                "answer": "Да, у студента будет адрес корпоративной электронной почты. Его выдаёт деканат факультета."
            },
            "en": {
                "question": "Will a student have a corporate email address?",
                "answer": "Yes, the student will have a corporate email address. It is issued by the faculty dean’s office."
            },
            "zh": {
                "question": "学生会有学校邮箱吗？",
                "answer": "会的。学生会获得学校邮箱，邮箱由学院教务办公室发放。"
            }
        }
    }
]

employment_questions = [
    {
        "category": "employment",
        "translations": {
            "ru": {
                "question": "Как трудоустроиться от вуза?",
                "answer": "Официального трудоустройства или распределения вузом не предусматривается."
            },
            "en": {
                "question": "Can the university officially place me in a job?",
                "answer": "The university does not provide official job placement or mandatory assignment to employers."
            },
            "zh": {
                "question": "学校会统一安排就业吗？",
                "answer": "学校不提供官方统一就业分配，也不会强制安排学生到指定单位工作。"
            }
        }
    },
    {
        "category": "employment",
        "translations": {
            "ru": {
                "question": "Где узнать о вакансиях от вуза?",
                "answer": "Информацию о вакансиях можно узнать на ярмарке вакансий, на выпускающей кафедре или в деканате факультета."
            },
            "en": {
                "question": "Where can I find job vacancies from the university?",
                "answer": "Information about job vacancies can be found at career fairs, at the graduating department, or at the faculty dean’s office."
            },
            "zh": {
                "question": "在哪里可以了解学校提供的招聘信息？",
                "answer": "可以在招聘会、毕业教研室或学院教务办公室了解招聘信息。"
            }
        }
    }
]

study_process_questions = [
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Где найти актуальное расписание занятий?",
                "answer": "Актуальное расписание занятий можно посмотреть на сайте МТУСИ в разделе «Студенту» — «Расписание занятий», в личном кабинете студента МТУСИ, а также в телеграм-боте «Расписание»."
            },
            "en": {
                "question": "Where can I find the current class schedule?",
                "answer": "The current class schedule can be found on the MTUCI website in the “Students” section under “Class schedule”, in the MTUCI student personal account, and in the “Schedule” Telegram bot."
            },
            "zh": {
                "question": "在哪里可以查看最新课表？",
                "answer": "可以在 МТУСИ 网站“学生”栏目中的“课程表”查看，也可以在学生个人账户中查看，或使用 Telegram 机器人“Расписание”。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Почему в расписании указана пара, а преподаватель не пришёл?",
                "answer": "Если в расписании указана пара, но преподаватель не пришёл, необходимо обратиться на кафедру, на которой работает преподаватель, или в деканат факультета."
            },
            "en": {
                "question": "Why is a class listed in the schedule, but the teacher did not come?",
                "answer": "If a class is listed in the schedule but the teacher did not come, contact the department where the teacher works or the faculty dean’s office."
            },
            "zh": {
                "question": "课表上有课，但老师没有来，怎么办？",
                "answer": "如果课表上有课，但老师没有来，应联系该教师所在的教研室，或联系学院教务办公室。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Как узнать, изменилось ли расписание на завтра?",
                "answer": "Изменения расписания можно проверить на сайте МТУСИ в разделе «Студенту» — «Расписание занятий», в личном кабинете студента МТУСИ или в телеграм-боте «Расписание»."
            },
            "en": {
                "question": "How can I check if tomorrow’s schedule has changed?",
                "answer": "Schedule changes can be checked on the MTUCI website in the “Students” section under “Class schedule”, in the student personal account, or in the “Schedule” Telegram bot."
            },
            "zh": {
                "question": "怎么知道明天的课表有没有变化？",
                "answer": "可以在 МТУСИ 网站“学生”栏目中的“课程表”、学生个人账户，或 Telegram 机器人“Расписание”中查看课表变化。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Как понять, кто ведёт пару, если в расписании написано «?»?",
                "answer": "Если в расписании вместо преподавателя указано «?», необходимо обратиться на соответствующую кафедру или в деканат факультета."
            },
            "en": {
                "question": "How can I find out who teaches a class if the schedule shows “?”?",
                "answer": "If the schedule shows “?” instead of the teacher’s name, contact the relevant department or the faculty dean’s office."
            },
            "zh": {
                "question": "如果课表上老师一栏显示“？”，怎么知道是谁上课？",
                "answer": "如果课表上教师姓名显示为“？”，应联系相关教研室或学院教务办公室。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Почему расписание на сайте и в LMS не совпадает?",
                "answer": "Если расписание на сайте и в LMS не совпадает, возможно, возникли технические неполадки. Для уточнения информации необходимо обратиться в деканат факультета."
            },
            "en": {
                "question": "Why does the schedule on the website not match the schedule in the LMS?",
                "answer": "If the schedule on the website and in the LMS do not match, there may be a technical issue. Contact the faculty dean’s office to clarify the information."
            },
            "zh": {
                "question": "为什么网站上的课表和 LMS 里的课表不一致？",
                "answer": "如果网站课表和 LMS 中的课表不一致，可能是技术问题。建议联系学院教务办公室确认。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Кто может перенести занятие и как об этом узнают студенты?",
                "answer": "Все изменения в расписании осуществляются на основании служебной записки от заведующего кафедрой, направленной в сектор разработки расписания. Изменения публикуются на сайте МТУСИ в разделе «Студенту» — «Расписание занятий», в личном кабинете студента и в телеграм-боте «Расписание»."
            },
            "en": {
                "question": "Who can reschedule a class and how are students informed?",
                "answer": "All schedule changes are made based on an official memo from the head of the department sent to the schedule development unit. Changes are published on the MTUCI website in the “Students” section under “Class schedule”, in the student personal account, and in the “Schedule” Telegram bot."
            },
            "zh": {
                "question": "谁可以调整课程时间，学生怎么知道？",
                "answer": "所有课表变更都需要由教研室主任提交公务函，并发送给课表编制部门。变更信息会发布在 МТУСИ 网站“学生”栏目中的“课程表”、学生个人账户以及 Telegram 机器人“Расписание”中。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Куда обращаться, если замену в расписании не согласовали с группой?",
                "answer": "Все вопросы по замене расписания решаются с заведующим кафедрой."
            },
            "en": {
                "question": "Where should I go if a schedule replacement was not agreed with the group?",
                "answer": "All questions about schedule replacements are resolved with the head of the department."
            },
            "zh": {
                "question": "如果课程调整没有和小组协商，应联系哪里？",
                "answer": "所有关于课表替换或调整的问题，应联系教研室主任解决。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Можно ли не посещать внеурочный перенос без личного уведомления?",
                "answer": "Все пропуски занятий необходимо согласовывать с преподавателем, ведущим дисциплину."
            },
            "en": {
                "question": "Can I skip a rescheduled class if I was not personally notified?",
                "answer": "All class absences must be agreed with the teacher responsible for the course."
            },
            "zh": {
                "question": "如果没有被单独通知，可以不参加临时调整的课程吗？",
                "answer": "所有缺课情况都需要与授课教师协商。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Где публикуется информация о пересдачах?",
                "answer": "Информация о пересдачах публикуется на сайте МТУСИ в разделе «Студенту» — «Расписание занятий», в личном кабинете студента и в телеграм-боте «Расписание»."
            },
            "en": {
                "question": "Where is information about retakes published?",
                "answer": "Information about retakes is published on the MTUCI website in the “Students” section under “Class schedule”, in the student personal account, and in the “Schedule” Telegram bot."
            },
            "zh": {
                "question": "补考信息在哪里发布？",
                "answer": "补考信息会发布在 МТУСИ 网站“学生”栏目中的“课程表”、学生个人账户以及 Telegram 机器人“Расписание”中。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Сколько раз можно пересдавать экзамен?",
                "answer": "Обучающиеся, имеющие академическую задолженность, могут пройти промежуточную аттестацию по соответствующим дисциплинам или модулям не более двух раз в течение одного года с момента образования академической задолженности."
            },
            "en": {
                "question": "How many times can I retake an exam?",
                "answer": "Students who have academic debt may retake the assessment for the relevant courses or modules no more than two times within one year from the date when the academic debt appeared."
            },
            "zh": {
                "question": "考试可以补考几次？",
                "answer": "如果学生有需要补考的课程，可以在形成补考情况之日起一年内参加相关课程或模块的阶段性考核，但最多不超过两次。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Нужно ли писать заявление на пересдачу?",
                "answer": "На обычную пересдачу промежуточной аттестации заявление писать не требуется. Заявление подается только в случае, если студент четвертого курса для получения красного диплома хочет пересдать одну оценку «удовлетворительно» или две оценки «хорошо», если не набрал 75% отличных оценок. Такое заявление подается в Единый деканат."
            },
            "en": {
                "question": "Do I need to submit an application for a retake?",
                "answer": "For a regular retake of interim assessment, no application is required. An application is required only if a fourth-year student wants to retake one satisfactory grade or two good grades in order to qualify for an honors diploma because they did not reach 75% excellent grades. This application is submitted to the Unified Dean’s Office."
            },
            "zh": {
                "question": "补考需要写申请吗？",
                "answer": "普通补考不需要提交申请。只有在四年级学生为了获得红色毕业证，想重考一个“及格”成绩或两个“良好”成绩，并且优秀成绩比例未达到75%时，才需要提交申请。申请提交到统一教务办公室。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Что делать, если я не могу прийти на назначенную пересдачу?",
                "answer": "Уважительной причиной неявки на промежуточную аттестацию считается болезнь, подтвержденная медицинской справкой. Справку необходимо предъявить в Центр по работе с обучающимися — Единый деканат в течение трёх рабочих дней после её закрытия. Если справка предъявлена позже, причина неявки признается неуважительной."
            },
            "en": {
                "question": "What should I do if I cannot attend the scheduled retake?",
                "answer": "Illness confirmed by a medical certificate is considered a valid reason for missing an assessment. The certificate must be submitted to the Unified Dean’s Office within three working days after it is closed. If the certificate is submitted later, the absence is considered unjustified."
            },
            "zh": {
                "question": "如果不能参加安排好的补考怎么办？",
                "answer": "因病缺席可以被视为正当理由，但必须提供医疗证明。证明需要在结束后的三个工作日内提交到统一教务办公室。如果超过期限提交，缺席原因可能会被认定为不正当。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Что считается допуском к экзамену?",
                "answer": "К экзамену допускаются студенты, получившие оценку по курсовой работе или курсовому проекту, а также зачёт, если они предусмотрены учебным планом по данной дисциплине."
            },
            "en": {
                "question": "What is required to be admitted to an exam?",
                "answer": "Students are admitted to an exam if they have received a grade for the course paper or course project, as well as a pass/fail test result, if these are required by the curriculum for the course."
            },
            "zh": {
                "question": "参加考试需要满足什么条件？",
                "answer": "如果该课程教学计划中要求课程论文、课程设计或考查，学生需要先获得相应成绩或通过考查，才可以参加考试。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Что делать, если преподаватель ошибочно не поставил оценку в ведомость?",
                "answer": "Если преподаватель ошибочно не поставил оценку в ведомость, необходимо обратиться к преподавателю, ведущему дисциплину."
            },
            "en": {
                "question": "What should I do if the teacher mistakenly did not enter my grade?",
                "answer": "If the teacher mistakenly did not enter your grade in the record, contact the teacher responsible for the course."
            },
            "zh": {
                "question": "如果老师误将成绩漏录了怎么办？",
                "answer": "如果老师误将成绩漏录到成绩单中，需要联系该课程的授课教师。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Как узнать, есть ли у меня допуск к экзамену?",
                "answer": "Информацию о допуске к экзамену можно уточнить в Едином деканате или у преподавателя."
            },
            "en": {
                "question": "How can I find out if I am admitted to an exam?",
                "answer": "You can check information about exam admission at the Unified Dean’s Office or with the teacher."
            },
            "zh": {
                "question": "怎么知道自己是否可以参加考试？",
                "answer": "可以在统一教务办公室或向授课教师确认是否具备考试资格。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Кто решает, могу ли я сдавать предмет досрочно?",
                "answer": "Вопрос о досрочной сдаче промежуточной аттестации решает деканат факультета."
            },
            "en": {
                "question": "Who decides whether I can take a subject early?",
                "answer": "The faculty dean’s office decides whether a student may take an interim assessment early."
            },
            "zh": {
                "question": "谁决定我能不能提前考试？",
                "answer": "是否可以提前参加阶段性考核，由学院教务办公室决定。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Как перейти на индивидуальный график обучения?",
                "answer": "Индивидуальный график обучения распространяется только на студентов, перешедших из другого вуза, студентов другого направления или студентов, вышедших из академического отпуска."
            },
            "en": {
                "question": "How can I switch to an individual study schedule?",
                "answer": "An individual study schedule is available only for students who transferred from another university, changed their field of study, or returned from academic leave."
            },
            "zh": {
                "question": "如何转为个人学习计划？",
                "answer": "个人学习计划通常只适用于从其他大学转入的学生、转专业的学生，或从休学后恢复学习的学生。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Можно ли ускорить или замедлить обучение?",
                "answer": "Индивидуальная программа обучения распространяется только на студентов, перешедших из другого вуза, студентов другого направления или студентов, вышедших из академического отпуска."
            },
            "en": {
                "question": "Can I speed up or slow down my studies?",
                "answer": "An individual study program is available only for students who transferred from another university, changed their field of study, or returned from academic leave."
            },
            "zh": {
                "question": "可以加快或放慢学习进度吗？",
                "answer": "个人学习计划通常只适用于从其他大学转入的学生、转专业的学生，或从休学后恢复学习的学生。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Как сменить направление или форму обучения?",
                "answer": "Для смены направления или формы обучения необходимо взять справку об обучении в Едином деканате и обратиться в деканат или центр обучения того направления или формы обучения, на которые студент хочет перейти."
            },
            "en": {
                "question": "How can I change my field or form of study?",
                "answer": "To change your field or form of study, you need to obtain a certificate of study from the Unified Dean’s Office and contact the dean’s office or education center of the field or form of study you want to transfer to."
            },
            "zh": {
                "question": "如何更换专业方向或学习形式？",
                "answer": "需要先在统一教务办公室领取在读证明，然后联系想转入的专业方向或学习形式对应的院系办公室或教学中心。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Что делать, если я не укладываюсь в сроки по индивидуальному учебному плану?",
                "answer": "Если студент не укладывается в сроки по индивидуальному учебному плану, необходимо обратиться в деканат факультета с подтверждающими документами."
            },
            "en": {
                "question": "What should I do if I cannot meet the deadlines in my individual study plan?",
                "answer": "If you cannot meet the deadlines in your individual study plan, contact the faculty dean’s office and provide supporting documents."
            },
            "zh": {
                "question": "如果无法按个人学习计划规定时间完成怎么办？",
                "answer": "如果无法按个人学习计划规定时间完成，应携带证明材料联系学院教务办公室。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "С кем согласовывается переход на индивидуальный учебный план?",
                "answer": "Переход на индивидуальный учебный план согласовывается с деканатом факультета."
            },
            "en": {
                "question": "Who approves the transfer to an individual study plan?",
                "answer": "Transfer to an individual study plan is approved by the faculty dean’s office."
            },
            "zh": {
                "question": "个人学习计划需要和谁确认？",
                "answer": "转为个人学习计划需要与学院教务办公室确认。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Как взять академический отпуск?",
                "answer": "Для оформления академического отпуска необходимо написать заявление в Едином деканате и предоставить подтверждающий документ."
            },
            "en": {
                "question": "How can I take academic leave?",
                "answer": "To apply for academic leave, you need to submit an application to the Unified Dean’s Office and provide a supporting document."
            },
            "zh": {
                "question": "如何申请休学？",
                "answer": "申请休学需要在统一教务办公室提交申请，并提供相关证明文件。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "На сколько максимум можно уйти в академический отпуск?",
                "answer": "Срок академического отпуска необходимо уточнять в Едином деканате, так как он зависит от основания предоставления отпуска и действующих правил университета."
            },
            "en": {
                "question": "What is the maximum duration of academic leave?",
                "answer": "The duration of academic leave should be clarified at the Unified Dean’s Office, as it depends on the reason for the leave and current university rules."
            },
            "zh": {
                "question": "休学最长可以休多久？",
                "answer": "休学期限需要向统一教务办公室确认，因为具体期限取决于休学原因和学校现行规定。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Как оформить академический отпуск по здоровью?",
                "answer": "Для оформления академического отпуска по состоянию здоровья необходимо написать заявление в Едином деканате и предоставить заключение медицинской комиссии."
            },
            "en": {
                "question": "How can I apply for academic leave for health reasons?",
                "answer": "To apply for academic leave for health reasons, submit an application to the Unified Dean’s Office and provide a medical commission report."
            },
            "zh": {
                "question": "因健康原因如何申请休学？",
                "answer": "因健康原因申请休学，需要向统一教务办公室提交申请，并提供医疗委员会结论。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Можно ли получить отсрочку от армии?",
                "answer": "Отсрочка от армии предоставляется юношам очной формы обучения, поступившим сразу после школы."
            },
            "en": {
                "question": "Can I get deferment from military service?",
                "answer": "Deferment from military service is granted to male full-time students who entered the university immediately after graduating from school."
            },
            "zh": {
                "question": "可以获得兵役延期吗？",
                "answer": "兵役延期适用于高中毕业后直接进入大学全日制学习的男性学生。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Можно ли взять академический отпуск перед началом семестра, если ещё не учился?",
                "answer": "Да, академический отпуск можно оформить перед началом семестра, даже если студент ещё не приступил к обучению."
            },
            "en": {
                "question": "Can I take academic leave before the semester starts if I have not studied yet?",
                "answer": "Yes, academic leave can be arranged before the semester starts, even if the student has not yet begun studying."
            },
            "zh": {
                "question": "如果还没开始上课，可以在学期开始前申请休学吗？",
                "answer": "可以。即使学生还没有开始学习，也可以在学期开始前申请休学。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Кто подписывает приказ на академический отпуск?",
                "answer": "Приказ на академический отпуск подписывают ректор и декан факультета."
            },
            "en": {
                "question": "Who signs the order for academic leave?",
                "answer": "The order for academic leave is signed by the rector and the faculty dean."
            },
            "zh": {
                "question": "休学命令由谁签署？",
                "answer": "休学命令由校长和学院院长签署。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Могут ли отказать в академическом отпуске?",
                "answer": "Если у студента есть подтверждающие документы, в академическом отпуске отказать не могут."
            },
            "en": {
                "question": "Can academic leave be refused?",
                "answer": "If the student has supporting documents, academic leave cannot be refused."
            },
            "zh": {
                "question": "学校可以拒绝休学申请吗？",
                "answer": "如果学生有相关证明文件，学校不能拒绝休学申请。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Кто ведёт учёт посещаемости?",
                "answer": "Учёт посещаемости ведут старосты групп и преподаватели дисциплин, которые имеют доступ к ведомостям посещаемости."
            },
            "en": {
                "question": "Who keeps attendance records?",
                "answer": "Attendance records are kept by group leaders and course teachers who have access to attendance sheets."
            },
            "zh": {
                "question": "谁负责记录出勤？",
                "answer": "出勤记录由班长和授课教师负责，他们可以查看出勤表。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Что делать, если преподаватель ошибочно отметил отсутствие?",
                "answer": "Если преподаватель ошибочно отметил отсутствие, необходимо обратиться к этому преподавателю. Преподаватель должен написать служебную записку на изменение посещаемости."
            },
            "en": {
                "question": "What should I do if the teacher mistakenly marked me absent?",
                "answer": "If the teacher mistakenly marked you absent, contact that teacher. The teacher must write an official memo to correct the attendance record."
            },
            "zh": {
                "question": "如果老师误记我缺勤怎么办？",
                "answer": "如果老师误记缺勤，需要联系该教师。教师应提交公务函，以修改出勤记录。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Учитываются ли опоздания?",
                "answer": "Опоздания учитываются на усмотрение каждого преподавателя."
            },
            "en": {
                "question": "Are late arrivals counted?",
                "answer": "Late arrivals are counted at the discretion of each teacher."
            },
            "zh": {
                "question": "迟到会被记录吗？",
                "answer": "是否记录迟到，由每位授课教师自行决定。"
            }
        }
    },
    {
        "category": "study",
        "translations": {
            "ru": {
                "question": "Влияет ли посещаемость на стипендию?",
                "answer": "Посещаемость может повлиять на скидку на обучение."
            },
            "en": {
                "question": "Does attendance affect the scholarship?",
                "answer": "Attendance may affect the tuition discount."
            },
            "zh": {
                "question": "出勤会影响奖学金吗？",
                "answer": "出勤可能会影响学费折扣。"
            }
        }
    }
]

foreign_site_faq_questions = [
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что делать, если в лечебном учреждении предлагают оплатить услугу, которая якобы не входит в ДМС?",
                "answer": "Перед оплатой необходимо обратиться на медицинский пульт страховой компании. Телефон указан в бланке полиса ДМС. Сотрудник страховой компании уточнит, входит ли услуга в программу страхования, и подскажет, нужно ли оплачивать её самостоятельно."
            },
            "en": {
                "question": "What should I do if a clinic asks me to pay for a service that is supposedly not covered by my VHI insurance?",
                "answer": "Before paying, contact the medical assistance line of your insurance company. The phone number is listed on your voluntary health insurance policy. The insurance company will clarify whether the service is covered and whether you need to pay for it yourself."
            },
            "zh": {
                "question": "如果医院要求我自费支付据说不包含在自愿医疗保险中的服务，该怎么办？",
                "answer": "付款前应先联系保险公司的医疗服务热线。电话号码通常写在自愿医疗保险单上。保险公司工作人员会确认该服务是否包含在保险范围内，并说明是否需要自行支付。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Какие документы иностранный гражданин должен всегда иметь при себе в России?",
                "answer": "Иностранному гражданину необходимо всегда иметь при себе паспорт, миграционную карту, регистрацию, свидетельство о дактилоскопической регистрации, а также фотографию полиса ДМС в телефоне или карточку страховой компании с её данными."
            },
            "en": {
                "question": "What documents should a foreign citizen always carry in Russia?",
                "answer": "A foreign citizen should always carry a passport, migration card, registration document, fingerprint registration certificate, and either a photo of the voluntary health insurance policy on the phone or an insurance company card with the relevant details."
            },
            "zh": {
                "question": "外国公民在俄罗斯应随身携带哪些文件？",
                "answer": "外国公民应随身携带护照、移民卡、登记证明、指纹登记证明，以及手机中的自愿医疗保险单照片或保险公司信息卡。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Как связаться с сотрудником МТУСИ по миграционному учету?",
                "answer": "Связаться с сотрудником по миграционному учету МТУСИ можно по электронной почте indec@mtuci.ru, по телефону +7 (495) 957-79-95, добавочный 437, а также через телеграм-канал @indec_mtuci."
            },
            "en": {
                "question": "How can I contact the MTUCI migration registration officer?",
                "answer": "You can contact the MTUCI migration registration officer by email at indec@mtuci.ru, by phone at +7 (495) 957-79-95, extension 437, or through the Telegram channel @indec_mtuci."
            },
            "zh": {
                "question": "如何联系 МТУСИ 负责移民登记的工作人员？",
                "answer": "可以通过邮箱 indec@mtuci.ru、电话 +7 (495) 957-79-95 转 437，或 Telegram 频道 @indec_mtuci 联系 МТУСИ 负责移民登记的工作人员。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "В какие сроки нужно встать на миграционный учет при новом въезде в Россию?",
                "answer": "По общему правилу иностранные граждане должны встать на миграционный учет не позднее 7 рабочих дней со дня въезда в Россию. Для некоторых стран сроки отличаются: граждане Казахстана, Армении и Киргизии могут подать документы в течение 30 календарных дней, граждане Таджикистана и Узбекистана — в течение 15 календарных дней, граждане Украины и Беларуси — в течение 90 календарных дней."
            },
            "en": {
                "question": "What are the deadlines for migration registration after entering Russia?",
                "answer": "As a general rule, foreign citizens must register for migration purposes no later than 7 working days after entering Russia. For some countries the deadlines differ: citizens of Kazakhstan, Armenia and Kyrgyzstan may submit documents within 30 calendar days; citizens of Tajikistan and Uzbekistan within 15 calendar days; citizens of Ukraine and Belarus within 90 calendar days."
            },
            "zh": {
                "question": "新入境俄罗斯后，多久内需要办理移民登记？",
                "answer": "通常情况下，外国公民应在入境俄罗斯后不晚于7个工作日内办理移民登记。部分国家有不同期限：哈萨克斯坦、亚美尼亚、吉尔吉斯斯坦公民可在30个自然日内提交材料；塔吉克斯坦和乌兹别克斯坦公民为15个自然日；乌克兰和白俄罗斯公民为90个自然日。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Когда и куда иностранные обучающиеся МТУСИ должны подавать документы для регистрации?",
                "answer": "Иностранные обучающиеся должны быть зарегистрированы по месту фактического проживания. Если студент планирует жить в общежитии МТУСИ, университет рекомендует обратиться в Отдел по работе с иностранными учащимися в течение 3 рабочих дней с момента въезда. Если студент проживает самостоятельно, регистрацию оформляет собственник помещения через районный отдел МВД по вопросам миграции или МФЦ «Мои документы»."
            },
            "en": {
                "question": "When and where should MTUCI international students submit documents for registration?",
                "answer": "International students must be registered at the place where they actually live. If a student plans to live in an MTUCI dormitory, the university recommends contacting the International Students Office within 3 working days after entering Russia. If the student lives independently, registration is handled by the property owner through the local migration department of the Ministry of Internal Affairs or the My Documents center."
            },
            "zh": {
                "question": "МТУСИ 外国学生应在什么时候、向哪里提交登记材料？",
                "answer": "外国学生应在实际居住地址办理登记。如果学生计划住在 МТУСИ 宿舍，学校建议在入境后3个工作日内联系外国学生事务部门。如果学生自行租房或居住在校外，登记由房屋所有人通过当地 МВД 移民事务部门或“Мои документы”中心办理。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для оформления регистрации иностранному студенту?",
                "answer": "Для оформления регистрации необходимо предоставить оригинал и 2 копии всех заполненных страниц паспорта, оригинал и 2 копии миграционной карты, оригинал и 2 копии прошлой регистрации при продлении, фото 3×4, копию карты дактилоскопии и копию действующих сертификатов медицинского освидетельствования."
            },
            "en": {
                "question": "What documents are required for an international student’s registration?",
                "answer": "For registration, you need the original and 2 copies of all completed passport pages, the original and 2 copies of the migration card, the original and 2 copies of the previous registration if it is being extended, a 3×4 photo, a copy of the fingerprint registration card, and copies of valid medical examination certificates."
            },
            "zh": {
                "question": "外国学生办理登记需要哪些材料？",
                "answer": "需要提交护照所有已填写页面的原件和2份复印件、移民卡原件和2份复印件、如为延期则需上一份登记证明原件和2份复印件、3×4照片、指纹登记卡复印件，以及有效体检证明复印件。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Какие требования к копиям документов для регистрации?",
                "answer": "Копии документов должны быть хорошо читаемыми, все отметки должны быть различимыми, бумага должна быть формата А4. Можно размещать несколько страниц документа на одной стороне листа при сохранении читаемости. Печать с двух сторон допускается и приветствуется. Паспорт нужно копировать полными разворотами, без разделения на страницы. Фотографии документов с заметными искажениями не принимаются."
            },
            "en": {
                "question": "What are the requirements for document copies for registration?",
                "answer": "Document copies must be clearly readable, all stamps and marks must be visible, and the paper size must be A4. Several document pages may be placed on one side of a sheet if they remain readable. Double-sided printing is allowed and welcome. Passport copies must be made as full two-page spreads, not as separate pages. Distorted photos of documents are not accepted."
            },
            "zh": {
                "question": "登记材料复印件有什么要求？",
                "answer": "复印件必须清晰可读，所有印章和标记都应能看清，纸张只能使用 A4。可以在一面纸上放置多个页面，但必须保持清晰。允许并建议双面打印。护照必须按完整展开页复印，不能拆成单页。明显变形的文件照片不予接受。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что будет, если нарушить сроки подачи документов на регистрацию?",
                "answer": "При нарушении сроков подачи документов законодательством РФ предусмотрены административные штрафы от 5000 до 800 000 рублей, административное выдворение и запрет на въезд в Россию на срок до 5 лет. Если студент проживает в общежитии и несвоевременно подает документы, может рассматриваться вопрос о выселении."
            },
            "en": {
                "question": "What happens if I miss the deadline for submitting registration documents?",
                "answer": "If the deadline is missed, Russian law may impose administrative fines from 5,000 to 800,000 rubles, administrative expulsion, and a ban on entering Russia for up to 5 years. If the student lives in a dormitory and submits documents late, eviction from the dormitory may also be considered."
            },
            "zh": {
                "question": "如果错过提交登记材料的期限会怎样？",
                "answer": "如果未按时提交登记材料，根据俄罗斯法律，可能被处以5000至800000卢布的行政罚款、行政驱逐出境，并可能被禁止入境俄罗斯最长5年。住在宿舍的学生如果未按时提交材料，还可能被考虑取消住宿资格。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что происходит с регистрацией при поездках по России?",
                "answer": "При постановке на учет в новом месте пребывания, например в гостинице, прежний миграционный учет в общежитии может быть автоматически прекращен. После возвращения в Москву или прибытия в следующее место пребывания нужно снова встать на миграционный учет. Обязательно заберите отрывной талон уведомления о прибытии из прошлого места пребывания."
            },
            "en": {
                "question": "What happens to my registration when I travel within Russia?",
                "answer": "When you register at a new place of stay, for example at a hotel, your previous migration registration at the dormitory may be automatically cancelled. After returning to Moscow or arriving at the next place of stay, you need to register again. Be sure to take the detachable part of the arrival notification from your previous place of stay."
            },
            "zh": {
                "question": "在俄罗斯境内旅行时，登记会发生什么变化？",
                "answer": "如果你在新的停留地点办理登记，例如酒店，原来的宿舍移民登记可能会自动终止。返回莫斯科或到达下一个居住地点后，需要重新办理移民登记。请务必从上一个停留地点带走到达通知的可撕联。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что происходит с регистрацией при поездках за границу?",
                "answer": "При выезде за границу действующий миграционный учет прекращает считаться действующим с момента отметки о выезде на пограничном контроле. После возвращения в Россию необходимо снова встать на миграционный учет в течение 3 дней с момента пересечения границы, даже если срок старой регистрации еще не истек."
            },
            "en": {
                "question": "What happens to my registration when I travel abroad?",
                "answer": "When you leave Russia, your current migration registration is no longer valid from the moment the border control exit stamp is placed. After returning to Russia, you must register again within 3 days after crossing the border, even if the old registration has not expired yet."
            },
            "zh": {
                "question": "出国旅行时，登记会发生什么变化？",
                "answer": "离开俄罗斯时，从边检盖出境章的那一刻起，原有移民登记不再有效。返回俄罗斯后，即使旧登记的有效期尚未结束，也需要在入境后3天内重新办理移民登记。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что делать иностранному студенту при въезде в Россию?",
                "answer": "При пересечении границы иностранный гражданин получает новую миграционную карту и сам заполняет цель въезда. У обучающегося должна быть указана цель въезда «УЧЕБА». После пересечения границы в течение 3 дней нужно обратиться в Отдел по работе с иностранными учащимися."
            },
            "en": {
                "question": "What should an international student do when entering Russia?",
                "answer": "When crossing the border, a foreign citizen receives a new migration card and fills in the purpose of entry. Students, postgraduate students, trainees and interns must indicate “study” as the purpose of entry. Within 3 days after crossing the border, contact the International Students Office."
            },
            "zh": {
                "question": "外国学生入境俄罗斯时应该做什么？",
                "answer": "过境时，外国公民会收到新的移民卡，并自行填写入境目的。学生、研究生、进修生和实习生应填写“学习”作为入境目的。入境后3天内需要联系外国学生事务部门。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Когда нужно подавать документы на продление визы?",
                "answer": "Обращаться за продлением визы необходимо не позднее 20 рабочих дней до окончания срока действия визы, чтобы сотрудники университета успели подготовить документы с учетом требований законодательства РФ."
            },
            "en": {
                "question": "When should I submit documents to extend my visa?",
                "answer": "You must apply for visa extension no later than 20 working days before the visa expires so that university staff can prepare the documents in accordance with Russian legal requirements."
            },
            "zh": {
                "question": "什么时候需要提交签证延期材料？",
                "answer": "必须在签证到期前不少于20个工作日申请延期，以便学校工作人员根据俄罗斯法律要求准备材料。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Какие документы нужны иностранному студенту для оформления визы?",
                "answer": "Для оформления визы необходимо предоставить оригинал и 2 копии заполненных страниц паспорта, оригинал и 2 копии миграционной карты, оригинал и 2 копии регистрации, фото 3×4, копию карты дактилоскопии и копию действующих сертификатов медицинского освидетельствования."
            },
            "en": {
                "question": "What documents does an international student need for visa processing?",
                "answer": "For visa processing, you need the original and 2 copies of completed passport pages, the original and 2 copies of the migration card, the original and 2 copies of registration, a 3×4 photo, a copy of the fingerprint registration card, and copies of valid medical examination certificates."
            },
            "zh": {
                "question": "外国学生办理签证需要哪些材料？",
                "answer": "办理签证需要提交护照已填写页面的原件和2份复印件、移民卡原件和2份复印件、登记证明原件和2份复印件、3×4照片、指纹登记卡复印件，以及有效体检证明复印件。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Какой размер госпошлины за оформление многократной визы?",
                "answer": "Размер госпошлины за оформление многократной визы составляет 1920 рублей."
            },
            "en": {
                "question": "What is the state fee for a multiple-entry visa?",
                "answer": "The state fee for issuing a multiple-entry visa is 1,920 rubles."
            },
            "zh": {
                "question": "办理多次入境签证的国家手续费是多少？",
                "answer": "办理多次入境签证的国家手续费为1920卢布。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Как оплатить госпошлину за оформление визы?",
                "answer": "Госпошлину можно оплатить в приложении Сбербанк Онлайн или у сотрудников банка. Образец квитанции можно получить в Отделе по работе с иностранными учащимися либо оплатить онлайн с помощью сотрудников отдела. Важно правильно оплатить квитанцию и ввести корректные данные, так как она подается в комплекте документов в МВД."
            },
            "en": {
                "question": "How can I pay the visa state fee?",
                "answer": "The state fee can be paid through Sberbank Online or with bank staff. You can get a sample receipt at the International Students Office or pay online with the help of its staff. It is important to enter the correct details because the receipt is submitted together with the documents to the Ministry of Internal Affairs."
            },
            "zh": {
                "question": "签证国家手续费如何支付？",
                "answer": "可以通过 Сбербанк Онлайн 应用或银行工作人员支付。缴费单样本可在外国学生事务部门领取，也可以在该部门工作人员帮助下在线支付。务必正确填写付款信息，因为收据会随材料一起提交给 МВД。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что происходит с визой иностранного студента при академическом отпуске?",
                "answer": "Иностранные обучающиеся, находящиеся в академическом отпуске, сохраняют статус обучающегося и имеют право продлевать учебную визу на срок академического отпуска."
            },
            "en": {
                "question": "What happens to an international student’s visa during academic leave?",
                "answer": "International students on academic leave keep their student status and have the right to extend their study visa for the period of academic leave."
            },
            "zh": {
                "question": "外国学生休学期间，签证会怎样？",
                "answer": "处于休学期间的外国学生仍保留学生身份，并有权在休学期限内延长学习签证。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Нужно ли иностранному студенту оформлять медицинскую страховку?",
                "answer": "Да. Все иностранные граждане должны иметь полис добровольного медицинского страхования, действующий со дня пересечения границы и до конца срока пребывания в России. При отсутствии полиса ДМС или договора с медицинской организацией может быть составлен административный протокол о нарушении порядка въезда и пребывания в России."
            },
            "en": {
                "question": "Does an international student need medical insurance?",
                "answer": "Yes. All foreign citizens must have voluntary health insurance valid from the day they cross the border until the end of their stay in Russia. Without VHI or a medical service agreement, an administrative protocol may be issued for violating entry and stay rules in Russia."
            },
            "zh": {
                "question": "外国学生需要办理医疗保险吗？",
                "answer": "需要。所有外国公民都必须持有自愿医疗保险，保险应从入境之日起一直有效到在俄罗斯停留期结束。如果没有自愿医疗保险或医疗服务合同，可能会因违反入境和居留规定被出具行政违法记录。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Какая медицинская страховка подойдет иностранному студенту?",
                "answer": "Полис ДМС должен включать амбулаторно-поликлиническое обслуживание, лечебно-диагностические мероприятия, вызов врача на дом, экстренную стационарную помощь, медицинскую эвакуацию и репатриацию. Рекомендуемое страховое покрытие — не менее 500 000 рублей."
            },
            "en": {
                "question": "What type of medical insurance is suitable for an international student?",
                "answer": "The VHI policy should include outpatient care, treatment and diagnostic services, home doctor visits, emergency hospital care, medical evacuation and repatriation. Recommended coverage is at least 500,000 rubles."
            },
            "zh": {
                "question": "外国学生适合办理哪种医疗保险？",
                "answer": "自愿医疗保险应包括门诊服务、诊疗服务、上门医生服务、紧急住院救治、医疗转运和遣返。建议保险金额不少于500000卢布。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Оформляет ли университет медицинскую страховку для иностранных студентов?",
                "answer": "Иностранные обучающиеся могут обратиться к сотруднику Отдела по работе с иностранными учащимися для оформления полиса ДМС от проверенных партнеров университета. В стоимость полиса ДМС включен медосмотр с указанием группы здоровья."
            },
            "en": {
                "question": "Does the university arrange medical insurance for international students?",
                "answer": "International students can contact the International Students Office to arrange a VHI policy through the university’s trusted partners. The cost of the policy includes a medical check-up with a health group indication."
            },
            "zh": {
                "question": "学校可以为外国学生办理医疗保险吗？",
                "answer": "外国学生可以联系外国学生事务部门，通过学校认可的合作伙伴办理自愿医疗保险。保险费用中包含体检，并会注明健康组别。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что такое ежегодный медосмотр для иностранных студентов?",
                "answer": "Иностранные граждане, находящиеся в России, обязаны ежегодно проходить медицинский осмотр для получения справки о здоровье. Такая справка нужна для проживания в общежитии и для предоставления в учебное заведение."
            },
            "en": {
                "question": "What is the annual medical check-up for international students?",
                "answer": "Foreign citizens staying in Russia must undergo an annual medical check-up to obtain a health certificate. This certificate is required for dormitory residence and for submission to the educational institution."
            },
            "zh": {
                "question": "外国学生每年体检是什么？",
                "answer": "在俄罗斯停留的外国公民必须每年进行体检，以获得健康证明。该证明用于宿舍住宿，也需要提交给学校。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что такое дактилоскопическая регистрация?",
                "answer": "Дактилоскопическая регистрация и фотографирование — обязательная процедура для иностранных граждан, которые планируют находиться в России более 90 дней подряд. Перед процедурой нужно пройти медицинское освидетельствование. Во время процедуры снимаются отпечатки пальцев и проводится фотографирование. После прохождения выдается зеленая карточка свидетельства о дактилоскопической регистрации."
            },
            "en": {
                "question": "What is fingerprint registration?",
                "answer": "Fingerprint registration and photographing are mandatory for foreign citizens who plan to stay in Russia for more than 90 consecutive days. A medical examination must be completed before the procedure. During the procedure, fingerprints are taken and a photo is made. After completion, a green fingerprint registration certificate card is issued."
            },
            "zh": {
                "question": "什么是指纹登记？",
                "answer": "指纹登记和拍照是计划在俄罗斯连续停留超过90天的外国公民必须完成的程序。办理前需要先进行体检。办理过程中会采集指纹并拍照。完成后会发放绿色的指纹登记证明卡。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Где посмотреть список медицинских организаций для медосмотра перед дактилоскопической регистрацией?",
                "answer": "Перечень уполномоченных медицинских организаций для медицинского освидетельствования в Москве указан в приложении к постановлению Правительства Москвы от 28 сентября 2021 г. № 1517-ПП. Ссылка: https://kdp121.mos.ru/global_ruffe_tech/docs/1517ppm.pdf"
            },
            "en": {
                "question": "Where can I find the list of medical organizations for the examination before fingerprint registration?",
                "answer": "The list of authorized medical organizations for medical examination in Moscow is provided in the appendix to Moscow Government Resolution No. 1517-PP dated September 28, 2021. Link: https://kdp121.mos.ru/global_ruffe_tech/docs/1517ppm.pdf"
            },
            "zh": {
                "question": "在哪里可以查看指纹登记前体检机构名单？",
                "answer": "莫斯科获授权进行体检的医疗机构名单见莫斯科市政府2021年9月28日第1517-ПП号决议附件。链接：https://kdp121.mos.ru/global_ruffe_tech/docs/1517ppm.pdf"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Кому и когда нужно проходить дактилоскопическую регистрацию?",
                "answer": "Дактилоскопическую регистрацию проходят все иностранные граждане, планирующие пребывать в России более 90 дней подряд, кроме граждан Республики Беларусь. Свидетельство о прохождении дактилоскопической регистрации нужно предъявить сотруднику по миграционному учету в Отделе по работе с иностранными учащимися при следующем продлении срока пребывания."
            },
            "en": {
                "question": "Who needs fingerprint registration and when?",
                "answer": "All foreign citizens planning to stay in Russia for more than 90 consecutive days must complete fingerprint registration, except citizens of Belarus. The fingerprint registration certificate must be shown to the migration registration officer at the International Students Office during the next extension of stay."
            },
            "zh": {
                "question": "哪些人需要办理指纹登记，什么时候办理？",
                "answer": "除白俄罗斯公民外，所有计划在俄罗斯连续停留超过90天的外国公民都需要办理指纹登记。下一次延长停留期限时，应向外国学生事务部门负责移民登记的工作人员出示指纹登记证明。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Медицинский полис и медицинское освидетельствование — это одно и то же?",
                "answer": "Нет. Медицинский полис позволяет получать медицинскую помощь на территории субъекта РФ, где он оформлен, например в Москве. Медицинское освидетельствование — это обязательная процедура для иностранных граждан, планирующих находиться в России более 90 дней подряд."
            },
            "en": {
                "question": "Are medical insurance and medical examination the same thing?",
                "answer": "No. A medical insurance policy allows you to receive medical care in the region of Russia where it was issued, for example in Moscow. A medical examination is a mandatory procedure for foreign citizens planning to stay in Russia for more than 90 consecutive days."
            },
            "zh": {
                "question": "医疗保险和体检是一回事吗？",
                "answer": "不是。医疗保险是在办理地所在的俄罗斯联邦主体内获得医疗服务的文件，例如在莫斯科办理则适用于莫斯科。体检是计划在俄罗斯连续停留超过90天的外国公民必须完成的程序。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Входит ли медицинское освидетельствование в стоимость медицинского полиса?",
                "answer": "Нет. Медицинское освидетельствование оплачивается отдельно и пройти его можно только в медицинских организациях, утвержденных Правительством Москвы."
            },
            "en": {
                "question": "Is the medical examination included in the cost of medical insurance?",
                "answer": "No. The medical examination is paid separately and can only be completed at medical organizations approved by the Moscow Government."
            },
            "zh": {
                "question": "体检费用包含在医疗保险里吗？",
                "answer": "不包含。体检需要单独付费，并且只能在莫斯科市政府批准的医疗机构进行。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Можно ли выбросить миграционную карту, если срок в ней истек?",
                "answer": "Нет, миграционную карту необходимо сохранять, так как ее нужно будет сдать в аэропорту при выезде из России."
            },
            "en": {
                "question": "Can I throw away my migration card if the date on it has expired?",
                "answer": "No, you must keep your migration card because it will need to be handed in at the airport when leaving Russia."
            },
            "zh": {
                "question": "如果移民卡上的期限过期了，可以丢掉吗？",
                "answer": "不可以。移民卡必须保留，因为离开俄罗斯时需要在机场交回。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что делать, если осталась старая регистрация?",
                "answer": "Регистрацию с истекшим сроком действия нужно сдать в Отдел по работе с иностранными учащимися при продлении документов. Если при пересечении границы пограничная служба не забрала регистрацию, ее можно сдать в Отдел по работе с иностранными учащимися или оставить у себя."
            },
            "en": {
                "question": "What should I do if I still have my old registration document?",
                "answer": "Expired registration should be submitted to the International Students Office when extending documents. If border control did not take your registration when you crossed the border, you may either submit it to the International Students Office or keep it."
            },
            "zh": {
                "question": "如果手里还有旧登记证明怎么办？",
                "answer": "过期的登记证明应在办理文件延期时交给外国学生事务部门。如果过境时边检没有收走登记证明，可以交给外国学生事务部门，也可以自己保留。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что делать иностранному гражданину, если он потерял документы?",
                "answer": "Если иностранный гражданин потерял паспорт, миграционную карту или регистрацию, нужно незамедлительно обратиться в отделение полиции за справкой об утере и сообщить об этом в Отдел по работе с иностранными учащимися. Для восстановления паспорта нужно обратиться в посольство своей страны. После получения нового паспорта необходимо в течение 3 дней обратиться в Отдел по работе с иностранными учащимися для переоформления остальных документов. Для восстановления миграционной карты нужно обратиться в полицию и в отделение по вопросам миграции МВД по месту проживания."
            },
            "en": {
                "question": "What should a foreign citizen do if they lose documents?",
                "answer": "If a foreign citizen loses a passport, migration card or registration document, they must immediately contact the police to obtain a loss certificate and then inform the International Students Office. To restore a passport, contact your country’s embassy. After receiving a new passport, contact the International Students Office within 3 days to reissue the other documents. To restore a migration card, apply to the police and to the local migration department of the Ministry of Internal Affairs."
            },
            "zh": {
                "question": "外国公民丢失证件该怎么办？",
                "answer": "如果丢失护照、移民卡或登记证明，应立即到警察局开具遗失证明，并通知外国学生事务部门。补办护照需要联系本国使馆。拿到新护照后，应在3天内联系外国学生事务部门重新办理其他文件。补办移民卡需要向警察局提交申请，并联系居住地 МВД 移民事务部门。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что делать, если во время обучения истекает срок действия паспорта иностранного студента?",
                "answer": "Необходимо заранее продлить или заменить паспорт в посольстве своей страны. После получения нового паспорта нужно в течение 3 дней обратиться в Отдел по работе с иностранными учащимися для внесения данных в личное дело и постановки на миграционный учет по новому документу. Нужно предоставить справку из посольства с фактической датой выдачи паспорта и два нотариально заверенных перевода нового паспорта. Студентам из визовых стран также нужно оформить перенос многократной визы из старого паспорта в новый."
            },
            "en": {
                "question": "What should I do if my passport expires during my studies?",
                "answer": "You should extend or replace your passport in advance at your country’s embassy. After receiving the new passport, contact the International Students Office within 3 days to update your personal file and migration registration. You must provide an embassy certificate with the actual passport issue date and two notarized translations of the new passport. Students from visa countries also need to transfer the multiple-entry visa from the old passport to the new one."
            },
            "zh": {
                "question": "学习期间护照快到期了怎么办？",
                "answer": "应提前在本国使馆延期或更换护照。拿到新护照后，需要在3天内联系外国学生事务部门，以更新个人档案并用新证件办理移民登记。需提供使馆出具的护照实际签发日期证明，以及新护照的两份公证翻译。来自签证国家的学生还需要将多次入境签证从旧护照转移到新护照。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Что происходит при выселении иностранного студента из общежития?",
                "answer": "После завершения обучения иностранный гражданин должен выселиться из общежития в течение 3 дней с даты, указанной в приказе об отчислении. При выселении университет подает в МВД уведомление об убытии из места пребывания для снятия с миграционного учета."
            },
            "en": {
                "question": "What happens when an international student moves out of the dormitory?",
                "answer": "After completing studies, a foreign citizen must move out of the dormitory within 3 days from the date stated in the expulsion order. When the student moves out, the university submits a departure notification to the Ministry of Internal Affairs to remove the student from migration registration."
            },
            "zh": {
                "question": "外国学生从宿舍退宿时会发生什么？",
                "answer": "完成学业后，外国公民应在除名命令中注明日期起3天内搬离宿舍。退宿时，大学会向 МВД 提交离开居住地点通知，以取消移民登记。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Можно ли иностранному студенту жить в общежитии во время академического отпуска?",
                "answer": "Нет. После предоставления академического отпуска формируется приказ о выселении из общежития."
            },
            "en": {
                "question": "Can an international student live in the dormitory during academic leave?",
                "answer": "No. After academic leave is granted, an order for eviction from the dormitory is issued."
            },
            "zh": {
                "question": "外国学生休学期间可以住在宿舍吗？",
                "answer": "不可以。学生获批休学后，学校会形成退宿命令。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Когда ставится штамп о продлении срока временного пребывания на миграционной карте?",
                "answer": "Отметка о продлении срока временного пребывания ставится в миграционной карте иностранного гражданина, прибывшего в Россию для обучения в безвизовом порядке. Если студент живет в общежитии, отметка ставится при продлении миграционного учета через Отдел по работе с иностранными учащимися. Если студент не живет в общежитии, нужно обращаться в территориальный отдел МВД по вопросам миграции по месту регистрации."
            },
            "en": {
                "question": "When is the extension stamp placed on the migration card?",
                "answer": "The extension mark is placed on the migration card of a foreign citizen who entered Russia for study without needing a visa. If the student lives in a dormitory, the mark is placed when migration registration is extended through the International Students Office. If the student does not live in a dormitory, they must contact the local migration department of the Ministry of Internal Affairs at the place of registration."
            },
            "zh": {
                "question": "什么时候会在移民卡上盖临时停留延期章？",
                "answer": "以免签方式来俄罗斯学习的外国公民，其临时停留延期标记会盖在移民卡上。如果学生住在宿舍，该标记通常在通过外国学生事务部门延长移民登记时办理。如果学生不住在宿舍，需要联系登记地的 МВД 移民事务部门。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Может ли иностранный обучающийся работать?",
                "answer": "Иностранные обучающиеся имеют право работать в свободное от учебы время без разрешения на работу в образовательных организациях высшего образования, где они обучаются, а также выполнять работу в других организациях во время каникул. Работодатель обязан корректно оформить трудоустройство и подать в территориальный орган МВД уведомление о заключении трудового договора с иностранным обучающимся."
            },
            "en": {
                "question": "Can an international student work?",
                "answer": "International students may work in their free time without a work permit at the higher education institution where they study, and may also work in other organizations during vacations. The employer must properly arrange the employment and notify the local office of the Ministry of Internal Affairs about the employment contract with the international student."
            },
            "zh": {
                "question": "外国学生可以工作吗？",
                "answer": "外国学生可以在课余时间在其就读的高等教育机构工作，无需办理工作许可；也可以在假期期间在其他单位工作。雇主必须依法办理劳动关系，并向当地 МВД 机构提交与外国学生签订劳动合同的通知。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Почему в новой регистрации с видом на жительство указан паспорт?",
                "answer": "По законодательству РФ документом, удостоверяющим личность иностранного гражданина, обычно является паспорт или заграничный паспорт. Вид на жительство подтверждает право проживания в России и указывается в дополнительных сведениях в части уведомления, которая остается у сотрудников МВД. Даже если отрывная часть регистрации не содержит сведений о виде на жительство, в информационных системах МВД обычно есть отметка о его наличии."
            },
            "en": {
                "question": "Why does my new registration show my passport if I have a residence permit?",
                "answer": "Under Russian law, the identity document of a foreign citizen is usually a passport or international passport. A residence permit confirms the right to live in Russia and is recorded in additional information in the part of the notification kept by the Ministry of Internal Affairs. Even if the detachable part of the registration does not show the residence permit, the Ministry’s systems usually contain information about it."
            },
            "zh": {
                "question": "已经有居留许可，为什么新登记上还是写护照？",
                "answer": "根据俄罗斯法律，外国公民的身份证件通常是护照或国际护照。居留许可是确认在俄罗斯居住权利的文件，通常写在 МВД 留存部分的补充信息中。即使登记证明的可撕联上没有显示居留许可，МВД 信息系统中通常会记录该信息。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Как иностранному студенту узнать, нужна ли ему виза?",
                "answer": "Учебную визу до приезда в Россию нужно оформить, если вы не являетесь гражданином Азербайджана, Южной Осетии, Беларуси, Казахстана, Кыргызстана, Молдовы, Грузии, Таджикистана, Украины, Армении, Узбекистана, России, а также если у вас нет дипломатической визы. Гражданам остальных стран необходимо оформить учебную визу до въезда в Россию."
            },
            "en": {
                "question": "How can I know whether I need a visa?",
                "answer": "You must obtain a study visa before coming to Russia if you are not a citizen of Azerbaijan, South Ossetia, Belarus, Kazakhstan, Kyrgyzstan, Moldova, Georgia, Tajikistan, Ukraine, Armenia, Uzbekistan or Russia, and if you do not hold a diplomatic visa. Citizens of other countries must obtain a study visa before entering Russia."
            },
            "zh": {
                "question": "怎么知道我是否需要签证？",
                "answer": "如果你不是阿塞拜疆、南奥塞梯、白俄罗斯、哈萨克斯坦、吉尔吉斯斯坦、摩尔多瓦、格鲁吉亚、塔吉克斯坦、乌克兰、亚美尼亚、乌兹别克斯坦或俄罗斯公民，并且没有外交签证，则必须在来俄罗斯前办理学习签证。其他国家公民也需要在入境俄罗斯前办理学习签证。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для легального пребывания в России студенту из визовой страны?",
                "answer": "Студенту из визовой страны нужно знать об однократной визе, многократной визе, миграционной карте, уведомлении о прибытии или регистрации, а также о МОДФ — обязательных процедурах медицинского освидетельствования, дактилоскопии и фотографирования иностранных граждан. Однократная виза оформляется только в стране гражданства и позволяет один въезд в Россию. Многократная виза оформляется только в России и позволяет въезжать много раз."
            },
            "en": {
                "question": "What documents should a student from a visa country know about for legal stay in Russia?",
                "answer": "A student from a visa country should know about a single-entry visa, multiple-entry visa, migration card, arrival notification or registration, and MODF — the mandatory medical examination, fingerprinting and photographing procedures for foreign citizens. A single-entry visa is issued only in the country of citizenship and allows one entry into Russia. A multiple-entry visa is issued only in Russia and allows multiple entries."
            },
            "zh": {
                "question": "来自签证国家的学生需要了解哪些合法停留文件？",
                "answer": "来自签证国家的学生需要了解一次入境签证、多次入境签证、移民卡、到达通知或登记，以及 МОДФ，即外国公民必须完成的体检、指纹登记和拍照程序。一次入境签证只能在国籍所在国办理，只允许进入俄罗斯一次。多次入境签证只能在俄罗斯办理，可以多次入境。"
            }
        }
    },
    {
        "category": "foreign_site_faq",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для легального пребывания в России студенту из безвизовой страны?",
                "answer": "Студенту из безвизовой страны нужно знать о миграционной карте, уведомлении о прибытии или регистрации, а также о МОДФ — обязательных процедурах медицинского освидетельствования, дактилоскопии и фотографирования иностранных граждан. Миграционная карта выдается на границе и содержит данные иностранного гражданина, дату пересечения границы и цель въезда. Регистрация подтверждает легальность нахождения иностранного гражданина в России."
            },
            "en": {
                "question": "What documents should a student from a visa-free country know about for legal stay in Russia?",
                "answer": "A student from a visa-free country should know about the migration card, arrival notification or registration, and MODF — the mandatory medical examination, fingerprinting and photographing procedures for foreign citizens. The migration card is issued at the border and contains the foreign citizen’s information, border crossing date and purpose of entry. Registration confirms the legality of stay in Russia."
            },
            "zh": {
                "question": "来自免签国家的学生需要了解哪些合法停留文件？",
                "answer": "来自免签国家的学生需要了解移民卡、到达通知或登记，以及 МОДФ，即外国公民必须完成的体检、指纹登记和拍照程序。移民卡在边境发放，包含外国公民信息、入境日期和入境目的。登记证明外国公民在俄罗斯合法停留。"
            }
        }
    }
]
migration_site_questions = [
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Какие законы регулируют пребывание иностранных граждан в России?",
                "answer": "Правовое положение иностранных граждан в России регулируется федеральными законами о правовом положении иностранных граждан, о порядке выезда из Российской Федерации и въезда в Российскую Федерацию, о миграционном учете иностранных граждан, а также КоАП РФ, Уголовным кодексом РФ и другими нормативными актами в сфере миграции."
            },
            "en": {
                "question": "What laws regulate the stay of foreign citizens in Russia?",
                "answer": "The stay of foreign citizens in Russia is regulated by federal laws on the legal status of foreign citizens, entry to and exit from the Russian Federation, migration registration, as well as the Code of Administrative Offences, the Criminal Code, and other migration-related regulations."
            },
            "zh": {
                "question": "外国公民在俄罗斯停留需要遵守哪些法律？",
                "answer": "外国公民在俄罗斯停留需要遵守关于外国公民法律地位、出入境、居留登记的联邦法律，以及行政违法法典、刑法和其他移民管理相关规定。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Какая цель въезда должна быть указана у иностранного студента?",
                "answer": "У иностранного студента, обучающегося по очной или очно-заочной форме, цель въезда в Россию должна быть указана как «учеба». Эта цель указывается в миграционной карте и визе и должна соответствовать фактической цели пребывания."
            },
            "en": {
                "question": "What purpose of entry should an international student indicate?",
                "answer": "For a full-time or part-time international student, the purpose of entry to Russia must be “study”. This purpose is indicated in the migration card and visa and must match the actual purpose of stay."
            },
            "zh": {
                "question": "外国学生入境目的应该写什么？",
                "answer": "全日制或非全日制在读外国学生入境俄罗斯时，入境目的应写为“学习”。该目的会写在移民卡和签证中，并且必须与实际停留目的一致。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что такое постановка на миграционный учет?",
                "answer": "Постановка на миграционный учет, или регистрация, дает иностранному гражданину право легально находиться на территории Российской Федерации. Иностранный студент обязан вставать на миграционный учет по месту фактического проживания."
            },
            "en": {
                "question": "What is migration registration?",
                "answer": "Migration registration allows a foreign citizen to legally stay in the Russian Federation. An international student must register at the place where they actually live."
            },
            "zh": {
                "question": "什么是居留登记？",
                "answer": "居留登记是外国公民在俄罗斯合法停留的重要手续。外国学生必须按照实际居住地址办理居留登记。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Когда нужно вставать на миграционный учет после прибытия?",
                "answer": "Иностранный гражданин должен оформить постановку на миграционный учет в день прибытия в место проживания, в крайнем случае — в ближайший рабочий день."
            },
            "en": {
                "question": "When should I complete migration registration after arrival?",
                "answer": "A foreign citizen should complete migration registration on the day of arrival at the place of residence, or at the latest on the next working day."
            },
            "zh": {
                "question": "到达居住地后什么时候需要办理居留登记？",
                "answer": "外国公民应在到达居住地当天办理居留登记，最晚也应在下一个工作日办理。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Куда обращаться для миграционного учета, если студент живет в общежитии?",
                "answer": "Если иностранный студент проживает в общежитии университета, для постановки на миграционный учет необходимо обратиться в день прибытия в Отдел по работе с иностранными учащимися по адресу: г. Москва, ул. Авиамоторная, д. 8а, кабинет 345."
            },
            "en": {
                "question": "Where should I go for migration registration if I live in the dormitory?",
                "answer": "If an international student lives in a university dormitory, they must contact the International Students Office on the day of arrival. Address: 8a Aviamotornaya Street, Moscow, room 345."
            },
            "zh": {
                "question": "如果住在学校宿舍，去哪里办理居留登记？",
                "answer": "如果外国学生住在学校宿舍，应在到达当天联系外国学生事务部门。地址：莫斯科，Авиамоторная 街 8а 号，345 室。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для миграционного учета в общежитии?",
                "answer": "Для постановки на миграционный учет в общежитии нужны паспорт и нотариально заверенный перевод паспорта, по которому пересекалась граница РФ; копии страниц паспорта со всеми отметками; миграционная карта; копия миграционной карты."
            },
            "en": {
                "question": "What documents are required for migration registration in the dormitory?",
                "answer": "For migration registration in the dormitory, you need your passport and notarized translation of the passport used to cross the Russian border, copies of all passport pages with stamps, the migration card, and a copy of the migration card."
            },
            "zh": {
                "question": "住在宿舍办理居留登记需要哪些文件？",
                "answer": "需要提交入境俄罗斯时使用的护照及其公证翻译件、护照所有带章页面的复印件、移民卡以及移民卡复印件。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Куда обращаться для миграционного учета, если студент живет в квартире?",
                "answer": "Если иностранный студент проживает в частном секторе, например в квартире или апартаментах, для постановки на миграционный учет необходимо обратиться к владельцу жилого помещения."
            },
            "en": {
                "question": "Where should I register if I live in a private apartment?",
                "answer": "If an international student lives in private accommodation, such as an apartment, they must contact the owner of the accommodation to complete migration registration."
            },
            "zh": {
                "question": "如果自己租房，居留登记怎么办？",
                "answer": "如果外国学生自己租房，例如住在公寓或私人住房，应联系房东办理居留登记。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для миграционного учета при проживании в квартире?",
                "answer": "При проживании в частном секторе обычно нужны паспорт и нотариально заверенный перевод, миграционная карта, выписка из приказа о зачислении, а при продлении регистрации — ходатайство о продлении срока временного пребывания в РФ, которое можно получить в Отделе по работе с иностранными учащимися."
            },
            "en": {
                "question": "What documents are needed for registration if I live in a private apartment?",
                "answer": "If you live in private accommodation, you usually need your passport and notarized translation, migration card, enrollment order extract, and, for registration extension, a request letter for extension of temporary stay in Russia, which can be obtained from the International Students Office."
            },
            "zh": {
                "question": "自己租房办理居留登记需要哪些文件？",
                "answer": "通常需要护照及公证翻译件、移民卡、录取或入学命令摘录。如果是延长登记，还需要临时停留期限延长申请函，该文件可在外国学生事务部门获取。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что происходит с регистрацией после выезда из России?",
                "answer": "Каждый раз при выезде из России и повторном въезде предыдущая миграционная карта и временная регистрация становятся недействительными. После нового въезда нужно заново подать документы для постановки на миграционный учет."
            },
            "en": {
                "question": "What happens to registration after leaving Russia?",
                "answer": "Each time a foreign student leaves Russia and enters again, the previous migration card and temporary registration become invalid. After re-entry, documents must be submitted again for migration registration."
            },
            "zh": {
                "question": "离开俄罗斯后原来的居留登记还有效吗？",
                "answer": "每次离开俄罗斯并重新入境后，之前的移民卡和临时居留登记都会失效。重新入境后，需要重新提交材料办理居留登记。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что нужно проверить в миграционной карте при въезде?",
                "answer": "При пересечении границы необходимо проверить, чтобы персональные данные в миграционной карте были указаны правильно, дата въезда на штампе пограничной службы была верной, а цель въезда была указана как «учеба»."
            },
            "en": {
                "question": "What should I check in my migration card when entering Russia?",
                "answer": "When crossing the border, check that your personal data in the migration card is correct, the entry date on the border stamp is correct, and the purpose of entry is indicated as “study”."
            },
            "zh": {
                "question": "入境时需要检查移民卡上的哪些信息？",
                "answer": "过境时应检查移民卡上的个人信息是否正确，边检章上的入境日期是否正确，入境目的是否写为“学习”。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что делать перед поездкой, чтобы на границе правильно оформили миграционную карту?",
                "answer": "Перед поездкой рекомендуется запросить по электронной почте у сотрудников Отдела по работе с иностранными учащимися справку о том, что вы являетесь студентом. При пересечении границы эту справку можно показать сотрудникам пограничной службы для правильного внесения данных в миграционную карту."
            },
            "en": {
                "question": "What should I do before travelling so that my migration card is filled correctly?",
                "answer": "Before travelling, it is recommended to request a certificate confirming that you are a student from the International Students Office by email. At the border, you can show this certificate to help ensure that your migration card is filled in correctly."
            },
            "zh": {
                "question": "旅行前怎样避免移民卡信息填写错误？",
                "answer": "建议出行前通过电子邮件向外国学生事务部门申请在读证明。过境时可以向边检人员出示该证明，以便正确填写移民卡信息。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что делать при изменении места пребывания?",
                "answer": "При изменении места пребывания необходимо встать на миграционный учет по новому адресу на следующий рабочий день после прибытия. Для этого нужно обратиться к владельцу жилого помещения."
            },
            "en": {
                "question": "What should I do if I change my place of stay?",
                "answer": "If you change your place of stay, you must complete migration registration at the new address on the next working day after arrival. Contact the owner of the accommodation for this."
            },
            "zh": {
                "question": "如果更换居住地点怎么办？",
                "answer": "如果更换居住地点，需要在到达新住处后的下一个工作日按新地址办理居留登记。应联系住房所有者办理。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Нужно ли заново оформлять миграционный учет после проживания в гостинице или хостеле?",
                "answer": "Да. Если студент меняет место проживания, например останавливается в гостинице или хостеле, а затем возвращается в общежитие, необходимо заново пройти постановку на миграционный учет, даже если предыдущие документы остались на руках."
            },
            "en": {
                "question": "Do I need to register again after staying in a hotel or hostel?",
                "answer": "Yes. If a student changes their place of stay, for example stays in a hotel or hostel and then returns to the dormitory, migration registration must be completed again, even if the previous documents are still in hand."
            },
            "zh": {
                "question": "住过酒店或青旅后还需要重新登记吗？",
                "answer": "需要。如果学生更换了停留地点，例如住过酒店或青旅后又回到宿舍，即使原来的文件还在手里，也需要重新办理居留登记。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Когда нужно продлевать учебную визу?",
                "answer": "Учебную визу необходимо продлевать минимум за 45 дней до окончания срока действия текущей визы. Если подать документы позднее, визу продлить может быть невозможно, и студенту придется выехать из РФ и оформлять новую визу по приглашению."
            },
            "en": {
                "question": "When should I extend my student visa?",
                "answer": "A student visa must be extended at least 45 days before the current visa expires. If documents are submitted later, extension may become impossible and the student may have to leave Russia and apply for a new visa by invitation."
            },
            "zh": {
                "question": "学习签证什么时候需要延期？",
                "answer": "学习签证应至少在当前签证到期前45天办理延期。如果提交材料太晚，可能无法延期，学生将需要离开俄罗斯并重新通过邀请函办理签证。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что нужно сделать после продления визы?",
                "answer": "После продления визы необходимо заново оформить постановку на миграционный учет в день получения новой визы."
            },
            "en": {
                "question": "What should I do after my visa is extended?",
                "answer": "After your visa is extended, you must complete migration registration again on the day you receive the new visa."
            },
            "zh": {
                "question": "签证延期后需要做什么？",
                "answer": "签证延期后，需要在拿到新签证当天重新办理居留登记。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что делать после отчисления иностранному студенту?",
                "answer": "Если иностранный студент завершил или прекратил обучение и вышел приказ об отчислении, он должен покинуть территорию Российской Федерации в течение трех рабочих дней с даты выхода приказа, но не позднее срока действия визы или срока, указанного в миграционной карте."
            },
            "en": {
                "question": "What should an international student do after expulsion or graduation?",
                "answer": "If an international student completes or stops studying and an expulsion order is issued, they must leave the Russian Federation within three working days from the date of the order, but no later than the visa validity period or the period indicated in the migration card."
            },
            "zh": {
                "question": "外国学生被除名或结束学习后需要做什么？",
                "answer": "如果外国学生完成或停止学习，并且学校发布除名命令，学生必须在命令发布之日起三个工作日内离开俄罗斯联邦，但不得晚于签证有效期或移民卡上注明的停留期限。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что такое РВПО?",
                "answer": "РВПО — это разрешение на временное проживание в целях получения образования. С 1 января 2023 года иностранные граждане, обучающиеся очно по программам бакалавриата, специалитета, магистратуры или аспирантуры в государственной образовательной организации, могут обратиться за оформлением РВПО."
            },
            "en": {
                "question": "What is RVPO?",
                "answer": "RVPO is a temporary residence permit for education purposes. Since January 1, 2023, foreign citizens studying full-time in bachelor’s, specialist, master’s, or postgraduate programs at a state educational organization may apply for RVPO."
            },
            "zh": {
                "question": "什么是 РВПО？",
                "answer": "РВПО 是以接受教育为目的的临时居留许可。自2023年1月1日起，在国家教育机构全日制学习本科、专家、硕士或研究生项目的外国公民可以申请 РВПО。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Какие преимущества дает РВПО?",
                "answer": "РВПО выдается на весь период обучения и дополнительно на 180 календарных дней после окончания учебы. Также многократная виза оформляется сразу на весь срок действия РВПО, не требуется ежегодно подтверждать проживание, можно безвыездно проживать в РФ, учиться и работать на основании РВПО, не нужно подтверждать знание русского языка, истории и законодательства РФ, а также появляется право на бесплатную медицинскую помощь по ОМС."
            },
            "en": {
                "question": "What are the advantages of RVPO?",
                "answer": "RVPO is issued for the entire study period plus 180 calendar days after graduation. A multiple-entry visa is issued for the full RVPO validity period. Annual residence confirmation is not required. It allows the student to live in Russia without leaving, study and work based on RVPO, avoid the Russian language, history and law exam requirement, and receive free medical care under OMS."
            },
            "zh": {
                "question": "РВПО 有什么优点？",
                "answer": "РВПО 的有效期覆盖整个学习期间，并在学习结束后额外延长180个自然日。多次签证可直接按 РВПО 有效期办理；不需要每年确认居住；可以在俄罗斯境内连续居住；可以学习和工作；不需要证明俄语、俄罗斯历史和法律知识；并可获得 ОМС 免费医疗服务。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Продлевает ли РВПО право проживания в общежитии?",
                "answer": "Нет. Получение РВПО не продлевает право проживания в общежитии. Проживать в общежитии МТУСИ можно только до окончания срока обучения, указанного в учебных документах."
            },
            "en": {
                "question": "Does RVPO extend the right to live in the dormitory?",
                "answer": "No. Receiving RVPO does not extend the right to live in the dormitory. A student may live in MTUCI dormitories only until the end of the study period indicated in their academic documents."
            },
            "zh": {
                "question": "РВПО 会延长住宿舍的权利吗？",
                "answer": "不会。获得 РВПО 不会延长住宿舍的权利。学生只能在学习文件规定的学习期限内住在 МТУСИ 宿舍。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Какие ограничения есть у РВПО?",
                "answer": "РВПО действует только в регионе получения. Оно может быть аннулировано, если иностранный гражданин находится за пределами РФ более 6 месяцев суммарно в течение календарного года, неоднократно привлекается к административной ответственности, переходит на очно-заочную или заочную форму обучения либо досрочно прекращает обучение."
            },
            "en": {
                "question": "What restrictions does RVPO have?",
                "answer": "RVPO is valid only in the region where it was issued. It may be cancelled if a foreign citizen stays outside Russia for more than 6 months in total during a calendar year, repeatedly receives administrative penalties, switches to part-time or distance study, or stops studying early."
            },
            "zh": {
                "question": "РВПО 有哪些限制？",
                "answer": "РВПО 只在签发地区有效。如果外国公民在一个自然年内累计离开俄罗斯超过6个月、多次受到行政处罚、转为非全日制或函授学习，或提前终止学习，РВПО 可能会被取消。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для оформления РВПО?",
                "answer": "Для оформления РВПО нужны заявление в двух экземплярах, паспорт и нотариально заверенный перевод всех страниц паспорта, фотография 3,5×4,5, справка об отсутствии судимости при необходимости, документы, подтверждающие статус обучающегося, документ об оплате госпошлины, уведомление о постановке на миграционный учет, миграционная карта, результаты медицинского освидетельствования и дактилоскопической регистрации."
            },
            "en": {
                "question": "What documents are required for RVPO?",
                "answer": "To apply for RVPO, you need an application in two copies, passport and notarized translation of all passport pages, a 3.5×4.5 photo, a criminal record certificate if required, documents confirming student status, proof of state fee payment, migration registration notice, migration card, medical examination results, and fingerprint registration documents."
            },
            "zh": {
                "question": "申请 РВПО 需要哪些文件？",
                "answer": "需要提交两份申请表、护照及所有页面的公证翻译件、3.5×4.5 照片、无犯罪记录证明如适用、学生身份证明文件、缴纳国家手续费的证明、居留登记通知、移民卡、体检结果以及指纹登记材料。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Как подать документы на РВПО?",
                "answer": "Для подачи документов на РВПО нужно зарегистрироваться на портале mc.mos.ru, выбрать услугу РВПО, загрузить документы в личный кабинет, дождаться сообщения о возможности личной подачи, подать документы лично в ММЦ Сахарово, ожидать решения до 2 месяцев, затем получить штамп РВПО и при необходимости визу. После получения РВПО в течение 7 рабочих дней нужно переоформить миграционный учет и сообщить об этом в Отдел по работе с иностранными учащимися."
            },
            "en": {
                "question": "How can I apply for RVPO?",
                "answer": "To apply for RVPO, register at mc.mos.ru, select the RVPO service, upload the documents, wait for a message allowing personal submission, submit the documents in person at the Sakharovo Migration Center, wait up to 2 months for a decision, then receive the RVPO stamp and visa if needed. After receiving RVPO, re-register your place of stay within 7 working days and inform the International Students Office."
            },
            "zh": {
                "question": "如何申请 РВПО？",
                "answer": "需要在 mc.mos.ru 注册，选择 РВПО 服务，在个人账户上传文件，等待可以现场提交的通知，然后亲自到 Сахарово 移民中心提交材料。决定通常最多需要2个月。获批后领取 РВПО 盖章，如有需要也领取签证。获得 РВПО 后，应在7个工作日内重新办理居留登记，并通知外国学生事务部门。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Когда нужно проходить дактилоскопическую регистрацию?",
                "answer": "Все иностранные граждане, планирующие пребывать в России более 90 дней подряд, обязаны пройти дактилоскопическую регистрацию в течение 90 дней с даты въезда."
            },
            "en": {
                "question": "When should fingerprint registration be completed?",
                "answer": "All foreign citizens planning to stay in Russia for more than 90 consecutive days must complete fingerprint registration within 90 days from the date of entry."
            },
            "zh": {
                "question": "什么时候需要办理指纹登记？",
                "answer": "计划在俄罗斯连续停留超过90天的外国公民，必须在入境之日起90天内完成指纹登记。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Где проходить медицинское освидетельствование перед дактилоскопией?",
                "answer": "Медицинское освидетельствование необходимо проходить в уполномоченных медицинских организациях из перечня, утвержденного Правительством Москвы."
            },
            "en": {
                "question": "Where should I complete the medical examination before fingerprint registration?",
                "answer": "The medical examination must be completed in authorized medical organizations from the list approved by the Moscow Government."
            },
            "zh": {
                "question": "指纹登记前在哪里体检？",
                "answer": "体检必须在莫斯科政府批准名单中的授权医疗机构进行。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Какие документы нужны для медицинского освидетельствования иностранного гражданина?",
                "answer": "Для медицинского освидетельствования нужны паспорт и его копия, нотариально заверенный перевод паспорта, сделанный на территории РФ, и его копия, миграционная карта и ее копия, виза и ее копия для визовых стран, а также регистрация и ее копия."
            },
            "en": {
                "question": "What documents are needed for a foreign citizen’s medical examination?",
                "answer": "For the medical examination, you need your passport and copy, notarized passport translation made in Russia and its copy, migration card and copy, visa and copy for visa countries, and registration notice and copy."
            },
            "zh": {
                "question": "外国公民体检需要哪些文件？",
                "answer": "需要护照及复印件、在俄罗斯境内办理的护照公证翻译件及复印件、移民卡及复印件、签证及复印件如适用，以及居留登记证明及复印件。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Куда обращаться после получения медицинских сертификатов для дактилоскопии?",
                "answer": "После получения трех медицинских сертификатов для прохождения дактилоскопической регистрации и фотографирования необходимо обратиться в подразделение ГБУ «Миграционный центр» по адресу: г. Москва, ул. Бахрушина, 18, стр. 1, либо в Миграционный центр Сахарово."
            },
            "en": {
                "question": "Where should I go after receiving medical certificates for fingerprint registration?",
                "answer": "After receiving three medical certificates, you must go for fingerprint registration and photographing to the Migration Center unit at 18 Bakhrushina Street, building 1, Moscow, or to the Sakharovo Migration Center."
            },
            "zh": {
                "question": "拿到体检证明后去哪里办理指纹登记？",
                "answer": "拿到三份体检证明后，需要前往莫斯科 Бахрушина 街18号1栋的“移民中心”部门，或前往 Сахарово 移民中心办理指纹登记和拍照。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что делать, если потерял миграционную карту?",
                "answer": "В день обнаружения пропажи миграционной карты нужно обратиться в ближайшее отделение полиции и сообщить об утере в Отдел по работе с иностранными учащимися, администратору гостиницы или собственнику квартиры. После получения справки об утере нужно обратиться в отдел МВД по вопросам миграции по месту проживания для получения дубликата миграционной карты, затем подать документы для нового уведомления о прибытии."
            },
            "en": {
                "question": "What should I do if I lose my migration card?",
                "answer": "On the day you discover the loss, contact the nearest police station and inform the International Students Office, hotel administrator, or apartment owner. After receiving a loss certificate, contact the migration department of the Ministry of Internal Affairs at your place of residence to obtain a duplicate migration card, then submit documents for a new arrival notification."
            },
            "zh": {
                "question": "如果丢失移民卡怎么办？",
                "answer": "发现移民卡丢失当天，应前往最近的警察局报案，并通知外国学生事务部门、酒店管理员或房东。取得遗失证明后，需要到居住地所属 МВД 移民部门申请移民卡副本，然后提交材料重新办理到达通知。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что делать, если потерял уведомление о прибытии?",
                "answer": "В день обнаружения пропажи уведомления о прибытии необходимо сообщить об этом в Отдел по работе с иностранными учащимися, администратору гостиницы или собственнику квартиры. Если студент проживает в общежитии, Отдел по работе с иностранными учащимися самостоятельно оформит дубликат. При самостоятельном проживании нужно обратиться в отдел МВД по вопросам миграции вместе с собственником квартиры или администратором гостиницы."
            },
            "en": {
                "question": "What should I do if I lose my arrival notification?",
                "answer": "On the day you discover the loss of the arrival notification, inform the International Students Office, hotel administrator, or apartment owner. If you live in the dormitory, the International Students Office will prepare a duplicate. If you live independently, you must contact the migration department of the Ministry of Internal Affairs together with the apartment owner or hotel administrator."
            },
            "zh": {
                "question": "如果丢失到达通知怎么办？",
                "answer": "发现到达通知丢失当天，应通知外国学生事务部门、酒店管理员或房东。如果住在学校宿舍，外国学生事务部门会办理副本。如果自己租房，需要和房东或酒店管理员一起到 МВД 移民部门办理。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что делать, если потерял паспорт с российской визой?",
                "answer": "В день обнаружения пропажи паспорта с визой нужно обратиться в ближайшее отделение полиции, сообщить об утере в Отдел по работе с иностранными учащимися, затем получить справку об утере и обратиться в консульский отдел посольства своей страны для оформления нового паспорта. После получения нового паспорта необходимо сообщить в Отдел по работе с иностранными учащимися и подать документы для новой визы или переноса визы, а затем оформить новое уведомление о прибытии."
            },
            "en": {
                "question": "What should I do if I lose my passport with a Russian visa?",
                "answer": "On the day you discover the loss, contact the nearest police station, inform the International Students Office, obtain a loss certificate, and contact the consular section of your embassy to issue a new passport. After receiving the new passport, inform the International Students Office, submit documents for a new visa or visa transfer, and then complete a new arrival notification."
            },
            "zh": {
                "question": "如果丢失带俄罗斯签证的护照怎么办？",
                "answer": "发现护照和签证丢失当天，应前往最近的警察局报案，并通知外国学生事务部门。取得遗失证明后，需要联系本国驻俄罗斯使馆领事部门办理新护照。拿到新护照后，应通知外国学生事务部门，提交办理新签证或签证转移的材料，然后重新办理到达通知。"
            }
        }
    },
    {
        "category": "migration",
        "translations": {
            "ru": {
                "question": "Что делать, если потерял паспорт при безвизовом въезде?",
                "answer": "При потере паспорта иностранному гражданину из безвизовой страны нужно в день обнаружения пропажи обратиться в полицию, сообщить об утере в Отдел по работе с иностранными учащимися, получить справку об утере и обратиться в посольство своей страны для оформления нового паспорта. После получения нового паспорта необходимо в течение 3 рабочих дней оформить новое уведомление о прибытии."
            },
            "en": {
                "question": "What should I do if I lose my passport and entered Russia without a visa?",
                "answer": "If a foreign citizen from a visa-free country loses their passport, they must contact the police on the day of discovery, inform the International Students Office, obtain a loss certificate, and apply to their embassy for a new passport. After receiving the new passport, a new arrival notification must be completed within 3 working days."
            },
            "zh": {
                "question": "免签入境后护照丢了怎么办？",
                "answer": "免签国家的外国公民发现护照丢失当天，应前往警察局报案，通知外国学生事务部门，取得遗失证明，并联系本国使馆办理新护照。拿到新护照后，需要在3个工作日内重新办理到达通知。"
            }
        }
    }
]

def get_category_id(cursor, code):
    cursor.execute(
        "SELECT id FROM Category WHERE code = %s",
        (code,)
    )
    row = cursor.fetchone()

    if row is None:
        raise ValueError(
            f"Категория '{code}' не найдена. "
            "Сначала добавьте её в scripts/init_db.py и запустите py scripts/init_db.py."
        )

    return row["id"]


def question_exists(cursor, question_text, language):
    cursor.execute(
        """
        SELECT id
        FROM Translation
        WHERE question_text = %s AND language = %s
        """,
        (question_text, language)
    )
    row = cursor.fetchone()
    return row is not None


def add_question(cursor, item):
    category_id = get_category_id(cursor, item["category"])

    ru_question = item["translations"]["ru"]["question"]

    if question_exists(cursor, ru_question, "ru"):
        print(f"Пропущено, уже есть в базе: {ru_question}")
        return

    cursor.execute(
        """
        INSERT INTO Question (category_id)
        VALUES (%s)
        RETURNING id
        """,
        (category_id,)
    )

    question_id = cursor.fetchone()["id"]

    for language, translation in item["translations"].items():
        cursor.execute(
            """
            INSERT INTO Translation (question_id, language, question_text, answer_text)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (question_id, language) DO NOTHING
            """,
            (
                question_id,
                language,
                translation["question"],
                translation["answer"]
            )
        )

    print(f"Добавлен вопрос: {ru_question}")


def seed_database():
    connection = get_db_connection()
    cursor = connection.cursor()

    all_question_blocks = [
        library_questions,
        military_questions,
        graduation_questions,
        activities_questions,
        study_questions,
        documents_questions,
        international_questions,
        it_support_questions,
        medical_questions,
        housing_questions,
        organizational_questions,
        transfer_questions,
        discipline_questions,
        practice_questions,
        attestation_questions,
        psychological_service_questions,
        disciplinary_commission_questions,
        scholarship_questions,
        first_year_questions,
        employment_questions,
        study_process_questions,
        foreign_site_faq_questions,
        migration_site_questions,
    ]

    for question_block in all_question_blocks:
        for item in question_block:
            add_question(cursor, item)

    connection.commit()
    cursor.close()
    connection.close()

    print("Данные успешно добавлены в базу PostgreSQL.")


if __name__ == "__main__":
    seed_database()
