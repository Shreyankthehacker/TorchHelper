


def food101Data():
  import os , requests , zipfile
  from pathlib import Path

  data_path = Path("data/")
  image_path  = data_path / "pizza_steak_sushi"
def food101Data():
  import os , requests , zipfile
  from pathlib import Path

  data_path = Path("data/")
  image_path  = data_path / "pizza_steak_sushi"

  if image_path.is_dir():
    print(f"{image_path} directory exists")
  else :
    print(f"Did not found {image_path} directory ..... creating one ")
    image_path.mkdir(parents = True , exist_ok = True)

  zipfile_name = "pizza_steak_sushi.zip"
  with open(data_path / zipfile_name,"wb") as f:
    request = requests.get("https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip")
    print("Downloadingggggg pizza steak sushii")
    f.write(request.content)

  with zipfile.ZipFile(data_path / zipfile_name, 'r') as zip_ref:
      zip_ref.extractall(image_path)

  os.remove(data_path / zipfile_name)
  image_path.mkdir(parents = True , exist_ok = True)

  zipfile = "pizza_steak_sushi.zip"
  with open(data_path / zipfile,"wb") as f:
    request = requests.get("https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/zipfile")
    print("Downloadingggggg pizza steak sushii")
    f.write(request.content)

  os.remove(data_path / zipfile)


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
