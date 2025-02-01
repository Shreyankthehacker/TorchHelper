


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
