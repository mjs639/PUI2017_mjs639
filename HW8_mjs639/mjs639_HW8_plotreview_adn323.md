# Review of mjs639 HW8 plot
# adn323

I think the plot is relatively easy to read and clearly shows the discrepancy between average SAT scores geospatially. Making it in Carto allows a user to inetract with the map provding further insights than would be available just with a rendered image. Aesthetically the plot works and colour coded dot points are an effective way to communicate the point, however there are some areas in which I think the plot could be improved to better communicate and show the points:
* Due to green being used in the map to show forested areas and parks some of the lighter greens can be confused with parks. I would consider using a different colour to show the data one that is not currently used on the map. 
* The legend provides less insights than it could as only the max and min are shown. I would consider grouping the data into category ranges and having a legend display the different ranges with the corresponding colours.
* The rendered image includes a large portion of the map with no data points that is redundant. I personally have encountered this issue on Carto before and symphatise with Matt as it can be difficult to get the full scope of the points in and not include anything else, however ideally this should not be included in the map or try and center the data set to the middle of the image with some excess map on either end.

I believe the plot is honest and conveys the information without emphasizing any point.

![bashrc aliases and functions](https://raw.githubusercontent.com/mjs639/PUI2017_mjs639/master/CUSP%20Screenshots/Screen%20Shot%202017-11-11%20at%204.49.07%20PM.png)


#### Figure 1 represents high schools across New York City. The color of each representative dot reflects the average SAT score for 2012. Darker dots represent schools with higher scores, while lighter dots represent schools with lower scores, as per the legend on the top left of the map. 

A link to the interactive map is below, and the notebook used to generate the dataset was uploaded to the original repo.

https://mjs639.carto.com/builder/10f6d682-fad1-4050-87ea-703f4120f7a9/embed
