# PUI2017_mjs639

For this assignment, I embedded several directories (CUSP, Courses, and PUI2017) in order to keep my documents for this course and future courses organized. I used the export function to create an environmental variable ($PUI2017), and used this variable to create an alias (pui2017)

Using this alias, I am now able to directly enter the PUI2017 directory with minimal keystrokes.

Below is a screenshot of my bash_profile showing the environmental variable and alias:

![Alt text](/Users/Matthew/Desktop/CUSP Screenshots/bash_profile_edit.png)

Below is a sreenshot showcasing the usage of the alias:

![Alt text](/Users/Matthew/Desktop/CUSP Screenshots/pwd_showcase.png)

One thing that has me confused is the fact that, when opening the bash_profile for editing (via 'nan0 ~/.bash_profile') I am able to see the image included above. However, when I open the file outside of this method, or if I call 'head bash_profile' or 'tail bash_profile' I get the following:

![Alt text](/Users/Matthew/Desktop/CUSP Screenshots/bash_profile_file.png)

The environmental variable and alias are both working properly, but I can't figure out why they do not appear. 