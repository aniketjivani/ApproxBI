Implement TAGI, comparison with other methods (SVGD, VI, MCMC?) and some experiments. 
What we want to check:

- is an apple-to-apple comparison possible?
- quality of posterior (for non-Gaussian, multimodal examples potentially) - note that calibration doesn't exactly answer this question.
- computational efficiency


(if 1 and 2 are possible, there's a good scope of extending TAGI to NN models - specifically NODEs once we can resolve the conceptual issues of propagating uncertainties in time)

Thanks to Jiayuan for all the help getting started on TAGI.

Other resources for inference
1. https://github.com/normal-computing/posteriors/tree/main/posteriors
2. https://github.com/DartML/Stein-Variational-Gradient-Descent
3. https://sanyamkapoor.com/kb/the-stein-gradient/


Original code for TAGI (from James Goulet et al.): https://github.com/CivML-PolyMtl/TAGI


Miscellaneous things to try / check:

1. How does the choice of kernel make learning the SVGD posterior more / less efficient? Would non-stationary kernels be useful in some applications?

2. Can we use some other divergence measure to improve the quality of the approximation? Clearly, other Stein operators are possible. What is the theoretical connection? What are algorithmic connections to normalizing flows?

3. Are there systematic ways to adapt the kernel bandwidth in each gradient-descent step?

4. Is there a nice way to do kernel operations in Fourier space ala FNOs?

5. Connections to other divergence measures?