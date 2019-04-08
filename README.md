[//]: # (Image References)

[image1]: ./img/MainMenu.jpg "Main Menu"
### Heuristics Workshop
This is the starter code for the Heuristics workshop. The first of a three part series focusing on traditional AI techniques.
This session will focus on heuristics and we'll implement the A* algorithm to solve sliding puzzles!

To successfully implement A* you will need to follow the instructions for the following PuzzleSolver class methods in solver.py:
    
    - score_board
    - expand
    - get_total_cost
    - explore

### Getting Started
1. Make sure you have [Python 3.6](https://www.python.org/) installed.

2. Clone the repository
    ```bash
    git clone https://github.com/mezzX/HeuristicWorkshop
    ```
    
3. Use [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) to create a new environment and install dependencies. [Click Here](https://nbviewer.jupyter.org/github/johannesgiorgis/school_of_ai_vancouver/blob/master/intro_to_data_science_tools/01_introduction_to_conda_and_jupyter_notebooks.ipynb) if you need a detail guide on using conda.

    - __Linux__ or __Mac__: 
    ```bash
    conda create --name sliding python=3.6
    source activate sliding
    pip install -r requirements.txt
    ```
  
    - __Windows__: 
    ```bash
    conda create --name sliding python=3.6 
    activate sliding
    pip install -r requirements.txt
    ```

### Instructions
Navigate to the directory and run puzzle.py

    python puzzle.py

![Main Menu][image1]

1. Click on Browse to select an image to be used for the puzzle tiles. 
   Brain_icon.png and smiley_face.png have provided in this repo as puzzle tiles.

2. Select the size of the puzzle. Selecting 3 will make it a 3x3 sliding puzzle.

3. Set how many moves to generate to shuffle the board.

4. (Optional) Set a seed to be used when shuffling the board. A value of 0 will result in a random board.

5. Finally click start to generate the puzzle.

### Controls
Arrow keys to move the tiles around the gap<br>
'r' key to go back to the main menu<br>
's' key to have the algorithm solve the puzzle<br>
