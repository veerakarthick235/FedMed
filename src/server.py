import flwr as fl
import os

def weighted_average(metrics):
    accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
    examples = [num_examples for num_examples, _ in metrics]
    
    accuracy = sum(accuracies) / sum(examples)
    

    log_file = "training_log.csv"
    
    with open(log_file, "a") as f:
        f.write(f"{accuracy}\n")
        
    print(f"✅ ROUND AGGREGATED: Global Model Accuracy is now {accuracy:.2%}")
    return {"accuracy": accuracy}

strategy = fl.server.strategy.FedAvg(
    evaluate_metrics_aggregation_fn=weighted_average,
    min_fit_clients=2,       
    min_available_clients=2,  
)
if os.path.exists("training_log.csv"):
    os.remove("training_log.csv")
    print("🧹 Cleared old dashboard logs.")

print("🚀 Central Server for Brain Tumor Detection is Running...")
print("waiting for Hospital A and Hospital B to connect...")


fl.server.start_server(
    server_address="0.0.0.0:8080",
    config=fl.server.ServerConfig(num_rounds=5), 
    strategy=strategy,
)
