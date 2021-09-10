# Setup Environment:

```bash
conda env create -f environment_asteroids.yml
conda activate asteroids_env
```

To connect this new environment to jupyterhub, run (Shouldn't be needed)
```bash
conda install -c anaconda ipykernel
```
and then,

```bash
python -m ipykernel install --user --name=asteroids_env
```
