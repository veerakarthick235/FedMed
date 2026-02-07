import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, random_split
import os

def load_data(node_id, num_nodes=2):
    """
    Loads the Brain Tumor Dataset.
    Automatically finds the data folder to avoid path errors.
    """
    
    
    possible_paths = [
        './data/archive/Training',    
        './data/Training',            
        '../data/archive/Training',   
        '../data/Training',
        './data/brain_tumor_dataset/Training'
    ]

    
    train_dir = None
    for path in possible_paths:
        if os.path.exists(path):
            train_dir = path
            test_dir = path.replace('Training', 'Testing')
            break
    
    
    if train_dir is None:
        print("\n❌ CRITICAL ERROR: Could not find the 'Training' folder.")
        print("Please check that your folder structure looks like one of these:")
        print("   FedMed_Project/data/archive/Training")
        print("   FedMed_Project/data/Training")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Files in ./data: {os.listdir('./data') if os.path.exists('./data') else 'No data folder found'}\n")
        raise FileNotFoundError("Could not locate dataset.")

    print(f"✅ Found dataset at: {train_dir}")

    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    
    full_trainset = torchvision.datasets.ImageFolder(root=train_dir, transform=transform)
    testset = torchvision.datasets.ImageFolder(root=test_dir, transform=transform)

    
    partition_size = len(full_trainset) // num_nodes
    lengths = [partition_size] * num_nodes
    
    
    if sum(lengths) < len(full_trainset):
        lengths[-1] += len(full_trainset) - sum(lengths)

    datasets = random_split(full_trainset, lengths)
    trainloader = DataLoader(datasets[node_id], batch_size=32, shuffle=True)
    testloader = DataLoader(testset, batch_size=32)

    return trainloader, testloader