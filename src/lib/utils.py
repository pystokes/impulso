#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

import sys, os
import copy, shutil, glob
import yaml
import datetime

from logging import DEBUG, INFO
from logging import getLogger

# Set HOME directory.
IMPULSO_HOME = os.environ['IMPULSO_HOME']

# Set logger.
logger = getLogger('impulso')


def load_hparams(yaml_path):
    logger.debug(f'Load hyperparameters: {yaml_path}')
    with open(yaml_path) as f:
        hparams = yaml.load(f)
    logger.info('Load hparams')
    logger.info(hparams)
    return hparams


def save_hparams(save_path, hparams):
    logger.debug(f'Save hyperparameters: {save_path}')
    with open(save_path, 'w') as f:
        yaml.dump(hparams, f, default_flow_style=False)


def issue_id():
    logger.debug('Generate issue ID.')
    id = datetime.datetime.now().strftime('%m%d-%H%M-%S%f')[:-4]
    return id


def backup_before_run(exec_type, hparams):
    logger.debug('Backup conditions before run.')

    if exec_type == 'dataset':
        output_home = os.path.join(IMPULSO_HOME, f'datasets/{hparams[exec_type]["data_id"]}')
        hparams_to_save = copy.deepcopy(hparams)
        drop_keys = list(hparams.keys())
        drop_keys.remove('dataset')
        for key in drop_keys:
            del hparams_to_save[key]

    elif exec_type in ['prepare', 'train', 'test', 'predict']:
        output_home = os.path.join(IMPULSO_HOME, f'experiments/{hparams["prepare"]["experiment_id"]}')
        hparams_to_save = copy.deepcopy(hparams)
        if exec_type == 'prepare':
            del hparams_to_save['dataset']

    else:
        pass

    if exec_type in ['dataset', 'prepare']:
        os.makedirs(os.path.join(output_home, 'hparams'), exist_ok=True)
        save_hparams(os.path.join(output_home, 'hparams/hparams.yaml'), hparams_to_save)

        copy_from = os.path.join(IMPULSO_HOME, 'src')
        copy_to = os.path.join(output_home, 'src')
        if os.path.exists(copy_to):
            shutil.rmtree(copy_to)
        shutil.copytree(copy_from, copy_to)


if __name__ == '__main__':
    """
    __main__ is for DEBUG.
    """
    # Check hparams.
    from pprint import pprint
    hparams = load_hparams(os.path.join(IMPULSO_HOME, 'hparams/hparams.yaml'))
    pprint(hparams)

    # Check ID.
    id = issue_id()
    print(id)
