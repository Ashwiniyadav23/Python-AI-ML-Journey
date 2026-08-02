# conda — an alternative environment/package manager

conda create --name myenv python=3.11    # create an environment with a specific Python version
conda activate myenv                      # activate it
conda install pandas numpy                # install packages
conda deactivate                          # exit the environment
conda env list                            # see all environments you've created