1. This problem is similar to denoising/edge detection etc. using GANs. Image to Image Translation, because the input and output are both images (and not noise). 
2. It's not a classification problem. And is also supervised learning problem. (**Rethink on this**)
3. Next step: Check how image to image translation works using GANs, the code should be almost similar.

**Step 1:** Reading through Pix2Pix Blog

1. Good trick: Save the loaded datasets as NumPy Arrays in .npz format. This will save time while loading data during experimentations again and again. NumPy has savez_compressed function, 
   import using from numpy import savez_compressed
