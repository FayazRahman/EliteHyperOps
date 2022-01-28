# EliteHyperOps
Create_Dataset.py is used to generate data on which we train the Neural Network in train.py file. The reason we are training the Neural Network , instead of using the actual Frank Wolfe is because FW is computationally expensive. And in our end goal to detect braess routes we need to apply it multiple times. A well trained NN will give us lower computational cost and make our solution realtime.

Graph.py and Model.py are the File that contain actual Franke Wolfe Algorithm Implementation. Example.py is used to combine them and run actual Franke Wolfe Algorithm. Data.py contains all the data(like graphs, demand, capacity, potential routes that need to be checked for braess routes(braess indexes)) which corresponds to Hyperloop Station in Pune. frank_wolfe_nn is our trained Neural Network. Presently it is trained on 3100 data points with average loss of 8.170. Main.py uses the trained Neural Network to output the Braess Routes. Here, we have searched for braess routes only in links between the Hyperloop Platforms, because these routes that have the highest concentration of traffic during peak hours. But our software is eqully capable of scanning the whole network for these braess routes. 

We have two folders for SUMO Simulation, which simulates the Hyperloop station. Using it we confirmed the effectiveness of our software, by howing that removing/dinincentivising the braess routes helps improve traffic condition. The ORIGINAL folder contains the SUMO Simulation for normal Hyperloop Station. The 2nd folder contains the SUMO simulation after removing the braess routes as returned by the output of main.py. Using any random deman, we found that the Routes that needs to be Disincentivised are :  (64, 75, 81, 82, 93). This is the number of edge, related to the adjecency list of the graph in data.py . After running the simulation, by executing Configuration files in these foulder in SUMO GUI, the results were: 
1)The time taken by traffic to reach its destination in original network : 1595 seconds 
2)The time taken by traffic to reach its destination in network devoid of braess routes: 1511 seconds 

How to use the software in the real Hyperloop Station.

1) Given demand and capacities  at a particular instant of time, our software outputs braess routes, in a network of routes which act as bottlenecks and hence need special attention.
2) These braess routes are a function of demand and time. That is, braess routes change from time to time as demand of people using a particular route changes. Hence we would need to run the software first with the predicted demand of each routes, using ticketing information and then using realtime data from Mobile Signals,and CCTV cameras.
3) We would use these braess routes, till they "just" start acting as bottle necks ,following which, we would disincentivise them. This can be done by changing direction on LED Sign Boards, and notifying the user on an app which would tell them most optimised routes. Using the principle of collective intelligence, we would tell every passenger the routes which would be best for the overall traffic condition, and not necessarily the shortest path for that particular individual.  .
4) Before implementing the results of Main.py, we can simulate the traffic with SUMO to know the effectiveness of the solution.

Hence, Our Software can revolutionalize how we tackle the problem of Traffic Management.  

EliteHyperOps Project created by team members, for Hyperops Competition of IIT Bombay Techfest 2021:-
Uday Uppal
Fayaz Rahman
Yashvardhan Gaur(Team Leader)
Tarush

graph.py, model.py taken from this [awesome repo](https://github.com/ZhengLi95/User-Equilibrium-Solution) by [ZhengLi95.](https://github.com/ZhengLi95)
