---
title: 'DataFlippers : A drag and drop interface to build machine learning models'
tags:
  - Python
  - Data Science
  - Statistics
  - AI
authors:
  - name: Charles Bennington
    orcid: 0009-0005-0682-163X
    affiliation: "1" # (Multiple affiliations must be quoted)
affiliations:
 - name: Department of Computer Science, Gonzaga University, USA
   index: 1
date: 26 March 2026
bibliography: paper.bib
---

<!--
Important Notes: 
    Length : 750 words - 1,000 words
-->

# Statement of need

## Programming as a barrier to machine learning
Many educators cite that programming is a barrier to entry to machine learning [@bart2016implementing;@thayer2020practical;@brunner2016teaching]. This is because many tools and libraries for machine learning are called programmatically. Building a GUI to interface with theses tools would allow for novices to learn machine learning, without the pre-requisite of knowing how to code. 

## Machine learning literacy
This lack of accessible entry points limits the potential for widespread machine learning literacy. As AI increasingly permeates various aspects of modern life understanding its underlying principles becomes essential.  AI literacy empowers individuals to critically evaluate these systems, fostering informed decision-making and promoting responsible technological development[@provost2013data;@jain2021smart]. Moreover, a basic grasp of AI models can demystify complex technologies, enabling students to navigate a world shaped by intelligent systems with greater confidence and agency.[@hsu2025effects]

Therefore, there's an urgent need for tools that prioritize accessibility and intuitive learning. A low barrier to entry is paramount; users should be able to explore core data science concepts without needing prior programming experience. The target audience for this software is high schoolers and early undergraduates, hoping to learn more about machine learning. 


# Software design

## Inspiration
Scratch[@resnick2009scratch], a visual programming language designed for children, offers a compelling model for accessible computational learning. Its intuitive drag-and-drop interface allows beginners to grasp fundamental programming concepts without needing to decipher complex syntax. Scratch's interface has been proven to be effective at teaching novices programming concepts, and assist learners when the transition to "real" programming[@armoni2015scratch].  

## Drag and drop design
The drag and drop interface is designed to reduce the syntactic complexity of programming down to drag and drop blocks, with the layout and design imitating underlying python libraries. This ensures that users have an low floor to learning, while also paving the way for them to transition to writing code later. 

![Image showing the difference between python blocks, and the drag and drop DataFlippers interface. Both the code and the DataFlippers blocks result in the same thing, however the blocks are much easier for novices to understand.  ](paper_images/Python_v_datascratch.png "Image showing the complexity of coding versus the new drag and drop interface.")


Each drag and drop block is modeled after basic shapes, this gives the user visual signifier, indicating where each block should be dropped on the interface. This ensures the interface is intuitive to people without machine learning experience. 

![Image of the fullscreen DataFlippers project page. The example dataset here is the penguins dataset.  ](paper_images/Full_software.png "Image showing a full view of the DataFlippers suite.")

Users are also enabled to perform basic statistical analysis, this can be done by removing all of the pipeline blocks, and only plotting via the "Inputs and Outputs" block. Users can also see column specific statistics by clicking on a dropdown menu on each column block.  

![Image showing the basic statistical capabilities of the DataFlippers framework. This shows the island type versus the bill length on the penguins.](paper_images/basic_stats.png "Image showing model comparison for the software. ")

The interface also allows the user to input manual predictions, allowing for novices to interact with their newly created AI models. This tab enables the user to export their saved models as software, which is where a user can save their trained model, and access it later. DataFlippers also enables the exporting as pickle, which fulfills the needs of potential power users, by allowing them to interface with the python object directly, if desired. The source code is available at [DataFlippers GitHub](https://github.com/cbennington852/DataFlippers), and the software can be downloaded on windows or linux for free at the [DataFlippers homepage](https://cbennington852.github.io/DataFlippers/)

# Teaching materials

## Informal user testing
DataFlippers has undergone informal usability testing with a small group of novice users. While using an early version of DataFlippers in October of 2025, a user remarked his disappointment at being unable to plot multiple models at the same time. Feedback from these sessions was used to improve the overall design of the drag and drop plotting, and later add a multi-model setup. This is documented on the [DataFlippers history section](https://cbennington852.github.io/DataFlippers/#history-and-evolution-of-software) on the website. 

![Image showing the model comparison. This would allow novices to understand and visually see the differences between different types of machine learning models. This example shows a comparison between a DecisionTreeRegressor, and a LinearRegressor.  ](paper_images/Example_model_comparison.png "Image showing model comparison for the software. ")

## User documentation
The main DataFlippers page features a [walkthrough tutorial](https://cbennington852.github.io/DataFlippers/Basics/My-First-AI-Model) on how to use the software. The website also features descriptions of core machine learning concepts such as [classification](https://cbennington852.github.io/DataFlippers/Basics/Classifiers), [regression](https://cbennington852.github.io/DataFlippers/Basics/Regressors), [validators](https://cbennington852.github.io/DataFlippers/Basics/Validators), and [pre-processors](https://cbennington852.github.io/DataFlippers/Basics/Preproccessors).

## Example datasets & Lab questions
Datascratch comes pre-loaded with several example datasets. These example datasets allow novices to get learning right away, without having to procure a dataset first. These datasets are a blend of commonly used data science teaching datasets such as [palmers_penguins](https://cbennington852.github.io/DataFlippers/Example-Datasets/penguins)[@palmerpenguins], [diamonds dataset](https://cbennington852.github.io/DataFlippers/Example-Datasets/diamond_measurements)[@Waskom2021] and the iris dataset[@iris_53], as well as datasets that would be enticing to a younger audience, such as a dataset containing information about [pokemon](https://cbennington852.github.io/DataFlippers/Example-Datasets/pokemon_statistics)[@KagglePokemon] and a dataset about [minecraft biome](https://cbennington852.github.io/DataFlippers/Example-Datasets/minecraft_biomes) statistics[@KaggleMinecraft]. These example datasets come with 3-5 lab questions each, which can be accessed from the main DataFlippers website. These lab questions are intended to be part of an in-person class exercise, where students could participate in groups of 2-3 to complete the lab questions, with guidance from an educator. 

DataFlippers then underwent a second informal usability testing with a small group of different novice users, where users were tasked with completing tasks that would later become the lab questions, during this informal user study the participants enjoyed the penguins dataset the most, with one of them suggesting a penguin become the mascot for the software. 

Additionally, there is a set of [lecture slides](https://cbennington852.github.io/DataFlippers/Lessons/1.-Introduction). These cover how to use the software, as well as some basic machine learning topics. The goal of these slideshows is to give educators quality materials that they can pick up and adapt to their course as needed. 




