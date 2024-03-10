import numpy as np
from pathlib import Path as P
import os
import shutil
from glob import glob

N = 50
DATA_DIR = P('../Voice-Privacy-Challenge-2024/data')
DATASET = 'libri_test'
systems = ['hi', 'mcadams', 'beta_.05', 'beta_.06', 'beta_.065', 'beta_.07']
output = P('./hfc_listening_test')

def main():
    # generate list of N random numbers
    gt_dir = f'{DATA_DIR}/{DATASET}'
    rng = np.random.default_rng(12345)

    system_dirs = [gt_dir] + [P(str(DATA_DIR / DATASET) +f'*_{system}') for system in systems]
    output_dirs = [output/P('gt')] + [output/system for system in systems]
    
    wav_names = sorted(glob(str(system_dirs[1]) + '/wav/*.wav'))
    wav_names = [os.path.basename(wav_name) for wav_name in wav_names]
    print(wav_names)
    selected_wav_names = rng.choice(wav_names, N, replace=False)

    for system_dir, output_dir in zip(system_dirs, output_dirs):
        for wav_name in selected_wav_names:
            src = system_dir / P('wav') / wav_name
            #print(str(src))
            src = glob(str(src))
            if len(src) != 1:
                print(f'{wav_name} not found in {system_dir}')
            else:
                src = src[0]
                dst = output_dir / wav_name
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(src, dst)


if __name__ == '__main__':
    main()