


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

import os
import zipfile

from pathlib import Path

import requests

def download_data(source: str, 
                  destination: str,
                  remove_source: bool = True) -> Path:
    """Downloads a zipped dataset from source and unzips to destination.

    Args:
        source (str): A link to a zipped file containing data.
        destination (str): A target directory to unzip data to.
        remove_source (bool): Whether to remove the source after downloading and extracting.
    
    Returns:
        pathlib.Path to downloaded data.
    
    Example usage:
        download_data(source="https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip",
                      destination="pizza_steak_sushi")
    """
    # Setup path to data folder
    data_path = Path("data/")
    image_path = data_path / destination

    # If the image folder doesn't exist, download it and prepare it... 
    if image_path.is_dir():
        print(f"[INFO] {image_path} directory exists, skipping download.")
    else:
        print(f"[INFO] Did not find {image_path} directory, creating one...")
        image_path.mkdir(parents=True, exist_ok=True)
        
        # Download pizza, steak, sushi data
        target_file = Path(source).name
        with open(data_path / target_file, "wb") as f:
            request = requests.get(source)
            print(f"[INFO] Downloading {target_file} from {source}...")
            f.write(request.content)

        # Unzip pizza, steak, sushi data
        with zipfile.ZipFile(data_path / target_file, "r") as zip_ref:
            print(f"[INFO] Unzipping {target_file} data...") 
            zip_ref.extractall(image_path)

        # Remove .zip file
        if remove_source:
            os.remove(data_path / target_file)
    
    return image_path

from torchvision import datasets , transforms
def Imagedataloaders(    train_dir: str,
    test_dir: str,
    transform: transforms.Compose,
    batch_size: int):


  from torchvision import datasets , transforms
  from torch.utils.data import DataLoader


  train_dataset = datasets.ImageFolder(train_dir , transform = transform)
  test_dataset = datasets.ImageFolder(test_dir , transform = transforms)

  train_dataloader = DataLoader(train_dataset , batch_size , True , pin_memory=True)
  test_dataloader = DataLoader(test_dataset , batch_size , False,pin_memory = True)

  class_name = train_dataloader.classes
  return train_dataloader , test_dataloader , class_name
