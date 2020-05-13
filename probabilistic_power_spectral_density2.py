from obspy import read
from obspy.signal import PPSD
from obspy.imaging.cm import pqlx
from obspy.io.xseed import Parser


st = read("IN.ZIRO..SHZ.D.2020.092.000051.SAC")
parser = Parser("ZIRODATALESS.SEED")
ppsd = PPSD(st[0].stats, metadata=parser)
ppsd.add(st)

st = read("IN.ZIRO..SHZ.D.2020.092.000051.SAC")
ppsd.add(st)

ppsd.plot(cmap=pqlx)
