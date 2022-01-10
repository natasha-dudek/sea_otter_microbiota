import argparse
import os
import string
import sys
import re

import matplotlib.pyplot as plt
import numpy as np
import pylab as P

parser = argparse.ArgumentParser(description='This script will create boxplots visualizing the community composition of gingival and rectal samples at a given taxonomic level (phylum, class, etc). Please note that input csv files must have Unix/Mac line endings.')

parser.add_argument('gingival', metavar='gingival_asvs.csv', type=str, nargs=1,
                    help='Path to a csv file containing the relative abundance of taxa in gingival samples. The first column should be sample IDs, the first row should be the name of each taxonomic group.')
                    
parser.add_argument('rectal', metavar='rectal_asvs.csv', type=str, nargs=1,
                    help='Path to a csv file containing the relative abundance of taxa in rectal samples. The first column should be sample IDs, the first row should be the name of each taxonomic group.')                            

parser.add_argument('-v', '--verbose', action="store_true", help='Print the median median relative abundance of each taxon across all samples')

args = parser.parse_args()
    
def median(lst): 
    """
    Get the median value of a list
    
    Arguments:
        lst (list) -- list of ints or floats

    Returns:
        (int or float) -- median value in the list
    """
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0

def get_tax_groups(file):
    """
    Create mapping between taxonomic groups and the relative abundance of that group in each sample
    
    Arguments:
        file (map) -- map representation of relative abundance input file
    
    Returns:
        relAbs (dict) -- maps tax group index (determined by which column it is in the csv file) to list of the group name and relative abundances per sample (e.g.: {1: ['Streptococcus', 0.5, 0.25, 0.25]})
    """
    relAbs = {}
    
    line_counter = 0
    for s in file:
        _ = s.split(",")
        if line_counter == 0:
            for i in range(1,len(_)):
                relAbs[i] = [_[i]]
            line_counter = 1
            continue
    
        for i in range(1,len(_)): # skip first column = sampleID  
            relAbs[i].append(float(_[i]))  

    return relAbs

def get_medians(relAbs):
    """
    Creates dictionary that will later allow us to sort phyla by how abudant/common they are across samples.
    
    Note that for tax groups where median is zero, we will instead sort by average.
    
    Arguments:
        relAbs (dict) -- maps tax group index (determined by which column it is in the csv file) to list of the group name and relative abundances per sample (e.g.: {1: ['Streptococcus', 0.5, 0.25, 0.25]})
    
    Returns:
        medians (dict) -- maps tax groups to their median median relative abundance across all samples
    """
    medians = {}
    for i in relAbs:
        median_relAb = median(relAbs[i][1:])
        if median_relAb != 0:
            medians[relAbs[i][0]] = median_relAb
        else:
            # penalize all averages by 100 so that they are behind tax groups 
            # for which median could be meaningfully calculated
            medians[relAbs[i][0]] = sum(relAbs[i][1:])/len(relAbs[i][1:])-100 
    
    return medians

def sort_by_median(medians, verbosity):
    """
    Make a list of taxonomic groups ordered by decreasing median median relative abundance

    Arguments:
        medians (dict) -- maps tax groups to their median median relative abundance across all samples
        verbosity (int) -- user defined parameter specifying whether or not to print rel abs of each tax group
    Returns:
        tax_order (list) -- names of tax groups in order of decreasing median median relative abundance
    """
    tax_order = []   
    for key, value in sorted(medians.items(), key=lambda x:x[1], reverse=True):
        tax_order.append(key)
        if verbosity > 0: print(key, value)
    
    return tax_order

