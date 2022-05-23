
# Language Analytics - Spring 2022
# Portfolio Assignment 3

This repository contains the code and descriptions from the third assigned project of the Spring 2022 module Language Analytics as part of the bachelor's tilvalg in Cultural Data Science at Aarhus University - whereas the overall Language Analytics portfolio (zip-file) consist of 5 projects, 4 class assignments + 1 self-assigned.

## Repo structure
### This repository has the following directory structure:

| **Folder** | **Description** |
| ----------- | ----------- |
| ```input``` | Contains the input data (will be empty) |
| ```output``` | Contains the results (outputs like plots or reports)  |
| ```src``` | Contains code for assignment 3 |
| ```utils``` | Contains utility functions written by [Ross](https://pure.au.dk/portal/en/persons/ross-deans-kristensenmclachlan(29ad140e-0785-4e07-bdc1-8af12f15856c).html), and which have been used in the assignments |

Also containing a ```MITLICENSE``` for guidelines of how to reproduce and use the data in this repository, as well as a ```.txt``` reqirements-file, where the required installments will be listed.

## Assignment description
The official description of the assignment from github/brightspace: [assignment description](https://github.com/CDS-AU-DK/cds-language/blob/main/assignments/assignment3.md).

In this assignment, you are going to write a .py script which can be used for network analysis. As we saw last week, pretty much anything can be formalised as a network. We're not going to focus on creating the edgelists for this project; instead, the goal is to have a script that would work the same way on any input data, as long as the input format is correct.

So, as test data, I recommend that you use the files in the folder called network_data. However, the final script should be able to be resused and work on any undirected, weighted edgelist with the same column names.

Your script should do the following:

- If the user enters a single filename as an argument on the command line:
- Load that edgelist
- Perform network analysis using networkx
- Save a simple visualisation
- Save a CSV which shows the following for every node:
name; degree; betweenness centrality; eigenvector_centrality
- If the user enters a directory name as an argument on the command line:
- Do all of the above steps for every edgelist in the directory
- Save a separate visualisation and CSV for each file


### The goal of the assignment 
The goal of this assignment was to demonstrate that I have a good understanding of how to perform network analysis on undirected, weighted edgelists using networkx. By the end of this assignment, I would have a script which can be resued for future projects to perform a quick, simple network analysis

### Data source
The data used in this assignment is the in class flowers-folder from UCloud (shared-drive/CDS-VIS/flowers). 

Link to flowers dataset: [flowers dataset](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/index.html).


## Methods
To solve this assignment i have worked with ```opencv``` in order to both calculate the histograms as well as for the general image processing (using the ```calcHist```, ```imread```, ```normalize``` and ```compareHist```). Futhermore i used the ```jimshow``` and ```jimshow_channel``` from the ```utils```-folder, along with the ```matplotlib``` for plotting and visualisation.

## Usage (reproducing results)
These are the steps you will need to follow in order to get the script running and working:
- load the given data into ```input```
- make sure to install and import all necessities from ```requirements.txt``` 
- change your current working directory to the folder above src in order to get access to the input, output and utils folder as well 
- the following should be written in the command line:

      - cd src (changing the directory to the src folder in order to run the script)
      
      - python image_search.py (calling the function within the script)
      
- when processed, there will be a messagge saying that the script has succeeded and that the outputs can be seen in the output folder 



## Discussion of results
The result of this script is an image which contains one target flower image and the calculated three similar images, as well as the calculated distance scores of the images. Furthermore, a csv file is made with the results (similar images). 

For further development, it could have been interesting to look at how to make the script run with a user defined input. Since this code have already been through a transision from jupiter notebook to .py script, it would not have been much change to do. For the user to parse an argument via the command line when running the code, the script would have been more reproduceble/reuseble, because of the fact that the user wpuld be able to define the target image themselves. 


