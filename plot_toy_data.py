# %%
import matplotlib.pyplot as plt
import toy_data as td


plt.rc("axes.spines", right=True, top=True)
plt.rc("figure", dpi=300, 
       figsize=(9, 3)
      )
plt.rc("font", family="serif")
plt.rc("legend", edgecolor="none", frameon=True)

dataset = td.gen_mog6_samples(n_samples=1000)
pos_xy, p_xy = td.density_mog6(d=7.0, ngrid=50)

plt.figure()

plt.imshow(p_xy.squeeze().numpy().T, 
           extent=(-7, 7, -7, 7), 
           origin='lower', 
           cmap='viridis')


plt.xlabel(r"$x_1$")
plt.ylabel(r"$x_2$")

plt.scatter(dataset[:, 0], 
            dataset[:, 1], 
            s=2, 
            color='red', 
            alpha=0.5)
# %%
