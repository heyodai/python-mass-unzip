import os
import argparse
import logging
import zipfile
import time

epoch_time = int(time.time())
if not os.path.exists('logs'):
    os.makedirs('logs')
    
logging.basicConfig(filename=f'logs/{epoch_time}.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def unzip_file(full_path, directory):
    try:
        with zipfile.ZipFile(full_path, 'r') as zip_ref:
            logging.info(f'Unzipping file {full_path}')
            zip_ref.extractall(directory)
        logging.info(f'Successfully unzipped file {full_path}')
    except Exception as e:
        logging.error(f'Failed to unzip file {full_path}, error: {str(e)}')

def delete_file(full_path):
    try:
        os.remove(full_path)
        logging.info(f'Successfully deleted zip file {full_path}')
    except Exception as e:
        logging.error(f'Failed to delete file {full_path}, error: {str(e)}')

def main():
    parser = argparse.ArgumentParser(description='Unzip and delete zip files in a directory.')
    parser.add_argument('dir', type=str, help='The directory to process')
    
    args = parser.parse_args()
    directory = args.dir

    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            full_path = os.path.join(directory, filename)
            unzip_file(full_path, directory)
            delete_file(full_path)

if __name__ == "__main__":
    main()
