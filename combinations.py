import numpy as np
import torch
from torch import nn
import pickle
from nn_model import NeuralNetwork, FrankWolfeDataset
from itertools import combinations
from torch.utils.data import Dataset, DataLoader
from model import TrafficFlowModel
from main import turn_off_braess, turn_on_braess, get_input, demand
from data import braess_idxs 
tm=TrafficFlowModel()
model = NeuralNetwork()
model.load_state_dict(torch.load("frank_wolfe_nn"))
model.eval()
#test_dataset = FrankWolfeDataset("test_dataset")
#print (test_dataset)
#test_dataloader = DataLoader(test_dataset, batch_size=128, shuffle=True)
#with torch.no_grad():    
 #  out_data = model(torch.from_numpy(test_dataset[0][0]).float())
#lt=tm.__link_flow_to_link_time(out_data)
#pt=tm.__link_time_to_path_time(lt)
#print(out_data,out_data.shape)
#average_time = np.mean()
#print(pt,pt.shape)
min=10000000000000
tracker_i=0
tracker_j=0
for(i in range(0,13)):
    comb = combinations(braess_idxs, i)
    for j in comb:
        turn_off_braess(c for c in j)
        with torch.no_grad():    
            out_data = model(torch.from_numpy(get_input(demand)).float())
        lt=tm.__link_flow_to_link_time(out_data)
        pt=tm.__link_time_to_path_time(lt)
        #average_time = np.mean()
        if(pt<min):
            min=pt
            tracker_i=i
            tracker_j=j  
        turn_on_braess(c for c in j)
print(min,tracker_i,tracker_j)

 