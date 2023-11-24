import base64
import asyncio

import httpx

from image_describer.tasks import predict_image_title

N_REQUESTS = 1
IMAGE_PATH = "tests/static/test_image.jpg"


def encode_image_file_to_base64(file_path=IMAGE_PATH):
    with open(file_path, "rb") as image_file:
        binary_data = image_file.read()
        base64_encoded = base64.b64encode(binary_data)
        base64_string = base64_encoded.decode("utf-8")
    return base64_string


async def main():
    image = encode_image_file_to_base64()
    data = {"image": f"data:image/png;base64,{image}"}
    async with httpx.AsyncClient() as client:
        for x in range(N_REQUESTS):
            print("Sending Image to Describe")
            response = await client.post(
                "http://localhost:9000/api/v1/predictions", json=data, timeout=None
            )
            print(response)


if __name__ == "__main__":
    asyncio.run(main())
