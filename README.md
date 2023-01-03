# IMPROVE Singularity Containers
Each curated community model is deployed in a Singularity container that is extended to support standardized execution of all currated community models. This repository contains *build recipies*/*definintion files* and tools for building model specific singularity/apptainer images. 

1. Setting up repository
2. Building container images
3. Running a container
4. Best practices for build recipies 

## Setup ##

Clone the repository into a location of your choice:

```bash
git clone https://github.com/JDACS4C-IMPROVE/Singularity.git
cd Singularity
```

## Build and Deploy model images ##

From within the Singularity repo call:

1. `make`
2. `make deploy`

If you want to deploy the images at a different location invoke the make command and set PREFIX to a path of your choosing, default is the current directory. The deploy process will create an image directory at the specified location and copy the image files into it.

```make deploy PREFIX=/my/deploy/path/```


## Running an IMPROVE Container

Every container has a standardized scriptfor training the model called *train.sh* and a standard location (*/candle_data_dir*) for model input and output. *train.sh* expects /candle_data_dir To train a model you have to make your data directory available inside the container as */candle_data_dir*.  

```bash

singularity exec --nv --bind ${IMPROVE_DATA_DIR}:/candle_data_dir ${CONTAINER} train.sh ${GPUID} 

```

With:  
**IMPROVE_DATA_DIR** path to data directory
**CONTAINER** *path/and/name* of image file
**GPUID** 

For more examples see the [documentation](http://)




### Best Practices for Build Recipes
see: (https://sylabs.io/guides/3.7/user-guide/definition_files.html)

When crafting your recipe, it is best to consider the following:

- Always install packages, programs, data, and files into operating system locations (e.g. not /home, /tmp , or any other directories that might get commonly binded on). 
- Clearly define install location prior installing. Don't make any assumptions, e.g. create and change into a build or install dir prior checking out github repos.
- Document your container. If your runscript doesn’t supply help, write a %help or %apphelp section. A good container tells the user how to interact with it.
- If you require any special environment variables to be defined, add them to the %environment and %appenv sections of the build recipe.
- Files should always be owned by a system account (UID less than 500).
- Ensure that sensitive files like /etc/passwd, /etc/group, and /etc/shadow do not contain secrets.
- Build production containers from a definition file instead of a sandbox that has been manually changed. This ensures greatest possibility of reproducibility and mitigates the “black box” effect.

## Basic commands
Create a singularity container from a def file. In the first case, an image is created.
In the second example, a writable container is created.
In the third example, an image is created from a writable container.

```
# Here we use as a pseudo standard the workspace directory for writable containers.
# IMPROVE environment variables begin with I
export IHOME=/homes/brettin/Singularity/workspace
export ISL=${IHOME}/sandboxes
export IIL=${IHOME}/images

singularity build --sandbox ${ISL}/${SANDBOX} $DEFILE
singularity build $IIL/${SANDBOX}.sif ${ISL}/${SANDBOX}
singularity build $IIL/${IMAGE}.sif $DEFFILE



```



