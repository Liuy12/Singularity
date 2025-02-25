import json
import os

from example import IBenchmark

import candle

# Just because the tensorflow warnings are a bit verbose
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# This should be set outside as a user environment variable
os.environ["CANDLE_DATA_DIR"] = os.environ["HOME"] + "/improve_data_dir"

# file_path becomes the default location of the example_default_model.txt file
file_path = os.path.dirname(os.path.realpath(__file__))


# In the initialize_parameters() method, we will instantiate the base
# class, and finally build an argument parser to recognize your customized
# parameters in addition to the default parameters.The initialize_parameters()
# method should return a python dictionary, which will be passed to the run()
# method.
def initialize_parameters():
    i_bmk = IBenchmark(
        file_path,  # this is the path to this file needed to find default_model.txt
        "example_default_model.txt",  # name of the default_model.txt file
        "keras",  # framework, choice is keras or pytorch
        prog="example_baseline",  # basename of the model
        desc="IMPROVE Benchmark",
    )

    gParameters = candle.finalize_parameters(
        i_bmk
    )  # returns the parameter dictionary built from
    # default_model.txt and overwritten by any
    # matching comand line parameters.

    return gParameters


def run(params):
    # fetch data
    # preprocess data
    # save preprocessed data
    # define callbacks
    # build / compile model
    # train model
    # infer using model
    # etc
    print("running third party code")
    print("returning training metrics")
    metrics = {"val_loss": 0.101, "pcc": 0.923, "scc": 0.777, "rmse": 0.036}
    # metrics is used by the supervisor when running
    # HPO workflows (and possible future non HPO workflows)

    # Dumping results into file, workflow requirement
    val_scores = {
        "key": "val_loss",
        "value": metrics["val_loss"],
        "val_loss": metrics["val_loss"],
        "pcc": metrics["pcc"],
        "scc": metrics["scc"],
        "rmse": metrics["rmse"],
    }
    # ~/improve_data_dir/Example
    # $ tree .
    # .
    # ├── Data
    # └── Output
    #     └── EXP000
    #         └── RUN000
    #             └── scores.json

    with open(params["output_dir"] + "/scores.json", "w", encoding="utf-8") as f:
        json.dump(val_scores, f, ensure_ascii=False, indent=4)

    return metrics  # metrics is used by the supervisor when running
    # HPO workflows (and possible future non HPO workflows)


def main():
    params = initialize_parameters()
    scores = run(params)
    print(params["data_dir"])

    # demonstrating a list
    for i, value in enumerate(params["dense"]):
        print("dense layer {} has {} nodes".format(i, value))


if __name__ == "__main__":
    main()
