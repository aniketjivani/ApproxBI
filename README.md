Implement TAGI, comparison with other methods (SVGD, VI, MCMC?) and some experiments. 
What we want to check:

- is an apple-to-apple comparison possible?
- quality of posterior (for non-Gaussian, multimodal examples potentially) - note that calibration doesn't exactly answer this question.
- computational efficiency


(if 1 and 2 are possible, there's a good scope of extending TAGI to NN models - specifically NODEs once we can resolve the conceptual issues of propagating uncertainties in time)

Thanks to Jiayuan for all the help getting started.

See how to structure code for Bayesian Inference from other libraries: e.g. https://github.com/normal-computing/posteriors/tree/main/posteriors
and https://github.com/DartML/Stein-Variational-Gradient-Descent


Original code for TAGI (from James Goulet et al.): https://github.com/CivML-PolyMtl/TAGI

