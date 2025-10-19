# Overview

This project is a Smart Habit Tracker that helps users create, track, and manage their daily or weekly habits. The main goal was to build something practical while learning how to integrate Python applications with a cloud database, and to explore user authentication with Firebase. 

The software lets users sign up and log in securely, add new habits, view their habits, update them, delete them, and mark habits as completed. All habit data is stored in a Google Firestore cloud database, which allows the information to persist even if the program is closed. The project demonstrates CRUD operations (Create, Read, Update, Delete) in a real-world context, along with basic authentication and session management.

You can watch a demo of my software here: [Software Demo Video](https://youtu.be/sgitE24qk3I)

# Cloud Database

For this project, I used Google Firestore, a NoSQL cloud database provided by Firebase. Firestore is convenient because it allows me to store structured data without setting up and managing my own server, and it provides easy integration with Python.

The database structure is simple:

- Collection: `habits`
  - Document: Auto-generated ID for each habit
    - `user_id` → The ID of the user who owns this habit
    - `habit_name` → Name of the habit
    - `target_per_week` → How many times the user wants to complete it weekly
    - `completed_times` → Tracks how many times the habit has been completed
    - `last_updated` → Timestamp of the last update

# Development Environment

Refer to the requirements.txt file.

* Visual Studio Code
* Python 3.13.1
* Virtual Environment (venv)
* Git / GitHub
* Firebase
* Firestone
* Pyrebase
* Python-dotenv

# Useful Websites

- [Cloud Databases](https://www.mongodb.com/resources/basics/databases/cloud-databases)
- [NoSQL Tutorial](https://www.guru99.com/nosql-tutorial.html)
- [Firestore](https://firebase.google.com/docs/firestore)
- [Authentication](https://cloud.google.com/docs/authentication/client-libraries#python)
- [Firestore YouTube Tutorials](https://www.youtube.com/watch?v=2yNyiW_41H8&t=197s)
- [Creating Database](https://medium.com/@androidcrypto/setup-of-a-cloud-firestore-database-tutorial-step-by-step-1ccc9ec52005)
- [Authentication Tutorial](https://dev.to/shahabmalikk/getting-started-with-firebase-authentication-a-comprehensive-guide-1j81)
- [Stack Overflow](https://stackoverflow.com/questions)

# Future Work

- Add real-time updates
- Implement better input validation
- Build a web or mobile front-end 
- Include reminders or notifications for habit completion
- Add reporting or analytics to show progress trends over time
- Explore integrating ML/AI features to suggest habit goals or track patterns
- Create more connected collections to better organize data