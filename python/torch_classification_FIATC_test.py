from fiat_tool.FIATClassificationDataset import FIATClassificationDataset
from torch.utils.data import DataLoader


batch_size = 1
training_epochs = 1

datasets = FIATClassificationDataset('C://Github//FIAT//example_dataset//food//',
                                     label_height=224,
                                     label_width=224,
                                     isColor=True,
                                     isNorm=False)

data_loader = DataLoader(datasets, batch_size=batch_size, shuffle=True)

for epoch in range(training_epochs): # 앞서 training_epochs의 값은 15로 지정함.
    avg_cost = 0
    avg_acc = 0
    total_batch = len(data_loader)

    for x_input, y_input in data_loader:
        print('x_input shape = ', x_input.shape)
        print('y_input shape = ', y_input.shape)




print('Training loop finished')