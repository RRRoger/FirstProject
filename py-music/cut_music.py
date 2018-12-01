# -*- encoding: utf-8 -*-

"""
    中了抖音的毒, 此脚本用户提取抖音视频中的音频, 并支持视频剪辑
"""
from pydub import AudioSegment

def min2millisec(t):
    """
    将`03:36`转化成毫秒
    :param t: min string like '00:43'
    :return: millisec int
    """
    if not t:
        return t
    tim = t.split(":")[::-1]
    depth = 0
    rel = 60
    res = 0
    for s in tim:
        res += float(s) * (rel ** depth)
        depth += 1
    return res * 1000

def cut_music(source_path, dest_path, start=False, end=False):
    """
        python 剪辑mp3
        必须是绝对路径
    """
    print "%s ~ %s" % (start, end)

    start = min2millisec(start)
    end = min2millisec(end)

    sound = AudioSegment.from_mp3(source_path)
    if not end:
        sound_cut = sound[start:]
    elif not start:
        sound_cut = sound[:end]        
    elif start and end:
        sound_cut = sound[start:end]
    else:
        raise Exception('agrs start and end set at least one!')

    sound_cut.export(dest_path, format="mp3")
    return "OK"

source_path = "/Users/chenpeng/Desktop/小了白了兔.mp3"
dest_path = "/Users/chenpeng/Desktop/小了白了兔new.mp3"

end = False
start = False

# from 00:05 to 00:43

start = "00:00"
end = "00:20"

cut_music(source_path, dest_path, start, end)
