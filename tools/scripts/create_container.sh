srun -K --ntasks=1 --gpus-per-task=1 -N 1 --cpus-per-gpu=10 -p H100 --mem=50000 \
  --container-mounts=/netscratch/naeem:/netscratch/naeem,/home/iqbal/aldi:/home/iqbal/aldi \
  --container-image=/netscratch/naeem/aldi_detectron2.sqsh   \
  --container-save=/netscratch/naeem/aldi_detectron2.sqsh \
  --time=00-02:00 \
  --pty /bin/bash
