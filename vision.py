import glob
import os
import pandas as pd
from PIL import Image
from io import BytesIO
from ollama import Client

client = Client(host='https://llm.local.naim.run')


def load_or_create_dataframe(filename: str) -> pd.DataFrame:
    """Load a DataFrame from a CSV file, or create a new one if the file doesn't exist.

    Args:
        filename (str): The name of the CSV file to load or create.

    Returns:
        pd.DataFrame: The loaded or newly created DataFrame.
    """
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    return pd.DataFrame(columns=['image_file', 'description'])


def get_png_files(folder_path: str) -> list:
    """Get a list of all PNG files in a specified folder.

    Args:
        folder_path (str): The path to the folder containing the images.

    Returns:
        list: A list of file paths to the PNG images.
    """
    return sorted(glob.glob(f"{folder_path}/*.png"))


def process_image(image_file: str, dataframe: pd.DataFrame) -> None:
    """Process an image file by generating a description and adding it to the DataFrame.

    Args:
        image_file (str): The path to the image file to process.
        dataframe (pd.DataFrame): The DataFrame to append the image description to.
    """
    print(f"\nProcessing {image_file}\n")
    try:
        with Image.open(image_file) as img, BytesIO() as buffer:
            img.save(buffer, format='PNG')
            image_bytes = buffer.getvalue()

        full_response = ''
        for response in client.generate(model='llava',
                                        prompt='describe this image and make sure to include anything notable about '
                                               'it (include text you see in the image):',
                                        images=[image_bytes], stream=True):
            print(response['response'], end='', flush=True)
            full_response += response['response']

        dataframe.loc[len(dataframe)] = [image_file, full_response]
    except Exception as e:
        print(f"Error processing {image_file}: {e}")


def main():
    df = load_or_create_dataframe('image_descriptions.csv')
    image_files = get_png_files("./images")

    print(image_files[:3])
    print(df.head())

    for image_file in image_files:
        if image_file not in df['image_file'].values:
            process_image(image_file, df)

    df.to_csv('image_descriptions.csv', index=False)


if __name__ == "__main__":
    main()
