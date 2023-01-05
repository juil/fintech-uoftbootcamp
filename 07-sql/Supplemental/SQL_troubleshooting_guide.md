# SQL Troubleshooting Guide

This troubleshooting guide contains common issues and fixes pertaining to the use of pgAdmin and postgreSQL.

## Unable to Import/Export CSV via pgAdmin

In the event of an error when using pgAdmin's data import tool, the database tables can be created and populated using the provided .sql files. The following details two methods for manually creating and populating the tables:

### Execute .sql file via pgAdmin Query Editor

Each activity will contain schema.sql files that can be used to create the database tables. The table can then be populated using pgAdmin's data import tool and the CSV files provided. If the data import tool fails, a seed.sql file is also provided that will manually insert the data into the tables. Please run the seed.sql file after the schema.sql file to ensure that the table is properly configured before data is inserted.

![sql-file-manual-insert](Images/sql-file-manual-insert.png)

### Execute .sql file via postgreSQL CLI

PostgreSQL additionally provides a Command Line Interface (CLI) to access and query SQL databases/tables, and execute .sql files. This method has the advantage of being a native operation in which the data import operation is done entirely within the postgreSQL environment, providing reliability and speed.

In order to access the postgreSQL CLI, you'll have to first set the `PATH` environment variable to point to the postgreSQL binaries. Windows users will have to use the Command Prompt, as Git Bash has issues with the psql CLI. When ready, run one of the following commands, depending on your operating system:

* Mac OS: `export PATH=$PATH:/Library/PostgreSQL/12/bin`.
* Windows: `SET PATH=%PATH%;C:\Program Files\PostgreSQL\12\bin`

**Note:** At the time of this writing, PostgreSQL has been updated to version 12. Therefore, if your PostgreSQL version is still on 11, then your paths may be the following:

* Mac OS: `/Library/PostgreSQL/11/bin`
* Windows: `C:\Program Files\PostgreSQL\11\bin`

Make sure to check that the PATH changes have gone into effect; use the respective `ECHO` syntax for your operating system to query the contents of the environmental `PATH` variable. You may have to restart your terminal for changes to go into effect.

![export-psql-path](Images/export-psql-path.png)

![export-psql-path-windows](Images/export-psql-path-windows.PNG)

Now navigate to the folder containing the .sql file and run the following command:

`psql -U <username> -d <database> -f <sql-file>`.

In this case, the command should be the following:

`psql -U postgres -d mortgage_db -f seed.sql`.

* `psql`: The postgreSQL CLI
* `-U` : The username of the postgreSQL account.
* `-d` : The specified database.
* `-f` : The filepath to the .sql file.

![sql-file-CLI](Images/sql-file-CLI.png)

![psql-insert-windows](Images/psql-insert-windows.PNG)

### SQLAlchemy, Psycopg2, and Pandas DataFrames

Data can also be written from a Pandas DataFrame directly to a PostgreSQL table using the in-built `to_sql` function. In order to make the connection to the PostgreSQL database, additional libraries such as `sqlalchemy` and `psycopg2` must be installed; `sqlalchemy` acts as the connection manager, while `psycopg2` acts as the PostgreSQL drivers needed to connect specifically to a PostgreSQL DB.

In order to import the `sqlalchemy` and `psycopg2` libraries, they will first need to be installed into the Anaconda environment.

* `conda install -c anaconda sqlalchemy`

* `pip install psycopg2`

![sqlalchemy-psycopg2-import](Images/sqlalchemy-psycopg2-import.png)

In addition, the data residing within the CSV will need to be imported into a Pandas DataFrame. Therefore, the `read_csv` function should be used.

![dataframe-read-csv](Images/dataframe-read-csv.png)

Next, the connection to the PostgreSQL database will need to be established. In order to make the connection, a database URI or connection string should be provided.

Database connection strings typically consist of the following parameters:

* `<connector>://<username>:<password>@<server>:<port>/<database>`

The database connection string in this case was the following:

* `postgresql://postgres:postgres@localhost:5432/mortgage_db`

