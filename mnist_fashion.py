import torch
from torch import nn, optim
from torch.utils.data import TensorDataset, DataLoader, Dataset
from torch.functional import F
import idx2numpy
import zipfile
import os

import matplotlib.pyplot as plt
import numpy as np

# Open Dataset
MNIST_FASHION_PATH = "dataset/MNIST_FASHION"
IMG = "t10k-images-idx3-ubyte"
LABEL = "t10k-labels-idx1-ubyte"

MNIST = os.path.join(MNIST_FASHION_PATH, "t10k-images-idx3-ubyte.zip")
with zipfile.ZipFile(MNIST, "r") as f:
    with f.open(IMG) as file:
        X = idx2numpy.convert_from_file(file)
        y = idx2numpy.convert_from_file(os.path.join(MNIST_FASHION_PATH, LABEL))

X = X.copy()
y = y.copy()

# Label Mapping
label = {
    0: "T-shirt/Top",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

# Convert from Numpy to Tensor
X = torch.FloatTensor(X)
y = torch.LongTensor(y)
dataset = TensorDataset(X, y)


# Train, Val and Test Split
TRAIN_SIZE = 0.8
train_size = int(TRAIN_SIZE * len(dataset))

val_size = int(len(dataset) - train_size) // 2
test_size = int(len(dataset) - train_size) // 2

train_dataset, val_dataset, test_dataset = torch.utils.data.random_split(
    dataset, lengths=[train_size, val_size, test_size]
)

# Train Loader & Val Loader
train_loader = DataLoader(train_dataset, batch_size=100)
val_loader = DataLoader(val_dataset, batch_size=100)


# Model
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.dummy_param = nn.Parameter(torch.empty(0))
        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.fc1 = nn.Linear(in_features=64 * 6 * 6, out_features=600)
        self.drop = nn.Dropout(0.5)
        self.fc2 = nn.Linear(in_features=600, out_features=120)
        self.fc3 = nn.Linear(in_features=120, out_features=10)

    def forward(self, x):
        x = x.view(-1, 1, 28, 28)
        x = self.layer1(x)
        x = self.layer2(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.log_softmax(x, dim=1)
        return x


INPUT_SIZE = 28 * 28
HIDDEN_SIZE = 64
NUM_CLASSES = 10

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = Model().to(device)

criterion = nn.NLLLoss()
optimizer = optim.AdamW(model.parameters())

EPOCHS = 100


# Function of Training Model
def train(EPOCHS, model):
    cnt = 0
    for epoch in range(EPOCHS):
        for features, targets in train_loader:
            features, targets = features.to(device), targets.to(device)

            outs = model(features)

            loss = criterion(outs, targets)

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

            cnt += 1

            if not (cnt % 50):
                total = 0
                correct = 0

                for features, targets in val_loader:
                    features, targets = features.to(device), targets.to(device)

                    outs = model(features)

                    preds = outs.argmax(1)

                    correct += torch.sum(preds == targets)

                    total += targets.shape[0]

                accuracy = correct.item() / total

            if not (cnt % 500):
                print(
                    "Iteration: {}, Loss: {}, Accuracy: {}%".format(
                        cnt, loss.data, accuracy
                    )
                )


# Training Model
train(10, model=model)

# output :
# iteration: 500, Loss: 0.3056876063346863, Accuracy: 0.866%


# Testing Model
fig, axes = plt.subplots(2, 5, figsize=(15, 6))

for i, ax in enumerate(axes.flat):
    idx = np.random.choice(range(len(test_dataset)))
    X, y = test_dataset[idx]
    outs = model(X.to(device)).argmax(1)
    outs = label[outs.item()]
    y = label[y.item()]

    ax.imshow(X)
    ax.set_title(f"pred : {outs} | actual : {y}", fontsize=9)
    ax.axis("off")

plt.show()
