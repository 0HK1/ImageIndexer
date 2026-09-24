
import imagehash
from PIL import Image


class FileHandler:
    def phash_to_vector(self, phash_str: str) -> list[float]:
        binary = bin(int(phash_str, 16))[2:].zfill(64)

        return [float(bit) for bit in binary]

    def process_image(self, image_path: str) -> tuple[str, list[float]]:
        img = Image.open(image_path)
        phash  = str(imagehash.phash(img))
        vector = self.phash_to_vector(phash)
        return phash, vector
