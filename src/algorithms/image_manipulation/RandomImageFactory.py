from __future__ import annotations
from src.algorithms.image_manipulation.Resolution import Resolution
from PIL import Image
from hashlib import sha512
from datetime import datetime
from os import path
import numpy as np


class RandomImageFactory:
    @classmethod
    def generate_random_image(cls: RandomImageFactory, res: Resolution, file: str = ""):
        pixels = cls.create_image_array(res)
        image = cls.create_image_from_array(pixels)
        cls.save_image(image, file)
        return 0

    @classmethod
    def create_image_array(cls: RandomImageFactory, res: Resolution) -> np.ndarray:
        return np.random.randint(low=0, high=255, size=(res.height, res.width, 3))

    @classmethod
    def create_image_from_array(cls: RandomImageFactory, pixels: np.ndarray) -> Image:
        return Image.fromarray(pixels.astype("uint8")).convert("RGB")

    @classmethod
    def save_image(cls: RandomImageFactory, image: Image, file: str) -> None:
        file = file if file else cls.generate_file_path()
        image.save(file)
        return

    @classmethod
    def generate_file_path(cls, ext: str = "png"):
        base_path = f"{path.dirname(path.realpath(__file__))}/sample-data/out"
        current_time = datetime.now().ctime().encode("utf-8")
        hex_digits = sha512(current_time).hexdigest()[:20]
        return f"{base_path}/{hex_digits}.{ext}"