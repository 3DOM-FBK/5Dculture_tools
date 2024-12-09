# UrbanRewind
The script provides a command-line interface to perform two distinct processes: a search via the Europeana API and a regression analysis on data sets, with a highly customisable configuration. Depending on the value of the --process parameter, the workflow can be configured to collect data from Europeana or apply a regression model with an extensive set of options for data preprocessing and model training. The code is designed to be versatile and configurable for processing complex data.

## Raccolta degli argomenti tramite la riga di comando
The main topics collected include:
--process: determines the process to be executed.
--outDir: the output directory where the results are saved.
- Additional parameters specific to each process:
    - For the ‘Europeana’ process, includes --europeanaToken, --europeanaQuery, and --maxRows to configure the search.
    - For the Regression process, it collects detailed information such as the path to the root directory (--rootDir), the attribute to be predicted (--attr_to_predict), the path to the training and prediction files, and various parameters to configure the regression model.

## Processo "Europeana"
- If the --process parameter is set to ‘europeana’, the script executes another Python script (europeana_search.py) that interacts with the Europeana API.
- The parameters --europeanaToken, --europeanaQuery, and --maxRows are used to configure the search, and the results are saved in the directory specified with --outDir.

## Processo "Regression"
- If the --process parameter is set to ‘regression’, the script executes another Python script (regression_3dom_OCB_2503.py) to run a regression model on a specified dataset.
- Regression-related parameters include:
    --rootDir: the root directory of the data.
    --attr_to_predict: the attribute to be predicted (dependent variable).
    --train_dir, --train_file: specify the directory and CSV file for the training data set.
    --predict_dir, --predict_files: specify the directory and CSV files for the prediction data set.
    --scaling, --isrfe, --isaugm: options for normalisation, feature elimination and augmentation of the data.
    --regressor: specifies the type of regressor to be used (options such as ‘svr’, ‘rf’, ‘mlp’, ‘catboost’).

## Gestione degli errori
If the --process parameter does not match one of the two valid values (‘european’ or ‘regression’), the script terminates with an error and prints a specific error message.

# Installazione
In the folder provided is the `Dockerfile`, which contains all the libraries required for the application to function correctly. Alternatively, you can download the pre-compiled image directly from Docker Hub by running the following command:

`docker pull 3domfbk/UrbanRewind:<tag>`

# Esempio
Below are some examples of the use of the different regressors:

### Catboost
`python main.py --process regression --outDir <YOUR_DIR> --rootDir <YOUR_DIR> --attr_to_predict h --train_dir <YOUR_DIR> --train_file <YOUR_CSV_FILE> --export_suffix_train _augm_ --predict_dir <YOUR_DIR> --predict_files <YOUR_CSV_FILE> --export_suffix_predict _pred_ --regressor catboost --isrfe False`