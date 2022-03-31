<p align="center">
  <img src="https://github.com/JakobFinci/mandelbot/blob/main/images/mandelbot1.png"/>
</p>
<h1 align="center">The Mandelbot+</h1>

### A bot designed to determine what types of music people associate with mandelbrot sequences and what common trends appear among them.

## About the Project
The Mandelbot Plus is a collection of two bots: Mandelbot Alpha and Mandelbot Beta, as well as assorted utilities (unit testing tools, data visualization tools, etc). The Mandelbot was created by, and is the intellectual property of, Eliyahu Suskind and Priscila Morales. Its ultimate purpose is to create and update an algorithm to find songs that pair well perceptually with Mandelbrot zoom sequence videos through data analytics and computing.

<p align="center">
  <img src="https://github.com/JakobFinci/mandelbot/blob/main/images/mauda.jpeg"/>
</p>
<p>
    <em>An early digital depicition of the Mandelbrot set, circa 1978</em>
</p>

## Acknowledgments
Special thanks is awarded to Xander Kramer of UIC, who helped run the sampling efforts to collect the baseline perceptual song data.
Huge thanks is also awarded to those who participated in said sampling; your data makes the Mandelbot run....literally!

## Installation
This project was developed for conda-based python environments. As such, we do not guarantee that all dependencies are UNIX tested, nor that the core source code is compatible with the rendering interfacing on that OS.

## Setup
While this project is intended for use on a local setup, it may still be run on a smaller computer, such as a Raspberry Pi, with limited functionality.

For best results, we suggest having
- 2GB of RAM storage
- stable internet connection
- a means of displaying visuals
- [Jupyter](https://jupyter.org/)

### Local Setup
1. First, clone the repository to your computer:
    ```
    git clone https://github.com/JakobFinci/mandelbot.git
    ```

2. It's recommended that you run this project from a Python virtual environment with an anaconda interpreter, which can be set up like this:
    ```
    source /home/your-user/anaconda3/bin/activate
    conda activate base
    ```

3. If you don't already have pip installed, run this command from your new virtual environment:
    ```
    sudo apt install python-pip
    ```

4. Finally, use pip to install the required packages from the default source, PyPi, for packages and dependencies:
    ```
    pip install -r requirements.txt
    ```
    
## Running the Code

### On your local machine
1. From a new terminal, navigate to the `bin` folder of your Mandelbot repo. (Note that you may need to run a different version of the executable depending on your environment)
    ```
    cd [your-path-to-Mandelbot]/bin
    ```
    
2. In order for Mandelbot+ to work, it needs Spotify API keys. Please create a new file in the root titled "config.py":
    ```
    touch src/config.py
    ```
    Then, enter this file in a text editor of your choice and assign your Spotify client ID and client secret (these can be obtained from Spotify [here](https://developer.spotify.com/dashboard/login)) as well as your Spotify user ID to variables as strings using the following template:
    ```
    CLIENT_ID = "INSERT YOUR CLIENT ID HERE"
    CLIENT_SECRET = "INSERT YOUR CLIENT SECRET HERE"
    USERNAME = "INSERT YOUR USER ID HERE"
    ```

3. Begin a Python kernel. We recommend using Jupyter Lab with the Mandelbot+:
    ```
    jupyter lab
    ```
    
4. Once a Python kernel has been initiated, run the data miner, Mandelbot Alpha, from the root directory:
    ```
    %run src/mandelbot_alpha.py
    ```
    
5. From here you can utilize data visualization fuctions that will be defined by Mandelbot Alpha. If an NameError occurs, please re-run Mandelbot Alpha. We recommend running the following function to generate all graphs
    ```
    create_all_graphs()
    ```
    
 6. In addition, you can generate a machine-learning based playlist of optimized Mandelbrot zoom pairing songs by running Mandelbot Beta. This will then generate two machine learning Mandelbrot playlists. As this feature has some bugs, we have provided an example of one of these ML-generated playlist pairs which are accessible [here](https://open.spotify.com/playlist/7Gy8UubRjqosfKFdfyPQYM) and [here](https://open.spotify.com/playlist/3hILKSNoihLr3h8BqlMqn0) (Please note that this functionality will later be improved as to where it will generate playlists in .CSV format onto a user's computer)
    ```
    %run src/mandelbot_beta.py
    ```   
  
## External Dependencies
The following are required to run this program. Note that requirements may already be satisfied and additional platform-specific dependencies may be required depending on your target environment.

### General Use
- [pip](https://pypi.org/project/pip/)
- [pandas](https://pypi.org/project/pandas/)

### Data Visualization
- [matplotlib](https://pypi.org/project/matplotlib/)

### Data Source
- [spotipy](https://pypi.org/project/spotipy/)
