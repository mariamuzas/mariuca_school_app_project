# Mariuca School App
The Mariuca School App is a web app designed to simplify the process of running a school offering cooking courses. 
The app offers the ability to register new student and create courses, as well as adding existing students to new courses. 
The simplicity of the app is exactly the desired result as the Mariuca School App aims to remove the clutter from the everyday running of a cookery school. 

## MVP

The app should:

- Allow the school to create and edit Students
- Allow the school to create and edit Courses
- Allow the school to book members on specific classes
- Show a list of all upcoming courses
- Show all students that are booked in for a particular class

## Example Extensions

- The School could be able to give its students Premium or Standard membership. Standard students can only be signed up for Beginner and Intermediate courses, Premium members would be entitled to Advanced courses


## Setup
Create the database of this project:
```
$ psql -d school_manager -f db/school_manager.sql

```

Seed the database:
```
$ python3 console.py
```

Run the script:
```
$  flask run
```
<br />

<img width="1279" alt="MariucaSchool_landing_page" src="https://user-images.githubusercontent.com/65955047/103486498-49c6f000-4df6-11eb-8fbb-ecb357884b91.png">
