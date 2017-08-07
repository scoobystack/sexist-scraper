# sexist-scraper

### Setup postgres db
- Install postgres: [Postgress App](https://postgresapp.com/)
  - Be sure to add the PostgressApp bin dir to your PATH in your bash profile
```
export PATH="/Applications/Postgres.app/Contents/Versions/9.5/bin:$PATH"
```
- Start postgres by launching Postgres in Applications folder
- Create scraper user and db
```
psql    #open psql prompt
create user scraper with password 'scraper'; 
create database scraper owner scraper;
\q      #quit psql
```

### Activate virtualenv and install deps
- In project root activate virtual environment   
```. /venv/bin/active```
- Install versioned dependencies from requirements.txt   
```pip install -r requirements.txt```
