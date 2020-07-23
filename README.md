# Path-Finding-Algorithm-with-Visulisation

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
This is a personal project for me to apply the algorithms that I learnt in University into real life examples. This project focuses on the A* Path Search Algorithm that I learnt during my sophomore year [Optimisation](https://esd.sutd.edu.sg/courses/40002-optimisation/) module in my [Business Analytics](https://esd.sutd.edu.sg/academics/undergraduate-programme/focus-tracks/business-analytics-and-operations-research/) 


<a id= "point_2"></a>
##  2. A* Path Search Algorithm Overview
This subsection intends to give a high level overview of the concept of the A* Path Search Algorithm.
The goal of the aims A* Path Search Algorithm is to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). </br>
The algorithm is made up of two functions: f(n) = g(n) + h(n) </br>
* Cost Function,g(n)  </br>
Calcualtes the cost of the path from the start node to n.
* Heuristic Function, h(n)  </br>
 **Estimates** the cost of the cheapest path from n to the goal. In this project, we use Manhattan distance which takes the absolute value of the horizontal and vertical distance between the current and end node.

The visualisation is built on Python with the [PyGame](https://www.pygame.org/wiki/about) package used for the generation of the visuals.

<a id= "point_3"></a>
##  3. Usage
The A* Path Search Algorithm Visualisation in this project uses a square grid.
1. Declare the **Start**, use the left mouse button to click on desired start node(Orange Block)
2. Delcare the **End**, use the left mouse button to click on desired end node(Sky Blue Block)
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
* visualisation_example.png - Screenshot of the A* Path Finding Visualisation program

<a id= "point_6"></a>
## 6. Lessons Learnt and Conclusion
* Object Oriented Programming (OOP)
* PyGame

<a id= "point_7"></a>
## 7. Acknowledgment
- The first acknowledgemnt goes to [Tim Rusica](https://www.linkedin.com/in/tim-ruscica/?originalSubdomain=ca), who's [Youtube tutorial](https://www.youtube.com/watch?v=JtiK0DOeI4A&list=PL28vvpnD7LBsqocFbqyZBV8IeR8mAg2HF) on the Python PyGame Implementation was an integral part of this project.
- Wikipedia A* Search Algorithm [Article.](https://en.wikipedia.org/wiki/A*_search_algorithm)
- Computerphile [Youtube video](https://www.youtube.com/watch?v=ySN5Wnu88nE&t=42s) on A* Search Algorithm. 
