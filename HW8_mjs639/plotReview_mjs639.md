## Plot Review for mjs639

I found this plot interesting, as it gives an initial glance at a topic that can be analyzed in more depth : how SAT scores vary depending on neighborhood's socio-economic characterstics. 



![image of env](https://github.com/biabbiassago/PUI2017_bb1569/blob/master/HW9_bb1569/satmap.png)


Link to interactive map:  https://mjs639.carto.com/builder/10f6d682-fad1-4050-87ea-703f4120f7a9/embed




__CLARITY__:  

It was easy to understand what the map represents, since the legend is very evident. However, I think it would have been better to have specified that SAT Score Average is BY SCHOOL, as this was only clear after reading the caption. 

One thing that would help clarity, in my opinion, is to improve the scale. The SAT scores go from a min of 800 to a max of 2100, so I think it would be useful to have that specified on the legend. I really like how the average is marked, and I think you could also add 25% and 75% percentiles. 

This is a minor comment -- but for the screenshot, I would have chosen an area that centers the datapoints a bit better, as having all the Jersey area shown in the map takes space away from the relevant part. Obviously this is irrelevant in the interactive map. 

__AESTHETIC__  :   

The choice of color makes it a bit hard to interpret the map. In particular, for very low SAT Average Score, the bright yellow color is too similar to the maps' background color, making it hard to see where the points are. At a first glance, low SATs appear under-represented.

I would use a color like red, or blue, that is not present in the initial map. 

I think that using a gradient rather than bins colors makes it a bit harder to differentiate between levels of SAT score. In particular, it is a bit difficult to compare two data points that are a bit spatially far from each other and have a similar shade of green.  You could choose to cut off points (for example at percentiles) in different-color bins.


__HONESTY__:   

All the dots are the same size which is a good choice, since it is does not give more importance to higher or lower scores. 
A plus of using the gradient rather than groups is that the map's smaller differences are detected (although maybe a bit harder to see at first glance). 

However, as I mentioned before, having a light color that is hard to see makes it seem like the average score is higher than in reality, and this impacts the honesty of the plot. 

A last suggestion would be to think of a way to deal with overlapping dots, perhaps changing the alpha-levels for some bins. In this plot, the darker dots show a lot more so when dots are overlapping it is hard to see the lower-score schools. 
