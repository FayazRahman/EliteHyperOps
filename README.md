# EliteHyperOps
Create_Dataset.py is used to generate data on which we train the Neural Network in train.py file. Graph.py and Model.py are the File that contain actual Franke Wolfe Algorithm Implementation. Example.py is used to combine them and run actual Franke Wolfe Algorithm. Data.py contains all the data(like graphs, demand, capacity, potential routes that need to be checked for braess routes(braess indexes)) which corresponds to Hyperloop Station in Pune. frank_wolfe_nn is our trained Neural Network. Presently it is trained on 3100 data points with average loss of 8.170. Main.py uses the trained Neural Network to output the Braess Routes. 

How to use it in Hyperloop Station.
1) So, at a higher level of abstraction, given deman and capacities  at a particular instant of time, our  software outputs braess routes which are bottlenecks i the system.
graph.py, model.py taken from this [awesome repo](https://github.com/ZhengLi95/User-Equilibrium-Solution) by [ZhengLi95.](https://github.com/ZhengLi95)
