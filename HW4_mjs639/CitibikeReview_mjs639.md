IDEA: People prefer to ride bike for short distance, which is less than 20 minutes**

Null hypothesis: The ratio of trips less or equal to 20 minutes is the same or less than the ratio of trips more than 30 minutes.  

H0: Tlong >= Tshort

Alternative hypothesis The ratio of trips less or equal to 20 minutes is more than the ratio of trips more than 30 minutes. 

H1: Tlong < Tshort

The significance threshold is 5%

-------------------------------------------------------------------
This is an interesting idea to test, and I think you extracted the necessary data to test for significance. You might have done some extra work, even; since the idea you propose does not make a hypothesis about whether there is a difference in distance against the day of the week, I don't think you needed to view the data in that way.

In your initial idea and hypotheses, you are comparing trips that are 20 minutes or shorter against trips that are longer than 30 minutes. This leaves out all trips that are between 20 and 30 minutes. I would recommend selecting one value (20 or 30) as the threshold between long and short trips. I noticed that, later in the assignment you assign Tshort and Tlong as a metric based on what side of df['trip duration'] = 1200 they fall on, which sets 20 minutes as the threshold. Working with that number, I would recommend rephrasing the hypotheses as follows:

Null hypothesis: The ratio of trips less than or equal to 20 minutes in length is the same or smaller than the ratio of trips more than 20 minutes in length.   

H0: Tshort <= Tlong

Alternative hypothesis: The ratio of trips less than or equal to 20 minutes in length is larger than the ratio of trips more than 20 minutes in length.   

H1: Tshort > Tlong

To test this, I believe you simply need to calculate the ratio of rides that fall in both categories. You have already counted the number of each type, which you used to plot figure 1a. Rather than breaking down the data by date, you can simply determine the ratio by dividing both counts by the sample size. 

Using the flowchart to determine which test you should run, I believe the best fit would be the chi-squared goodness of fit test, with Yates' correlation. We are looking at the ratios of short and long rides, and want to determine if the ratios found in the data are relevant. The hypothesis made requires a prior information (we assume that shorter trips are more prevalent), and we have one variable (the length of the trip) pulled from one sample, which two categories: short trip or long trip. 


# FBB good, in the worded Null/Alternative "ratio" of trips should be "fraction" of trips, and this is a test for proportions. 
