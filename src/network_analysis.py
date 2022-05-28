# Importing relevant programs
import argparse
import os 
import pandas as pd
import pandas as pd
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,20)


# Get data for single file
def read_file(filename):
    filepath = os.path.join("input", "network_data", filename)
    data = pd.read_csv(filepath, sep = "\t")
    return data


# Get data for file in folder
def read_directory(filename):
    filepath = os.path.join(filename)
    data = pd.read_csv(filepath, sep = "\t")
    return data


# Run through folder
def join(path):
    all_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            all_files.append((file, path + "/" + str(file)))
    return all_files

# The following function takes whatever file is given from the folder 'network_data' and runs a network analysis on it. The outputs of this function is a picture of the network and a dataframe which shows name, degree, betweenness centrality and eigenvector centrality of the network. 

# Giving my function a suitable name with parameters
def network_analysis(data, filename = None):
    if filename is None:
        out_img = "network_analysis.png"
        out_file = "network_analysis.csv"
    else:
        out_img = filename + "_network_analysis.png"
        out_file = filename + "_network_analysis.csv"

    # Taking that data (which is an edgelist) and taking the columns we want in our network 
    G = nx.from_pandas_edgelist(data, "Source", "Target", ["Weight"])
    # Making/plotting a network using networkx and labeling the nodes 
    nx.draw_networkx(G, with_labels=True, node_size=20, font_size=10)
    # Saving the network as .png in an output folder
    outpath = os.path.join('..', 'output', out_img)
    plt.savefig(outpath, dpi = 300, bbox_inches = "tight")
    
    # Next up is to find the different informations needed in our network analysis 
    # G.degree prints both the name and the degree of the node
    gathered = list(G.degree)
    # So i split the pair-list into two seperate: name and degree
    name, degree = zip(*gathered)
    # Then putting them back into their own lists (seperated)
    list(name)
    list(degree)
    
    # Finding betweenness centrality using networkx
    bc = nx.betweenness_centrality(G)
    # Saving into a dataframe, naming the columns so that I later can get only the centrality column into my own table
    bc_df = pd.DataFrame(bc.items(), columns = ["Name", "Centrality"]) 
    
    # Finding eigenvector centrality using networkx
    ec = nx.eigenvector_centrality(G)
    # Saving into a dataframe, naming the columns so that I later can get only the eigenvector column into my own table 
    ec_df = pd.DataFrame(ec.items(), columns = ["Name", "Eigenvector"])
    
    # Gathering them in a list for then to write that list to a .csv file
    list_of_columns = list(zip(name, degree, bc_df["Centrality"], ec_df["Eigenvector"]))
    
    # Saving it as a dataframe with list of columns as well as the name for those coloumns
    network_dframe = pd.DataFrame(list_of_columns, columns = ["Name", "Degree", "Betweenness Centrality", "Eigenvector Centrality"])
    
    # Writing it to a csv
    network_dframe.to_csv("output/" + out_file, encoding = "utf-8")
    
def parse_args():
    # Intialise argeparse
    ap = argparse.ArgumentParser()
    # Command line parameters and help lines
    ap.add_argument("-fn", "--filename", required=False, help = "Name of the file you want to do network analysis on")
    ap.add_argument("-d", "--directory", required=False, help = "Name of the directory you want to do network analysis on")
    args = vars(ap.parse_args())
    return args



def main():
    args = parse_args()
    if args["filename"] is not None:
        data = read_file(args["filename"])
        print(data)
        network_analysis(data)
    
    if args["directory"] is not None:
        all_files = join(args["directory"])
        print(all_files)
        for file in all_files:
            data = read_directory(file[1])
            network_analysis(data, file[0])
            
    print("Script succeeded, results can be seen in output-folder") 
    
if __name__ == "__main__":
    main()
