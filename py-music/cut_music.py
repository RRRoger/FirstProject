# -*- encoding: utf-8 -*-

"""sh
# 安装需要用到的库
brew install libav # macos
sudo apt-get install libav-tools # ubuntu

sudo pip install pydub # 安装需要的py库
"""

"""sh
# 安装工具 ffmpeg 
# 用法 https://www.jianshu.com/p/7ed3be01228b

brew install ffmpeg # macos
ffmpeg -i source_path dest_path
"""
from pydub import AudioSegment

def format(t):
	if not t:
		return t
	"""
	将`03:36`转化成毫秒
	"""
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

	start = format(start)
	end = format(end)

	sound = AudioSegment.from_mp3(source_path)
	if not end:
		sound_cut = sound[start:]
	elif not start:
		sound_cut = sound[:end]
	else:
		sound_cut = sound[start:end]

	sound_cut.export(dest_path, format="mp3")
	return "OK"

source_path = "/Users/chenpeng/Desktop/whoever.mp3"
dest_path = "/Users/chenpeng/Desktop/whoever2.mp3"

end = False
start = False

# from 03:36 to 04:06
start = (0 * 60 + 5) * 1000 + 500
end = (0 * 60 + 43) * 1000

start = "00:5.5"
end = "00:43"


cut_music(source_path, dest_path, start, end)
