import kagglehub

# Download latest version
path = kagglehub.dataset_download(
	"karansarpal/fremtpl2-french-motor-tpl-insurance-claims"
)
print("Path to dataset files:", path)

with open("_datapath.py", "w") as f:
	f.write(f"DATAPATH = {path}")
print("Dataset path available as _datapath.DATAPATH")