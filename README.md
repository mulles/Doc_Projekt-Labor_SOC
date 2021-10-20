# Documentation for Embedded State of Charge (SOC) Algorithm for Lead Acid Battery 
Documentation (Projektarbeit) for Projekt-Labor @ Beuth University for Applied Science.

This document describes the research, implementation and verification of an embedded State of Charge (SOC) algorithm for lead acid batteries. The Algo is based on KalmanFilter (KF). It can be used for lithium batteries as well, if the open circuit voltage (OCV) lookup-table is adjusted acordingly. 

**Build/Compile the Latex document**

Linux:  
`$ git clone https://github.com/mulles/Doc_Projekt-Labor_SOC`  
`$ cd Doc_Projekt-Labor_SOC`  
`$ make` (obsolte with new ptythontex integration use TeXStudio a Latex IDE with special build commands COULDDO complete

SHOULDDO Add CI to build on remote machine aka linux ubuntu server:  
`$ sudo apt install texlive-lang-german cm-super texlive-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra`  
`$ dflatex main.tex | pythontex --interpreter python:python3 main.tex | pdflatex main.tex`  
