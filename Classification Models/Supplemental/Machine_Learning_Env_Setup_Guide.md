# Machine Learning Environment Setup Guide

This guide serves as a step by step process for setting up and validating the tools required for the machine learning portion of the curriculum. Many of these tools are needed to train and test machine learning models. Without these tools, class activities and code cannot be completed.

This guide will include installation and verification steps for the following technologies:

* [Imbalanced-learn](#Imbalanced-learn)

* [PyDotPlus](#PyDotPlus)

## Imbalanced-learn

### Install

The `imbalanced-learn` package has several dependencies which should already be installed in the default conda environment. Please refer to the [troubleshooting](#Troubleshooting) section for details about this environment.

Open the terminal, and execute the following command to install `imbalanced-learn`.

* Use the `conda install` command to download the `imbalanced-learn` module.

  ```shell
  conda install -c conda-forge imbalanced-learn
  ```

  ![imbalanced_learn_install.png](Images/imbalanced_learn_install.png)

### Verify Installation

Once the `imbalanced-learn` download is complete, verify the installation completed successfully.

* Use the `conda-list package_name` name, substituting `package_name` with `imbalanced-learn` to verify the `imbalanced-learn` library installed successfully.

  ```shell
  conda list imbalanced-learn
  ```

  ![Verify imbalanced-learn installation](Images/imbalanced_learn_verify.png)

## PyDotPlus

The `pydotplus` package is used to create a visual representation of decision trees. If you have any issues installing this library in Windows, please read the [Troubleshooting section below](#Troubleshooting).

### Installation Process

Open the terminal (Git Bash in Windows), and execute the following commands to install `pydotplus` and the additional libraries required. It's important to install these libraries in the order they are listed below.

```shell
conda install python-graphviz
conda install graphviz
conda install -c conda-forge pydotplus
```

#### Verify Installation

Once the `pydotplus` and the additional libraries download is complete, verify the installation completed successfully.

* Open the terminal and use the `conda list graphviz` and `conda list pydotplus` commands to identify if the `pydotplus` and `graphviz` libraries installed successfully.

  ![Verify graphviz installation](Images/graphviz-verify.png)

  ![Verify pydotplus installation](Images/pydotplus-verify.png)


## Troubleshooting

It can be frustrating when packages do not install correctly. Use the below approaches to troubleshoot installation issues and get your machine learning libraries up and running!

### Graphviz

Windows users might run into issues with the GraphViz installation, in which case here are additional instructions:

1. Download and install the stable version of the Windows GraphViz executable package from the [GraphViz downloads page](https://www.graphviz.org/download/).

   ![Downloading the GraphViz executable package for Windows](Images/graphviz_win_app.gif)

2. Edit your environment variables by clicking on start and type "environment," next select the "Edit the system variables" option.

    ![Edit Environment Variables](Images/edit-system-var-win.gif)

3. Click on the "Environment Variables" button at the bottom.

    ![Edit Environment Variables Button](Images/graphvizev.png)

4. Select the "Path" variable and click "Edit."

    ![Edit Environment Variables Path](Images/graphvizev2.png)

5. Click on an empty line and add the two GraphViz paths. These paths may differ depending on the directory where GraphViz was installed in your computer, be sure to corroborate these paths.

    ```text
    C:\Program Files (x86)\GraphViz2.38
    C:\Program Files (x86)\GraphViz2.38\bint
    ```

    ![Edit Environment Variables Path](Images/graphvizev3.png)

6. Click on the "Ok" button in all the opened windows to finish and restart GitBash if you have it running.

### Imbalanced-learn Installation Prerequisites

If you run into any issues with any of the imbalanced-learn machine learning models, try updating both scikit-learn and imbalanced-learn:

```shell
pip install -U scikit-learn
pip install -U imbalanced-learn
```

Then restart JupyterLab and try again.

### Update Conda Environment

An out-of-date Anaconda environment can create issues when trying to install new packages. Follow the below steps to update your conda environment.

1. Deactivate your current conda environment. This is required in order to update the global conda environment. Be sure to quit any running applications, such as Jupyter, prior to deactivating the environment.

    ```shell
    conda deactivate
    ```

2. Update conda.

    ```shell
    conda update conda
    ```

3. Create a fresh conda environment to use with PyViz.

    ```shell
    conda create -n mlenv python=3.7 anaconda
    ```

4. Activate the new environment.

    ```shell
    conda activate mlenv
    ```

5. Install the **imbalanced-learn** package.

    ```shell
    conda install -c conda-forge imbalanced-learn
    ```

Consult the [imbalanced-learn](https://imbalanced-learn.readthedocs.io/en/stable/) documentation for additional information about the **imbalanced-learn** library.

### Anaconda is not Running!

If you have issues running or updating anaconda, you can check if the package is correctly installed by running the following command in your terminal.

```shell
conda list anaconda
```

After running this command, you should see a list with the anaconda packages installed in your environment, at least the packages in the red square should be listed.

![Anaconda List](Images/anaconda-env-list.png)

In case you guess your anaconda environment is broken, deactivate your current virtual environment and create a new one as it was described above.

### Checking the Current Version of a Package

In addition to the `conda list` method, you can also validate which version of a package is installed in your environment by running the following command in the terminal.

```shell
python -c "import <package_name>;print(<package_name>.__version__)"
```

Where `<package_name>` is the name of the package you want to verify. For example, to corroborate the current version of the `imblearn` package you should run the following command.

```shell
python -c "import imblearn;print(imblearn.__version__)"
```

This is the output you should see on the terminal window.

![Package version check](Images/package-version.png)


### Package is not Installed in Windows

Sometimes you can get the following message when you install a package using `conda install`

```shell
EnvironmentNotWritableError: The current user does not have write permissions to the target environment.
 environment location: C:\ProgramData\Anaconda3
```

If you ever see this message, try running the Git Bash terminal as `Administrator`. In Windows 10 you can do it as follows.

1. Right-click on the Git Bash icon.

2. Go over the `More` option.

3. Chose the `Run as administrator` option.
