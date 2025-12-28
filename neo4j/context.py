from strawberry.dataloader import DataLoader
from dataloaders import batch_load_companies

def get_context():
    return {
        "company_loader": DataLoader(load_fn=batch_load_companies)
    }
