#
# PULL REQUEST GUIDELINES 
Kindly ensure that you have followed and checked all the below mentioned criteria before attempting a pull request

#
## Quick Links
- [Guidelines For Git](https://github.com/Shaik-Kamiloon/Test-Sample/blob/main/docs/pull_request_template.md#-Guidelines-For-Git)
- [LabVIEW Coding Standards](https://github.com/Shaik-Kamiloon/Test-Sample/blob/main/docs/pull_request_template.md#-LabVIEW-Coding-Standards)

#
## Guidelines For Git  
Hope you have read the file mentioning all the necessary guidelines on how to name the branches in your repository, 
modules and files names for your assignments and the commit message formats as specified before proceeding to the next step.

If not, kindly go through the file. You can find it through the below given link.

[GitHub Guidelines](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

#
## LabVIEW Coding Standards
Having the right functionalities satisfied by the code designed cannot be complete without providing readability to the user. Make sure your code can checklist all the below mentioned standards of coding before attempting to commit a pull request.

#
### 1️⃣ Proper Naming 
Having a suitable name for every necessary detail in a short and crisp way is really important. Ensure that your code contains **Proper Names** for

- [ ] Every VI, control and indicator 
- [ ] Boolean controls, indicators and constants ( Name for booleans can indicate the purpose/ state using a "?" such as "Reset?" for a boolean used to reset)
- [ ] Variables used in the Block Diagram
- [ ] Files created/ used by the VI
- [ ] Section, Key and Values in ini files
- [ ] Every Name can be Upper case/ Lower case but first letter of each word should be in Upper case

#
### 2️⃣ Proper Grouping 
Ensure that blocks of your code are grouped accordingly 
- [ ] Visually (Grouping as per their appearance on the Front Panel)
- [ ] Functionally (Grouped as per the usage of elements in the form of Clusters)
- [ ] SubVIs wherever necessary (Grouping code as SubVIs whenever there can be a better readability)
- [ ] Folders (Grouping VIs, SubVIs and TypeDefs into proper folders having the proper naming)
- [ ] Proper Icons for every VI and SubVI (Use the option to edit icon to create meaningful icons that depict the functionality of the VI or SubVI)
- [ ] In the VI, have all the controls to the left and all indicators to the right

#
### 3️⃣ Visibility Area
- [ ] The Front Panel only shows the interested area in the window when the VI is run
- [ ] The Block Diagram doesn't have unnecessary empty spaces
- [ ] Proper options are enabled to have the interested area in display (Window appearance)

#
### 4️⃣ Straight Wires
- [ ] Ensure the connecting wires are as straight as possible with zero to minimum wire bends and crossovers (It is always better to follow this **WHILE** coding and not after coding)
- [ ] No coercion dots
- [ ] Error wires are straight without any bends
- [ ] Merge error is used when there are multiple error wires at the output
- [ ] The error wire has to be holding the entire code (All the code should be mostly above the error wire)

#
### 5️⃣ Neat and Readable Code 
- [ ] The block diagram is neat (It is always better to code neat **WHILE** coding itself)
- [ ] Proper Comments are used wherever necessary to explain the working
- [ ] Labels are used for structures (Right click on the structure to make the label visible)

#
### 6️⃣ Handle Error & Exit Cases
- [ ] All the errors are handled accordingly (You can use Simple Error Handler for error handling)
- [ ] The Exit case needs a Panel Close event wherever necessary
- [ ] All the opened references such as File References, Queue References, etc. are closed properly

#
#### Additional Information If Any about the file
You can provide the information here 

#
#### Comments (Optional)
Any comments for the user or for yourself
