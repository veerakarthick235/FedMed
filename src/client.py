import flwr as fl
import torch
from model import Net, train, test
from utils import load_data
import sys

if len(sys.argv) < 2:
    print("Usage: python client.py [node_id]")
    sys.exit(1)
    
NODE_ID = int(sys.argv[1]) 

print(f"🏥 Loading data for Hospital {NODE_ID}...")
trainloader, testloader = load_data(node_id=NODE_ID, num_nodes=2)
print(f"✅ Data Loaded: {len(trainloader.dataset)} training images.")

net = Net()

class HospitalClient(fl.client.NumPyClient):
    def get_parameters(self, config):
        return [val.cpu().numpy() for _, val in net.state_dict().items()]

    def set_parameters(self, parameters):
        params_dict = zip(net.state_dict().keys(), parameters)
        state_dict = {k: torch.tensor(v) for k, v in params_dict}
        net.load_state_dict(state_dict, strict=True)

    def fit(self, parameters, config):
        self.set_parameters(parameters)
        # Train locally for 1 epoch
        train(net, trainloader, epochs=1)
        return self.get_parameters(config={}), len(trainloader.dataset), {}

    def evaluate(self, parameters, config):
        self.set_parameters(parameters)
        loss, accuracy = test(net, testloader)
        return float(loss), len(testloader.dataset), {"accuracy": float(accuracy)}

print(f"🏥 Hospital {NODE_ID} connecting to server...")
fl.client.start_numpy_client(server_address="127.0.0.1:8080", client=HospitalClient())