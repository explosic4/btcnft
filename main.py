import os
import json

folder_path = './btcnft'

def process_all_json_files(folder_path):
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
        for file in files:
            file_path = os.path.join(folder_path, file)
            print(file_path)

            data = read_data(file_path)
            print("时间轴", data["x"])
            print("地板价（卖盘最低价）", data["y"]["floorPrice"])
            print("平均成交价", data["y"]["avgPrice"])
            print("成交笔数", data["y"]["salesCount"])
            print("交易额", data["y"]["volumePrice"])

    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred while processing files in {folder_path}: {e}")


def read_data(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data["data"]["curves"]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")


if __name__ == '__main__':
    process_all_json_files(folder_path)
