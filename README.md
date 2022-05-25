
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
The data used in this assignment is the in class folder from UCloud (shared-drive/CDS-VIS/network_data). 


## Methods
To solve this assignment i have worked with ```argparse``` in order to parse arguments when calling the main function from command line. And as networking tool i used ```networkx```. At last, i used ```matplotlib``` for visualisation.

## Usage (reproducing results)
These are the steps you will need to follow in order to get the script running and working:
- load the given data into ```input```
- make sure to install and import all necessities from ```requirements.txt``` 
- change your current working directory to the folder above src in order to get access to the input, output and utils folder as well 
- the following should be written in the command line:

      - cd src (changing the directory to the src folder in order to run the script)
      
      - python network_analysis.py -f 1H4.csv (calling the function within the script with and argument of choise)
      
- when processed, there will be a messagge saying that the script has succeeded and that the outputs can be seen in the output folder 



## Discussion of results
The results of this assignment is a table for the given file which shows the values of the network analysis shuch as name, degree, betweenness centrality and eigenvector_centrality of the edgelist. The other result is an image of the network showing the different nodes, their connections and the clusters of the network. This script can both be called on a single file (argument: filename) and with a directory (argument: directory), which makes it possible to get network analysis on multiple data at once. 

