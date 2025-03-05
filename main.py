import numpy as np
import pandas as pd

from data import common_scale as dict

# Define file paths
FILE_PATH = "data/data.csv"  
OUTPUT_FILE = "data/comp_sci_student_data.csv"

def parse_data():
    """
    Parses and processes student data from a CSV file.

    The function filters out female students, selects relevant columns, 
    and saves the cleaned data to a new CSV file.

    Returns:
        DataFrame: Processed DataFrame if successful, otherwise None.
    """
    try:
        df = pd.read_csv(FILE_PATH)

        # Filter dataset and retain necessary columns
        df = df[df["Gender"] != "Female"]
        df = df[['Gaming', 'Last', 'Overall', 'Attendance', 'Preparation']]
        
        # Save processed data
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"CSV file saved successfully as: {OUTPUT_FILE}")

        return df

    except FileNotFoundError:
        print(f"Error: File '{FILE_PATH}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def get_gpa_value(gpa, gpa_dict):
    """
    Computes a precise GPA score by interpolating between two closest GPA values.

    Args:
        gpa (float): The GPA value to be converted.
        gpa_dict (dict): Dictionary mapping GPA values to scores.

    Returns:
        float: Interpolated GPA score.
    """
    gpa_keys = np.array([float(k) for k in gpa_dict.keys()])

    # Return exact GPA score if available
    if str(gpa) in gpa_dict:
        return gpa_dict[str(gpa)]

    # Identify closest lower and upper GPA values
    lower_gpa = gpa_keys[gpa_keys <= gpa].max(initial=gpa_keys.min())
    upper_gpa = gpa_keys[gpa_keys >= gpa].min(initial=gpa_keys.max())

    # Retrieve corresponding scores
    lower_score = gpa_dict[str(lower_gpa)]
    upper_score = gpa_dict[str(upper_gpa)]

    # Linear interpolation between the two scores
    interpolated_score = lower_score + (upper_score - lower_score) * ((gpa - lower_gpa) / (upper_gpa - lower_gpa))
    
    return float(round(interpolated_score, 2))

def getSPS(df):
    """
    Computes the Student Performance Score (SPS) and normalizes it to a 1-10 scale.

    Args:
        df (DataFrame): Processed student dataset.

    Returns:
        list: Sorted list of normalized SPS scores.
    """
    scores = []

    for _, row in df.iterrows():
        # Retrieve mapped values from the dictionary
        prep = dict["preparation"]["categories"].get(row["Preparation"], 0)
        att = dict["attendance"]["categories"].get(row["Attendance"], 0)

        # Compute precise GPA scores
        o_gpa = get_gpa_value(float(row["Overall"]), dict["overall"]["categories"])
        l_gpa = get_gpa_value(float(row["Last"]), dict["last"]["categories"])

        # Compute weighted SPS score
        norm_sps = ((prep * 7) + (att * 6) + (o_gpa * 9) + (l_gpa * 5)) / (7 + 6 + 9 + 5)
        scores.append(round(norm_sps, 4))

    return sorted(scores)

# Execute the functions
parsed_df = parse_data()
if parsed_df is not None:
    sps_scores = getSPS(parsed_df)
    print(sps_scores)
