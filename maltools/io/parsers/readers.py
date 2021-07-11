from gzip import GzipFile

import xmltodict
import pandas as pd


def read_xml(filepath):
    """
    Read an XML file or compressed XML file exported from MyAnimeList and convert the anime or manga list it contains
    to a pandas DataFrame.

    Args:
        filepath (str): Path to the file. File must end with .gz or .xml to be read.

    Returns (pandas DataFrame): DataFrame of the entries in the file

    """
    dfs = []

    # parse xml into an OrderedDict
    if str(filepath).endswith('.gz'):
        od = xmltodict.parse(GzipFile(filepath))
    elif str(filepath).endswith('.xml'):
        with open(filepath) as fd:
            od = xmltodict.parse(fd.read())
    else:
        raise ValueError('Unexpected file extension.')

    key1 = 'myanimelist'  # top level key
    for key2 in od[key1]:
        if key2 != 'myinfo':

            entries = od[key1][key2]  # entries are separate OrderedDict
            for orderedDict in entries:
                # convert OrderedDict to dataframe
                df_entry = pd.DataFrame(orderedDict, index=[0])
                dfs.append(df_entry)

    # combine dataframes for separate entries into a single dataframe
    df = pd.concat(dfs).reset_index()
    return df
