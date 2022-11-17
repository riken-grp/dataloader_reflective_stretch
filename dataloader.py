# coding: utf-8

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import tqdm
import logging
import json

from PIL import Image

import torch
from torch.utils.data import Dataset
from torchvision import transforms


logger = logging.getLogger("logger").getChild("dataset")


class Dataset(Dataset):
    def __init__(self, data_path):
        super().__init__()
        self.data = self.read_data(data_path)

    def read_data(self, path):
        print("Reading files...")
        with open(path, "r") as f:
            data = [json.loads(l.strip()) for l in f]
        print("Read {} dialogues".format(len(data)))

        SEP_TOKEN = "[SEP]"

        def concat_tokens(tokens_list):
            text = ""
            for tokens in tokens_list:
                text += tokens if text == "" else (SEP_TOKEN+tokens)
            if text == "":
                text = "なし"
            return text

        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )])

        data_list = []
        pbar = tqdm.tqdm(data, total=len(data))
        for d in pbar:
            position = concat_tokens(d["position_midasi"])
            pose = concat_tokens(d["pose_midasi"])
            has = concat_tokens(d["has_midasi"])
            low_table = concat_tokens(d["low_table_midasi"])
            dining_table = concat_tokens(d["dining_table_midasi"])
            kitchen = concat_tokens(d["kitchen_midasi"])

            utterance = " ".join(d["midasi"])
            response = " ".join(d["r_"+"midasi"])

            data_list.append({
                "idx": [int(d["filename"][:2]+d["filename"][3:])],
                "utterance": utterance,
                "response": response,
                "viewpoint": [int(d["viewpoint"])],
                "position": position,
                "pose": pose,
                "has": has,
                "low_table": low_table,
                "dining_table": dining_table,
                "kitchen": kitchen,
                "image": transform(Image.open(os.path.join("./data/image", d["filename"]+".jpg"))),
                "category": [d["action"]],
            })

        return data_list

    def __len__(self):
        return len(self.data)


if __name__ == "__main__":
    data_path = "./data/scenario/scenario.integrated.json"
    dataset = Dataset(data_path)
    import pdb; pdb.set_trace()
