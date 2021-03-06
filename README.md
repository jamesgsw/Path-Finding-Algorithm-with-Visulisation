# Path-Finding-Algorithm-with-Visualisation

## Table of Contents:
* [1. About the  Project](#point_1)
* [2. A* Path Search Algorithm Overview](#point_2)
* [3. Usage](#point_3)
* [4. Viewing](#point_4)
* [5. Files in this Repository](#point_5)
* [6. Lessons Learnt and Conclusion](#point_6)
* [7. Acknowledgment](#point_7)

<a id= "point_1"></a>
##  1. About the  Project
This is a personal project for me to apply the algorithms that I learnt in University into real life examples. This project focuses on the A* Path Search Algorithm that I learnt during my sophomore year [Optimisation](https://esd.sutd.edu.sg/courses/40002-optimisation/) module in my [Business Analytics.](https://esd.sutd.edu.sg/academics/undergraduate-programme/focus-tracks/business-analytics-and-operations-research/) 

| <img width="400" alt="visualisation_example" src="https://user-images.githubusercontent.com/36501392/88307153-2fb0be00-cd3e-11ea-8300-89aa457fd699.png"> |
| :--: |
| Screenshot of the A* Path Finding Algorithm Program Project |

<a id= "point_2"></a>
##  2. A* Path Search Algorithm Overview
This subsection intends to give a high level overview of the concept of the A* Path Search Algorithm.
The goal of the aims A* Path Search Algorithm is to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). </br></br>The visualisation is built with Python using the [PyGame](https://www.pygame.org/wiki/about) package for the generation of the visuals. </br></br>
The algorithm is made up of two functions: f(n) = g(n) + h(n) </br>
* **Cost Function, g(n)**  </br>
Calculates the cost of the path from the start node to n.
* **Heuristic Function, h(n)**  </br>
 **Estimates** the cost of the cheapest path from n to the goal. In this project, we use Manhattan distance which takes the absolute value of the horizontal and vertical distance between the current and end node.

Wikipedia has an excellent representation of the function of the code through pseudocode linked [here.](https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode)

The image below is the diagramatic flow of how the main function triggers the different functions within the source code(Named: aStarPathFindingAlgo.py). The main(WIN, WIDTH) is the container function which procedurely calls upon the different functions for the algorithm and visualisation to run.
| ![A_ Star Path Finding Algorithm Diagram Flow](https://user-images.githubusercontent.com/36501392/88306632-8e296c80-cd3d-11ea-9a5c-8720e50648be.png) |
| :--: |
| Flow Diagram of various methods in source code |

<a id= "point_3"></a>
##  3. Usage
The A* Path Search Algorithm Visualisation in this project uses a square grid.
1. Declare the **Start**, use the left mouse button to click on desired start node(Orange Block)
2. Declare the **End**, use the left mouse button to click on desired end node(Sky Blue Block)
3. Declare the **Barriers**, use the left mouse button to click/drag the desired nodes to be the barrier
4. Start Path Finding Algo, hit space bar button on keyboard
5. Reset Grid, hit "c" key on keyboard

<a id= "point_4"></a>
##  4. Viewing
* The best way to view this project is to download the source code of the project and run the Python script using Python 3.7.7
* An alternative way to view this project is through an online Python Shell. Link [here](https://repl.it/@jamesgsw/A-Path-Finding-Visualisation), press the run button on the top of the webpage

<a id= "point_5"></a>
## 5. Files in this Repository
* aStarPathFindingAlgo.py - Source Code for the A* Path Finding Visualisation

<a id= "point_6"></a>
## 6. Lessons Learnt and Conclusion
* Object Oriented Programming (OOP) </br>
Having a hands-on experience seeing how objects are interacted through this personal project. </br></br>
* PyGame </br>
Learning a new Python package which I thought I would never find a use. </br></br>
* Software Architecture Design </br>
Using LucidCharts web app to design a architecture design with inspiration from UML standards. I believe this new knowledge is essential for project documentaion when referring back in the future.

<a id= "point_7"></a>
## 7. Acknowledgment
- The first acknowledgment goes to [Tim Rusica](https://www.linkedin.com/in/tim-ruscica/?originalSubdomain=ca), who's [Youtube tutorial](https://www.youtube.com/watch?v=JtiK0DOeI4A&list=PL28vvpnD7LBsqocFbqyZBV8IeR8mAg2HF) on the Python PyGame Implementation was an integral part of this project.
- Wikipedia A* Search Algorithm [Article.](https://en.wikipedia.org/wiki/A*_search_algorithm)
- Computerphile [Youtube video](https://www.youtube.com/watch?v=ySN5Wnu88nE&t=42s) on A* Search Algorithm.
