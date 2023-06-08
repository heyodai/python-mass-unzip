import os
import argparse
import logging
import zipfile
import time

epoch_time = int(time.time())
if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

handler = logging.FileHandler(filename=f'logs/{epoch_time}.log', mode='w')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

def unzip_file(full_path, directory):
    filename = os.path.basename(full_path)
    name, extension = os.path.splitext(filename)
    target_directory = os.path.join(directory, name)
    
    try:
        os.makedirs(target_directory, exist_ok=True)
        with zipfile.ZipFile(full_path, 'r') as zip_ref:
            logger.info(f'Unzipping file {full_path} into directory {target_directory}')
            zip_ref.extractall(target_directory)
        logger.info(f'Successfully unzipped file {full_path}')
    except Exception as e:
        logger.error(f'Failed to unzip file {full_path}, error: {str(e)}')

def delete_file(full_path):
    try:
        os.remove(full_path)
        logger.info(f'Successfully deleted zip file {full_path}')
    except Exception as e:
        logger.error(f'Failed to delete file {full_path}, error: {str(e)}')

def main():
    start_time = time.time()

    parser = argparse.ArgumentParser(description='Unzip and delete zip files in a directory.')
    parser.add_argument('dir', type=str, help='The directory to process')
    
    args = parser.parse_args()
    directory = args.dir

    zip_files = [f for f in os.listdir(directory) if f.endswith(".zip")]
    total_files = len(zip_files)

    for i, filename in enumerate(zip_files, start=1):
        full_path = os.path.join(directory, filename)
        unzip_file(full_path, directory)
        delete_file(full_path)
        logger.info(f'Processed {i} out of {total_files}')

    elapsed_time = time.time() - start_time
    logger.info(f'Elapsed time: {elapsed_time} seconds')

if __name__ == "__main__":
    main()
