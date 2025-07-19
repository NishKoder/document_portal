## Command needs to follow

### Create project directory

```sh
mkdir <project-directory>
cd <project-directory>
code .
```

## Conda environment setup

```sh
conda create -p <env-path> python=<python-version> -y
conda activate <env-path>
pip install -r requirements.txt
```

## Git commands

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push
```