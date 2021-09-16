import matplotlib.pyplot as plt
import seaborn as sns


# Subplot seaborn / create figure
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle("Figure Title")

sns.histplot(data=data, x="x axis data name", bins=50, ax=axes[0])
#rotate labels / xticks
plt.setp(axes[0].xaxis.get_majorticklabels(), rotation=45)
# set axes labels
axes[0].set_xlabel("xlabel)
axes[0].set_ylabel("tlabel")


