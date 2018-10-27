#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import cv2
import os
import random
import glob
import json
import numpy as np
from tqdm import tqdm
from .lib import utils

from logging import DEBUG
from logging import getLogger

logger = getLogger('impulso')
logger.setLevel(DEBUG)

# Set HOME directory.
IMPULSO_HOME = os.environ['IMPULSO_HOME']


class Aggregator(object):

    def __init__(self, exec_type, hparams):
        logger.info('Begin init of Aggregator')
        self.exec_type = exec_type
        self.hparams = hparams
        self.hparams[exec_type]['data_id'] = utils.issue_id()
        self.hparams[exec_type]['output_train'] = os.path.join(IMPULSO_HOME,
                                                               'datasets',
                                                               self.hparams[exec_type]['data_id'],
                                                               'train')
        self.hparams[exec_type]['output_test'] = os.path.join(IMPULSO_HOME, 'datasets', 'test')

        logger.info('Backup hparams.yaml and src')
        utils.backup_before_run(self.exec_type, self.hparams)
        logger.info('End init of Aggregator')


    def load_data(self, dtype):
        logger.info('Load dataset')

        # Get resized size
        resize_w = self.hparams['common']['resize']['width']
        resize_h = self.hparams['common']['resize']['height']

        # Set directory path
        input_dir = self.hparams[self.exec_type][dtype+'_path']
        bbox_path = self.hparams[self.exec_type][dtype+'_json']
        
        # Load ground truth
        with open(bbox_path, encoding='utf-8') as f:
            bboxes = json.load(f)
        
        # Load images and ground truth
        logger.info(f'Loading images in {input_dir}')
        images = []
        labels = []
        image_names = []
        for box in tqdm(bboxes):
            image_path = os.path.join(input_dir, box['FileName'])
            print(image_path)
            # Input image
            image = cv2.imread(image_path)
            org_h, org_w, _ = image.shape
            image = cv2.resize(image, (resize_w, resize_h))
            images.append(image)
            # Label image
            label_image = np.zeros(resize_h * resize_w).reshape(resize_h, resize_w)
            for rectangle in box['BBox']:
                left = int(rectangle['Left'] * resize_w / org_w) 
                top = int(rectangle['Top'] * resize_h / org_h) 
                width = int(rectangle['Width'] * resize_w / org_w) 
                height = int(rectangle['Height'] * resize_h / org_h) 
                label_image[top:top+height+1, left:left+width+1] = 1. 
            # For rectangle data: END
            labels.append(label_image.flatten())
            image_names.append(box['FileName'])

        self.x = np.array(images)
        self.t = np.array(labels)
        self.filename = np.array(image_names)


    def save_data(self, dtype):
        logger.info('Begin saving data: ' + dtype)
        x_dir = os.path.join(self.hparams['dataset']['output_' + dtype], 'x')
        t_dir = os.path.join(self.hparams['dataset']['output_' + dtype], 't')
        
        # Create output directories
        for output_dir in [x_dir, t_dir]:
            os.makedirs(output_dir, exist_ok=True)
        
        # Save as numpy.array
        np.save(file=os.path.join(x_dir, 'x.npy'), arr=self.x)
        np.save(file=os.path.join(t_dir, 't.npy'), arr=self.t)
        np.save(file=os.path.join(x_dir, 'filename.npy'), arr=self.filename)

        logger.info('End saving data: ' + dtype)


if __name__ == '__main__':
    """add"""