Then, instantiate a connection to the database by using the newly created database connection string with the `create_engine` function.

![create-engine](Images/create-engine.png)

Finally, now that the connection to the PostgreSQL database has been established, the `to_sql` function can be used to write DataFrame contents to the specified PostgreSQL table. The `to_sql` function uses the following parameters:

* `name`: Name of the SQL table
* `con`: The SQLAlchemy engine loaded with DB drivers
* `if_exists`: How to behave if the table already exists.
  
  * fail: Raise a ValueError.
  * replace: Drop the table before inserting new values.
  * append: Insert new values to the existing table.
  
* `index`: Writes the DataFrame index as a column.
* `dtype`: Specifies the datatype for columns in dictionary format.

![sqlalchemy-pandas-write](Images/sqlalchemy-pandas-write.png)

Lastly, in order to check if the data was properly inserted, the in-built Pandas `read_sql_query` DataFrame function can be used to query a database and read the results as a Pandas DataFrame.

![sqlalchemy-pandas-read](Images/sqlalchemy-pandas-read.png)

### PgAdmin cannot connect to the server or will not start

A common issue with starting the pgAdmin client is that the postgres service is not running. The postgres service must be started before any connection is made by a client, for example pgAdmin.

#### Windows

  - Press the window key and type `Services`.

  - Open the Services app. The services are in alphabetical order. Scroll down and find the postgres server entry.

![](Images/pg_check.png)

  - The status column should say running. If it does not then you will need to start the service. Right click on the entry and select `Start`.

![](Images/pg_start.png)

  - The postgres service should now report `Running` and client connection can be made.

![](Images/pg_run.png)

#### Mac

Services in windows are called processes in Mac.

  - Open a terminal and type the following command:
        ``` shell
        ps -ef | grep -i postgres
        ```

![](Images/pg_running_mac.png)

  - You should see an entry for a running process where the path points to the postgres install location.

  - On mac postgres will either install in `/usr/local/var/postgres` (older) or `/Library/PostgresSQL/<some_version>` (newer).

  - In the postgres install directory there will be `bin` and `data` folders. The `-D` parameter specifies the data folder path.

  - If there is not an entry and you need to start the process, type:

      ``` shell
      sudo -u postgres pg_ctl start -D  /Library/PostgresSQL/<some_version>/data
      ```

  - If `pg_ctl` is not found then postgres is either not installed or was installed in `/Library/PostgresSQL/<some_version>`. Assuming that it is installed to `/Library` it will need to be added to the user's path. An easy way to do this is to add the following entries to either `~/.bash_profile`, `~/.bashrc` or `~/.zshrc`. Any of these files will work and if none of them exist create an empty file in the user's home directory ,`~`, with one of the names. Make sure the profile file is for the correct shell, i.e. `bash` or `zsh`, the student uses. You can edit the file in vsCode.
    >**Important**: Replace some verison with the correct version number.
    ``` shell
    export PATH="/Library/PostgresSQL/<some_version>/bin:$PATH"
    export PGDATA="/Library/PostgresSQL/<some_version>/data:$PATH"
    ```

  - Once the entries are added, save the file and exit.

  - Now reload the environment variables with:

    ``` shell 
    . ~/.bash_profile
    ```
    >**Important**: Replace `.bash_profile` with the name of the file that you edited above.

  - Postgres will need to be started with user that was created when it was installed. The default username is `postgres` but students sometimes change this un-intentionally. To get the username type:

    ``` shell
    stat /Library/PostgresSQL/<some_version>/data
    ```

![](Images/pg_stat.png)

  - If the directory permissions are not `drwx------` then pgAdmin will not start on MacOS 11+. Run the following command to set the correct permissions:

    ``` shell
    sudo chmod -R 0700 /Library/PostgresSQL/<some_version>/
    ```

  - Finally start the service with:

    ``` shell
    sudo -u postgres pg_ctl start -D /Library/PostgresSQL/<some_version>/data
    ```
![](Images/pg_started_mac.png)
>**Important**: Replace `postgres` if the user owner is different.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

