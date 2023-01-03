# Python Installation & Environment

## Anaconda

Install [Anaconda](https://docs.anaconda.com/anaconda/install/)

## Conda

Conda [User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/)

### Instlaling Conda Virtual Environment

	conda --version
	conda update conda
	conda update anaconda
	conda create -n dev python=3.7 anaconda
	conda init zsh
	# JupyterLab
	python -m ipykernel install --user --name dev
	conda install -c conda-forge nodejs
	
	conda activate dev
	conda deactivate
