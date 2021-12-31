import time
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


def checkspill(loader1, loader2):
    hash_loader1 = []
    hash_loader2 = []

    for loader_inx, loader in enumerate([loader1, loader2]):
        for data, _ in loader:
            if loader_inx == 0:
                for i in range(data.shape[0]):
                    d = data[i]
                    hash_loader1.append(hash(np.array(d).tobytes()))
            elif loader_inx == 1:
                for i in range(data.shape[0]):
                    d = data[i]
                    hash_loader2.append(hash(np.array(d).tobytes()))

    set_hash_loader1 = set(hash_loader1)
    set_hash_loader2 = set(hash_loader2)

    print(len(hash_loader1), len(set_hash_loader1))

    print(f"Loader 1 had {len(hash_loader1) - len(set_hash_loader1)} duplicates")
    print(f"Loader 2 had {len(hash_loader2) - len(set_hash_loader2)} duplicates")

    print(f"Test and train had {len(set_hash_loader1.intersection(set_hash_loader2))} samples in common.")








if __name__ == "__main__":
    import webdataset as wds
    dataset_testing = test_dataset()
    cleandata = cleantest()
    manualdata = manualtest()
    batch_size = 4096
    dataset = (
        wds.WebDataset("shards/a/shard{0000000..002000}.tar")
            .shuffle(1000)
            .decode()
            .to_tuple("x.pyd", "y.pyd")
    )

    train_loader = torch.utils.data.DataLoader(dataset,num_workers=24 ,batch_size=4096)

    test_loader = torch.utils.data.DataLoader(dataset=dataset_testing,
                                              batch_size=batch_size,
                                              shuffle=True)

    clean_loader = torch.utils.data.DataLoader(dataset=cleandata,
                                               batch_size=batch_size,
                                               shuffle=True)

    manual_loader = torch.utils.data.DataLoader(dataset=manualdata,
                                                batch_size=batch_size,
                                                shuffle=True)

    checkspill(manual_loader,manual_loader)