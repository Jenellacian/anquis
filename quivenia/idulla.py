import torch
import torch.nn as nn
import torch.optim as optim

def main(rank, world_size):
    setup(rank, world_size)
    
    # Create a simple model and move it to the appropriate device
    model = nn.Linear(10, 10).to(rank)
    # Wrap the model using DistributedDataParallel
    ddp_model = DDP(model, device_ids=[rank])
    
    # Define a loss function and an optimizer
    criterion = nn.MSELoss()
    optimizer = optim.SGD(ddp_model.parameters(), lr=0.001)
    
    # Dummy input and target
    inputs = torch.randn(20, 10).to(rank)
    targets = torch.randn(20, 10).to(rank)
    
    # Forward pass
    outputs = ddp_model(inputs)
    loss = criterion(outputs, targets)
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    
    # Extract gradients
    all_gradients = [param.grad for param in ddp_model.parameters()]
    
    # Perform all_reduce on gradients
    for grad in all_gradients:
        dist.all_reduce(grad, op=dist.ReduceOp.SUM)
        grad /= world_size  # Average the gradients
    
    # Step the optimizer
    optimizer.step()
    
    cleanup()

if __name__ == "__main__":
    world_size = 4
    torch.multiprocessing.spawn(main,
                                args=(world_size,),
                                nprocs=world_size,
                                join=True)
