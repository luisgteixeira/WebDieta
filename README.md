# WebDieta

## Requirements
* Python 3
* Package psycopg2
* PostgreSQL

## Getting Started

### Install psycopg2
```
$ pip3 install psycopg2
$ pip3 install psycopg2-binary
```

### Install PostgreSQL Ubuntu
```
$ sudo apt-get update
$ sudo apt-get install postgresql postgresql-contrib
```

### Configure PostgreSQL Ubuntu
`$ sudo -u postgres psql`
```SQL
CREATE USER user WITH PASSWORD 'password';
CREATE DATABASE webdieta WITH OWNER user ENCODING 'utf-8';
```
