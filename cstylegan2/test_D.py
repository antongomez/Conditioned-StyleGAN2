import json
import os

from trainer import Trainer
from dataset import DatasetManager

from torch.utils import data
import numpy as np
import argparse

import matplotlib.pyplot as plt

def show_confusion_matrix(confusion_matrix, save_folder):
  confusion_matrix = np.array(confusion_matrix)
  print(confusion_matrix)

  # Plot confusion matrix as heatmap
  plt.imshow(confusion_matrix, cmap='Blues')

  plt.title('Confusion Matrix')
  plt.xlabel('Predicted label')
  plt.ylabel('True label')

  # Add color bar
  plt.colorbar()

  # Add text annotations
  for i in range(confusion_matrix.shape[0]):
      for j in range(confusion_matrix.shape[1]):
          plt.text(j, i, confusion_matrix[i, j],
                  horizontalalignment='center',
                  verticalalignment='center',
                  color='black')
          
  plt.savefig(f'{save_folder}/cm.png')

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, help='Name argument')

args = parser.parse_args()
name = args.name

root = './models'

folder = './data'

save_folder = f'./test/{name}/D'

os.makedirs(save_folder, exist_ok=True)

with open(os.path.join(root, name, 'config.json'), 'r') as file:
    config = json.load(file)

batch_size = config['batch_size']
channels = config['channels']
image_size = config['image_size']

dataset_manager = DatasetManager(folder, train=False)
dataset = dataset_manager.get_test_set()
print("Dataset length:", len(dataset))
loader = data.DataLoader(dataset, num_workers=0, batch_size=batch_size,
                                    drop_last=True, shuffle=True, pin_memory=False)

model = Trainer(**config)
model.load(-1, root=root)

correct_per_class, total_per_class, confusion_matrix = model.calculate_accuracy(loader, show_progress=True, confusion_matrix=True)

# Imprimimos a accuracy por clase
for i, (correct, total) in enumerate(zip(correct_per_class, total_per_class)):
    print(f'Class {i}: {correct}/{total} ({correct/total:.2%})')
# Imprimimos a matriz de confusion en cor
show_confusion_matrix(confusion_matrix, save_folder=save_folder)


