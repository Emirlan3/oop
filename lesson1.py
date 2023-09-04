""" введение в postgreSQL. Создание баз данных и таблиц """
# id username password
# 1 test  1234

# MySQL, Firestore, MongoDB, MarinaDB, SQrinaDB, SQlite, PostgresSQL

# Примеры СУБД(система управление базами )

# PostgreSQL - система упарвление БД (это комплекс программ, позваляющий создават бд и манипулировать ими (администрирование бд))

# Бд - оранизованная структура для хранение взаимосвязенных данных (больших объемов)

# SQL (Structured Query Language) -> декларативный язык структурированнх запросов - язык вопросов, изпользумемый для сохранение. изменение, 
# удаление и извлеченние данных бд

# 1. sudo -i -u postgres - переход учетную запись  postgres
# psql - перехоод к командной строке

# 2. sudo -u postgres psql - преход к командной строке (под юзенром postgres и подключение к бд posrgres)

# psql - переход к командной строке (под вашим и поделключение к вашей бд) (для работы этой командной должень существовать юзер 
# и бд в терминале)

# \l - список бвзы данных
# \du - список полбзаватель
# \c <db_name> -> пожклячение бд db_name
# \c <db_name> - подключение всех таблиц в бд
# \d <table_name> - простмотр родроюной таблиц инфо о таблице table_name
# \d - выход
# SQL запросы
# 1.CREATE DATABESE <db_name>; - создание бд
# 2. CREATE TABLE - <table_name(column_name type, ...)>; - > создание таблицы
# 3. CREATE USER <username>;
    # CREATE USER <username> WITH PASSWORD 'your_password' ; -> создание пользователя

# 4. ALTER ROLE <usernmae> WITH <PRIVILEGE>' , предоставление права пользавателью