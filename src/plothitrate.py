import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
font = {
	'size'		: '20'}
mpl.rc('font', **font)
yber, ymulti, yrf, ysvm, yhybrid = [],[],[],[],[]
x,x2,y1,y2,y3,y4,y5 = [],[],[],[],[],[],[]

for i in range(1,5):
	csv_reader = csv.reader(open('hitrate-vs-chi2-dt' + str(i) + '.csv'))
	x,x2,y1,y2,y3,y4,y5 = [],[],[],[],[],[],[]
	for line in csv_reader:
		x.append(float(line[1]))
		x2.append(float(line[0]))
		y1.append(float(line[8]))
		y2.append(float(line[9]))
		y3.append(float(line[10]))
		y4.append(float(line[11]))
		y5.append(float(line[12]))
	yber.append(y1)
	ymulti.append(y2)
	yrf.append(y3)
	ysvm.append(y4)
	yhybrid.append(y5)


#fig = plt.figure()
#ax1 = fig.add_subplot(2, 3, 1)
#ax2 = fig.add_subplot(2, 3, 2)
#ax3 = fig.add_subplot(2, 3, 3)
#ax4 = fig.add_subplot(2, 3, 4)
#ax5 = fig.add_subplot(2, 3, 5)
figs = []
axes = []
#fig = plt.figure()
#for i in range(1,6):
	#figs.append(plt.figure(i))
	#axes.append(fig.add_subplot(2, 3, i))


#axes = [ax1, ax2, ax3, ax4, ax5]
y = [yber, ymulti, yrf, ysvm, yhybrid]
titles = ['Bernoulli', 'Multinomial', 'Random Forest', 'SVM', 'Hybrid']

for i in range(len(y)):
	f = plt.figure(i)
	#plt.switch_backend('QT4Agg')
	figs.append(f)
	plt.plot(x, y[i][0], 'ks-', label="Binary")
	plt.plot(x, y[i][1], 'ko-', label="Count")
	plt.plot(x, y[i][2], 'kv-', label="L2-normalized")
	plt.plot(x, y[i][3], 'k^-', label="0-1 mapped")
	plt.xscale('log')
	plt.xlabel("Vocabulary size", fontsize=25)
	plt.ylabel("Hit ratio", fontsize=25)
	plt.title(titles[i])
	plt.legend(loc=2, prop={'size':14})
	plt.ylim((0.40, 0.80))
	#mng = plt.get_current_fig_manager()
	#mng.frame.Maximize(True)
	#plt.savefig(titles[i] + '-hitrate.svg', format='svg')
	#plt.legend(bbox_to_anchor=(0., 0.98, 1., .1), loc=2, ncol=5, mode="expand", borderaxespad=0.)

plt.show()