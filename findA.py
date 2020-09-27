# 三个约定
# ppg，mel，spec指的一句话的整个序列；ppgs，mels，specs指的是多句话的ppg序列们，对应的是wavs
# 语谱图变wav：  wav_cn_rep = spectrogram2wav_for_ppg_cbhg(spec_rep)
# wav写入磁盘：  write_wav(write_path, wav_cn_rep, sr=16000):


# 逻辑
# 输入：en_sentence_txt = 'Hello', en_sentence_fname = 'LJ001', en_wav_dir_path, en_ppg_dir_path, en_spec_dir_path
# en_final_cn_idx_path, cn_ppg_dir_path, cn_spec_dir_path
# 输出：en_sentence_wav_orig，cn_sentence_wav_rep

import os
import numpy as np

from audio import spectrogram2wav_for_ppg_cbhg, write_wav