def format_data(tax_order, relAbs):
    """
    Formats data for plotting
    
    Arguments:
        tax_order (list) -- names of tax groups in order of decreasing median median relative abundance
        relAbs (dict) -- maps tax group index (determined by which column it is in the csv file) to list of the group name and relative abundances per sample (e.g.: {1: ['Streptococcus', 0.5, 0.25, 0.25]})
    
    Returns:
        data_to_plot (list) -- for each taxon, a list of relative abundance per sample
        phyla_labels (list) -- names of tax groups, from least to most abundant/common
    """
    data_to_plot = []  
    phyla_labels = []   
    
    for i in tax_order:
        for key in relAbs:
            if relAbs[key][0] == i:
                data_to_plot.append(relAbs[key][1:]) # remember element 0 is the english name of the tax group
        
        # Add alphanumeric identifiers to candidate phyla labels
        if i == "SR1":
            phylum = "Absconditabacteria (SR1)"
        elif "Saccharibacteria" in i: 
            phylum = "Saccharibacteria (TM7)"
        elif "Parcubacteria" in i: 
            phylum = "Parcubacteria (OD1)"
        elif "Microgenomates" in i: 
            phylum = "Microgenomates (OP11)"
        elif "Armatimonadetes" in i: 
            phylum = "Armatimonadetes (OP10)"
        elif "Marinimicrobia" in i: 
            phylum = "Marinimicrobia (SAR406)"
        elif "Latescibacteria" in i: 
            phylum = "Latescibacteria (WS3)"
        elif "Aminicenantes" in i: 
            phylum = "Aminicenantes (OP8)"
        elif "Cloacimonetes" in i: 
            phylum = "Cloacimonetes (WWE1)"
        else:
            phylum = i
            
        phyla_labels.append(phylum)
    
    data_to_plot.reverse()
    phyla_labels.reverse()
    
    return data_to_plot, phyla_labels

def plot(sample_type, infile, verbosity):
    """
    Create boxplot showing relative abundance on the x-axis and taxa on the y-axis
    
    Arguments:
        sample_type (str) -- "gingival" or "rectal"
        infile
        verbosity (int) -- user defined parameter specifying whether or not to print rel abs of each tax group
    """
    
    # Open input files
    file = open(infile).readlines()
    file = map(str.strip,file)    
    
    # Get relative abundance of each taxonomic group
    relAbs = get_tax_groups(file)

    # Get median median abundance of each tax group across all samples
    # Sort tax groups by decreasing median median relative abundance
    medians = get_medians(relAbs)
    tax_order = sort_by_median(medians, verbosity)
    
    # format data as needed to plot 
    data_to_plot, phyla_labels = format_data(tax_order, relAbs)
    
    # Start plotting
    if sample_type == "gingival":
        ax = fig.add_subplot(121)
    else:
        ax = fig.add_subplot(122)
    
    # Plot data points    
    for i in range(len(data_to_plot)):
        y = data_to_plot[i]
        
        # Add scattering on the x-axis to minimize overlap between data points
        # But only if there are more than 3 data points per phylum
        if len(data_to_plot[i]) > 3:
            x = np.random.normal(1+i, 0.08, size=len(y)) # scatter
        else:
            x = 1+i # no scatter
        
        if sample_type != "rectal":
            P.plot(y, x, color='#4fc657', marker='.', linestyle="None", alpha=0.2, markersize = 10)  
        else:
            P.plot(y, x, color='#ba7d28', marker='.', linestyle="None", alpha=0.2, markersize = 10) 
    
    ##Create the boxplot
    bp = ax.boxplot(data_to_plot, vert=False, sym='') 
    
    ## Custom y-axis labels = taxonomic group labels
    ax.set_yticklabels(phyla_labels)
        
    # Change outline color, fill color and linewidth of the boxes
    for box in bp['boxes']:
        # Change outline color
        box.set( color='#000000', linewidth=0.6, linestyle='-')
    
    # Change linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#000000', linewidth=0.6, linestyle='-')
    
    # Change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#000000', linewidth=0.6)
        
    # Change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#000000', linewidth=0.6)
    
    # Make x-axis on a log scale
    ax.set_xscale('log')
    
    # Add title to each subplot
    if sample_type == "rectal":
        ax.set_title('Rectal')
    else:
        ax.set_title('Gingival')
    
    # Add labels on x-axis    
    ax.set_xlabel('Relative abundance (%)')
    #plt.xticks(rotation=90)
    
    # "Rotate" plot by 90 degrees -- i.e. taxonomic group on the y-axis instead of x-axis
    ax = plt.gca()
    ax.invert_xaxis()

# Create a figure instance
fig = plt.figure(1, figsize=(11, 6))

plot("rectal", args.rectal[0], args.verbose)
plot("gingival", args.gingival[0], args.verbose)

plt.tight_layout()
plt.savefig("Fig2AB.pdf")
