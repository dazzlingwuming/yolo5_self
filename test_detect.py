if __name__ =="__main__":
    import torch

    print(torch.hub.get_dir())

    # Model
    model = torch.hub.load(r"C:\Users\lihaodong\.cache\torch\hub\ultralytics_yolov5_master", 'yolov5s',source="local")  # or yolov5n - yolov5x6, custom
    print(torch.hub.get_dir())
    # Images
    img = r"G:\机器学习\kaggle数据集\多物体检测\多鸽子.jpg"  # or file, Path, PIL, OpenCV, numpy, list

    # Inference
    results = model(img)

    # Results
    results.show()  # or .show(), .save(), .crop(), .pandas(), etc.

