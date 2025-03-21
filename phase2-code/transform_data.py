from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv
import ast
import json
import re
import xlsxwriter
# Load environment variables from .env file
load_dotenv()

# Get the DATABASE_URI, DATABASE_NAME, and COLLECTION_NAME from environment variables
database_uri = os.getenv('DATABASE_URI')
db_name = os.getenv('DB_NAME')
humans = os.getenv('DB_COLLECTION_1')
mod_bot = os.getenv('DB_COLLECTION_2')
adv_bot = os.getenv('DB_COLLECTION_3')

# Connect to MongoDB using the URI from environment variable
client = MongoClient(database_uri)

# Create or switch to your desired database
db = client[db_name]

# Fetch data from the collection
humans_mouse_movements = db[humans]
mod_bot_mouse_movements = db[mod_bot]
adv_bot_mouse_movements = db[adv_bot]

# Get all documents in each collection
humans_cursor = humans_mouse_movements.find()
mod_bot_cursor = mod_bot_mouse_movements.find()
adv_bot_cursor = adv_bot_mouse_movements.find()

def convert_to_temp_df(cursor):
    df_dict = {}

    for doc in cursor:
        doc_id = str(doc["_id"])  # Convert ObjectId to string
        doc["_id"] = doc_id  # Store _id as string
        df_dict[doc_id] = pd.DataFrame([doc])  # Each doc is a separate DataFrame
    return df_dict

humans_dict = convert_to_temp_df(humans_cursor)
mod_bot_dict = convert_to_temp_df(mod_bot_cursor)
adv_bot_dict = convert_to_temp_df(adv_bot_cursor)

def parse_mouse_movements(s):
    """Extract (x, y) coordinates from a string like '[(938,1920)][(1024,768)]'."""
    return [tuple(map(int, xy)) for xy in re.findall(r"\((\d+),(\d+)\)", s)]

def parse_mouse_move_times(s):
    """Extract timestamps as strings, checking for non-integer values."""
    values = s.split(",")
    # Check if all values can be converted to integers
    valid_values = [value for value in values if value.isdigit()]
    
    # Last entry is a blank
    return valid_values

def parse_mouse_total_movement(s):
    # Use regex to find all occurrences of pairs of square brackets
    bracket_pairs = re.findall(r'\[.*?\]', s)
    no_brackets = [pair[1:-1] for pair in bracket_pairs] # remove brackets
    return no_brackets

def unpack_data(df_dict):
    for key, df in df_dict.items():
        df_new = pd.DataFrame(columns = df.columns)
        # Parse string for other columns
        df_new["mousemove_client_height_width"] =  parse_mouse_movements(df["mousemove_client_height_width"].iloc[0])
        df_new["mousemove_times"] =  parse_mouse_move_times(df["mousemove_times"].iloc[0])
        df_new["mousemove_visited_urls"] = parse_mouse_total_movement(df["mousemove_visited_urls"].iloc[0])

        # Split the monuse movement type & coordinates
        pattern = re.compile(r'^([a-zA-Z]+)\((\d+,\d+)\)$')
        mouse_move = df["mousemove_total_behaviour"].apply(parse_mouse_total_movement).iloc[0]
        # Extract columns
        split_data = [(match.group(1), f"({match.group(2)})") if (match := pattern.match(entry)) else (None, None) for entry in mouse_move]
        df_split = pd.DataFrame(split_data, columns=["mousemove_type", "mousemove_height_width"])
        df_new = pd.concat([df_new, df_split], axis=1)
       
        df_new["_id"] = df["_id"].iloc[0]
        df_new['session_id'] = df["session_id"].iloc[0]
        df_new['unique_id'] = df["unique_id"].iloc[0]
        df_new.drop(columns=["mousemove_total_behaviour"], inplace=True)
        df_new = df_new[['_id', 'session_id', 'unique_id', 'mousemove_client_height_width', 'mousemove_times', 'mousemove_type','mousemove_height_width', 'mousemove_visited_urls']]
        df_dict[key]= df_new
    return df_dict


humans_dct_new = unpack_data(humans_dict)
mod_bot_dct_new = unpack_data(mod_bot_dict)
adv_bot_dct_new = unpack_data(adv_bot_dict)

# Save to Excel file

output_folder = os.getenv('OUTPUT_FOLDER')

def save_dict_to_excel(df_dict, filename, output_folder=output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, f"{filename}")
    with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
        for sheet_name, df in df_dict.items():
            df.to_excel(writer, sheet_name=sheet_name[:31])  # Sheet names have a 31-character limit
    print(f"Data saved to {filename}")

save_dict_to_excel(humans_dct_new, "humans_transformed_data.xlsx")
save_dict_to_excel(mod_bot_dct_new, "mod_bot_transformed_data.xlsx")
save_dict_to_excel(adv_bot_dct_new, "adv_bot_transformed_data.xlsx")
