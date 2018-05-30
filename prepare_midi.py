
import music21
import glob
import os


def prepare_midi(path)
	score = music21.converter.parse('cali.mid')
	key = score.analyze('key')
	print(key.tonic.name, key.mode)
	
	dirList = glob.glob("./midi/**/*.mid",recursive=True)
	for fn in dirList:
 	   tail=fn.split('/')[-1:][0]
    	   print(tail)
    	   s = converter.parse(fn)
    	   k = s.analyze('key')
    	   print(k.tonic.name,k.mode)
    	   i = interval.Interval(k.tonic, pitch.Pitch('C5'))
    	   sNew = s.transpose(i)
    	   if key.mode=='minor':
     	      sNew.write('midi',fp='./sad/'+tail)
    	   else:
     	      sNew.write('midi',fp='./happy/'+tail)

