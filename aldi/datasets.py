from detectron2.data.datasets import register_coco_instances

# Cityscapes 
register_coco_instances("cityscapes_train", {},         "datasets/cityscapes/annotations/cityscapes_train_instances.json",                  "datasets/cityscapes/leftImg8bit/train/")
register_coco_instances("cityscapes_val",   {},         "datasets/cityscapes/annotations/cityscapes_val_instances.json",                    "datasets/cityscapes/leftImg8bit/val/")

# Foggy Cityscapes
register_coco_instances("cityscapes_foggy_train", {},   "datasets/cityscapes/annotations/cityscapes_train_instances_foggyALL.json",   "datasets/cityscapes/leftImg8bit_foggy/train/")
register_coco_instances("cityscapes_foggy_val", {},     "datasets/cityscapes/annotations/cityscapes_val_instances_foggyALL.json",     "datasets/cityscapes/leftImg8bit_foggy/val/")
# for evaluating COCO-pretrained models: category IDs are remapped to match
register_coco_instances("cityscapes_foggy_val_coco_ids", {},     "datasets/cityscapes/annotations/cityscapes_val_instances_foggyALL_coco.json",     "datasets/cityscapes/leftImg8bit_foggy/val/")

# Sim10k
register_coco_instances("sim10k_cars_train", {},             "datasets/sim10k/coco_car_annotations.json",                  "datasets/sim10k/images/")
register_coco_instances("cityscapes_cars_train", {},         "datasets/cityscapes/annotations/cityscapes_train_instances_cars.json",                  "datasets/cityscapes/leftImg8bit/train/")
register_coco_instances("cityscapes_cars_val",   {},         "datasets/cityscapes/annotations/cityscapes_val_instances_cars.json",                    "datasets/cityscapes/leftImg8bit/val/")

# CFC
register_coco_instances("cfc_train", {},         "datasets/cfc/coco_labels/cfc_train.json",                  "datasets/cfc/images/cfc_train/")
register_coco_instances("cfc_val",   {},         "datasets/cfc/coco_labels/cfc_val.json",                    "datasets/cfc/images/cfc_val/")
register_coco_instances("cfc_channel_train", {},         "datasets/cfc/coco_labels/cfc_channel_train.json",                  "datasets/cfc/images/cfc_channel_train/")
register_coco_instances("cfc_channel_test",   {},         "datasets/cfc/coco_labels/cfc_channel_test.json",                    "datasets/cfc/images/cfc_channel_test/")


# Phenobench
register_coco_instances("pheno_train", {},         "/netscratch/naeem/phenobench/coco_annotations/coco_plants_panoptic_train.json", "/netscratch/naeem/phenobench/train/")
register_coco_instances("pheno_val", {},         "/netscratch/naeem/phenobench/coco_annotations/coco_plants_panoptic_val.json", "/netscratch/naeem/phenobench/val/")
register_coco_instances("syn_pheno_train", {},         "/netscratch/naeem/sugarbeet_syn_v2/coco_annotations/instances_train.json", "/netscratch/naeem/sugarbeet_syn_v2/images")
register_coco_instances("syn_pheno_val", {},         "/netscratch/naeem/sugarbeet_syn_v2/coco_annotations/instances_val.json", "/netscratch/naeem/sugarbeet_syn_v2/images")