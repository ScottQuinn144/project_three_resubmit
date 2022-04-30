# **Battleships**
## **Overview:**
This is a python led game built by Heroku. The game runs on Code Institute's mock terminal. The game is single player battleships game with the objective to destroy 3 randomly placed ships on a 5x5 grid board with 15 wrong attempts.

### **Aim**

##### Player-
- The player selects a row and a column within the 5x5 gaming area to eliminate three randomly placed ships. The aim is to destroy the ships before running out of missles.

##### Developer-
- The main aim for the developer is to create a bug free game which allows users to enjoy a simple game of Battleships while also providing scope to improve and add more complexity and functionality to the game in later iterations.

- The second aim is for the developer to showcase his python skills within the coding of this game. Using the BDD method of testing, the developer's aim in the first release is to create a game without bugs.

### **How to Play**

- Player will be asked there name and once given the game shall commence. Like a traditional battleships game, the player will choose a position on the gameboard to send one of there missiles. They do this by submitting a row number and a column number. The game will use this data to see if they have sunk one of the three ships on the board or if they have missed the ships. There are three ships and 15 missiles. If the player sinks all three ships, they win the game, otherwise, they will lose the game.

## **Code Modal:**
- I used an array model as I believed it was easiest to achieve my developer goals of creating a simple yet bug free game. With the array modal, I am able to iterate through indexes and manupulate what they hold in order to display the required messages back to the user. The array modal allows for absolutes in data validation as I can recieve input from a user, check the index and data it holds and respond accordingly. Arrays also allow for easy resetting of the game. A simple while loop hold all the key componants to iterate through the array until the final argument is reached. This project is entirely done with backend programming. 

- In the future I would look at making this game with a TDD approach and as a front end project. Using a framework like jest and javaScript I could see myself using classes instead of arrays. 

### **Disclaimer**

This site was built for educational purposes only. All rights to the title name, battleships idea or other remain with the copyright owners. `Battleships` is an educational project by the developer.

Developer: Scott Quinn