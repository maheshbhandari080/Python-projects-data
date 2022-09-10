#!/usr/bin/env python
# coding: utf-8

# In[12]:


# NumPy is imported, seed is set
import numpy as np
# Starting step
step = 50
dice = np.random.randint(1,7)
# Roll the dice
#print(np.random.randint(1,7))

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(step)
print(dice)


# In[14]:


import numpy as np
# Initialize random_walk
np.random.seed(123)
random_walk = [0]

# Complete the range
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]
    

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
print(step)


# In[17]:


import numpy as np

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step -1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
print(dice)
print(step)


# In[31]:


# NumPy is imported, seed is set
import numpy as np
# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)
print(random_walk)
print(step)
print(dice)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)
plt.show()

# Show the plot


# In[34]:


# NumPy is imported; seed is set
import numpy as np
# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
#print(all_walks)
import matplotlib.pyplot as plt
plt.plot(all_walks)
plt.show()


# In[35]:


import numpy as np
import matplotlib.pyplot as plt
# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)
print(np_aw)
# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)
# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


# In[ ]:




