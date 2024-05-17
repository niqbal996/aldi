srun -K --ntasks=1 --gpus-per-task=1 -N 1 --cpus-per-gpu=20 -p H100 --mem=50000 \
  --container-mounts=/netscratch/naeem:/netscratch/naeem,/home/iqbal/aldi:/home/iqbal/aldi \
  --container-image=/netscratch/naeem/aldi_detectron2.sqsh \
  --mail-type=end --mail-user=naeem.iqbal@dfki.de --job-name=aldi_uda \
  --container-workdir=/home/iqbal/aldi \
  --time=1-00:00 \
  bash tools/scripts/uda.sh
