
from torchvision import datasets , transforms
def Imagedataloaders(    train_dir: str,
    test_dir: str,
    transform: transforms.Compose,
    batch_size: int):


  from torchvision import datasets , transforms
  from torch.utils.data import DataLoader


  train_dataset = datasets.Imagefolder(train_dir , transform = transform)
  test_dataset = datasets.ImageFolder(test_dir , transform = transforms)

  train_dataloader = DataLoader(train_dataset , batch_size , True , pin_memory=True)
  test_dataloader = DataLoader(test_dataset , batch_size , False,pin_memory = True)

  class_name = train_dataloader.classes
  return train_dataloader , test_dataloader , class_name

