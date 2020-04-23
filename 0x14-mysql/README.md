# 0x14-mysql
## 4-mysql_configuration_primary, 4-mysql_configuration_replica
Having a replica member on for your MySQL database has 2 advantages:
    Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data
    Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed
Requirements:
    MySQL primary must be hosted on web-01 - do not use the bind-address, just comment out this parameter
    MySQL replica must be hosted on web-02
    Setup replication for the MySQL database named tyrell_corp
    Provide your MySQL primary configuration as answer file(my.cnf or mysqld.cnf) with the name 4-mysql_configuration_primary
    Provide your MySQL replica configuration as an answer file with the name 4-mysql_configuration_replica
## 5-mysql_backup
Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
Requirements:
    The MySQL dump must contain all your MySQL databases
    The MySQL dump must be named backup.sql
    The MySQL dump file has to be compressed to a tar.gz archive
    This archive must have the following name format: day-month-year.tar.gz
    The user to connect to the MySQL database must be root
    The Bash script accepts one argument that is the password used to connect to the MySQL database