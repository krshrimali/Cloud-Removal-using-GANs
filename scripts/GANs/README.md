## Solution using GANs

This is a start to solving the problem using GANs. Here is the expected pipeline:

1. Think yourself on how it will proceed. Which type of GANs do we need to use?
2. Make a shallow code based on what you thought.
3. Go through the literature review, what has been done before and how close were you to the existing solutions? What are their evaluation metrics? What is SOTA in this task? Make a list.
4. Implement the existing solutions, and use the augmented data using change in intensity/brightness/blurring/noising etc. Do you see any improvements?

**Extras**

1. Divide the data using technique of detecting IQA (using BRISQUE or something else, maybe Divine or something like Full Reference IQA), or using variance of laplacian measure (calculate the average variance of laplacian for that). Note: 250 images with cloud, and 1250 without cloud. Need heavy data augmentation. Method important than the output - Ojha sir. So don't care about getting more data.
