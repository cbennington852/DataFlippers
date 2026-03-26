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

A lack of coding skills limits machine learning(ML) access. [@bart2016implementing;@thayer2020practical;@brunner2016teaching], This is because many ML tools require coding. This lack of accessibility limits widespread ML literacy, hindering critical evaluation of AI in modern life [@provost2013data;@jain2021smart]. To address this, we need intuitive tools that prioritize a low barrier to entry. DataFlippers aims to provide high schoolers and early undergraduates a GUI based software to explore core data science & build ML models without requiring prior programming experience.

##  State of the field

There are several no-code low code platforms available on the internet. However these are often designed with power users in mind, making them frustrating to novices. Additionally these softwares are often geared toward commercial data science use, with a focus on integration with common business tools. 

| Name        | Description                | Target Audience | License              | Drag and drop |
|-------------|----------------------------|-----------------|----------------------|---------------|
| DataBricks  | Generative AI              | Businesses     | Paid / Commercial    | No            |
| Power BI    | Visualization Interface    | Businesses     | Paid / Commercial    | Yes           |
| Rapid Miner | Training / Visualization   | Data Scientists | Free for individuals | No            |
| JASP        | Statistics / Visualization | Upper Undergraduate / Graduate        | Free                 | No            |

The platforms that are free and tailored to students, such as JASP[@JASP2025] is catered to teaching students statistics, rather than expressly teaching them ML. 


# Software design

## Inspiration
Scratch[@resnick2009scratch], a visual programming language designed for children, offers a compelling model for accessible computational learning. Its intuitive drag-and-drop interface allows beginners to grasp fundamental programming concepts without needing to decipher complex syntax. Scratch's interface has been proven to be effective at teaching novices programming concepts, and assist learners when they transition to "real" programming[@armoni2015scratch].  

## Software architecture and core project libraries
The language for this software is python & PyQt, this is because python possesses several commonly used ML libraries[@burridge2022teaching], such as pandas[@reback2020pandas], matplotlib[@Hunter:2007], and scikit-learn[@scikit-learn;].The core ML models are provided by scikit-learn[@scikit-learn;]. There are several reasons for choosing scikit-learn, one of them is portability. scikit-learn is very common within the entry level ML field, so this means that skills that novice learn from DataFlippers could translate easily to programmatic skills, if the novice decides to learn programming. Additionally, the scikit-learn is very friendly for first time users, featuring extensive documentation, which can be viewed by hovering on each items tooltip. Pandas[@reback2020pandas] is used for handling the data, this is because pandas supports the importing of multiple standard filetype formats, such as csv, excel, and parquet. Matplotlib is utilized for the plotting features, this is because matplotlib interfaces well with the PyQt background, as well as being another standard ML library. 

![Diagram of the overall software architecture. ](paper_images/inner_workings_drawing.png "Image showing the software design of the GUI")

## Drag and drop design
The drag and drop interface is designed to reduce the syntactic complexity of programming down to drag and drop blocks, with the layout and design imitating underlying python libraries. This ensures that users have an low floor to learning, while also paving the way for them to transition to writing code later. 

![Image showing the difference between python blocks, and the drag and drop DataFlippers interface. Both the code and the DataFlippers blocks have same result. ](paper_images/Python_v_datascratch.png "Image showing the complexity of coding versus the new drag and drop interface.")


Each drag and drop block is loosely modeled after the buildable blocks from Scratch. This gives the user visual signifier, indicating where each block should be dropped on the interface. This ensures the interface is intuitive to people without ML experience. 

![Image of the fullscreen DataFlippers project page.](paper_images/Full_software.png "Image showing a full view of the DataFlippers suite.")

Users are also enabled to perform basic statistical analysis, this can be done by removing all of the pipeline blocks, and only plotting via the "Inputs and Outputs" block. Users can also see column specific statistics by clicking on a dropdown menu on each column block.  The interface also allows the user to input manual predictions, allowing for novices to interact with their newly created AI models. This tab enables the user to export their saved models as software, which is where a user can save their trained model, and access it later. DataFlippers also enables the exporting as pickle, which fulfills the needs of potential power users, by allowing them to interface with the python object directly, if desired.
# Teaching materials

## Informal user testing
DataFlippers has undergone informal usability testing with a small group of novice users. While using an early version of DataFlippers in October of 2025, a user remarked his disappointment at being unable to plot multiple models at the same time. Feedback from these sessions was used to improve the overall design of the drag and drop plotting, and later add a multi-model setup.

![Image showing the model comparison. This would allow novices to understand and visually see the differences between different types of ML models. ](paper_images/Example_model_comparison.png "Image showing model comparison for the software. ")

DataFlippers later underwent a second usability test, in which users would be instructed to complete common data science and ML tasks. The "penguins" dataset consistently elicited the most positive feedback from participants, with participants stating that the penguins offered easily visualizable attributes such as flipper length, weight and species. This provided inspiration for both the name and the logo for DataFlippers.

## User documentation
The main DataFlippers page features a [walkthrough tutorial](https://cbennington852.github.io/DataFlippers/Basics/My-First-AI-Model) on how to use the software. The website also features descriptions of core ML concepts such as [classification](https://cbennington852.github.io/DataFlippers/Basics/Classifiers), [regression](https://cbennington852.github.io/DataFlippers/Basics/Regressors), [validators](https://cbennington852.github.io/DataFlippers/Basics/Validators), and [pre-processors](https://cbennington852.github.io/DataFlippers/Basics/Preproccessors). The source code is available at [DataFlippers GitHub](https://github.com/cbennington852/DataFlippers), and the software can be downloaded on windows or linux for free at the [DataFlippers homepage](https://cbennington852.github.io/DataFlippers/)


## Example datasets & Lab questions
Datascratch comes pre-loaded with several example datasets. These example datasets allow novices to get learning right away, without having to procure a dataset first. These datasets are a blend of commonly used data science teaching datasets such as [palmers_penguins](https://cbennington852.github.io/DataFlippers/Example-Datasets/penguins)[@palmerpenguins], [diamonds dataset](https://cbennington852.github.io/DataFlippers/Example-Datasets/diamond_measurements)[@Waskom2021] and the iris dataset[@iris_53], as well as datasets that would be enticing to a younger audience, such as a dataset containing information about [pokemon](https://cbennington852.github.io/DataFlippers/Example-Datasets/pokemon_statistics)[@KagglePokemon] and a dataset about [minecraft biome](https://cbennington852.github.io/DataFlippers/Example-Datasets/minecraft_biomes) statistics[@KaggleMinecraft]. These example datasets come with 3-5 lab questions each, which can be accessed from the main DataFlippers website. These lab questions are intended to be part of an in-person class exercise, where students could participate in groups of 2-3 to complete the lab questions, with guidance from an educator. 

Additionally, there is a set of [lecture slides](https://cbennington852.github.io/DataFlippers/Lessons/1.-Introduction). These cover how to use the software, as well as some basic ML topics. The goal of these slideshows is to give educators quality materials that they can pick up and adapt to their course as needed. 

# References