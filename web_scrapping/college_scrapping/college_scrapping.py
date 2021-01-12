import pandas as pd
import os
import shutil
import time
from wikipedia import wikipedia

start_time = time.time()
CSV_FOLDER = os.path.join("sources", "csv")
MAP_FOLDER = "map_csv"
QC_INSTITUTIONS = "quebec_institutions.csv"
BC_INSTITUTIONS = "british_columbia_institutions.csv"
AB_INSTITUTIONS = "alberta_institutions.csv"
ON_INSTITUTIONS = "ontario_institutions.csv"

provinces = [
    QC_INSTITUTIONS, BC_INSTITUTIONS, AB_INSTITUTIONS, ON_INSTITUTIONS
]
provinces_names = {
    QC_INSTITUTIONS: "quebec",
    BC_INSTITUTIONS: "british_columbia",
    AB_INSTITUTIONS: "alberta",
    ON_INSTITUTIONS: "ontario"
}


def cleanup(path):
    """
    Removes all files and dirs in a directory
    :param path: the path to the directory for cleanup
    """
    if os.listdir(path):
        for file in os.listdir(path):
            filepath = os.path.join(path, file)
            if os.path.isfile(filepath):
                os.unlink(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)


print("cleaning up the 'map_csv' folder")
cleanup(MAP_FOLDER)

for province in provinces:
    # create the output folder
    province_name = provinces_names[province]
    os.mkdir(os.path.join(MAP_FOLDER, province_name))
    province_path = os.path.join(MAP_FOLDER, province_name)
    # get the province csv
    source_path = os.path.join(CSV_FOLDER, province)
    df = pd.read_csv(source_path, encoding="ISO-8859-1")
    cities = df['City'].unique()
    for city in cities:
        institutions = []
        map_path = os.path.join(province_path, "{}.csv".format(city))
        with open(map_path, 'w') as f:
            f.write("Latitude-Longitude, Name")
            for institution in df[df['City'] == city]['Name']:
                try:
                    wiki_page = wikipedia.page(institution)
                    if wiki_page and institution == wiki_page.title and wiki_page.coordinates:
                        latitude, longitude = wiki_page.coordinates
                        print("{}, {} {}".format(institution, latitude, longitude))
                        f.write("\n{}, {} {}".format(institution, latitude, longitude))
                except Exception:
                    print("Could not find coordinates for {}, skipping it".format(institution))
                    continue

print("Total execution time: {} seconds".format(time.time() - start_time))
