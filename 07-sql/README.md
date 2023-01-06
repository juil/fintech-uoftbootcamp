# Unit 07: SQL

## PostgreSQL

### psql: Command line tool

[Homebrew](https://wiki.postgresql.org/wiki/Homebrew)
```
$ brew install postgresql
$ brew services start postgresql # or "brew services run postgresql" to have it not restart at boot time
# or the pg_ctl command it mentions
```

[Cheat sheet](https://tomcam.github.io/postgres/)

### Useful Notes

Change default user:
```
$ export PGDATABASE=mydata
$ export PGUSER=myuser
$ psql
```
[reddit](https://www.reddit.com/r/PostgreSQL/comments/ryx0cf/psql_change_default_database_from_postgres_to/)

