# -*- coding: utf-8 -*-
import sys
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import nbformat
import pandas as pd
import seaborn as sns
from nbformat.reader import NotJSONError


def get_kernel(notebook_file):
    try:
        # print(notebook_file)
        notebook_object = nbformat.read(notebook_file, as_version=4)
        if notebook_object.metadata:
            if 'language_info' in notebook_object.metadata:
                return notebook_object.metadata.language_info.name
            elif 'kernelspec' in notebook_object.metadata:
                if 'language' in notebook_object.metadata.kernelspec:
                    return notebook_object.metadata.kernelspec.language
                if 'name' in notebook_object.metadata.kernelspec:
                    return notebook_object.metadata.kernelspec.name
                else:
                    print(notebook_object.metadata)
                    print(notebook_file)  # kernelspec.name
    except nbformat.reader.NotJSONError:
        print(f"skipping {notebook_file}", file=sys.stderr)


def language_histogram(input_path):
    languages = Counter()
    for python_file in Path(input_path).glob("**/*.ipynb"):
        if not python_file.is_file():
            continue
        else:
            languages[get_kernel(python_file)] += 1
    custom_params = {"axes.spines.right": False, "axes.spines.top": False}
    sns.set_theme(style="ticks", rc=custom_params)
    pd.DataFrame.from_dict(languages,
                           orient='index',
                           columns=['language']).sort_values(by='language').plot.barh()
    plt.savefig('hist.png')
    return(languages)


if __name__ == "__main__":
    language_histogram(sys.argv[1])