conda env create -f environment.yml -n verify-repro
conda activate verify-repro
python -m ipykernel install --user --name verify-repro
jupyter nbconvert --execute --to notebook \
	--inplace \
	--ExecutePreprocessor.kernel_name=verify-repro analysis.ipynb